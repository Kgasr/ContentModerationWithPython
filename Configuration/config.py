import os, json, requests
from dotenv import load_dotenv
from os.path import join, dirname

def get_config_from_env(keys):
    try:
        config_pairs = {}
        """Setup to read env file for various parameters"""
        dotenv_path = join(dirname(__file__), 'var.env')
        load_dotenv(dotenv_path)
        for key in keys:
            value = os.getenv(key)
            config_pairs[key] = value
        return config_pairs
    except Exception as ex:
        raise Exception(str(ex))

def get_config(keys):
    try:
        config_pairs = {}
        config_path = os.path.join(os.path.dirname(os.getcwd()),"Configuration","config.json")
        with open(config_path) as config_file:
            config = json.load(config_file)
        for key in keys:
            value = config.get(key)
            config_pairs[key] = value
            if key == 'source_type':
                source = config.get("sources",{}).get(value,{}).get("source")
                config_pairs['source'] = source
        return config_pairs
    except Exception as ex:
        raise Exception(str(ex))

"""
keys = {'source_type', 'api_url','api_key'}
print(get_config_from_env(keys))
print(get_config_from_json(keys))
"""