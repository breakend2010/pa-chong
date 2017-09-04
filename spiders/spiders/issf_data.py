# -*- coding: utf-8 -*-
import scrapy

from spiders.items import IssfDataSpidersItem

class IssfDataSpider(scrapy.Spider):
    name = "issf-data"
    custom_settings = {
        'ITEM_PIPELINES': {
            'spiders.pipelines.JsonWriterPipeline': 400
        }
    }
    allowed_domains = ["www.issf-sports.org"]
    start_urls = ["http://www.issf-sports.org/competitions/results.ashx"]


    def parse(self, response):
    	'''
    	get the start_urls results
    	'''
    	competitions_lsts = response.xpath("//div[contains(@class, 'cship_list_wrapper')]/table/tr/td[3]/a/@href").extract()
    	for competition in competitions_lsts:
    		yield scrapy.Request("http://www.issf-sports.org/" + competition, callback=self.parse_competitions)
    def parse_competitions(self, response):
    	'''
    	get the results of "http://www.issf-sports.org/competitions/venue/schedule_by_discipline.ashx?cshipid=1900"
    	'''
    	competition_results_lst = response.xpath("//a/@href").extract()
    	for result in competition_results_lst:
    		if "detail.ashx" in result and "resultkey" in result:
    			yield scrapy.Request("http://www.issf-sports.org/" + result, callback=self.parse_competion_results)

    def parse_competion_results(self, response):
    	'''
    	get the results of "http://www.issf-sports.org/competitions/results/detail.ashx?cshipid=1900&resultkey=Q10000_I_2402171045.1.AR60.0"
    	'''
    	athletes_lst = response.xpath("//a[contains(@href, 'reskey')]/@href").extract()
    	for athlete in athletes_lst:
    		yield scrapy.Request("http://www.issf-sports.org/" + athlete, callback=self.parse_athlete_result)

    def parse_athlete_result(self, response):
    	'''
    	get the results of "http://www.issf-sports.org/pages/resulttargets.ashx?reskey=534843484e4d323331303139393130313b3b313930303b4652335834303b313b513b493b313b303b30"
    	'''
    	scores_list = response.xpath("//a[contains(@href, 'srid')]/@href").extract()
    	for scores in scores_list:
    		yield scrapy.Request("http://www.issf-sports.org/" + scores, callback=self.parse_scores)

    def parse_scores(self, response):
    	'''
    	get the last result of "http://www.issf-sports.org/pages/resulttargetdetails.ashx?srid=742847"
    	'''

    	results = response.xpath("//tr[contains(@class, 'even') or contains(@class, 'odd')]")
    	for result in results:
    		item = IssfDataSpidersItem()
    		item["project_name"] = "".join(response.xpath("//*[@id='content_top']/div/div[2]/div/span/div[1]/div/p[2]/text()").extract())
    		item["match_type"] = "".join(response.xpath("//*[@id='content_top']/div/div[2]/div/span/div[1]/div/p[3]/text()").extract())
    		item["athlete_name"] = "".join(response.xpath('//*[@id="content_top"]/div/div[2]/div/span/div[2]/div/p[1]/text()').extract())
    		item["athlete_nation"] = "".join(response.xpath('//*[@id="content_top"]/div/div[2]/div/span/div[2]/div/p[2]/text()').extract())
    		item["athlete_handedness"] = "".join(response.xpath('//*[@id="content_top"]/div/div[2]/div/span/div[2]/div/p[4]/text()').extract())
    		item["athlete_mastereye"] = "".join(response.xpath('//*[@id="content_top"]/div/div[2]/div/span/div[2]/div/p[5]/text()').extract())
    		item["series"] = "".join(response.xpath('//*[@id="content_top"]/div/div[2]/div/span/div[3]/h2/text()').extract())
    		item["start_time"] = "".join(response.xpath('//*[@id="content_top"]/div/div[2]/div/span/div[1]/div/p[4]/text()').extract())
    		item["num"] = "".join(result.xpath("th/text()").extract())
    		item["score"] = "".join(result.xpath("td/text()").extract())
    		item['link'] = response.url
    		yield item