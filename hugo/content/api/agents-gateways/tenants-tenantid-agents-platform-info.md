---
slug: tenants-tenantid-agents-platform-info
title: Get the Linux agent
description: >-
  Gets the Linux agent. This is usually followed by an API call to Download
  Linux Agent.


  Returns the JSON payload containing package name, package size, package
  checksum. The response also contains package S3 bucket URL for downloading the
  agent directly.
tags:
  - agents-gateways
path: '/api/v2/tenants/{tenantId}/agents/{platform}/info'
request:
  - get
layout: api-doc
draft: false
---
