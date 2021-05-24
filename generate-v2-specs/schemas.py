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

# Tenant
class Tenant(BaseModel):
    tenantId: str

# Agent policies
class AgentPolicies(BaseModel):
    agentPolicyId: UUID

# List of agent policies
ListAgentPolicies = {}

