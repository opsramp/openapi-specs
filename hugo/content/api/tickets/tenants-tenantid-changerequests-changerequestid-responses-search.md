---
slug: tenants-tenantid-changerequests-changerequestid-responses-search
title: Get change request responses
description: |-
  Gets responses of a change request.

  ##### Notes
  There are special characters that can be used in a query string:
  - (+) represents the next field and must be URL-encoded.
  - (:) represents equals. An example is `key : value`.
  - Space characters must be URL-encoded.
  - Date format must be yyyy-MM-ddTHH:mm:ssZ (GMT).
tags:
  - tickets
path: '/api/v2/tenants/{tenantId}/changeRequests/{changeRequestId}/responses/search'
request:
  - get
layout: api-doc
draft: false
---
