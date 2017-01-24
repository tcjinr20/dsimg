#!/usr/bin/env python
#coding:utf-8
import cv2

class smilar():
    def __init__(self, filename):
        img = cv2.imread(filename)
        self.s8 = cv2.resize(img, (8,8))

        gary = cv2.cvtColor(self.s8, cv2.COLOR_BGR2GRAY)

        val = cv2.mean(gary)

        self.__feature = []
        # for i in range(len(gary)):
        #     g = gary[i]
        #     for p in g:
        #         if p > val:
        #             self.__feature.append(1)
        #         else:
        #             self.__feature.append(0)

    def feature(self):
        return self.__feature

    def check(self, target):
        sm = 0
        for t, s in zip(target, self.__feature):
            if t != s:
                sm += 1
        #sm 数据越大，越不相似
        return sm
