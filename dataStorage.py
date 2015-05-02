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
    data = da.read_dailymotion(2)
    print yt.find_one()
    for x in xrange(len(data)):
        for y in data[x][u'list']:
            post_id = dm.insert_one(y).inserted_id
            print post_id

if __name__ == '__main__':
    main()