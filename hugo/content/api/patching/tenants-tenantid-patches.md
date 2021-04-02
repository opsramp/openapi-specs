---
slug: tenants-tenantid-patches
title: Search patches
description: >-
  Gets a tenant’s list of patches.

  ##### Query Variables

  Search for patches using these patch attributes:

  |Query Variables|Description|

  |---|---|

  |name|Patch name.|

  |uid|Patch unique ID.|

  |startReleaseDate|Search for patches released within a specific
  duration.<br>startReleaseDate indicates the from date.For example, a user
  wants to fetch list of patches released between 12-Aug-2018 through
  19-Aug-2018, provide startReleaseDate as 2018-08-12T05:40:51+0000 and
  endReleaseDate as 2018-08-19T08:30:20+0000.<br>Date format must be
  yyyy-MM-ddTHH:mm:ssZ (GMT).|

  |endReleaseDate|Search for patches released within a specific duration.
  endReleaseDate indicates the to date.<br>Date format must be
  yyyy-MM-ddTHH:mm:ssZ (GMT).|

  |extPatchId|External ID of a patch.|

  |severity|Severity of patch.|

  |category|Category in which a patch is created.|

  |type|Type of patch. Example: Windows|

  ##### Notes

  There are special characters that can be used in a query string:

  - (+) represents the next field and must be URL-encoded.

  - (:) represents equals. An example is key : value.

  - Space characters must be URL-encoded.
tags:
  - patching
path: '/api/v2/tenants/{tenantId}/patches'
request:
  - get
layout: api-doc
draft: false
---
