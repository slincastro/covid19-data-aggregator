import json

import crochet as crochet
from flask import Flask
from scrapy.crawler import CrawlerRunner

from NationalCovidSpider import NationalCovidSpider

crochet.setup()
app = Flask(__name__)
crawl_runner = CrawlerRunner()


@app.route('/')
def national_statistic():

    with open('data.txt') as json_file:
        data = json.load(json_file)

    return data


@app.route('/load')
def national_statistic():
    scrape_with_crochet()

    return 'Load ....'


@crochet.run_in_reactor
def scrape_with_crochet():
    crawl_runner.crawl(NationalCovidSpider)


if __name__ == '__main__':
    app.run(port='5002', host='0.0.0.0')
