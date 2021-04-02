---
slug: tenants-tenantid-agents-platform-download-package-name
title: Download Linux agent
description: >-
  Downloads the Linux agents.


  This usually follows calling the Get Agent Package for Linux API.


  1. To capture the agent file: Use the package name from the response headers
  with the specific header package-name. The content of the file is available in
  the response body.

  2. Create a file with the same name as provided in the header and then write
  the contents of the response body into the file.
tags:
  - agents-gateways
path: '/api/v2/tenants/{tenantId}/agents/{platform}/download/{package-name}'
request:
  - get
layout: api-doc
draft: false
---
