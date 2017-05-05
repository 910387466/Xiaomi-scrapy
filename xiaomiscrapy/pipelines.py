# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.files import FilesPipeline
from scrapy.utils.project import get_project_settings
import urllib
# from  scrapy.contrib.pipeline.media import MediaPipeline

class DuplicatesPipeline(object):

    def __init__(self):
        self.url_seen = set()

    def process_item(self,item,spider):
        if item['appID'] in self.url_seen:
            raise DropItem('Duplicate item found:%s'% item )
        else:
            self.url_seen.add(item['appID'])
            return item


class XiaomiscrapyPipeline(object):
    """
    为 写入到json的文件中
    """
    def __init__(self):
        self.file = codecs.open('items.json','wb',encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item))+'\n'
        self.file.write(line.decode('unicode_escape'))
        return item

class Xiaomi2scrapyPipeline(FilesPipeline):
    """
    为把下载的文件下载到本地。
    """
    @classmethod
    def get_media_requests(self, item, info):
        url = item['xiazaidizhi']
        name = item['mingzi']
        # yield scrapy.Request(url)
        settings = get_project_settings()
        settingslujing = settings['FILES_STORE']
        apksave = settingslujing.decode('utf-8')+name+'.apk'
        urllib.urlretrieve(url,apksave)
        # print url,name,'apk------download--------save ------ok'

    # def item_completed(self, results, item, info):
    #     print item['xiazaidizhi']


