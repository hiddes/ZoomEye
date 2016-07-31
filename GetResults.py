# coding: utf8
# Author: hidden
# Create:
from Functions import get
from Config import HOST_QUERY_KEYS, WEB_QUERY_KEYS, RESULT_KEYS


class BaseRequest(dict):
    def __init__(self, *args, **kwargs):
        super(BaseRequest, self).__init__(*args, **kwargs)
        self.page = 1
        self.url = ''
        self.facets = ''
        self.header = {}
        self.keys_worlds = set(HOST_QUERY_KEYS + WEB_QUERY_KEYS)

    def set_attr(self, key, kwargs):
        """
        设置传递的参数为属性，并在字典中删除该值
        :param key:
        :param kwargs:
        :return:
        """
        if key in kwargs and key in self.keys_worlds:
            self.__dict__[key] = kwargs.get(key)
            try:
                del self[key]
            except KeyError:
                pass

    def init_request(self, **kwargs):
        """
        初始化 请求包
        :param kwargs:
        :return:
        """
        for k in kwargs.keys():
            self.set_attr(k, kwargs)

    def send_request(self):
        if not self.url or not self.header:
            raise Exception('Please use HostRequest or WebRequest')
        query = ' '.join('%s:%s' % (k, v) for k, v in self.__dict__.iteritems() if k in self.keys_worlds)
        if not query:
            raise Exception('Not request')
        if self.facets:
            url = '&'.join(('query:%s' % query, 'page:%s' % self.page, 'facets:%s' % self.facets))
        else:
            url = '&'.join(('query:%s' % query, 'page:%s' % self.page))
        result = get(''.join((self.url, '?', url)), self.header)

    def get_result(self, page):
        self.page = page
        result = self.send_request()


class HostRequest(BaseRequest):
    def __init__(self, *args, **kwargs):
        super(HostRequest, self).__init__(args, kwargs)
        self.keys_worlds = HOST_QUERY_KEYS


class WebRequest(BaseRequest):
    def __init__(self, *args, **kwargs):
        super(WebRequest, self).__init__(args, kwargs)
        self.keys_worlds = WEB_QUERY_KEYS


def main():
    bq = BaseRequest()
    print len(bq)


if __name__ == '__main__':
    main()
