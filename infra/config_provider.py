import json


class ConfigProvider:

    @staticmethod
    def load_from_file():
        try:
            with open('../config.json', 'r') as f:
                config = json.load(f)
                print(f"Config loaded: {config}")
                return config
        except FileNotFoundError:
            print(f"File config.json not found.")
            exit(-1)
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file config.json.")
            exit(-1)

    @staticmethod
    def get_value(self, key):
        try:
            with open('../config.json', 'r') as f:
                config = json.load(f)
                return config.get(key)
        except FileNotFoundError:
            print(f"File config.json not found. Starting with an empty configuration.")
            exit(-1)
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file config.json. Starting with an empty configuration.")
            exit(-1)