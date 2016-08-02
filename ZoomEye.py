# coding: utf8
# Author: hidden
# Create: 2016.08.01
# import os
from GetResults import HostRequest, WebRequest
from Config import LOGIN_DATA, USERNAME, PASSWORD, HEADERS, AUTO_FILED
from Login import login

GET_TYPE = {'host': HostRequest, 'web': WebRequest}


class ZoomEye(object):
    def __init__(self, is_login=False, username='', password='', header=None, get_type=None):
        self.login = is_login
        self.username = username
        self.password = password
        self.header = header if header else dict()
        self.get_type = get_type if get_type else GET_TYPE.keys()[0]

        self.query_info = dict()
        self.init_config()

    def init_config(self):
        if self.login is True:
            if AUTO_FILED in self.header and isinstance(self.header, dict):
                HEADERS[AUTO_FILED] = self.header.get(AUTO_FILED)
            elif self.username and self.password:
                LOGIN_DATA['username'] = self.username
                LOGIN_DATA['password'] = self.password
            else:
                if LOGIN_DATA.get('username') == USERNAME and LOGIN_DATA.get('password') == PASSWORD:
                    raise Exception('Must input password and username')
            login()

    @staticmethod
    def set_dict_info(dict_info, item, step=':'):
        """
        往字典中添加数据
        :param dict_info: 必须是字典
        :param item: 可迭代对象（嵌套数组，则取前两个元素）
        :param step: 迭代对象中为字符串时， 切割符
        :return:
        >>> d = {}
        >>> set_dict_info(d, ('1:1','2:2'))
        """
        if not isinstance(dict_info, dict):
            return
        for i in item:
            if isinstance(i, (tuple, list)):
                if len(i) < 2:
                    continue
                text = i
            else:
                text = i.split(':')
                if len(text) < 2:
                    continue
            dict_info[text[0]] = text[1]

    def set_req_info(self, info, step=' '):
        """
        设置请求包中所包含的信息
        :param info: 按照一定格式排列的 字符串||可迭代对象||字典
        :param step: 指定字符串中的分割符（默认空格，只有字符串时才生效）
        :return:
        """
        if isinstance(info, dict):
            self.query_info.update(info)
        elif isinstance(info, basestring):
            self.set_dict_info(self.query_info, info.split(step))
        elif isinstance(info, (list, tuple)):
            self.set_dict_info(self.query_info, info)
        else:
            raise Exception('Error args')

    def start(self):
        """
        工作函数
        :return:
        """
        assert self.get_type in GET_TYPE, 'get type error'
        req = GET_TYPE.get(self.get_type)()


if __name__ == '__main__':
    ze = ZoomEye(is_login=True, username='hidden', password='test')
    print ze
