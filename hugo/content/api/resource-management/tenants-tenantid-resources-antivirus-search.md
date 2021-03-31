---
slug: tenants-tenantid-resources-antivirus-search
title: Get latest antivirus definitions on resources
description: >-
  Gets the latest antivirus definitions installed on resources.


  ##### Query Variables


  |Query Variables|Values|Description|

  |----|----|----|

  |status|- OUTOFDATE<br>- UPTODATE|Antivirus definition status on a
  resource.<br>Example: UPTODATE.|


  ##### Notes

  There are special characters that can be used in a query string:

  - (+) represents the next field and must be URL-encoded.

  - (:) represents equals. An example is key : value.

  - Space characters must be URL-encoded.

  - Date format must be yyyy-MM-ddTHH:mm:ssZ (GMT).
tags:
  - resource-management
path: '/api/v2/tenants/{tenantId}/resources/antivirus/search'
request:
  - get
layout: api-doc
draft: false
---
