from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException, File, Form, UploadFile
from pydantic import BaseSettings
from opsrampapiutils import utils as utils
from uuid import UUID
import schemas
import semver
import shutil


from info import info
from openapi import openapi
from security import security
from servers import servers
import yaml

OAS_FILENAME = 'opsramp-alerts.v2.generated.yaml'
OAS_DIR = 'oas-files'
OAS_FILEPATH = OAS_DIR + '/' + OAS_FILENAME


app = FastAPI( title = "Generate Agent Management APIs",
    description = "Live mock API endpoints",
    version="1.0",docs_url="/",
    openapi_url="/api/v1/openapi.json")

path_prefix = '/api/v2'

# Assigns agent resource policies
@app.post(path_prefix + "/tenants/{tenantId}/agentPolicies/{agentPolicyId}",
          response_model=list)
def assign_devices(tenantId: str, agentPolicyId: UUID):

    policy_list = [
      {
        "id": "042761ba-542e-4a7a-8e38-3ebbea7eeb16"
      },
      {
        "id": "023471da-698b-3a2e-1e93-6dbaca8eea23"
      },
      {
        "id": "855eb82e-3064-40a1-a26e-77efabe300da"
      }
    ]

    return policy_list



if __name__ == '__main__':
    oas = {}

    oas["openapi"] = openapi
    oas["info"] = info
    oas["servers"] = servers
    oas["security"] = security

    with open(OAS_FILEPATH, 'w') as f:
        data = yaml.dump(oas, f, default_flow_style=False, sort_keys=False)