# coding: utf8
# Author: hidden
# Create:
import os
import sqlite3


class ResultDB(object):
    """
    保存结果
    """
    def __init__(self, db_name):
        self.db_name = db_name
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()
        self.init_db()

    def init_db(self):
        """
        初始化数据库
        :return:
        """
        if os.path.exists(self.db_name):
            pass
        self.con.execute('CREATE TABLE cache(id INT KEY NOT NULL, keyworld MESSAGE_TEXT , result MESSAGE_TEXT )')
        self.con.execute('CREATE INDEX keyworld ON cache(keyworld)')
        self.con.commit()

    def save_db(self, table, filed_list):
        """
        保存数据库
        :param table: 数据表
        :param filed_list: 保存的字段列表
        :return:
        """
        sql = 'insert into %s values(%s)' % (table, ','.join('?' * len(filed_list)))
        self.cur.execute(sql, filed_list)
        self.con.commit()

    def get_db(self, table, filed):
        sql = 'select %s from %s' % (table, )


def main():
    result = ResultDB('test.db')
    print result


if __name__ == '__main__':
    main()
