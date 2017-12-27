# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AnjukeSpidersItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    arc = scrapy.Field()
    composition = scrapy.Field()
    price = scrapy.Field()
    floor = scrapy.Field()
    year = scrapy.Field()
    address = scrapy.Field()
    location = scrapy.Field()
    head_to = scrapy.Field()
    decoration = scrapy.Field()
    district = scrapy.Field()
    block = scrapy.Field()
    link = scrapy.Field()
    created_at = scrapy.Field()


class IssfDataSpidersItem(scrapy.Item):
    project_name = scrapy.Field()
    match_type = scrapy.Field()
    athlete_name = scrapy.Field()
    athlete_nation = scrapy.Field()
    athlete_handedness = scrapy.Field()
    athlete_mastereye = scrapy.Field()
    series = scrapy.Field()
    start_time = scrapy.Field()
    num = scrapy.Field()
    score = scrapy.Field()
    link = scrapy.Field()


class AsiaShootingItem(scrapy.Item):

    file_urls = scrapy.Field()
    title = scrapy.Field()
    files = scrapy.Field()


class AllitebooksItem(scrapy.Item):
    """docstring for AitebooksItem"""
    file_urls = scrapy.Field()
    title = scrapy.Field()
    files = scrapy.Field()


class LaoziliaoSpidersItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    link = scrapy.Field()
