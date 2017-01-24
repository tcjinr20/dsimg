#!/usr/bin/env python
#coding:utf-8

import getopt
import sys
import os
from db import RedisDB

from smilar import smilar

class Search():
    def __init__(self,filename):
        self.rdb = RedisDB()
        self.smi = smilar(filename)


    def find(self):
        list = self.rdb.getk('feature')
        # fea = eval(list["D:\\WWW\\opencv\\serach\\dataset\\100001.png"])
        # print self.smi.check(fea)
        for fn in list:
            if self.smi.check(eval(list[fn]))<5:
                print fn

if __name__ == '__main__':
    options, args = getopt.getopt(sys.argv[1:], 'f:')
    path = dict(options).get('-f')
    if path:
        if os.path.exists(path):
            sea = Search(path)
            #sea.find()
        else:
            print u'路劲不存在'
    else:
        print u'缺少路径'


