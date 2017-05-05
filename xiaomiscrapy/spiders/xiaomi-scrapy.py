#-*- coding:utf-8 -*-
__author__ = 'Administrator'

import scrapy
import  chardet

from xiaomiscrapy.items import XiaomiscrapyItem

from  scrapy.linkextractors import LinkExtractor
from  scrapy.spiders import CrawlSpider,Rule



class xiaomiSpider(scrapy.Spider):

    name = 'xiaomi'
    allowed_domains= ['app.mi.com']
    #1以下为多页爬取的代码
    # start_urls = ['http://app.mi.com/topList?page=%s' %n for n in xrange(1,4)]
    start_urls = ['http://app.mi.com/topList']
    # print start_urls
    #2以下为的方法为scrapy的多页爬取，但是不至为什么老师报错。
    # rules = (
    #     Rule(LinkExtractor(allow=(r'http://app\.mi\.com/topList\?page=\d+.*')),callback='parse_S'),
    # )
    baseul = 'http://app.mi.com'

    def parse(self, response):
        for sel in response.xpath('/html/body/div[4]/div/div[1]/div[1]/ul/li'):
            url2= self.baseul+sel.xpath('h5/a/@href').extract()[0].encode('utf-8')
            print url2
            yield scrapy.Request(url2,callback=self.parsexiangxi)
            # pass
        newxia = response.xpath('//a[@class="next"]/@href').extract()[0]
        #3下面的代码为多页爬取。
        if newxia:#下一页
            newxiayiye = self.start_urls[0]+newxia.encode('utf-8')
            yield scrapy.Request(newxiayiye,callback=self.parse)
        else:
            pass

    def parsexiangxi(self,response):
        item = XiaomiscrapyItem()
        items = []
        for oner in response.xpath('/html/body/div[4]/div[1]/div[2]'):
            item['gongsi'] = oner.xpath('/html/body/div[4]/div[1]/div[2]/div[1]/div/p[1]/text()').extract()[0]
            item['mingzi'] = oner.xpath('/html/body/div[4]/div[1]/div[2]/div[1]/div/h3/text()').extract()[0]
            item['fenlei'] = oner.xpath('/html/body/div[4]/div[1]/div[2]/div[1]/div/p[2]/text()[1]').extract()[0]
            item['pingjia'] = oner.xpath('/html/body/div[4]/div[1]/div[2]/div[1]/div/span/text()').extract()[0]
            item['xiazaidizhi'] = response.urljoin(self.baseul+oner.xpath('/html/body/div[4]/div[1]/div[2]/div[1]/div/div[2]/a/@href').extract()[0])
            # print xiazaidizhi
            # print gongsi,mingzi,fenlei,pingjia

        for xiangxi in response.xpath('/html/body/div[4]/div[1]/div[2]/div[2]/div/ul[1]'):
            daxiaoID = xiangxi.xpath('li/text()').extract()[1::2]
            item['ruanjiandaoxiao'] =daxiaoID[0]
            item['versions'] = daxiaoID[1]
            item['timeshijian'] = daxiaoID[2]
            item['baoming'] = daxiaoID[3]
            item['appID'] = daxiaoID[4]

            # print ruanjiandaoxiao,versions,timeshijian,bapming,appID

        for quanxiang in response.xpath('/html/body/div[4]/div[1]/div[2]/div[2]/div/ul[2]'):
            quanxianglist = quanxiang.xpath('li/text()').extract()
            quanxiangquanbu = ''
            for i in quanxianglist:
                quanxiangquanbu += i
            item['quanxiangquanbu'] = quanxiangquanbu
        items.append(item)
        return items