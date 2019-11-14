# *_*coding:utf-8 *_*
import re
import sys
import utils.tools as tools
import pymongo
import requests
import time
myclient = pymongo.MongoClient("127.0.0.1")
mydb = myclient["task_url_db"]
mycol = mydb["task_url"]
mycol.create_index([("url", 1)], unique=True)
data_cursor = mydb["task_info"]
data_cursor.create_index([("url", 1)], unique=True)

headers = {
    "client":"android",
    "App-Version":"6.27",
    "Host":"api-litchi.jstv.com",
    "User-Agent":"okhttp/3.9.0",
}

def remove_task(condition):
    result = mycol.delete_one(condition)
    if result:
        print("移除任务")
def save_info(data_info):
    result = data_cursor.insert(data_info)
    if result:
        print("存储成功")
def extract_info(json_data):
    try:
        data_infos = json_data["Data"]["List"]
        for data_info in data_infos:
            data = data_info["Data"]
            title = data["Title"]
            content = data["Summary"]
            img_url = data["Photo"]
            url = data["Href"]
            print(url)
            video_url = data["VideoUrl"]
            time_regx = r"/(\d+).shtml"
            time_str = tools.get_info(url, time_regx, fetch_one=True)
            release_time = tools.timestamp_to_date(time_str[:-3])
            like_count = data_info["LikeCount"]
            comment_cnt = data_info["CommentCnt"]
            # print(title)
            # print(release_time)
            # print(content)
            # print(img_url)
            # print(video_url)
            # print(like_count)
            # print(comment_cnt)
            data_info = {
                "url":url,
                "title":title,
                "release_time":release_time,
                "content":content,
                "img_url":img_url,
                "video_url":video_url,
                "like_count":like_count,
                "comment_cnt":comment_cnt
            }
            save_info(data_info)
    except Exception as e:
        print(e)
def parser_info():
    while True:
        url_list = list(mycol.find({}))
        if url_list:
            for url_info in url_list:
                url = url_info["url"]
                print(url)
                print("-" * 100)
                json_data = requests.get(url=url, headers=headers).json()
                extract_info(json_data)
                remove_task({"url":url})
        else:
            time.sleep(2)

if __name__ == '__main__':
    parser_info()