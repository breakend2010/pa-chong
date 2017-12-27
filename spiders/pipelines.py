# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import mysql.connector as MySQLdb
import json
from scrapy.pipelines.files import FilesPipeline
import scrapy


class SpidersPipeline(object):
    pass
    # def __init__(self):
    #     self.conn = MySQLdb.connect(host='192.168.2.224',
    #           user='pa_chong', password='po1fn9U0NxOVVYgN',
    #           database='pa_chong', charset="utf8", use_unicode=True)
    #     self.cursor = self.conn.cursor()

    # def process_item(self, item, spider):
    #     try:
    #         self.cursor.execute("""INSERT INTO anjuke (
    #                             title, arc,
    #                             composition, price, floor, location, year,
    #                             head_to, decoration, district, block,address,
    #                             created_at, link) VALUES
    #                     (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s, %s, %s)
    #                        """,
    #                    (item['title'],
    #                     item['arc'] ,
    #                     item['composition'],
    #                     item['price'],
    #                     item['floor'],
    #                     item['location'],
    #                     item['year'],
    #                     item['head_to'],
    #                     item['decoration'],
    #                     item['block'],
    #                     item['district'],
    #                     item['address'],
    #                     item['created_at'],
    #                     item['link']))
    #         self.conn.commit()
    #     except MySQLdb.Error as e:
    #         print("Something went wrong: {}".format(e))
    #     return item


class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open(spider.name + '.json', 'a')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item


class AsiaShootingPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        return [
            scrapy.Request(x, meta=item)
            for x in item.get(self.files_urls_field, [])
        ]

    def file_path(self, request, response=None, info=None):
        # start of deprecation warning block (can be removed in the future)
        def _warn():
            from scrapy.exceptions import ScrapyDeprecationWarning
            import warnings
            warnings.warn('file_key(url) method is deprecated, use '
                          'file_path(request, response=None, info=None)',
                          category=ScrapyDeprecationWarning, stacklevel=1)

        # check if called from file_key with url as first argument
        if not isinstance(request, scrapy.Request):
            _warn()
            url = request
        else:
            url = request.url

        # detect if file_key() method has been overridden
        if not hasattr(self.file_key, '_base'):
            _warn()
            return self.file_key(url)
        # end of deprecation warning block
        file_name = request.meta['title']
        # change to request.url after deprecation
        media_ext = url.split('/')[-1]
        return '%s' % file_name + media_ext.replace(' ', '_')


class AllitebooksPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        return [
            scrapy.Request(x, meta=item)
            for x in item.get(self.files_urls_field, [])
        ]

    def file_path(self, request, response=None, info=None):
        # start of deprecation warning block (can be removed in the future)
        def _warn():
            from scrapy.exceptions import ScrapyDeprecationWarning
            import warnings
            warnings.warn('file_key(url) method is deprecated, use '
                          'file_path(request, response=None, info=None)',
                          category=ScrapyDeprecationWarning, stacklevel=1)

        # check if called from file_key with url as first argument
        if not isinstance(request, scrapy.Request):
            _warn()
            url = request
        else:
            url = request.url

        # detect if file_key() method has been overridden
        if not hasattr(self.file_key, '_base'):
            _warn()
            return self.file_key(url)
        # end of deprecation warning block
        file_name = request.meta['title']
        # change to request.url after deprecation
        # media_ext = url.split('/')[-1]
        return '%s' % file_name  # + media_ext.replace(' ', '_')
