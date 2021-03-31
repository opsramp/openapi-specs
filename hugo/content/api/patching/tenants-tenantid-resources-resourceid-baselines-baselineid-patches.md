---
slug: tenants-tenantid-resources-resourceid-baselines-baselineid-patches
title: Check resource patch compliance against baseline
description: |-
  Checks the compliance of a resource against a patch baseline.

  ##### Notes
  There are special characters that can be used in a query string:
  - (+) represents the next field and must be URL-encoded.
  - (:) represents equals. An example is key : value.
  - Space characters must be URL-encoded.
tags:
  - patching
path: >-
  /api/v2/tenants/{tenantId}/resources/{resourceId}/baselines/{baselineId}/patches
request:
  - get
layout: api-doc
draft: false
---
