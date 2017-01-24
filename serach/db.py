#!/usr/bin/env python
#coding:utf-8

import redis
db = redis.StrictRedis(host='127.0.0.1', port=6379)

class RedisDB:
    client =db

    @classmethod
    def setk(self, key, value):
        self.client.hset(key, **value)

    @classmethod
    def getk(self , key):
        return self.client.hgetall(key)


