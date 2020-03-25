import json


class NationalRepository:

    def save(self, national_statistics):
        with open('data.txt', 'w') as outfile:
            json.dump(national_statistics.__dict__, outfile)

    def get_national_data():
        with open('data.txt') as json_file:
            data = json.load(json_file)
        return data
