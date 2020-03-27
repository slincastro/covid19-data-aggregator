import json

import pandas as pd

from src.configuration.configuration import Configuration


class CsvExtractor:
    def __init__(self):
        data_sources_configuration = Configuration.get_configuration("data_sources")
        self.configuration = data_sources_configuration["csv_covid_ecuador"]

    def get_data_by(self, filter):

        data = pd.read_csv(self.configuration["url"])
        column = filter["column"]
        value = filter["value"]

        province = data.loc[data[column] == value]
        province = province.replace(pd.np.nan, 0, regex=True)
        print(province)
        province_dict = province.to_dict(orient='records')
        province_json = json.dumps(province_dict)
        print(province_json)
        return province_json

