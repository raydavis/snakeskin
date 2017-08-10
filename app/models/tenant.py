from app import app, db
from app.models.base import Base
from app.proxies import canvas


"""
The `tenants` table tracks the top-level integrated environments which have data in the Learning Record Store.
A tenant incorporates a set of users, data sources, data consumers, and learning record statements.
Examples: "UC Berkeley", "Stanford", "UCB Test Data".
"""
class Tenant(Base):
    __tablename__ = 'tenants'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    scheme = db.Column(db.String(255))
    domain = db.Column(db.String(255))
    token = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Tenant %r>' % (self.name)

    def short_profile(self):
        return {
            'id': self.id,
            'name': self.name
        }

    def full_profile(self):
        return {
            'id': self.id,
            'name': self.name,
            'users': [u.short_profile() for u in self.users]
        }

    def get_user_profile(self, user):
        response = canvas.get_user_for_sis_id(self, user.external_id)
        return response.json()
