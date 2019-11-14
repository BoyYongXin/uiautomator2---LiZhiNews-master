import re
import sys
import requests
import time
import pymongo
myclient = pymongo.MongoClient("127.0.0.1")
mydb = myclient["task_url_db"]
mycol = mydb["task_url"]
for line in sys.stdin:
    task = re.search(r'>>>(.*?)<<<', line)
    if task:
        print(f"获取的任务url：{task.group(1)}")
        mycol.insert_one({"url":task.group(1)})
