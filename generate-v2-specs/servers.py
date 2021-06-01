servers = [
    "opsramp" : {
        "uri": "https://{tenant-name}.api.opsramp.com",
        "description" : "OpsRamp API URL"
    },
    "gateway" : {
        "uri" : "https://{gateway-fqdn}/api/v2/"
    }
]

api_prefix = '/api/v2'

security = {
    "type" : "oauth2",
    "description" : "OAuth2 security using flow client_credentials",
    "flows" : {
        "clientCredentials" : {
            "tokenUrl" : servers_opsramp_cloud[0]["uri"] + "/auth/oauth/token"
        }
    }
}
