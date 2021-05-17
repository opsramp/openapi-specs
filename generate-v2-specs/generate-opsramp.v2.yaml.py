from info import info
from openapi import openapi
from security import security
from servers import servers
import yaml

if __name__ == '__main__':
    oas = {}

    oas["openapi"] = openapi
    oas["info"] = info
    oas["servers"] = servers
    oas["security"] = security

    with open('generated-opsramp.v2.yaml', 'w') as f:
        data = yaml.dump(oas, f, default_flow_style=False, sort_keys=False)