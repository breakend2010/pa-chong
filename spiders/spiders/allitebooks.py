# -*- coding: utf-8 -*-
import scrapy
from spiders.items import AllitebooksItem


class AllitebooksSpider(scrapy.Spider):
    name = "allitebooks"
    allowed_domains = ["www.allitebooks.com"]
    start_urls = [
        'http://www.allitebooks.com/page/{}/'.format(i) for i in range(1, 742)]

    custom_settings = {
        'ITEM_PIPELINES': {
            'spiders.pipelines.AllitebooksPipeline': 1
        },
        'FILES_STORE': '/home/zhoub/python/allitebooks'
    }

    def parse(self, response):
        '''//*[@id="post-28550"]/div[2]/header/h2/a
        '''
        hrefs = response.xpath("//header/h2/a/@href").extract()
        for href in hrefs:
            self.logger.info(href)
            yield scrapy.Request(href, callback=self.parse_detail)

    def parse_detail(self, response):

        book_file = response.xpath(
            '//*[@id="main-content"]/div/article/footer/div/span[1]/a/@href') \
            .extract_first()
        self.logger.info(book_file.split('/')[-1])
        item = AllitebooksItem()
        item["file_urls"] = [book_file]
        item['title'] = book_file.split('/')[-1].replace(' ', '-')
        yield item
