from app import db
from app.models.base import Base


"""
The `statements` table keeps track of learning activities.
"""
class Statement(Base):
    __tablename__ = 'statements'

    uuid = db.Column(db.String(255), nullable=False, primary_key=True)
    statement = db.Column(db.JSON, nullable=False)
    verb = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    activity_type = db.Column(db.String(255), nullable=False)
    actor_type = db.Column(db.String(255), nullable=False)
    statement_type = db.Column(db.String(255), nullable=False)
    statement_version = db.Column(db.String(255), nullable=False)
    voided = db.Column(db.Boolean, nullable=False, default=False)

    tenant_id = db.Column(db.Integer, db.ForeignKey('tenants.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    tenant = db.relationship('Tenant', backref=db.backref('statements', lazy='dynamic'))

    credential_id = db.Column(db.Integer, db.ForeignKey('credentials.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    credential = db.relationship('Credential', backref=db.backref('statements', lazy='dynamic'))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('statements', lazy='dynamic'))

    def __init__(self, uuid, statement, verb, timestamp, activity_type, actor_type, statement_type, statement_version, voided, tenant, credential, user):
        self.name = name
        self.uuid = uuid
        self.statement = statement
        self.verb = verb
        self.timestamp = timestamp
        self.activity_type = activity_type
        self.actor_type = actor_type
        self.statement_type = statement_type
        self.statement_version = statement_version
        self.voided = voided
        self.tenant = tenant
        self.credential = credential
        self.user = user

    def __repr__(self):
        return '<Statement %r>' % (self.uuid)

    def serialize(self):
        return self.statement
