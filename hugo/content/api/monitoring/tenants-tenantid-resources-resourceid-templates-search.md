---
slug: tenants-tenantid-resources-resourceid-templates-search
title: Get assigned templates of resource
description: |-
  Gets templates assigned to a resource.

  >##### Notes
  >There are special characters that can be used in a query string:
  >- (+) represents the next field and must be URL-encoded.
  >- (:) represents equals. An example is key : value.
  >- Space characters must be URL-encoded.
  >- Date format must be yyyy-MM-ddTHH:mm:ssZ (GMT).
tags:
  - monitoring
path: '/api/v2/tenants/{tenantId}/resources/{resourceId}/templates/search'
request:
  - get
layout: api-doc
draft: false
---
