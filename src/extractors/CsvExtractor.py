import json
from datetime import datetime, timedelta

import pandas as pd

from src.configuration.configuration import Configuration
from src.resources.FilterParameters import FilterParameters
from src.resources.KeyValueFilter import KeyValueFilter


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

    def get_data_by_range_filter_per_day(self, province, date):
        today = date
        yesterday = self.get_yesterday_date(today)

        data_per_province = self.data.loc[self.data["nombre_provincia"] == province]
        data_today = self.get_data_consolidated_per_province(data_per_province, today)
        data_yesterday = self.get_data_consolidated_per_province(data_per_province, str(yesterday))

        column = "casos_confirmados"

        if not data_today[column]:
            return {'casos_confirmados':{ province : 0}}

        total_yesterday = 0 if not data_yesterday[column] else data_yesterday[column][province]
        data_today[column][province] = data_today[column][province] - total_yesterday

        return data_today


    def get_yesterday_date(self, today):
        yesterday = datetime.strptime(today, "%d/%m/%Y") + timedelta(days=-1)
        yesterday = yesterday.strftime("%d/%m/%Y")
        day = str(int(yesterday.split('/')[0]))
        month = str(int(yesterday.split('/')[1]))
        yesterday_date = day + "/"+month+"/"+yesterday.split('/')[2]
        return yesterday_date


    def get_data_consolidated_per_province(self, data, date):
        data = data.loc[data["fecha"] == date]
        grouped_data = data.groupby(["nombre_provincia"]).agg({'casos_confirmados': 'sum'})
        response_dict = grouped_data.to_dict()
        response_json = json.dumps(response_dict)
        response_json = json.loads(response_json)
        return response_json



