# Load the Pandas libraries with alias 'pd'
import json

import pandas as pd

class CsvExtractor:
    data = pd.read_csv("covid_ec.csv")

    def get_data_by(self, filter):
        column = filter["column"]
        value = filter["value"]

        province = self.data.loc[self.data[column] == value]
        province = province.replace(pd.np.nan, 0, regex=True)
        print(province)
        province_dict = province.to_dict(orient='records')
        province_json = json.dumps(province_dict)
        print(province_json)
        return province_json

extractor = CsvExtractor()

parameters = {
  "column": "nombre_provincia",
  "value": "pichincha"
}

extractor.get_data_by(parameters)
