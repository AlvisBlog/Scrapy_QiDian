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
                "insert into novel_info (novel_id,novel_name,novel_author,novel_author_id,novel_link,novel_score,novel_intro,novel_big_category,novel_small_category,novel_status,novel_read_link,novel_total_chapter)"
                "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                [item['novel_id'], item['novel_name'], item['novel_author'], item['novel_author_id'],
                 item['novel_link'], item['novel_score'],
                 item['novel_intro'], item['novel_big_category'], item['novel_small_category'], item['novel_status'],
                 item['novel_read_link'],item['novel_total_chapter'],])

            # 提交sql语句
            self.connect.commit()

        except Exception as error:

            with open("novel.log", "a+") as f:

                f.write(time.strftime("%Y-%m-%d %H:%M:%S") + "插入语句执行异常:%s" % error)

        return item
