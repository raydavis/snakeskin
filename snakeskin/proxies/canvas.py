import requests
import urllib


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

    response = requests.get(url, headers=auth_headers)
    return response
