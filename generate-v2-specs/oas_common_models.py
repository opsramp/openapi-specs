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


API_PREFIX = '/api/v2'
TENANT_NAME = 'api-2adc3'

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

SERVERS = [
    {
        "opsramp" : {
            "uri": "https://" + TENANT_NAME + ".api.opsramp.com",
            "description" : "OpsRamp cloud API endpoint root"
        }
    },
    {
        "gateway" : {
            "uri" : "https://{fqdn-of-gateway}/api/v2",
            "description" : "OpsRamp Gateway API endpoint root"
        }
    }
]

SECURITY = {
    "type" : "oauth2",
    "description" : "OAuth2 security using flow client_credentials",
    "flows" : {
        "clientCredentials" : {
            "tokenUrl" : SERVERS[0]["opsramp"]["uri"] + "/auth/oauth/token"
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