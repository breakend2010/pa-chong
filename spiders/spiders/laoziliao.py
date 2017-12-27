# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.selector import Selector
from spiders.items import LaoziliaoSpidersItem


class LaoziliaoSpider(scrapy.Spider):
    name = "laoziliao"
    custom_settings = {
        'ITEM_PIPELINES': {
            'spiders.pipelines.JsonWriterPipeline': 400
        }
    }
    allowed_domains = ["www.laoziliao.net"]
    start_urls = ['http://www.laoziliao.net/rmrb/1949-02-06-1']

    def parse(self, response):
        yield scrapy.Request(response.url, callback=self.parse_detail)

    def parse_detail(self, response):
        '''parse_detail
        '''

        articles = re.compile(
            r'\W*(?=<h2)').split(
            response.xpath('//*[@id="box"]/div[1]/div').extract()[0])
        for article in articles:
            if 'h2' in article and 'article' in article:
                # self.log.info("".join(Selector(text=article).xpath(
                #     '//div/text()').extract()))
                item = LaoziliaoSpidersItem()
                item['title'] = Selector(text=article).xpath(
                    '//h2/text()').extract()
                item['content'] = "".join(Selector(text=article).xpath(
                    '//div/text()').extract())
                item['link'] = response.url
                yield item
