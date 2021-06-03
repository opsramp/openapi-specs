import os, sys
sys.path.append("..")
from oas_common_models import *
from models import *

os.environ["TENANT_NAME"] = 'api-2adc3'

TITLE = 'oauth'
DESCRIPTION = 'API to obtain OAuth 2.0 Access Token'
ENDPOINT_SUFFIX = '/auth/oauth/token'

TENANT_NAME = os.getenv("TENANT_NAME")
print("TENANT_NAME", TENANT_NAME)
assert (TENANT_NAME != None), "TENANT_NAME is blank"



URI = 'https://' +  TENANT_NAME + '.opsramp.com' + ENDPOINT_SUFFIX
OAS_FILENAME = TITLE + '.v2.generated.yaml'
OATH_FILEPATH = '../oas'


app = FastAPI( title = TITLE,
    description = DESCRIPTION,
    version="2.0.0",docs_url="/",
    openapi_url= ENDPOINT_SUFFIX + '/openapi.json')


@app.post(ENDPOINT_SUFFIX, response_model=OAuthResponse,
          summary="Get OAuth 2.0 Access Token")
def post_client_credentiials(
    content_type = Header(..., example = "application/x-www-form-urlencoded"),
    accept = Header(..., example="application/json"),
    body: OAuthRequest = Body(
             ...,
             example = {
                "grant_type": "client_credentials",
                 "client_id": "jzhyhYKGkpEWAXcJ9Qd6mMkpSDMFqYUS",
                 "client_secret": "PCDNBBMx77RfdG3fCUsMnFvsEMu8y86BaN82JRpjqgBDqHbm8Hcxgj4ZKZg9gp88"
             },
         )):
    """
    Post the following information to get an OAuth 2.0 Access Token.
    - **grant_type**: "client_credentials. APIs use Client Credentials Grant type.
    - **client_id**: *key* from the integration.
    - **client_secret**: *secret* from the integration.
    """

    headers = { "content-type": "application/x-www-form-urlencoded", "Accept": "application/json" }
    data = {
        "grant_type": "client_credentials",
        "client_id": 'jzhyhYKGkpEWAXcJ9Qd6mMkpSDMFqYUS',
        "client_secret": 'PCDNBBMx77RfdG3fCUsMnFvsEMu8y86BaN82JRpjqgBDqHbm8Hcxgj4ZKZg9gp88'
    }

    r = requests.post(URI, data=data, headers=headers)
    response = dict(r.json())

    return response


if __name__ == '__main__':

    oas_fastapi = app.openapi()
    oas_fastapi['openapi'] = OPENAPI
    oas_fastapi['info'] = INFO
    oas_fastapi['servers'] = SERVERS['opsramp_auth']

    ordered_oas_fastapi = OrderedDict()

    first_few_keys = ['openapi', 'info', 'servers']

    for k in first_few_keys:
        ordered_oas_fastapi[k] = oas_fastapi[k]

    for k in oas_fastapi.keys():
        if k not in first_few_keys:
            ordered_oas_fastapi[k] = oas_fastapi[k]

    utils.print_dict_to_file(ordered_oas_fastapi, 'original-dict.json')
    utils.print_dict_to_file(ordered_oas_fastapi, 'ordered-dict.json')


    with open(OATH_FILEPATH + '/' + OAS_FILENAME, 'w') as f:
        data = yaml.dump(dict(ordered_oas_fastapi), f, default_flow_style=False, sort_keys=False)
