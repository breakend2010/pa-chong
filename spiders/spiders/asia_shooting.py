# -*- coding: utf-8 -*-
import scrapy
from spiders.items import AsiaShootingItem


class AsiaShootingSpider(scrapy.Spider):
    name = "asia-shooting"
    allowed_domains = ["www.asia-shooting.org"]

    custom_settings = {
        'ITEM_PIPELINES': {
            'spiders.pipelines.AsiaShootingPipeline': 1
        }
    }

    start_urls = ['http://192.168.2.224:8081/asia-shooting.html']

    def parse(self, response):

        tables = response.xpath("//html/body/div/table")

        for table in tables:
            title = "".join(table.xpath(
                "./tbody/tr/td[2]/text()").extract_first().split())
            urls = []
            slectors = table.xpath("./tbody/tr/td[3]/a/@href").extract()
            for selector in slectors:
                if not selector.startswith("http://www.issf-sports.org/"):
                    urls.append('http://www.asia-shooting.org' + selector)

            other_selectors = table.xpath(
                './tbody/tr/td/div/a/@href').extract()
            for selector in other_selectors:
                urls.append('http://www.asia-shooting.org' + selector)

            item = AsiaShootingItem()
            item["file_urls"] = urls
            item['title'] = title.replace('/', '-')
            yield item
