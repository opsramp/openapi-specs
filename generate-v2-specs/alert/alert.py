import os, sys
sys.path.append("..")
from oas_common_models import *
from models import *


TITLE = 'acknowledge-alert'
DESCRIPTION = 'Acknowledge an alert'
OAS_FILENAME = TITLE + '.v2.generated.yaml'
OATH_FILEPATH = '../oas'

with open('../integration-profiles/integration-profile-sample.json') as f:
    integration = json.load(f)

DOMAIN_NAME = integration['domain_name']
TENANT_SUBDOMAIN_NAME = integration["tenant_subdomain_name"]
TENANT_ID = integration["partner_id"]



app = FastAPI( title = TITLE,
    description = DESCRIPTION,
    version="v2",docs_url="/",
    openapi_url= '/openapi.json')


ENDPOINT = '/tenants/{clientId}/alerts/{alertId}/acknowledge'
@app.post(ENDPOINT, response_model=dict,
          summary="Acknowledge alert")
def acknowledge_alert(
        content_type : str = Header(..., example = CANONICAL_ACCESS_HEADER["Content-Type"]),
        accept : str = Header(..., example = CANONICAL_ACCESS_HEADER["Accept"]),
        authorization : str = Header(..., example = CANONICAL_ACCESS_HEADER["Authorization"]),
        clientId: ClientId = Field(...),
        alertId: AlertId = Field(...)
    ):
    """
    Acknowledge alert.
    - **TBD**: TBD.
    """

    OPSRAMP_ENDPOINT = '/tenants' + '/' + clientId + '/alerts' + '/' + alertId + '/acknowledge'
    print("ENDPOINT", OPSRAMP_ENDPOINT)
    #URI = 'https://' + TENANT_SUBDOMAIN_NAME + '.opsramp.com' + ENDPOINT
    URI =  "https://" + TENANT_SUBDOMAIN_NAME + "." +  DOMAIN_NAME + "/api/v2" + OPSRAMP_ENDPOINT
    print("URI:", URI)

    data = { }
    #r = requests.post(URI, data=data, headers=headers)
    r = {"blank" : "blank"}
    #response = dict(r.json())
    response = r
    utils.print_dict(response)

    return response


ENDPOINT = '/tenants/{clientId}/alerts/{alertId}'
@app.get(ENDPOINT, response_model=dict,
          summary="Get alert details")
def post_client_credentials(
        content_type : str = Header(..., example = CANONICAL_ACCESS_HEADER["Content-Type"]),
        accept : str = Header(..., example = CANONICAL_ACCESS_HEADER["Accept"]),
        authorization : str = Header(..., example = CANONICAL_ACCESS_HEADER["Authorization"]),
        clientId: ClientId = Field(...),
        alertId: AlertId = Field(...)
    ):
    """
    Get alert details.
    - **TBD**: TBD.
    """

    data = { }
    #r = requests.post(URI, data=data, headers=headers)
    r = {"blank" : "blank"}
    #response = dict(r.json())
    response = r
    utils.print_dict(response)

    return response

if __name__ == '__main__':

    oas_fastapi = app.openapi()
    oas_fastapi['openapi'] = OPENAPI
    oas_fastapi['info'] = INFO
    oas_fastapi['servers'] = SERVERS['opsramp_api']

    ordered_oas_fastapi = dict()

    first_few_keys = ['openapi', 'info', 'servers']

    for k in first_few_keys:
        ordered_oas_fastapi[k] = oas_fastapi[k]

    for k in oas_fastapi.keys():
        if k not in first_few_keys:
            ordered_oas_fastapi[k] = oas_fastapi[k]


    #print(type(oas_fastapi['paths']))
    paths = oas_fastapi['paths'].keys()

    #print(oas_fastapi['paths'].keys())

    for path in paths:
        #utils.print_dict(oas_fastapi['paths'][path])
        methods = oas_fastapi['paths'][path].keys()
        #print(oas_fastapi['paths'][path].keys())
        for method in methods:
            #utils.print_dict(oas_fastapi['paths'][path][method])
            parameters = oas_fastapi['paths'][path][method]['parameters']
            for parameter_index, parameter in enumerate(parameters):
                #print("parameter_index:", parameter_index)
                parameter_name = oas_fastapi['paths'][path][method]['parameters'][parameter_index]['name'].lower()

                if parameter_name in PARAMETER_DESCRIPTIONS:
                    oas_fastapi['paths'][path][method]['parameters'][parameter_index]["description"] = \
                        PARAMETER_DESCRIPTIONS[parameter_name]
                utils.print_dict(parameter)



    with open(OATH_FILEPATH + '/' + OAS_FILENAME, 'w') as f:
        data = yaml.dump(dict(ordered_oas_fastapi), f, default_flow_style=False, sort_keys=False)
