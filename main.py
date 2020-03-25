import json
import subprocess

from flask import Flask
from scrapy.crawler import CrawlerProcess

from spider import MySpider

app = Flask(__name__)

@app.route('/')
def national_statistic():
    execute_scrap()
    with open('data.txt') as json_file:
        data = json.load(json_file)

    return data


def execute_scrap():
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(MySpider)
    subprocess.check_output(process.start())


if __name__ == '__main__':
    app.run(port='5002', host='0.0.0.0')