---
slug: tenants-tenantid-rosters-search
title: Get organization rosters
description: |
  Gets the rosters in an organization.

  ## Special Characters
  There are special characters that can be used in a query string:
  - (+) represents the next field and must be URL-encoded.
  - (:) represents equals. An example is `key : value`.
  - Space characters must be URL-encoded.
  - Date format must be yyyy-MM-ddTHH:mm:ssZ (GMT).

  ## Differentiate Rosters
  To differentiate between partner-level and client-level rosters:
  - Client level roster: If `client` and client details are provided.
  - Partner-level roster: If `allClients: true` is provided.
tags:
  - alerts
path: '/api/v2/tenants/{tenantId}/rosters/search'
request:
  - get
layout: api-doc
draft: false
---
