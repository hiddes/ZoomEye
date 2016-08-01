# coding: utf8
# Author: hidden
# Create:
import os
import sqlite3
from Config import DEFAULT_DB_PATH


class ResultDB(object):
    """
    保存结果
    """

    def __init__(self, db_name=None):
        if not db_name:
            db_name = DEFAULT_DB_PATH
        self.db_name = db_name
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()
        self.init_db()

    def init_db(self):
        """
        初始化数据库
        :return:
        """
        self.create_table('cache', ['keyworld', 'result'], 'keyworld')

    def create_table(self, table_name, filed_list, index=None):
        self.cur.execute('''SELECT tbl_name FROM sqlite_master WHERE tbl_name="%s"''' % table_name)
        test = self.cur.fetchall()
        if test and len(test[0]) > 0:
            return
        try:
            self.con.execute(
                '''CREATE TABLE IF NOT EXISTS %s(%s)''' % (table_name, ', '.join(filed_list))
            )
            if index and index in filed_list:
                self.con.execute('''CREATE INDEX %s ON %s(%s)''' % (index, table_name, index))
        except Exception, e:
            print e
        finally:
            self.con.commit()

    def save_db(self, table, filed_list):
        """
        保存数据库
        :param table: 数据表
        :param filed_list: 保存的数据列表
        :return:
        """
        assert isinstance(filed_list, list) and len(filed_list) > 0, 'Insert data must list and not empty'
        sql = 'insert into %s values(%s)' % (table, ','.join('?' * len(filed_list[0])))
        for filed_li in filed_list:
            self.cur.execute(sql, filed_li)
        self.con.commit()

    def get_db(self, table, filed=None, where=None):
        if filed is None:
            sql = 'select * from %s' % table
        else:
            if not isinstance(filed, (list, tuple)):
                raise Exception('')
            sql = 'select %s from %s' % (','.join(filed), table)
        if where:
            sql += 'where ' + ' and '.join('%s=%s' % (k, v) for k, v in where.iteritems())
        try:
            self.cur.execute(sql)
            result = self.cur.fetchall()
            return result
        except Exception, e:
            print e


def main():
    result = ResultDB('test.db')
    print result


if __name__ == '__main__':
    main()
