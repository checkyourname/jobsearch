# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobsearchItem(scrapy.Item):
    # define the fields for your item here like:

    company_name=scrapy.Field()
    job_name=scrapy.Field()
    working_city=scrapy.Field()
    salary=scrapy.Field()
    release_time=scrapy.Field()



