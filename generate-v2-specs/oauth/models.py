import sys
sys.path.append("..")
from oas_common_models import *


# Request body
class OAuthRequest(BaseModel):
    grant_type: str
    client_id: str
    client_secret: str


# Response body
class OAuthResponse(BaseModel):
    access_token : str
    token_type : str
    expires_in : str
    scope : str

    class Config:
        schema_extra  = {
            "example" : {
              "access_token": "8b8778e5-949a-495c-a730-22809e08aa42",
              "token_type": "bearer",
              "expires_in": 7199,
              "scope": "global:manage"
            }
        }
