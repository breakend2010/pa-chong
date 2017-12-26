# -*- coding: utf-8 -*-
import scrapy


class LaoziliaoSpider(scrapy.Spider):
    name = "laoziliao"
    allowed_domains = ["www.laoziliao.net"]
    start_urls = ['http://www.laoziliao.net/']

    def parse(self, response):
        pass
