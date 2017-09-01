# -*- coding: utf-8 -*-
import scrapy


class IssfDataSpider(scrapy.Spider):
    name = "issf-data"
    allowed_domains = ["www.issf-sports.org"]
    start_urls = ["http://www.issf-sports.org/competitions/results.ashx"]

    def parse(self, response):
    	competitions_lsts = response.xpath("//div[contains(@class, 'cship_list_wrapper')]/table/tr/td[3]/a/@href").extract()
    	for competition in competitions_lsts:
    		yield scrapy.Request("http://www.issf-sports.org/" + competition, callback=self.parse_competitions)
    def parse_competitions(self, response):
    	competition_results_lst = response.xpath("//a/@href").extract()
    	for result in competition_results_lst:
    		if "detail.ashx" in result and "resultkey" in result:
    			yield scrapy.Request("http://www.issf-sports.org/" + result, callback=self.parse_competion_results)

    def parse_competion_results(self, response):
    	athletes_lst = response.xpath("//a[contains(@href, 'reskey')]/@href")
    	print(len(athletes_lst))

    