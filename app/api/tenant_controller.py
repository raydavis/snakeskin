from flask import Blueprint, jsonify

from app import app
from app.models.tenant import Tenant


tenant = Blueprint('tenant', __name__, url_prefix='/api/tenant')

@tenant.route('/')
def show_tenants():
    tenants = Tenant.query.all()
    return jsonify([t.short_profile() for t in tenants])

@tenant.route('/<tenant_id>')
def show_tenant_profile(tenant_id):
    tenant = Tenant.query.filter_by(id=tenant_id).first()
    return jsonify(tenant.full_profile())
