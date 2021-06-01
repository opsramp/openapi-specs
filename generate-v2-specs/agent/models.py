import sys
sys.path.append("..")
from oas_common_models import *


# Agent policies
class AgentPolicies(BaseModel):
    agentPolicyId: UUID

# List of agent policies
ListAgentPolicies = {}