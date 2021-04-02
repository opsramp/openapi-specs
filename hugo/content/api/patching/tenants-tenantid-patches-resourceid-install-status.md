---
slug: tenants-tenantid-patches-resourceid-install-status
title: Get patching status of all devices in a patch configuration
description: >-
  Gets the patching status of all devices in a patch configuration and display
  paginated output.


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
path: '/api/v2/tenants/{tenantId}/patches/{resourceId}/install/status'
request:
  - get
layout: api-doc
draft: false
---
