---
slug: tenants-tenantid-tickettype-slapolicies-search
title: Search SLA policies
description: >-
  Gets a list of all service level agreement policies along with their details.


  ##### Query Variables


  |Query Variable|Values|Description|

  |----|----|----|

  |queryString={queryString}|true, false|Status of the SLA policy. If
  active=true gets all the active SLA policiesIf active=false gets all the
  inactive SLA policies.|


  >##### Notes

  >SLA policies are valid only for incident and service request. Sample
  responses for response time, resolution breach time, resolution remainders,
  and response remainders use seconds format. 

  >

  >There are special characters that can be used in a query string:

  >- (+) represents the next field and must be URL-encoded.

  >- (:) represents equals. An example is `key : value`.

  >- Space characters must be URL-encoded.

  >- Date format must be yyyy-MM-ddTHH:mm:ssZ (GMT)
tags:
  - tickets
path: '/api/v2/tenants/{tenantId}/{ticketType}/slaPolicies/search'
request:
  - get
layout: api-doc
draft: false
---
