---
title: REST API Basics
linkTitle: REST API Basics
weight: 10
description: Describes basic REST API conventions that apply to all resource requests.
type: documentation
---

The REST API provides create, update, get, and delete operations on platform management resources. The resources are grouped in the following categories:

- Agents and Gateways
- Alerts
- Automation
- Exports
- Integrations
- Knowledge Base
- Metrics
- Monitoring
- Patching
- Resource Management
- Tenancy and Access Controls
- Tickets

View a summary of resource endpoints and operations in the next section.

The following topics describe basic REST API capabilities.

## Authentication

The API supports OAuth 2.0 authentication. All API requests require authentication.

To authenticate API requests you need to provide an ID and authentication token with the request. When you set up a custom integration, providing your credentials and specifying 'OAUTH2' authentication, you receive:

- *tenant ID*
- *key*
- *secret*

Use the *key* and *secret* values in the `/auth/oauth/token` API request to get the authentication token for subsequent API requests. The response provides the authentication token in the `access_token` field and the time interval for which the token is valid, in seconds, in the `expires-in` field.


Use the authentication token and *tenant ID* to authenticate subsequent API requests, passing the authentication token in the request header:

{{< code http >}}
"Authorization: Bearer {authenticationToken}"
{{< /code >}}

Where required, pass the *tenant ID* as a path parameter.

## Base URL

The API fully supports domain-specific partner and client URLs.

### Partners

Custom brand partners use a base URL that has the following format:

{{< code http >}}
https://{partnerName}.api.opsramp.com/api
{{< /code >}}

The `{partnerName}` part of the URL is a path parameter, which is replaced by the partner domain name. For example, the base URL for partner Alpha is: `https://alpha.api.opsramp.com/api`.

All other partners use the following base URL:

{{< code http >}}
https://api.opsramp.com/api
{{< /code >}}

### Clients

The base URL for a client who uses custom branding while the partner does not use custom branding is: `https://api.opsramp.com/api`.

Clients and partners who both use custom branding use the client URL, which has the following format:

{{< code http >}}
https://{clientName}.api.opsramp.com/api
{{< /code >}}

For example, if both partner Alpha and client Acme are private-labeled, the base URL is `https://acme.api.opsramp.com/api`.

## URL path parameters

The API documentation indicates variable URL path parameters using brackets: `{pathParameter}`. This permits operations on specific resources. For example, a tenant ID path parameter is represented as `{tenantID}`. When making an API request that requires a tenant ID to be specified, replace `{tenantID}` with the actual tenant ID.

## Versioning

API versioning ensures application and service compatibility. All API requests include an API version specification.

The API version identifier is appended to the base URL. For example, API version `v2` has the following URL format:

{{< code http >}}
https://api.opsramp.com/api/v2
{{< /code >}}

## HTTP request header

Use the following request header fields to provide data format and authentication information:

{{< table datatable=1  paging=0 searching=0 >}}
<thead class="thead-dark"><tr>
	<tr>
    <th width="30%">Header</th>
    <th width="70%">Value</th>
 </tr>
</thead>
<tbody>
<tr>
    <td>Accept</td>
    <td>application/json</td>
    </tr>
<tr>
    <td>Content-Type</td>
    <td>application/json</td>
    </tr>
<tr>
    <td>Authorization</td>
    <td>Bearer {accessToken} or Basic base64_encode(loginName:password)</td>
    </tr>
</tbody>
{{< /table >}}

## HTTP response header

the HTTP response header includes rate limit information for adjusting the API request frequency to accommodate performance and service changes.

{{< table datatable=1  paging=0 searching=0 >}}
<thead class="thead-dark">
<tr>
    <th>HTTP Header</th>
    <th>Description</th>
    <th>Example</th>
    </tr>
</thead>
<tbody>
<tr>
    <td>X-RateLimit-Limit</td>
    <td>Maximum number of requests per minute.</td>
    <td>X-RateLimit-Limit: 500</td>
    </tr>
<tr>
    <td>X-RateLimit-Remaining</td>
    <td>Number of requests remaining in the current rate limit window.</td>
    <td>X-RateLimit-Remaining: 14</td>
    </tr>
<tr>
    <td>X-RateLimit-Reset</td>
    <td>The time the current rate limit window resets, in UTC epoch seconds.</td>
    <td>X-RateLimit-Reset: 1491397260</td>
    </tr>
