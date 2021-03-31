---
slug: tenants-tenantid-patches-resourceid-scan-status
title: Get patch scan status of all devices of a missing job
description: >-
  Gets the patch scan status of all devices assigned to a missing patch job and
  display paginated output.


  ##### Query Variables


  |Query Variables|Description|

  |-----|-----|

  |id|Unique ID of the device.|

  |ipAddress|IP address of the device.|

  |resourceName|Name of the device.|

  |hostName|Host name of the device.|

  |aliasName|Alias name of the device.|

  |resourceType|Type of the device.|
tags:
  - patching
path: '/api/v2/tenants/{tenantId}/patches/{resourceId}/scan/status'
request:
  - get
layout: api-doc
draft: false
---
