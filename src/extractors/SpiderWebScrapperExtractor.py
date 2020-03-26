import json
from datetime import datetime

import scrapy

from src.domain.National import National
from src.repository.NationalRepository import NationalRepository


class SpiderWebScrapperExtractor(scrapy.Spider):
    name = 'dc_spider'

    def start_requests(self):
        print('start request')
        url = 'https://coronavirusecuador.com/'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print('starting to extract ....')
        data = self.extract_data(response)
        print('ready to respond ....')
        suspicious = data[0]
        confirmed = data[1]
        recoveries = data[2]
        deaths = data[3]
        time = datetime.now().timestamp()
        national_statistics = National(suspicious, confirmed, recoveries, deaths, time)
        print(json.dumps(national_statistics.__dict__))
        repository = NationalRepository()
        repository.save(national_statistics)

    def extract_data(self, response):
        out = response.xpath(
            "//div[@class = 'vcex-milestone-number']/span[@class = 'vcex-milestone-time vcex-countup']/text()"
        ).extract()
        return out
