import os
import requests
from http.cookiejar import LWPCookieJar
from pprint import pprint

def get_pad_list():
    jar = LWPCookieJar('hedgedoc.cookie')
    s = requests.Session()
    res = s.post(
        os.environ['HEDGEDOC_URL'] + '/login',
        cookies=jar,
        data={
            'email': os.environ['HEDGEDOC_USERNAME'],
            'password': os.environ['HEDGEDOC_PASSWORD'],
        },
        headers={
            'Accept-Encoding': 'gzip',
        }
    )
    assert res.status_code == 200
    data = s.get(
        os.environ['HEDGEDOC_URL'] + '/history',
        headers={
            'Accept-Encoding': 'gzip',
        }
    ).json()
    return data['history']
