import os
from json import load


def replace(string: str):
    if string is not None:
        for key, value in os.environ.items():
            string = string.replace(f"${{{key}}}", value)
    return string


def expect(json, key):
    return replace(json[key])


def optional(json, key):
    return replace(json.get(key))


# Config "struct"
class Config:
    def __init__(self, bucket, path):
        self.bucket = bucket
        self.path = path


def create_config(config_path: str):
    # read config json into a dict
    with open(config_path) as f:
        config = load(f)

    # client for bq operation
    bucket = expect(config, "bucket")
    path = expect(config, "path")

    # return the config object
    return Config(bucket, path)
