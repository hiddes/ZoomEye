# coding: utf8
# Author: flytrap
# Create:

# 登录url
ZOOM_EYE_API_URL = 'https://api.zoomeye.org'
LOGIN_URL = '/'.join((ZOOM_EYE_API_URL, 'user', 'login'))
HOST_SEARCH_URL = '/'.join((ZOOM_EYE_API_URL, 'host', 'search'))
WEB_SEARCH_URL = '/'.join((ZOOM_EYE_API_URL, 'web', 'search'))

USERNAME = 'hidden'
PASSWORD = '123123123'
# 登录信息
LOGIN_DATA = {
    'username': USERNAME,
    'password': PASSWORD
}

RET_TOKEN_FILED = 'access_token'
AUTO_FILED = 'Authorization'

DEFAULT_DB_PATH = 'log/ZoomEye.db'
HEADERS = {AUTO_FILED: None}

HOST_QUERY_KEYS = ['app', 'device', 'service', 'os', 'port', 'country', 'city']
WEB_QUERY_KEYS = ['webapp', 'component', 'framework', 'frontend', 'server', 'waf', 'os', 'country', 'city']
RESULT_KEYS = ['matches', 'facets', 'total']
