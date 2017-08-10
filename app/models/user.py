from sqlalchemy import sql

from app import db
from app.models.base import Base
from app.proxies import edo_oracle


"""
The `users` table keeps track of each user for which a learning activity has been received or an Opt-Out
request has been made.
"""
class User(Base):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    external_id = db.Column(db.String(255), nullable=False)

    tenant_id = db.Column(db.Integer, db.ForeignKey('tenants.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    tenant = db.relationship('Tenant', backref=db.backref('users', lazy='dynamic'))

    def __init__(self, name, external_id, tenant):
        self.name = name
        self.external_id = external_id
        self.tenant = tenant

    def __repr__(self):
        return '<User %r>' % (self.name)

    def short_profile(self):
        return {
            'id': self.external_id,
            'name': self.name
        }

    def full_profile(self):
        profile = self.tenant.get_user_profile(self)
        profile.update(edo_oracle.get_bio_data(self.external_id))
        profile.update(self.short_profile())

        return profile

    def get_data_sources(self):
        query = sql.text(
          "SELECT s.total, w.name FROM ("
               "SELECT credential_id, COUNT(*)::int AS total "
                    "FROM statements "
                    "WHERE user_id = :user_id AND tenant_id = :tenant_id "
                    "GROUP BY credential_id "
                    "ORDER BY credential_id DESC"
               ") s "
               "INNER JOIN credentials w ON w.id = s.credential_id")
        res = db.session.execute(query, {'user_id': self.id, 'tenant_id': self.tenant_id})
        resultset = [dict(row) for row in res]
        return resultset

    def get_recent_activities(self):
        query = sql.text(
            "SELECT statement, timestamp "
                "FROM statements "
                "WHERE user_id = :user_id AND tenant_id = :tenant_id "
                "ORDER BY timestamp DESC "
                "LIMIT 10")
        res = db.session.execute(query, {'user_id': self.id, 'tenant_id': self.tenant_id})
        resultset = [row['statement'] for row in res]
        return resultset

    def get_top_activities(self):
        query = sql.text(
            "SELECT activity_type, COUNT(*)::int AS total "
                "FROM statements "
                "WHERE user_id = :user_id AND tenant_id = :tenant_id "
                "GROUP BY activity_type "
                "ORDER BY total DESC")
        res = db.session.execute(query, {'user_id': self.id, 'tenant_id': self.tenant_id})
        resultset = [dict(row) for row in res]
        return resultset

    def get_total_activities(self):
        query = sql.text(
          "SELECT EXTRACT(year FROM timestamp)::int AS year, EXTRACT(month FROM timestamp)::int AS month, count(*)::int AS total "
               "FROM statements "
               "WHERE user_id = :user_id AND tenant_id = :tenant_id "
               "GROUP BY year, month "
               "ORDER BY year, month ASC")
        res = db.session.execute(query, {'user_id': self.id, 'tenant_id': self.tenant_id})
        resultset = [dict(row) for row in res]
        return resultset
