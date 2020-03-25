import os

import crochet as crochet
from flask import Flask, request
from scrapy.crawler import CrawlerRunner

from src.extractors.CsvExtractor import CsvExtractor
from src.extractors.NationalCovidSpider import NationalCovidSpider
from src.repository.NationalRepository import NationalRepository

crochet.setup()
app = Flask(__name__)
crawl_runner = CrawlerRunner()


@app.route('/Ecuador/live')
def national_statistic():
    scrape_with_crochet()
    data = NationalRepository.get_national_data()

    return data


@app.route('/Ecuador')
def data_filtering():
    by = request.args.get('by')
    value = request.args.get('equal')
    filter = {"column": by,
              "value": value}
    return CsvExtractor().get_data_by(filter)


@app.route('/load')
def load_data():
    scrape_with_crochet()

    return 'Loading ....'


@crochet.run_in_reactor
def scrape_with_crochet():
    crawl_runner.crawl(NationalCovidSpider)


if __name__ == '__main__':
    scrape_with_crochet()
    port = os.environ["PORT"]
    print('using port : ', port)
    app.run(port=port, host='0.0.0.0')
