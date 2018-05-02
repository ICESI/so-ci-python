import logging
import logging.config
import yaml

LOGGER = logging.getLogger('flask')

with open("op_stats/conf/logging.conf","r") as stream:
  global_config = yaml.load(stream)
logging.config.dictConfig(global_config['logging'])
