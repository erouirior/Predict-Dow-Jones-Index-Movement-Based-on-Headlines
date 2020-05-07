#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 14:50:21 2020

@author: yliu15
"""
### Craw data from reddit through year 2008-01-01 to 2020-04-30
import requests
import json
import csv
import time
import datetime

def getPushshiftData(after, before, sub):
    url = 'https://api.pushshift.io/reddit/search/submission/?size=1000&after='+str(after)+'&before='+str(before)+'&subreddit='+str(sub)
    #print(url)
    r = requests.get(url)
    data = json.loads(r.text)
    return data['data']
def collectSubData(subm):
    subData = list() #list to store data points
    title = subm['title']
    #url = subm['url']
    #try:
    #    flair = subm['link_flair_text']
    #except KeyError:
    #    flair = "NaN"    
    #author = subm['author']
    sub_id = subm['id']
    score = subm['score']
    created = datetime.datetime.fromtimestamp(subm['created_utc']) #1520561700.0
    numComms = subm['num_comments']
    #permalink = subm['permalink']
    
    #subData.append((sub_id,title,url,author,score,created,numComms,permalink,flair))
    subData.append((sub_id,title,score,created,numComms))
    subStats[sub_id] = subData
#Subreddit to query
sub='worldnews'
#before and after dates from 2008/01/01  to 2020/04/30
time_range = {'2008-01-01': 1199145600, '2009-01-01': 1230768000,\
             '2010-01-01': 1262304000, '2011-01-01': 1293840000,\
             '2012-01-01': 1325376000, '2013-01-01': 1356998400,\
             '2014-01-01': 1388534400, '2015-01-01': 1420070400,\
             '2016-01-01': 1451606400, '2017-01-01': 1483228800,\
             '2018-01-01': 1514764800, '2019-01-01': 1546300800,\
             '2018-01-01': 1514764800, '2019-01-01': 1546300800,\
             '2020-05-01': 1588291200}

before = time_range['2015-01-01'] 
after = time_range['2014-01-01'] 

subCount = 0
subStats = {}
data = getPushshiftData(after, before, sub)
while len(data) > 0:
    for submission in data:
        collectSubData(submission)
        subCount+=1
    # Calls getPushshiftData() with the created date of the last submission
    #print(len(data))
    #print(str(datetime.datetime.fromtimestamp(data[-1]['created_utc'])))
    after = data[-1]['created_utc']
    data = getPushshiftData(after, before, sub)
    
print(len(data))
def updateSubs_file():
    upload_count = 0
    location = "./stocknews/new_reddit_"
    print("input filename of submission file, please add .csv")
    filename = input()
    file = location + filename
    with open(file, 'w', newline='', encoding='utf-8') as file: 
        a = csv.writer(file, delimiter=',')
        headers = ["Post ID","Title","Score","Publish Date","Total No. of Comments"]
        a.writerow(headers)
        for sub in subStats:
            a.writerow(subStats[sub][0])
            upload_count+=1
            
        print(str(upload_count) + " submissions have been uploaded")
updateSubs_file()