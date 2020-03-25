import json
import os

import crochet as crochet
from flask import Flask
from scrapy.crawler import CrawlerRunner

from NationalCovidSpider import NationalCovidSpider
from repository.NationalRepository import NationalRepository

crochet.setup()
app = Flask(__name__)
crawl_runner = CrawlerRunner()


@app.route('/Ecuador')
def national_statistic():
    scrape_with_crochet()
    data = NationalRepository.get_national_data()

    return data


@app.route('/load')
def load_data():
    scrape_with_crochet()

    return 'Loading ....'


@crochet.run_in_reactor
def scrape_with_crochet():
    crawl_runner.crawl(NationalCovidSpider)


if __name__ == '__main__':
    port = os.environ["PORT"]
    print('using port : ', port)
    app.run(port=port, host='0.0.0.0')
