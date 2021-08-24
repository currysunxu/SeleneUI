import os

import yaml

from Salesforce.config.parseyaml import read_yaml_file

current_path = os.path.dirname(__file__)
yaml_cfg = yaml.full_load(read_yaml_file(current_path))


try:
    print(os.environ['environment'])
except Exception as e:
    os.environ['environment'] = yaml_cfg.get('Local')['LOCAL_ENV']

env_key = os.environ['environment']