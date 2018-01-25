#! /usr/bin/env python
# -*- coding: utf-8 -*-

# author
# email: shuangyang.qian@easystack.cn
# irc: qsyqian


import sys
import MySQLdb


class TransferMoney(object):

    def __init__(self, conn):
        self.conn = conn

    def check_account_available(self, accountid):
        cursor = self.conn.cursor()
        try:
            sql = "select * from account where acctid=%s" % accountid
            print "check_account_available:" + sql
            cursor.execute(sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception('账号不存在%s' % accountid)
        finally:
            cursor.close()

    def has_enough_money(self, accountid, money):
        cursor = self.conn.cursor()
        try:
            sql = "select * from account where acctid=%s and money>=%s"\
                  % (accountid, money)
            print "has_enough_money:" + sql
            cursor.execute(sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception('账号%s没有足够的钱' % accountid)
        except Exception as e:
            print e
        finally:
            cursor.close()

    def reduce_money(self, accountid, money):
        cursor = self.conn.cursor()
        try:
            sql = "update account set money=money-%s where acctid=%s" \
                  % (money, accountid)
            print "reduce_money:" + sql
            cursor.execute(sql)
            if cursor.rowcount != 1:
                raise Exception('账号%s减款失败' % accountid)
        except Exception as e:
            print e
        finally:
            cursor.close()

    def add_money(self, accountid, money):
        cursor = self.conn.cursor()
        try:
            sql = "update account set money=money+%s where acctid=%s" \
                  % (money, accountid)
            print "reduce_money:" + sql
            cursor.execute(sql)
            if cursor.rowcount != 1:
                raise Exception('账号%s加款失败' % accountid)
        except Exception as e:
            print e
        finally:
            cursor.close()

    def transfer(self, source_accountid, target_accountid, money):
        try:
            self.check_account_available(source_accountid)
            self.check_account_available(target_accountid)
            self.has_enough_money(source_accountid, money)
            self.reduce_money(source_accountid, money)
            self.add_money(target_accountid, money)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e


class getConnection(object):

    def connection(self, host, user, passwd, port, db):
        conn = MySQLdb.Connect(host=host,
                               user=user,
                               passwd=passwd,
                               port=port,
                               db=db)

        return conn


if __name__ == "__main__":
    source_accountid = sys.argv[1]
    target_accountid = sys.argv[2]
    money = sys.argv[3]

    host = '127.0.0.1'
    user = 'root'
    passwd = 'passw0rd'
    port = 3306
    db = 'imooc_test'

    gc = getConnection()
    conn = gc.connection(host, user, passwd, port, db)
    tr_money = TransferMoney(conn)

    try:
        tr_money.transfer(source_accountid, target_accountid, money)
    except Exception as e:
        print "出现一些问题" + str(e)
    finally:
        conn.close()
