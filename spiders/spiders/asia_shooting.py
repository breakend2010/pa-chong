# -*- coding: utf-8 -*-
import scrapy


class AsiaShootingSpider(scrapy.Spider):
    name = "asia-shooting"
    allowed_domains = ["www.asia-shooting.org"]
    start_urls = ['http://www.asia-shooting.org/']

    def parse(self, response):
        pass
