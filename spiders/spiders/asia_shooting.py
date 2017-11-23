# -*- coding: utf-8 -*-
import scrapy
from spiders.items import AsiaShootingItem


class AsiaShootingSpider(scrapy.Spider):
    name = "asia-shooting"
    allowed_domains = ["www.asia-shooting.org"]

    custom_settings = {
        'ITEM_PIPELINES': {
            'spiders.pipelines.AsiaShootingPipeline': 1
            # 'scrapy.pipelines.files.FilesPipeline': 1
        }
    }
    # ITEM_PIPELINES = {'scrapy.pipelines.files.FilesPipeline': 1}
    start_urls = ['http://192.168.2.224:8081/asia-shooting.html']
    def parse(self, response):

        tables = response.xpath("//html/body/div/table")

        for table in tables:
            title = "".join(table.xpath("./tbody/tr/td[2]/text()").extract_first().split())
            urls = []
            slector = table.xpath("./tbody/tr/td[3]/a/@href").extract()
            for file in slector:
                if not file.startswith("http://www.issf-sports.org/"):
                    urls.append('http://www.asia-shooting.org'+file)

            other_files = table.xpath('./tbody/tr/td/div/a/@href').extract()
            for file in other_files:
                urls.append('http://www.asia-shooting.org'+file)

            item = AsiaShootingItem()
            item["file_urls"] = urls #["http://www.asia-shooting.org/news/articlefiles/524-27SEA_Results.zip"]
            item['title']=title.replace('/','-')
            yield item
