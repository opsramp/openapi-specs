import sys
sys.path.append("..")
from oas_common_models import *

with open('./example-response-1.json') as f:
    example_response = json.load(f)


# Request body
class OAuthRequest(BaseModel):
    """
    This is the description of OAuthRequest
    """

    grant_type: str = Field(...,
                            title='grant_type',
                            description='[OAuth](https://www.oauth.com/) grant type. Use *client_credentials*.'
    )

    client_id: str = Field(...,
                           title='client_id',
                           description='This is the *key* from the integration.'
    )

    client_secret: str = Field(...,
                           title='client_secret',
                           description='This is the *secret* from the integration.'
    )


# Response body
class OAuthResponse(BaseModel):
    """
    This is the description of OAuthResponse
    """
    access_token : str =  Field(...,
                           title='access_token',
                           description='[OAuth 2.0](https://www.oauth.com/) Access Token'
    )
    token_type : str =  Field(...,
                           title='token_type',
                           description='Always of type: *bearer*'
    )
    expires_in : str =  Field(...,
                           title='expires_in',
                           description="""Seconds(*s*) to token expiry.\\
                                       OpsRamp\'s API Tokens expire in 7200s - 1s = 6199s"""
    )
    scope : str =  Field(...,
                           title='scope',
                           description='OAuth 2.0 scope: All APIs use the same scope: *global:manage*'

    )
    class Config:
        schema_extra  = { "example" : example_response }

