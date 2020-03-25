import json

import scrapy
from scrapy.crawler import CrawlerProcess

from National import National


class NationalCovidSpider(scrapy.Spider):
    name = 'dc_spider'

    def start_requests(self):
        print('start request')
        url = 'https://coronavirusecuador.com/'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        out = response.xpath("//div[@class = 'vcex-milestone-number']/span[@class = 'vcex-milestone-time vcex-countup']/text()").extract()
        national_statistics = National(out[0], out[1], out[2], out[3])
        print(json.dumps(national_statistics.__dict__))
        print("################################# Writing File #############################")
        with open('data.txt', 'w') as outfile:
            json.dump(national_statistics.__dict__, outfile)
        print("################################# Writing Finished #############################")


