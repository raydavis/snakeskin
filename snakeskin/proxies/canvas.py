import requests
import urllib

from flask import current_app as app


def get_user_for_sis_id(canvas_instance, sis_id):
    path = '/api/v1/users/sis_user_id:UID:{}'.format(sis_id)
    return request(canvas_instance, path)


def request(canvas_instance, path):
    url = urllib.parse.urlunparse([
      canvas_instance.scheme,
      canvas_instance.domain,
      urllib.parse.quote(path),
      '',
      '',
      ''
    ])
    auth_headers = {'Authorization': 'Bearer {}'.format(canvas_instance.token)}

    try:
        response = requests.get(url, headers=auth_headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        app.logger.error(e)
        return None
    else:
        return response
