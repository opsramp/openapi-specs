from servers import servers_opsramp_cloud, path_prefix

security = {
    "type" : "oauth2",
    "description" : "OAuth2 security using flow client_credentials",
    "flows" : {
        "clientCredentials" : {
            "tokenUrl" : servers_opsramp_cloud[0]["uri"] + "/auth/oauth/token"
        }
    }
}