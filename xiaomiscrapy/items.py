# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaomiscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    gongsi = scrapy.Field()
    mingzi = scrapy.Field()
    fenlei = scrapy.Field()
    pingjia = scrapy.Field()

    ruanjiandaoxiao = scrapy.Field()
    versions = scrapy.Field()
    timeshijian = scrapy.Field()
    baoming = scrapy.Field()
    appID = scrapy.Field()

    xiazaidizhi = scrapy.Field()
    quanxiangquanbu = scrapy.Field()