
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


def test_should_return_data_when_send_filter_with_infographic():
    province_filter = KeyValueFilter("nombre_provincia", "pichincha")
    infographic_filter = KeyValueFilter("infografia", 25)
    filters = [province_filter.__dict__, infographic_filter.__dict__]

    filter_parameters = FilterParameters(filters, "", "")
    response = extractor.get_data_by_range_filter(filter_parameters)

    print(len(response))
    assert len(response) == 3


def test_should_return_data_when_send_filter_with_infographic_and_date():
    province_filter = KeyValueFilter("nombre_provincia", "pichincha")
    infographic_filter = KeyValueFilter("infografia", 25)
    date_filter = KeyValueFilter("fecha", "26/3/2020")
    city_filter = KeyValueFilter("nombre_canton", "quito")
    filters = [province_filter.__dict__, infographic_filter.__dict__, date_filter.__dict__, city_filter.__dict__]

    filter_parameters = FilterParameters(filters, "", "")
    response = extractor.get_data_by_range_filter(filter_parameters)

    assert len(response) == 1


def test_should_return_data_per_day():

    response = extractor.get_data_by_range_filter_per_day("pichincha", "22/3/2020")
    print(response["casos_confirmados"])
    assert response["casos_confirmados"]["pichincha"] == 10


def test_should_parse_date_csv_format():
    today = '22/03/2020'
    expected_date = '21/3/2020'
    date = extractor.get_yesterday_date(today)

    assert expected_date == date


