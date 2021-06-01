from typing import List, Optional
from sqlalchemy.orm import Session

from fastapi import (
    Depends,
    FastAPI,
    Header,
    Body,
    HTTPException,
    File,
    Form,
    UploadFile
)

from pydantic import BaseSettings
import json

from opsrampapiutils import utils as utils
import semver
import shutil
from uuid import UUID
from models import *
from schemas import *
from parameters import *

import requests




from info import info
from openapi import openapi
from security import security
from servers import servers_opsramp_cloud, path_prefix
import yaml

SPEC_NAME = 'API to obtain OAuth 2.0 Access Token'
OAS_FILENAME = 'opsramp-oauth-token.v2.generated.yaml'
OAS_DIR = 'oas-files'
OAS_FILEPATH = OAS_DIR + '/' + OAS_FILENAME



app = FastAPI( title = 'SPEC_NAME',
    description = "Live mock API endpoints",
    version="1.0",docs_url="/",
    openapi_url= path_prefix + 'openapi.json')


tenant_name = 'api-2adc3'
oauth_api_path = '/auth/oauth/token'
@app.post(oauth_api_path)
def post_client_credentiials(content_type: str = Header('application/x-www-form-urlencoded'),
                             accept : str = Header('application/json'),
                             body: OAuthAccessTokenRequestBody = Body(
                                 ...,
                                 example = {
                                    "grant_type": "client_credentials",
                                     "client_id": "jzhyhYKGkpEWAXcJ9Qd6mMkpSDMFqYUS",
                                     "client_secret": "PCDNBBMx77RfdG3fCUsMnFvsEMu8y86BaN82JRpjqgBDqHbm8Hcxgj4ZKZg9gp88"
                                 },
                             )):

    auth_uri = 'https://' +  + '.opsramp.com' + oauth_api_path
    headers = {"Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json"}
    data = {
                "grant_type": "client_credentials",
                "client_id": 'jzhyhYKGkpEWAXcJ9Qd6mMkpSDMFqYUS',
                "client_secret": 'PCDNBBMx77RfdG3fCUsMnFvsEMu8y86BaN82JRpjqgBDqHbm8Hcxgj4ZKZg9gp88'
            }

    r = requests.post(auth_uri, data=data, headers=headers)
    response = dict(r.json())
    auth_token = str(response["token_type"]) + " " + str(response["access_token"])

    #print(type(json_response))
    #print(json_response)
    # response = json.dumps(json_response)
    return response





if __name__ == '__main__':
    oas = {}

    oas['openapi'] = openapi
    oas['info'] = info
    oas['servers'] = servers_opsramp_cloud
    oas['security'] = security

    post_operation_object = { 'temp' : 'temp' }

    paths = [
        {
            '/auth/oauth/token': {
                'summary' : 'test summary',
                'description' : 'test description',
                'post' : post_operation_object
            }
        }
    ]


    oas['paths'] = paths


    with open(OAS_FILEPATH, 'w') as f:
        data = yaml.dump(oas, f, default_flow_style=False, sort_keys=False)

    # print(HeaderOAuthToken.schema_json(indent=2))

    with open('oas-oauth-1.json', 'r') as f:
        oas_opshub_json = json.load(f)

    with open('oas-oauth-1.yaml', 'w') as f:
        data = yaml.dump(oas_opshub_json, f, default_flow_style=False, sort_keys=False)

    oas_fastapi = app.openapi()
    with open('oas-fastapi.yaml', 'w') as f:
        data = yaml.dump(oas_fastapi, f, default_flow_style=False, sort_keys=False)

    routes = app.routes
    print("routes:", routes)