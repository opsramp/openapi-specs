---
slug: tenants-orgid-clients-search
title: Search clients
description: >-
  Searches for clients.


  ##### Notes

  There are special characters that can be used in a query string:

  - (+) represents the next field and must be URL-encoded.

  - (:) represents equals. An example is `key : value`.

  - Space characters must be URL-encoded.

  - Date format must be yyyy-MM-ddTHH:mm:ssZ (GMT).


  ##### Query Variables

  |Query Variables|Values|Description|

  |----|----|----|

  |uniqueId|NA|Client ID.|

  |name|NA|Client name.|

  |activeStatus|true, false|Active status of client.|

  |startCreationDate|NA|Client created within a period of time. Provide the from
  date.<br>Example: 2016-08-18T06:52:24 0000|

  |endCreationDate|NA|Client created within a period of time. Provide the to
  date.<br>Example: 2016-08-20T06:52:24 0000|

  |startUpdationDate|NA|Client updated within a period of time. Provide the from
  update date.<br>Example: 2016-08-25T18:56:04 0000|

  |endUpdationDate|NA|Client updated within a period of time. Provide to update
  date.<br>Example: 2016-08-25T18:56:04 0000|
tags:
  - tenancy-access-controls
path: '/api/v2/tenants/{orgId}/clients/search'
request:
  - get
layout: api-doc
draft: false
---
