import sys
sys.path.append("..")
from oas_common_models import *


TITLE = 'oauth'
DESCRIPTION = 'API to obtain OAuth 2.0 Access Token'
ENDPOINT_SUFFIX = '/auth/oauth/token'
URI = 'https://' +  TENANT_NAME + '.opsramp.com' + ENDPOINT_SUFFIX
OAS_FILENAME = TITLE + '.v2.generated.yaml'
OATH_FILEPATH = '../oas'


app = FastAPI( title = TITLE,
    description = DESCRIPTION,
    version="2.0.0",docs_url="/",
    openapi_url= ENDPOINT_SUFFIX + '/openapi.json')


@app.post(ENDPOINT_SUFFIX)
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


    headers = {
                "Content-Type": content_type,
                "Accept": accept
            }

    data = {
                "grant_type": "client_credentials",
                "client_id": 'jzhyhYKGkpEWAXcJ9Qd6mMkpSDMFqYUS',
                "client_secret": 'PCDNBBMx77RfdG3fCUsMnFvsEMu8y86BaN82JRpjqgBDqHbm8Hcxgj4ZKZg9gp88'
            }

    r = requests.post(auth_uri, data=data, headers=headers)
    response = dict(r.json())
    auth_token = str(response["token_type"]) + " " + str(response["access_token"])

    return response


if __name__ == '__main__':

    oas_fastapi = app.openapi()
    with open(OATH_FILEPATH + '/' + OAS_FILENAME, 'w') as f:
        data = yaml.dump(oas_fastapi, f, default_flow_style=False, sort_keys=False)

    routes = app.routes
    #print("routes:", routes)