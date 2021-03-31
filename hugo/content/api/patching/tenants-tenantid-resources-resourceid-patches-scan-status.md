---
slug: tenants-tenantid-resources-resourceid-patches-scan-status
title: Get patch scan status of a device
description: >-
  Gets the details of patch scan status of a device.


  Patch scan of a device provides the details of latest patch scan performed on
  a device. This API is used to get the following patch scan details of a
  device:


  - Date of the last scan

  - Result of the last scan

  - Patches missing before the scan

  - Patches found missing after the scan

  - List of new patches found in the last scan
tags:
  - patching
path: '/api/v2/tenants/{tenantId}/resources/{resourceId}/patches/scan/status'
request:
  - get
layout: api-doc
draft: false
---
