# coding: utf8
# Author: flytrap
# Create:
import json
import requests

ERROR_LIST = ['error']


def check_error(req):
    if req.status_code != '200':
        print(req.status_code)
        json_data = req.json()
        if json_data.has_key('error'):
            error = json_data.get('error')
            message = json_data.get('message')
            print(error, message)
            return True


def post(url, data, to_json=True):
    """
    post method
    :param url: url
    :param data:
    :param to_json:
    :return:
    """
    try:
        data = json.dumps(data) if to_json else data
    except:
        pass
    # translate http request
    try:
        if url.strip().upper().startswith('HTTPS'):
            req = requests.post(url, data, verify=False)
        else:
            req = requests.post(url, data)
        if check_error(req):
            return
        return req.json() if to_json else req.text
    except Exception, e:
        print(e)


def get(url, headers, to_json=False):
    try:
        if url.strip().upper().startswith('HTTPS'):
            req = requests.get(url, headers, verify=False)
        else:
            req = requests.get(url, headers)
    except Exception, e:
        print(e)
        return
    if check_error(req):
        return
    return req.json() if to_json else req.text
