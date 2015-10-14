# -*- coding: utf-8 -*-

import sqlite3 as lite
import time
import os
class database():
    def __init__(self):
        self.con = lite.connect('data.db')
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS Account(sitename TEXT,username TEXT, password TEXT)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS Task(taskid TEXT,taskname TEXT)")
    def _rebuild(self):
        self.cur.execute("DROP TABLE IF EXISTS Account")
        self.cur.execute("DROP TABLE IF EXISTS Task")
        self.cur.execute("CREATE TABLE Account(sitename TEXT,username TEXT, password TEXT)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS Task(taskid TEXT,taskname TEXT)")
        return True
    def _add(self,table,a,b,c='Null'):
        if table == 'Account':
            self.cur.execute('INSERT INTO Account VALUES(?,?,?)',[a,b,c])
        else:
            self.cur.execute('INSERT INTO Task VALUES(?,?)',[a,b])
        return True
    def _del(self,table,a,b):
        self.cur.execute('DELETE FROM %s WHERE %s="%s"' %(table,a,b))
        return True
    def _update(self,table,a,b,c,d):
        self.cur.execute('UPDATE "%s" SET "%s"="%s" WHERE %s="%s"' %(table,a,b,c,d))
        return True
    def _search(self,table,a='Null',b='Null'):
        if a == 'Null':
            self.cur.execute('SELECT * FROM %s' %table)
        else:
            self.cur.execute('SELECT * FROM %s WHERE %s="%s"' %(table,a,b))
        rows = self.cur.fetchall()
        return rows
    def _done(self):
        self.cur.close()
        self.con.commit()
        self.con.close()
        '''
x = database()
x._rebuild()
x._done()
'''
