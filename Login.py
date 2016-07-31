# coding: utf8
# Author: flytrap
# Create:
from Config import LOGIN_URL, LOGIN_DATA, HEADERS
from Functions import post


def login(re_login=False):
    if HEADERS and re_login is False:
        return
    ret = post(LOGIN_URL, LOGIN_DATA)
    if ret is None:
        raise Exception('Login error')
    HEADERS['Authorization'] = 'JWT ' + ret.get('access_token')


if __name__ == '__main__':
    login()
    print HEADERS