</tbody>
{{< /table >}}


## HTTP methods

The API supports the following methods:

{{< table datatable=1  paging=0 searching=0 >}}
<thead class="thead-dark"><tr>
    <tr>
    <th width="30%">Method</th>
    <th width="70%">Description</th>
 </tr>
</thead>
<tbody>
<tr>
    <td>DELETE</td>
    <td>Remove a resource.</td>
    </tr>
<tr>
    <td>GET</td>
    <td>Get resource data.</td>
    </tr>
<tr>
    <td>POST</td>
    <td>Modify or update a resource.</td>
    </tr>
<tr>
    <td>PUT</td>
    <td>Create or overwrite a resource.</td>
    </tr>
</tbody>
{{< /table >}}

## Data encoding

The API supports JSON data encoding of request and response data.

Specify JSON encoding in the HTTP header `Content-Type` and `Accept` fields.

## HTTP status codes

These status codes are returned by the APIs:

{{< table datatable=1  paging=0 searching=0 >}}
<thead class="thead-dark"><tr>
<tr>
    <th width="15%">Status</th>
    <th width="30%">Message</th>
    <th width="55%">Description</th>
</tr>
  </thead>
<tbody>
<tr>
    <td>200</td>
    <td>Success</td>
    <td>Request succeeded.</td>
    </tr>
<tr>
    <td>400</td>
    <td>Bad Request</td>
    <td>Unable to authenticate.</td>
    </tr>
<tr>
    <td>401</td>
    <td>Unauthorized</td>
    <td>System or user is not authorized to use the API.</td>
    </tr>
<tr>
    <td>404</td>
    <td>Not found</td>
    <td>Resource was not found.</td>
    </tr>
<tr>
    <td>405</td>
    <td>Method not allowed</td>
    <td>HTTP method is not allowed for the resource or not supported by any resource.</td>
    </tr>
<tr>
    <td>407</td>
    <td>Proxy Authentication Required</td>
    <td>Token expired.</td>
    </tr>
<tr>
    <td>410</td>
    <td>Gone</td>
    <td>Tenant is unavailable or deactivated.</td>
    </tr>
<tr>
    <td>429</td>
    <td>Too Many Requests</td>
    <td>Request exceeds the rate limit.</td>
    </tr>
<tr>
    <td>500</td>
    <td>Internal Server Error</td>
    <td>Unexpected condition preventing the server from completing the request.</td>
    </tr>
</tbody>
{{< /table >}}

## Rate limit

The rate limit specifies the number of requests an API server accepts within a time interval to ensure quality of service. If the number of API requests exceeds the rate limit, requests are throttled. The request rate is expressed in requests-per-minute.

Using the rate limit information returned in the response headers permits applications to self-regulate API requests.

The following rate limits apply to each service provider, partner, and client, according to resource category.

{{< table datatable=1  paging=0 searching=0 >}}
<thead class="thead-dark">
<tr>
    <th>API Category</th>
    <th>GET (non-paginated)</th>
    <th>GET (paginated)</th>
    <th>POST/DELETE/PUT</th>
    </tr>
    </thead>
<tbody>
<tr>
    <td><!-- XREF "/alerts-apis/" -->Alerts</td>
    <td>500</td><td>50</td><td>200</td>
    </tr>
<tr>
    <td><!-- XREF "/metrics-apis/" -->Metric</td>
    <td>500</td><td>50</td>
    <td>5000</td></tr>
<tr>
    <td><!-- XREF "/infrastructure-apis/" -->Device</td>
    <td>500</td><td>50</td>
    <td>25</td></tr>
<tr>
    <td><!-- XREF "/ticketing-apis/" -->Tickets</td>
    <td>500</td>
    <td>50</td><td>50</td>
    </tr>
<tr>
    <td><!-- XREF "/api-reference/" -->Other APIs</td>
    <td>500</td><td>50</td>
    <td>50</td></tr>
</tbody>
{{< /table >}}

A request that is rejected because it exceeds the rate limit returns a `HTTP 429 Too Many Requests` status code with the following error information in the response body:

{{< code json >}}
{
    "error" : "throttled",
    "error_description" : "Too Many Requests"
}
{{< /code >}}

Additional rate limit errors received within one minute of the first error are not processed.
