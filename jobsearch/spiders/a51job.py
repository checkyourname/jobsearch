# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jobsearch.items import JobsearchItem
from scrapy.loader import ItemLoader

class A51jobSpider(CrawlSpider):
    name = '51job'
    allowed_domains = ['51job.com']
    start_urls = ['https://search.51job.com']
    first_url="https://search.51job.com/list/010000,000000,0000,00,9,99,%2520,2,1.html"
    rules = (
        Rule(LinkExtractor(allow=("search.51job.com/.*")),callback='parse_job',follow=True),
        Rule(LinkExtractor(allow=r"jobs.51job.com/\d+.html"),follow=True),
    )
    def parse_job(self,response):
        item_loader = ItemLoader(item=JobsearchItem(), response=response)
        for i in range(5,58):

            company=item_loader.add_xpath("company_name","normalize-space(/html/body/div[2]/div[4]/div[%i]/span[1]/a/text())"%i)
            job=item_loader.add_xpath("job_name","normalize-space(/html/body/div[2]/div[4]/div[%i]/p/span/a/text())"%i)
            working=item_loader.add_xpath("working_city","normalize-space(/html/body/div[2]/div[4]/div[%i]/span[2]/text())"%i)
            salary=item_loader.add_xpath("salary","normalize-space(/html/body/div[2]/div[4]/div[%i]/span[3]/text())"%i)
            time=item_loader.add_xpath("release_time","normalize-space(/html/body/div[2]/div[4]/div[%i]/span[4]/text())"%i)

            job_item = item_loader.load_item()
            return job_item


