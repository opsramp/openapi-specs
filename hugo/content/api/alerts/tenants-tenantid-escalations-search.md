---
slug: tenants-tenantid-escalations-search
title: Get alert escalation policies
description: >-
  Gets the alert escalation policies attached to an alert.


  ##### Notes

  There are special characters that can be used in a query string:

  (+) represents the next field and must be URL-encoded.

  (:) represents equals. An example is key : value.

  Space characters must be URL-encoded.

  Date format must be yyyy-MM-ddTHH:mm:ssZ (GMT).


  ##### Query Variables

  |Query Variable|Values|Description|

  |-----|-----|-----|

  |name|NA|Alert Escalation policy name. Only identical policies in query string
  name are displayed.|

  |allList|true, false|This string is applicable to a partner user to fetch
  client policies as well. By default, OpsRamp provides partner alert escalation
  policies if allList is not provided in the query string.<br> - Provide
  allList: true to fetch partner and client alert escalation policies.<br> -
  Provide allList: false to fetch only partner alert escalation policies.|

  |startCreationDate|NA|Search for policies created within a certain time frame.
  Provide a start date. An example: 2017-05-05T13:25:15 0000|

  |endCreationDate|NA|Provide an end date. An example: 2017-05-08T10:30:40 0000|

  |startUpdationDate|NA|Search for policies updated within a certain time frame.
  Provide a start date. An example: 2017-06-10T09:20:10 0000|

  |endUpdationDate|NA|Provide an end date. An example: 2017-06-15T08:10:30 0000|


  Use `"scope"` and `"allClients": true` to differentiate between partner and
  client level policies.


  Partner-level policy:

  - `"uniqueId"` in scope is specified as msp_id

  - `"allClients": true` indicates the policy is a partner level policy


  Client-level policy:

  - `"uniqueId"` in scope is specified as `"client_id"`.
tags:
  - alerts
path: '/api/v2/tenants/{tenantId}/escalations/search'
request:
  - get
layout: api-doc
draft: false
---
