# coding: utf8
# Author: flytrap
# Create:
from Config import LOGIN_URL, LOGIN_DATA, HEADERS, AUTO_FILED, RET_TOKEN_FILED
from Functions import post


def login(re_login=False):
    if HEADERS.get(AUTO_FILED) and re_login is False:
        return
    ret = post(LOGIN_URL, LOGIN_DATA)
    assert ret and RET_TOKEN_FILED in ret, '%s not get' % RET_TOKEN_FILED
    HEADERS[AUTO_FILED] = 'JWT ' + ret.get('access_token')


if __name__ == '__main__':
    login()
    print(HEADERS)
