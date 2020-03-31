import json

import pandas as pd

from src.configuration.configuration import Configuration


class CsvExtractor:

    def __init__(self, csv_url=""):
        data_sources_configuration = Configuration.get_configuration("data_sources")
        self.configuration = data_sources_configuration["csv_covid_ecuador"]
        url = self.configuration["url"] if not csv_url else csv_url
        self.data = pd.read_csv(url)

    def get_data_by(self, filter):
        data = self.data
        column = filter["column"]
        value = filter["value"]

        response = data.loc[data[column] == value]
        response = response.replace(pd.np.nan, 0, regex=True)
        response_dict = response.to_dict(orient='records')
        response_json = json.dumps(response_dict)
        return response_json

    def get_data_by_range_filter(self, data_filter):
        data = self.get_df_data_by_parameters(data_filter)

        response = data.replace(pd.np.nan, 0, regex=True)
        response_dict = response.to_dict(orient='records')
        response_json = json.dumps(response_dict)
        response_json = json.loads(response_json)
        return response_json

    def get_df_data_by_parameters(self, data_filter):
        data = self.data
        for filter in data_filter.filter:
            column = filter["column"]
            value = filter["value"]
            data = data.loc[data[column] == value]
        return data

    def get_data_by_range_filter_per_day(self, filter_parameters):
        data = self.get_df_data_by_parameters(filter_parameters)

        grouped_data = data.groupby(["nombre_provincia"]).agg({'casos_confirmados':'sum'})
        response_dict = grouped_data.to_dict()
        response_json = json.dumps(response_dict)
        response_json = json.loads(response_json)

        return response_json



