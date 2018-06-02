# -*- coding: utf-8 -*-
import time

import pymysql

from SpiderQiDian import settings

class Spider_qidian_Pipeline(object):

    def __init__(self):

        '''初始化连接数据库'''

        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            port=3306,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()

        print("数据库连接成功")

    def process_item(self, item, spider):

        try:
            self.cursor.execute(
                "insert into chapter_info (novel_id,chapter_volumeId,chapter_ccid,chapter_id,chapter_name,chapter_content,chapter_wordsCount,chapter_freeStatus,chapter_vipStatus,chapter_pubdate,chapter_price)"
                "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                [item['novel_id'], item['chapter_volumeId'], item['chapter_ccid'], item['chapter_id'],
                 item['chapter_name'], item['chapter_content'],
                 item['chapter_wordsCount'], item['chapter_freeStatus'], item['chapter_vipStatus'], item['chapter_pubdate'],
                 item['chapter_price'],])

            # 提交sql语句
            self.connect.commit()

        except Exception as error:

            with open("chapter.log", "a+") as f:

                f.write(time.strftime("%Y-%m-%d %H:%M:%S") + "插入语句执行异常:%s" % error)

        return item
