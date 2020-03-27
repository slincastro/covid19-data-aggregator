import codecs
import json

from src.extractors.SpiderWebScrapperExtractor import SpiderWebScrapperExtractor
from scrapy.http import HtmlResponse


def test_when_extract_html_file_give_me_4_values():
    response = load_html()
    data = SpiderWebScrapperExtractor().extract_data(response)
    expect_data = ['1,965', '1,403', '3', '34']
    assert data == expect_data


def test_when_parse_data_extractor_should_write_json_file():
    response = load_html()
    SpiderWebScrapperExtractor().parse(response)
    current_data = get_data()
    current_data["time"] = 0
    expected_data = {"suspicious": "1,965", "confirmed": "1,403", "recoveries": "3", "deaths": "34", "time": 0}
    assert current_data == expected_data


def load_html():
    file = codecs.open("test/resources/covid_stub.html", 'r')
    response = HtmlResponse(url="my HTML string", body=file.read(), encoding='utf-8')
    return response


def get_data():
    with open('data.txt') as json_file:
        data = json.load(json_file)
    return data
