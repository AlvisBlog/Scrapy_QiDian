# -*- coding: utf-8 -*-

url='https://book.qidian.com/ajax/comment/index?_csrfToken=lIC0fVZFexAn5wndoz7Jkc7LVDFOD7pbp4NeuEF1&bookId=1003580078'

chapter_url='https://book.qidian.com/ajax/book/category?_csrfToken=lIC0fVZFexAn5wndoz7Jkc7LVDFOD7pbp4NeuEF1&bookId=1004608738'

#content_url='https://read.qidian.com/ajax/chapter/chapterInfo?_csrfToken=lIC0fVZFexAn5wndoz7Jkc7LVDFOD7pbp4NeuEF1&bookId=1010734492&chapterId=389530162&authorId=4362771'

content_url='https://read.qidian.com/ajax/chapter/chapterInfo?_csrfToken=lIC0fVZFexAn5wndoz7Jkc7LVDFOD7pbp4NeuEF1&bookId=1010136878&chapterId=401510060&authorId=4362112'

content_url2='https://read.qidian.com/ajax/chapter/chapterInfo?_csrfToken=lIC0fVZFexAn5wndoz7Jkc7LVDFOD7pbp4NeuEF1&bookId=1010136878&chapterId=387986683&authorId=4362112'
import requests

import json

response=requests.get(content_url)
response2=requests.get(content_url2)

html=response.text.encode('ISO-8859-1').decode('utf8')
html2=response2.text.encode('ISO-8859-1').decode('utf8')

content=json.loads(html)
content2=json.loads(html2)

chapterInfo=content['data']['chapterInfo']
chapterInfo2=content2['data']['chapterInfo']


for key,value in chapterInfo2.items():
    print(key,value)
try:
    chapter_price=chapterInfo2['price']
except Exception as e:
    chapter_price=0
print(chapter_price)
# chapter_ccid=chapterInfo['ccid']
# print(chapter_ccid)
# chapter_id=chapterInfo['chapterId']
# print(chapter_id)
# chapter_name=chapterInfo['chapterName']
# print(chapter_name)
# chapter_content=chapterInfo['content']
# print(chapter_content)
# chapter_freeStatus=chapterInfo['freeStatus']
# print(chapter_freeStatus)
# chapter_vipStatus=chapterInfo['vipStatus']
# print(chapter_vipStatus)
# chapter_pubdate=chapterInfo['updateTime']
# print(chapter_pubdate)
# chapter_wordsCount=chapterInfo['wordsCount']
# print(chapter_wordsCount)
# chapter_volumeId=chapterInfo['volumeId']
# print(chapter_volumeId)
