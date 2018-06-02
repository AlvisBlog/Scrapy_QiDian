# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Spider_qidian_novel_Item(scrapy.Item):

    novel_id = scrapy.Field()

    novel_link = scrapy.Field()

    novel_name = scrapy.Field()

    novel_author = scrapy.Field()

    novel_author_id = scrapy.Field()

    novel_big_category = scrapy.Field()

    novel_small_category = scrapy.Field()

    novel_status = scrapy.Field()

    novel_intro = scrapy.Field()

    novel_word_num = scrapy.Field()

    novel_score = scrapy.Field()

    novel_read_link=scrapy.Field()

    novel_total_chapter = scrapy.Field()

    novel_price=scrapy.Field()


class Spider_qidian_chapter_Item(scrapy.Item):

    novel_id = scrapy.Field()

    chapter_volumeId = scrapy.Field()

    chapter_ccid=scrapy.Field()

    chapter_id = scrapy.Field()

    chapter_name=scrapy.Field()

    chapter_content=scrapy.Field()

    chapter_wordsCount = scrapy.Field()

    chapter_freeStatus=scrapy.Field()

    chapter_vipStatus=scrapy.Field()

    chapter_pubdate=scrapy.Field()

    chapter_price=scrapy.Field()






