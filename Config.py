# coding: utf8
# Author: flytrap
# Create:

# 登录url
import os

ZOOM_EYE_URL = 'https://api.zoomeye.org'
LOGIN_URL = '/'.join((ZOOM_EYE_URL, 'user', 'login'))

USERNAME = 'hiddes@126.com'
PASSWORD = 'zhidao.404'
# 登录信息
LOGIN_DATA = {
    'username': USERNAME,
    'password': PASSWORD
}

HEADERS = {}

HOST_QUERY_KEYS = ['app', 'device', 'service', 'os', 'port', 'country', 'city']
WEB_QUERY_KEYS = ['webapp', 'component', 'framework', 'frontend', 'server', 'waf', 'os', 'country', 'city']
RESULT_KEYS = ['matches', 'facets', 'total']
