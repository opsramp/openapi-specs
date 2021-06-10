import json, yaml
from enum import Enum, IntEnum
from typing import List, Optional
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



# Tenant
class Tenant(BaseModel):
    tenantId: str

# Partner
class Partner(BaseModel):
    partnerId: str

# Client
class Client(BaseModel):
    clientId: str