from app import db
from app.models.base import Base


"""
The `credentials` table identifies and authorizes software integrations which produce or consume Learning Record
Store data. Consumers such as research projects will set the `datashare` flag as well as `read_permission` to
gain access to any data source associated with the Tenant (except as denied by user opt-outs).
"""
class Credential(Base):
    __tablename__ = 'credentials'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    key = db.Column(db.String(255), nullable=False)
    secret = db.Column(db.String(255), nullable=False)
    read_permission = db.Column(db.Boolean, nullable=False, default=False)
    write_permission = db.Column(db.Boolean, nullable=False, default=False)
    datashare = db.Column(db.Boolean, nullable=False, default=False)

    tenant_id = db.Column(db.Integer, db.ForeignKey('tenants.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    tenant = db.relationship('Tenant', backref=db.backref('credentials', lazy='dynamic'))

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
        return '<Credential %r>' % (self.name)
