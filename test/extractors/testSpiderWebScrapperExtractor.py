import codecs
from src.extractors.SpiderWebScrapperExtractor import SpiderWebScrapperExtractor
from scrapy.http import HtmlResponse


def test_data_extractor():
    file = codecs.open("test/resources/covid_stub.html", 'r')
    response = HtmlResponse(url="my HTML string", body=file.read(), encoding='utf-8')
    data = SpiderWebScrapperExtractor().extract_data(response)
    assert data == ['1,965', '1,403', '3', '34']

