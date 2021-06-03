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
from collections import OrderedDict


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
from sqlalchemy.orm import Session
import requests
from opsrampapiutils import utils as utils


# API_PREFIX = '/api/v2'


OPENAPI = "3.0.0"

INFO = {
    "title": "opsramp",
    "version": "2.0.0",
    "description": "OpsRamp API Documentation",
    "contact": {
        "name": "OpsRamp Support",
        "email": "support@opsramp.com",
        "url": "https://www.opsramp.com/about-opsramp/contact-us"
    }
}

SERVERS = {
    "opsramp_auth" : {
        "uri": "https://" + "{tenant-name}" + ".api.opsramp.com",
        "description": "OpsRamp API server"
    },
    "opsramp_api": {
        "uri": "https://" + "{tenant-name}"  + ".api.opsramp.com/api/v2",
        "description" : "OpsRamp cloud API endpoint server"
    },
    "gateway" : {
        "uri" : "https://{fully-qualified-gateway-domain-name | gateway-ip-address}/api/v2",
        "description" : "OpsRamp Gateway API endpoint server"
    }
}

SECURITY = {
    "type" : "oauth2",
    "description" : "OAuth2 security using flow client_credentials",
    "flows" : {
        "clientCredentials" : {
            "tokenUrl" : SERVERS["opsramp_auth"]["uri"] + "/auth/oauth/token"
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