# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from newspider.items import NewspiderItem
# Scrapy中用作登录使用的一个包
from scrapy import FormRequest
class AutohomeSpider(CrawlSpider):
    name = 'autohome'
    allowed_domains = ['cuiqingcai.com']
    start_urls = ['https://cuiqingcai.com/']

    rules = (
        Rule(LinkExtractor(allow=('\.html',)), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response.url)
        item = NewspiderItem()
        item['categoryLink'] = response.url
        yield item