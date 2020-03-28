import json

from src.extractors.CsvExtractor import CsvExtractor
from src.resources.FilterParameters import FilterParameters
from src.resources.KeyValueFilter import KeyValueFilter

data_url = "test/resources/covid_ec.csv"
extractor = CsvExtractor(data_url)


def test_should_return_data_when_send_filter():
    province_filter = KeyValueFilter("nombre_provincia", "pichincha")
    filters = [province_filter.__dict__]
    filter_parameters = FilterParameters(filters, "", "")
    response = extractor.get_data_by_range_filter(filter_parameters)

    print(len(response))
    assert len(response) == 24


def test_should_return_data_when_send_filter():
    province_filter = KeyValueFilter("nombre_provincia", "pichincha")
    infographic_filter = KeyValueFilter("infografia", 25)
    filters = [province_filter.__dict__, infographic_filter.__dict__]

    filter_parameters = FilterParameters(filters, "", "")
    response = extractor.get_data_by_range_filter(filter_parameters)

    print(len(response))
    assert len(response) == 3


def test_should_return_data_when_send_filter():
    province_filter = KeyValueFilter("nombre_provincia", "pichincha")
    infographic_filter = KeyValueFilter("infografia", 25)
    date_filter = KeyValueFilter("fecha", "26/3/2020")
    city_filter = KeyValueFilter("nombre_canton", "quito")
    filters = [province_filter.__dict__, infographic_filter.__dict__, date_filter.__dict__, city_filter.__dict__]

    filter_parameters = FilterParameters(filters, "", "")
    response = extractor.get_data_by_range_filter(filter_parameters)

    assert len(response) == 1
