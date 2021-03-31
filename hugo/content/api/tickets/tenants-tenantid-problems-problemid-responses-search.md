---
slug: tenants-tenantid-problems-problemid-responses-search
title: Get problem responses
description: >-
  Gets responses of a problem.


  ##### Query Variables


  |Query Variable|Values|Description|

  |-----|----|-----|

  |startCreationDate|NA|Filter response with request creation date. Provide from
  date.<br>Example: 2016-03-29T10:15:55 0000 (GMT)|

  |endCreationDate|NA|Filter response with request creation date. Provide to
  date.<br>Example: 2016-03-31T11:20:55 0000 (GMT)|

  |internal|true, false|Internal or universal responses:<br>- If internal=true
  gets only the internal responses.<br>- If internal=false gets global
  responses.<br>- By default it gets all responses of the ticket.|


  ##### Notes

  There are special characters that can be used in a query string:

  - (+) represents the next field and must be URL-encoded.

  - (:) represents equals. An example is `key : value`.

  - Space characters must be URL-encoded.

  - Date format must be yyyy-MM-ddTHH:mm:ssZ (GMT)
tags:
  - tickets
path: '/api/v2/tenants/{tenantId}/problems/{problemId}/responses/search'
request:
  - get
layout: api-doc
draft: false
---
