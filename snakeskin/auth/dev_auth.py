from flask import (
    abort, current_app, flash, redirect, request,
)
from flask_login import (
    login_required, login_user, logout_user
)
from . import authorized_user

@current_app.route('/devauth/login', methods=['GET', 'POST'])
def login():
    logger = current_app.logger
    if current_app.config['DEVELOPER_AUTH_ENABLED']:
        if request.method == 'POST':
            if request.form['password'] != current_app.config['DEVELOPER_AUTH_PASSWORD']:
                logger.error('Wrong password entered in Developer Auth')
                return abort(403)
            user_id = request.form['uid']
            user = authorized_user.load_user(user_id)
            if user is None:
                logger.error('Unauthorized user ID {} entered in Developer Auth'.format(user_id))
                return abort(403)
            logger.info('Developer Auth used to log in as UID {}'.format(user_id))
            login_user(user)
            flash('Logged in successfully.')
            return redirect('/')
        else:
            return '''
                <form method="post">
                    <p>UID: <input type=text name=uid>
                    <p>Password: <input type=text name=password>
                    <p><input type=submit value=Login>
                </form>
            '''
    else:
        abort(403)

@current_app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')
