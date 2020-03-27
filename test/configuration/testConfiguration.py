from src.configuration import configuration


def test_get_coronavirus_configuration():
    dataSources = configuration.Configuration.get_configuration("data_sources")
    assert dataSources['coronavirusecuador']['url'] == 'https://coronavirusecuador.com/'
