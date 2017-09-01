# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import mysql.connector as MySQLdb

class SpidersPipeline(object):
    pass
    # def __init__(self):
    #     self.conn = MySQLdb.connect(host='192.168.2.224', user='pa_chong', password='po1fn9U0NxOVVYgN', database='pa_chong', charset="utf8", use_unicode=True)
    #     self.cursor = self.conn.cursor()

    # def process_item(self, item, spider):
    #     try:
    #         self.cursor.execute("""INSERT INTO anjuke (
    #                             title, arc,
    #                             composition, price, floor, location, year,
    #                             head_to, decoration, district, block,address, created_at, link)
    #                     VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s, %s, %s)""",
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
