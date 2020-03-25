import src

from scrapy.crawler import CrawlerProcess
from src.extractors.NationalCovidSpider import NationalCovidSpider

process = CrawlerProcess(
    {"USER_AGENT": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"}
)

process.crawl(NationalCovidSpider)
process.start()
