---
slug: tenants-tenantid-resources-resourceid-patches-install-status
title: Get patching status of a device
description: >-
  Gets the patching status of a device.


  Patching status of a device provides the details of the most recent patches
  performed on a device. This API is used to get the following details of
  patching performed on a device (or devices):


  - Completion status of the patch

  - Status of machine reboot

  - Last patch installation date

  - Last reboot time of the machine
tags:
  - patching
path: '/api/v2/tenants/{tenantId}/resources/{resourceId}/patches/install/status'
request:
  - get
layout: api-doc
draft: false
---
