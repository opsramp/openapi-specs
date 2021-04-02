---
slug: tenants-tenantid-resources-resourceid-notes-search
title: Search resource notes
description: >-
  Gets the latest antivirus definitions installed on resources.


  ##### Query Variables


  |Query Variables|Description|

  |----|----|

  |searchWord|Search with a unique word provided in the resource note.|

  |startCreationDate|Search for the resource note created within a duration.
  startCreationDate indicates the from date.|

  |endCreationDate|Search for the resource note created within a duration.
  endCreationDate indicates the to date.|

  |startUpdationDate|Search for the resource note created within a duration.
  startUpdationDate indicates the from date.|

  |endUpdationDate|Search for the resource note created within a duration.
  endUpdationDate indicates the to date.|

  |id|Resource ID|


  ##### Notes

  There are special characters that can be used in a query string:

  - (+) represents the next field and must be URL-encoded.

  - (:) represents equals. An example is key : value.

  - Space characters must be URL-encoded.

  - Date format must be yyyy-MM-ddTHH:mm:ssZ (GMT).
tags:
  - resource-management
path: '/api/v2/tenants/{tenantId}/resources/{resourceId}/notes/search'
request:
  - get
layout: api-doc
draft: false
---
