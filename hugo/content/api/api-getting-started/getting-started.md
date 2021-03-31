---
title: Getting started
linkTitle: Getting started
weight: 10
description: A quick start guide to authenticating and using the REST API.
type: documentation
---

This quick introduction to using the API shows how to get the OAuth2 authentication token needed for subsequent API requests. A simple API request is also made to verify successful authentication and connectivity.

## Step 1: Get the credentials needed to request an authentication token

1. From the console, elect **All Clients** and a client.
1. Select **Setup > Integrations > Integrations**.
1. In the **Available Integrations** section, click **Other > Custom Integration**.
1. Enter a **Name**, **Description**, and in **Category** choose **Custom**.
1. Click **Install**.
1. In the **Inbound** tab, choose **Authentication Type** `OAUTH2`.
1. Click **Save**.
1. Click the copy icons to save the `Tenant Id`, `Key`, and `Secret` field values, which are needed for the OAuth2 authentication token request.

## Step 2: Get an authentication token

This example shows how to request an authentication token request using your saved credentials. Enter the saved `Key` for the *client_id* parameter and the saved `Secret` for the *client_secret* parameter:

{{< code bash >}}
curl https://api-generic.opsramp.com/auth/oauth/token
	-H "Content-Type: application/x-www-form-urlencoded"
	-H "Accept: application/json"
	-d "grant_type=client_credentials&client_id=vT9JKxpm9E...6jTm58w&client_secret=vvSzrRb2JU...BPCgTke9XY"
	-X POST
{{< /code >}}

Successful authentication returns the authentication token in the *access_token* field:

{{< code json >}}
{"access_token":"7609c2...ea918","token_type":"bearer","expires_in":7199,"scope":"global:manage"}
{{< /code >}}

Use the token and the saved `Tenant Id` in subsequent API requests to authenticate with the server.

The token is valid for two hours as indicated by the returned *expires_in* field.

## Step 3: Make an API request to verify successful authentication

The following example searches for open alerts:

{{< code bash >}}
curl -X GET -k https://api-2adc3.opsramp.com/api/v2/tenants/client_1234/alerts/search?queryString=actions:OPEN'
	-H 'Accept: application/json' 
	-H 'Authorization: Bearer 7609c2...ea918' 
	-H 'Content-Type: application/json'
{{< /code >}}

The header *Authorization* field includes the authentication token returned with the previous request. The saved `Tenant Id`, *client_1234* in this example, is required as a path parameter.

Successful connectivity and authentication with the server returns JSON data, which shows that no alerts satisfy the search criteria:

{{< code json >}}
{
    "results": [],
    "totalResults": 0,
    "pageNo": 1,
    "pageSize": 100,
    "totalPages": 0,
    "nextPage": false,
    "descendingOrder": false
}
{{< /code >}}
