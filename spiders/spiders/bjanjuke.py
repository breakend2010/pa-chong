# -*- coding: utf-8 -*-
import scrapy
from spiders.items import AnjukeSpidersItem


class BjanjukeSpider(scrapy.Spider):
    name = "bjanjuke"
    allowed_domains = ["anjuke.com"]
    start_urls = (
        'http://beijing.anjuke.com/sale/index.html',
    )
    custom_settings = {
        'ITEM_PIPELINES': {
            'spiders.pipelines.SpidersPipeline': 400
        }
    }

    def parse(self, response):
        houseList = response.selector.xpath(
            '//div[contains(@class, "house-title")]/a/@href').extract()
        for houseUrl in houseList:
            yield scrapy.Request(houseUrl, callback=self.parseHouse)
        nextPages = response.selector.xpath(
            '//*[@id="content"]/div[5]/div[5]/a[7]/@href').extract()
        if nextPages:
            nextPage = response.urljoin(nextPages[0])
            print('page_url: ' + nextPage)
            yield scrapy.Request(nextPage, callback=self.parse)

    def parseHouse(self, response):
        item = AnjukeSpidersItem()
        item['title'] = "".join(response.selector.xpath(
            '//h3[@class="long-title"]/text()').extract())  # [0].split())
        item['arc'] = "".join(response.selector.xpath(
            '//*[@id="content"]/div[2]/div[1]/div[3]/div/div/div[1]/div[2]/dl[2]/dd/text()'
        ).extract())
        item['composition'] = "".join(response.selector.xpath(
            '//*[@id="content"]/div[2]/div[1]/div[3]/div/div/div[1]/div[2]/dl[1]/dd/text()').extract()[0].split())
        item['price'] = "".join(response.selector.xpath(
            '//*[@id="content"]/div[2]/div[1]/div[3]/div/div/div[1]/div[3]/dl[2]/dd/text()').extract()[0].split())
        item['floor'] = "".join(response.selector.xpath(
            '//*[@id="content"]/div[2]/div[1]/div[3]/div/div/div[1]/div[2]/dl[4]/dd/text()').extract()[0].split())
        item['location'] = "".join(response.selector.xpath(
            '//*[@id="content"]/div[2]/div[1]/div[3]/div/div/div[1]/div[1]/dl[2]/dd/p/a[2]/text()').extract()[0].split())
        item['year'] = "".join(response.selector.xpath(
            '//*[@id="content"]/div[2]/div[1]/div[3]/div/div/div[1]/div[1]/dl[3]/dd/text()').extract()[0].split())
        item['head_to'] = "".join(response.selector.xpath(
            '//*[@id="content"]/div[2]/div[1]/div[3]/div/div/div[1]/div[2]/dl[3]/dd/text()').extract()[0].split())
        item['decoration'] = "".join(response.selector.xpath(
            '//*[@id="content"]/div[2]/div[1]/div[3]/div/div/div[1]/div[3]/dl[1]/dd/text()').extract()[0].split())
        item['district'] = "".join(response.selector.xpath(
            '//*[@id="content"]/div[2]/div[1]/div[3]/div/div/div[1]/div[1]/dl[2]/dd/p/a[1]/text()').extract()[0].split())
        item['block'] = "".join(response.selector.xpath(
            '//*[@id="content"]/div[2]/div[1]/div[3]/div/div/div[1]/div[1]/dl[1]/dd/a[1]/text()').extract()[0].split())
        item['link'] = response.url
        item['created_at'] = "".join(response.selector.xpath(
            '//*[@id="content"]/div[2]/div[1]/div[3]/h4/span/text()').extract()[0].split())
        item['address'] = "".join(response.selector.xpath(
            '//*[@id="content"]/div[2]/div[1]/div[3]/div/div/div[1]/div[1]/dl[2]/dd/p/text()[2]').extract()[0].split())
        return item
