# -*- coding: utf-8 -*-
import scrapy
import sys


class PcautoSpider(scrapy.Spider):
    name = "pcauto"
    allowed_domains = ["pcauto.com.cn"]
    start_urls = (
        'http://price.pcauto.com.cn/price/q-l1.html',
        #'http://price.pcauto.com.cn/price/q-l2.html',
    )

    def parse(self, response):
        car_list = response.selector.xpath('//div[@class="lieBiao"]') #.extract()
        #print(car_list)
        for index, car in enumerate(car_list):
            print('#####')
            print(car.xpath('div[1]/div[2]/dl/dd[2]//text()').extract()[0])
            print('*****')
