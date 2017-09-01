#!/usr/bin/env python
# encoding: utf-8

from scrapy.crawler import CrawlerProcess

from spiders.spiders.issf_data import IssfDataSpider
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    # 'LOG_LEVEL' : 'CRITICAL'
    'LOG_LEVEL' : 'INFO'
})

process.crawl(IssfDataSpider)
process.start()
