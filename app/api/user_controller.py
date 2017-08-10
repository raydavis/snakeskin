from flask import Blueprint, jsonify

from app import app
from app.models.tenant import Tenant
from app.models.user import User


user = Blueprint('user', __name__, url_prefix='/api/tenant/<tenant_id>/user/<external_id>')

@user.route('/')
def show_user_profile(tenant_id, external_id):
    tenant = Tenant.query.filter_by(id=tenant_id).first()
    user = User.query.filter_by(tenant_id=tenant_id, external_id=external_id).first()
    return jsonify({
        'tenant': tenant.short_profile(),
        'user': user.full_profile()
    })

@user.route('/data_sources')
def show_user_data_sources(tenant_id, external_id):
    user = User.query.filter_by(tenant_id=tenant_id, external_id=external_id).first()
    result = user.get_data_sources()
    return jsonify(result)

@user.route('/recent_activities')
def show_user_recent_activities(tenant_id, external_id):
    user = User.query.filter_by(tenant_id=tenant_id, external_id=external_id).first()
    result = user.get_recent_activities()
    return jsonify(result)

@user.route('/top_activities')
def show_user_top_activities(tenant_id, external_id):
    user = User.query.filter_by(tenant_id=tenant_id, external_id=external_id).first()
    result = user.get_top_activities()
    return jsonify(result)

@user.route('/total_activities')
def show_user_total_activities(tenant_id, external_id):
    user = User.query.filter_by(tenant_id=tenant_id, external_id=external_id).first()
    result = user.get_total_activities()
    return jsonify(result)
