# -*- coding: utf-8 -*-
"""
Created on Fri May 01 20:28:22 2015

@author: todd
"""

from pymongo import MongoClient
import dataAcquisition as da

client = MongoClient()

db = client.big_data
yt = db.youtube
dm = db.dailymotion
users = db.users

def main():
    data = da.read_dailymotion(5)
    for x in xrange(len(data)):
        for y in data[x][u'list']:
            if dm.find_one({'id': y[u'id']}):
                dm.update({'id':y[u'id']}, y)
                print 'update'
            else:
                dm.insert_one(y)
                print 'insert'
    data = da.read_youtube(5)
    for x in xrange(len(data)):
        for y in data[x][u'items']:
            if yt.find_one({'id': y[u'id']}):
                yt.update({'id':y[u'id']}, y)
                print 'update'
            else:
                yt.insert_one(y)
                print 'insert'

if __name__ == '__main__':
    main()