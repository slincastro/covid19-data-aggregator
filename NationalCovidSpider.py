import json

import scrapy
from scrapy.crawler import CrawlerProcess

from national import National


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
        with open('data.txt', 'w') as outfile:
            json.dump(national_statistics.__dict__, outfile)


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(NationalCovidSpider)
process.start()
