import sys, inspect
import json, yaml
from enum import Enum, IntEnum
from typing import List, Optional, Type, NewType, ClassVar
from pydantic import (
    BaseSettings,
    BaseModel,
    Field,
    constr,
    ValidationError
)
from uuid import UUID
import semver
import shutil
#from collections import OrderedDict
#import collections


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
from fastapi.testclient import TestClient

from sqlalchemy.orm import Session
import requests
from opsrampapiutils import utils as utils


# API_PREFIX = '/api/v2'


OPENAPI = "3.0.0"

INFO = {
    "title": "OpsRamp APIs",
    "description": "OpsRamp API Documentation",
    "termsOfService": "https://www.opsramp.com/terms-of-use/",
     "contact": {
        "name": "OpsRamp Support",
        "email": "support@opsramp.com",
        "url": "https://www.opsramp.com/about-opsramp/contact-us"
    },
    "license": {
        "name": "OpsRamp Master Services Agreement",
        "url": "https://www.opsramp.com/terms-of-use/"
    },
    "version": "v2"
}

SERVERS = {
    "opsramp_auth" : [{
        "url": "https://" + "{tenant-name}" + ".api.opsramp.com",
        "description": "OpsRamp OAuth 2.0 access token API server"
    }],
    "opsramp_api": [{
        "url": "https://" + "{tenant-name}"  + ".api.opsramp.com/api/v2",
        "description" : "OpsRamp API server"
    }],
    "gateway" : [{
        "url" : "https://{fully-qualified-gateway-domain-name | gateway-ip-address}/api/v2",
        "description" : "OpsRamp Gateway API server"
    }]
}

SECURITY = {
    "type" : "oauth2",
    "description" : "OAuth2 security using flow client_credentials",
    "flows" : {
        "clientCredentials" : {
            "tokenUrl" : SERVERS["opsramp_auth"][0]["url"] + "/auth/oauth/token"
        }
    }
}

CANONICAL_ACCESS_HEADER = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": "bearer e0e273b9-39a0-44ac-a04c-9f79078e96f4",
}


class TenantId(str):
    pathParameter: ClassVar[bool] = True
    pass


class ClientId(TenantId):
    """Id of Client."""
    pass


class PartnerId(TenantId):
    """Id of Partner."""
    pass


class AlertId(str):
    """Id of the Alert."""
    pathParameter: ClassVar[bool] = True
    pass



# Extract doc strings from path parameter classes
PARAMETER_DESCRIPTIONS = {}
clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
for cls in clsmembers:
    class_name = cls[0].lower()
    class_object = cls[1]
    #print("cls_name:", class_name)
    if hasattr(class_object, 'pathParameter'):
        doc_string = class_object.__doc__
        if doc_string != None:
            #print(type(class_object.__doc__))
            PARAMETER_DESCRIPTIONS[class_name] = doc_string

#utils.print_dict(PARAMETER_DESCRIPTIONS)


#for parameter in PARAMETER_DESCRIPTIONS.keys():
    #print(ClientId.__doc__)
#    print(PARAMETER_DESCRIPTIONS[parameter])
    #d = json.loads(str(PARAMETER_DESCRIPTIONS[parameter]))
    #utils.print_dict(d)
