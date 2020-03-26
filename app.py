import json
import os

import crochet as crochet
from flask import Flask, request, Response, make_response, jsonify
from scrapy.crawler import CrawlerRunner

from src.extractors.CsvExtractor import CsvExtractor
from src.extractors.SpiderWebScrapperExtractor import SpiderWebScrapperExtractor
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
    filters = {"column": by,
               "value": value}
    filtered_data = CsvExtractor().get_data_by(filters)
    response = make_response(filtered_data)
    response.headers['Content-Type'] = 'application/json'
    return response


@app.route('/load')
def load_data():
    scrape_with_crochet()

    return 'Loading ....'


@crochet.run_in_reactor
def scrape_with_crochet():
    crawl_runner.crawl(SpiderWebScrapperExtractor)


if __name__ == '__main__':
    scrape_with_crochet()
    port = os.environ["PORT"]
    print('using port : ', port)
    app.run(port=port, host='0.0.0.0')
