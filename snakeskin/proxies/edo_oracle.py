import cx_Oracle

from flask import current_app as app


def get_bio_data(user_id):
    sql = ('SELECT GENDER_GENDEROFRECORD_CODE, BIRTH_DATE, EMAIL_EMAILADDRESS, ADDRESS_HOME_CITY '
             'FROM SISEDO.PERSONV00_VW '
             'WHERE IDENTIFIER_CAMPUSUID_ID = :user_id ')
    results = query(sql, user_id=user_id)

    if results:
        return results[0]
    else:
        return None

def query(sql, **params):
    dsn = cx_Oracle.makedsn(app.config['EDO_ORACLE_HOST'], app.config['EDO_ORACLE_PORT'], app.config['EDO_ORACLE_SID'])

    try:
        with cx_Oracle.connect(app.config['EDO_ORACLE_USERNAME'], app.config['EDO_ORACLE_PASSWORD'], dsn) as db:
            cursor = db.cursor()
            result = cursor.execute(sql, **params)
            rows = result.fetchall()
            columns = [i[0].lower() for i in cursor.description]
            zipped = [dict(zip(columns, row)) for row in rows]
            cursor.close()

    except cx_Oracle.DatabaseError as e:
        app.logger.error(e)
        zipped = None

    return zipped
