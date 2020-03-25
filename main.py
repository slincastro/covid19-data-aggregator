import json
import subprocess

import crochet as crochet
from flask import Flask
from scrapy.crawler import CrawlerProcess, CrawlerRunner

from spider import MySpider

crochet.setup()
app = Flask(__name__)
crawl_runner = CrawlerRunner()

@app.route('/')
def national_statistic():
    scrape_with_crochet()

    with open('data.txt') as json_file:
        data = json.load(json_file)

    return data

@crochet.run_in_reactor
def scrape_with_crochet():
    crawl_runner.crawl(MySpider)


if __name__ == '__main__':
    app.run(port='5002', host='0.0.0.0')