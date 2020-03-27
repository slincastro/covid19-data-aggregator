import json
import yaml


class Configuration:

    def get_configuration(section):
        with open("src/app_config.yml") as ymlfile:
            configuration = yaml.safe_load(ymlfile)

        return configuration[section]

