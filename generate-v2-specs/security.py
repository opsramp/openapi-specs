import servers

security = {
    "type" : "oauth2",
    "description" : "OAuth2 security using flow client_credentials",
    "flows" : {
        "clientCredentials" : {
            "tokenUrl" : servers.servers["url"] + "/auth/oauth/token"
        }
    }
}