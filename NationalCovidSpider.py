import json

import scrapy

from National import National
from repository.NationalRepository import NationalRepository


class NationalCovidSpider(scrapy.Spider):
    name = 'dc_spider'

    def start_requests(self):
        print('start request')
        url = 'https://coronavirusecuador.com/'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        data = self.extract_data(response)

        cases = data[0]
        siege = data[1]
        recoveries = data[2]
        diseases = data[3]

        national_statistics = National(cases, siege, recoveries, diseases)
        print(json.dumps(national_statistics.__dict__))
        NationalRepository.save(national_statistics)

    def extract_data(self, response):
        out = response.xpath(
            "//div[@class = 'vcex-milestone-number']/span[@class = 'vcex-milestone-time vcex-countup']/text()").extract()
        return out



