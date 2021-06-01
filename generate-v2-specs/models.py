from typing import Optional, List
from enum import Enum, IntEnum
from pydantic import (
    BaseModel,
    Field,
    constr,
    ValidationError
)
from uuid import UUID
import semver


class OAuthAccessTokenRequestHeader(BaseModel):
    content_type: str
    accept : str


class OAuthAccessTokenRequestBody(BaseModel):
    grant_type: str
    client_id: str
    client_secret: str



# Tenant
class Tenant(BaseModel):
    tenantId: str

# Agent policies
class AgentPolicies(BaseModel):
    agentPolicyId: UUID

# List of agent policies
ListAgentPolicies = {}

