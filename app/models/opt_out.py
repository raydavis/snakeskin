from app import db
from app.models.base import Base


"""
The `opt_out` table keeps track of students who have opted out of data use for Learning analytics projects.
"""
class OptOut(Base):
    __tablename__ = 'opt_out'

    credential_id = db.Column(db.Integer, db.ForeignKey('credentials.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False, primary_key=True)

    def __init__(self, name, description, key, secret, read_permission, write_permission, datashare, tenant):
        self.name = name
        self.description = description
        self.key = key
        self.secret = secret
        self.read_permission = read_permission
        self.write_permission = write_permission
        self.datashare = datashare
        self.tenant = tenant

    def __repr__(self):
        return '<OptOut %r %r>' % (self.credential_id, self.user_id)
