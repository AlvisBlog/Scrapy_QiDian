# -*- coding: utf-8 -*-

import re
import json

import scrapy
import requests


from SpiderQiDian.items import Spider_qidian_novel_Item,Spider_qidian_chapter_Item

class SpidernovelSpider(scrapy.Spider):


    name = 'spidernovel'




    def start_requests(self):

        for page in range(1,2):

            print("开始获取第%s页的小说"%page)

            visited_url='https://www.qidian.com/all?&page=%s'%page

            yield scrapy.Request(url=visited_url,callback=self.parse_novel_info)




    def parse_novel_info(self, response):

        html=response.text

        #一个页面中展示的所有小说
        novel_list=re.findall('<li data-rid(.*?)</li>',html,re.S)

        #初始化novel_item
        novel_item=Spider_qidian_novel_Item()

        #遍历提取小说数据数据
        for novel in novel_list:

            # 小说ID,从小说链接中截取最后的数字段作为小说ID
            novel_item['novel_id']=re.findall('<h4><a href=".*?info/(.*?)"',novel,re.S)[0]

            # 小说链接
            novel_item['novel_link']="https:"+re.findall('<a href="(.*?)"',novel,re.S)[0]

            # 小说名称
            novel_item['novel_name']=re.findall('<h4>.*?">(.*?)<',novel,re.S)[0]

            # 小说作者
            novel_item['novel_author']=re.findall('<a class="name".*?">(.*?)<',novel,re.S)[0]

            # 小说作者ID
            novel_item['novel_author_id'] = re.findall('<a class="name" href="//my.qidian.com/author/(.*?)"', novel, re.S)[0]

            # 小说大分类
            novel_item['novel_big_category']=re.findall('</em><a href=.*?">(.*?)<',novel,re.S)[0]

            # 小说子分类
            novel_item['novel_small_category']=re.findall('<a class="go-sub-type.*?">(.*?)<',novel,re.S)[0]

            # 小说状态
            novel_item['novel_status']=re.findall('</em><span >(.*?)</span>',novel,re.S)[0]

            # 小说简介
            novel_item['novel_intro']=re.findall('<p class="intro">(.*?)</p>',novel,re.S)[0].strip()

            # 小说评分信息链接:AjaxURL
            score_link='https://book.qidian.com/ajax/comment/index?_csrfToken=lIC0fVZFexAn5wndoz7Jkc7LVDFOD7pbp4NeuEF1&bookId=%s'%novel_item['novel_id']

            # 小说评分
            novel_item['novel_score']=json.loads(requests.get(score_link).text)['data']['rate']

            #小说章节信息链接:AjaxURL
            chapter_info_url = 'https://book.qidian.com/ajax/book/category?_csrfToken=lIC0fVZFexAn5wndoz7Jkc7LVDFOD7pbp4NeuEF1&bookId=%s/'%novel_item['novel_id']

            #提取信息，进行编码转换
            data1 = requests.get(chapter_info_url).text.encode('ISO-8859-1').decode('utf8')

            #json化数据
            data2 = json.loads(data1)

            #所有章节共同的阅读链接
            novel_item['novel_read_link'] = "https:" + data2['data']['firstChapterJumpurl']

            #小说章节数
            novel_item['novel_total_chapter']=data2['data']['chapterTotalCnt']

            yield novel_item

            datas = data2['data']['vs']

            for i in range(len(datas)):

                for chapter in datas[i]['cs']:

                    #章节ID
                    chapter_id = chapter['id']

                    #章节关联的小说ID
                    novel_id = novel_item['novel_id']

                    author_id=novel_item['novel_author_id']

                    chapter_info_url='https://read.qidian.com/ajax/chapter/chapterInfo?_csrfToken=lIC0fVZFexAn5wndoz7Jkc7LVDFOD7pbp4NeuEF1&bookId=%s&chapterId=%s&authorId=%s'%(novel_id,chapter_id,author_id)

                    yield scrapy.Request(url=chapter_info_url,callback=self.parse_chapter_info)




    def parse_chapter_info(self,response):

        chapter_item=Spider_qidian_chapter_Item()

        #单独的章节信息Ajax链接
        content_url=response.url

        #返回状态
        res = requests.get(content_url)

        #返回信息
        html = res.text.encode('ISO-8859-1').decode('utf8')

        #json内容
        content = json.loads(html)

        #章节信息
        chapterInfo = content['data']['chapterInfo']

        #章节对应小说ID
        chapter_item['novel_id']=re.findall('bookId=(.*?)&',content_url,re.S)[0]

        # 章节卷ID
        chapter_item['chapter_volumeId'] = chapterInfo['volumeId']

        #章节chapter_ccid
        chapter_item['chapter_ccid'] = chapterInfo['ccid']

        #章节ID
        chapter_item['chapter_id'] = chapterInfo['chapterId']

        #章节名称
        chapter_item['chapter_name'] = chapterInfo['chapterName']

        #章节内容
        chapter_item['chapter_content'] = chapterInfo['content']

        # 章节字数
        chapter_item['chapter_wordsCount'] = chapterInfo['wordsCount']

        #章节是否免费状态
        chapter_item['chapter_freeStatus'] = chapterInfo['freeStatus']

        #章节是否为VIP章节
        chapter_item['chapter_vipStatus'] = chapterInfo['vipStatus']

        #章节发布时间
        chapter_item['chapter_pubdate'] = chapterInfo['updateTime']

        #章节价格
        try:

            chapter_item['chapter_price']=chapterInfo['price']

        except Exception as e:

            chapter_item['chapter_price']=0


        yield chapter_item
