from pyblish_config import config

# load config, filter out attributes, save back
config_path = r'C:\my_config.json'
c = config.load_config_from_json(config_path)
c = config.filter_attrs(c, attributes=['url'])
config.filter_empty_plugins()
config.dump(path=config_path)
