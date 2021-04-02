---
slug: tenants-tenantid-sites-search
title: Search sites
description: |-
  Searches sites.

  ##### Query Variables

  |Query Variables|Description|
  |----|----|
  |id|Site unique id.|
  |name|Site name.|
  |parentId|Parent side ID.|

  ##### Notes
  There are special characters that can be used in a query string:
  - (+) represents the next field and must be URL-encoded.
  - (:) represents equals. An example is `key : value`.
tags:
  - resource-management
path: '/api/v2/tenants/{tenantId}/sites/search'
request:
  - get
layout: api-doc
draft: false
---
