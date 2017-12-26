# -*- coding: utf-8 -*-
import scrapy
import re


class LaoziliaoSpider(scrapy.Spider):
    name = "laoziliao"
    allowed_domains = ["www.laoziliao.net"]
    start_urls = ['http://www.laoziliao.net/rmrb/1949-02-06-1']

    def parse(self, response):
        '''//*[@id="33342"]
        //*[@id="box"]/div[1]/div/div[1]
        //*[@id="box"]/div[1]/div/div[2]
        //*[@id="box"]/div[1]/div/div[1]
        '''

        resp = response.xpath('//*[@id="box"]/div[1]/div').extract()
        print(re.compile(r'\W*(?=<h2)').split(resp[0])[3])
