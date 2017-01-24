#!/usr/bin/env python
#coding:utf-8

import sys
import getopt
import os
import functions as fun
import db
from smilar import smilar

class App:

    curdir = ''

    def __init__(self, path):
        self.root = os.path.realpath(path)
        self.curdir = self.root
        self.rdb = db.RedisDB()
        self.load()

    def run(self):
        if len(self.urllist) > 0:
            path = os.path.join(self.curdir, self.urllist.pop(0))
            if os.path.isfile(path):
                self.analysis(path)

            return self.run()
        else:
            return False

    #批量分析数据
    def analysis(self, filename):
        if fun.isImage(filename):
            dd={}
            dd['key'] = filename
            dd['value'] = smilar(filename).feature()
            self.rdb.setk('feature', dd)

    #文件匹配
    def parse(self):
        pass

    def stop(self):
        pass

    def load(self):
        ddb = self.rdb.getk('analysis')
        self.urllist = eval(ddb[self.curdir])
        # ddir = os.listdir(self.curdir)
        # self.rdb.setk('analysis',{'key':self.curdir , 'value':ddir})

if __name__ == '__main__':
    options, args = getopt.getopt(sys.argv[1:], 'a:', ['p'])
    path = dict(options).get('-a')
    if path:
        if os.path.exists(path):
            app = App(path)
            app.run()

        else:
            print u'路劲不存在'
    else:
        print u'缺少路径'