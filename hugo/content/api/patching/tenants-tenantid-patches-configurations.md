---
slug: tenants-tenantid-patches-configurations
title: Create patch configuration and execute
description: >-
  Creates a patch configuration and executes patches on the resources.


  ##### Notes

  - Approved Windows patches are installed on the device during the scheduled
  installation window.

  - The device is immediately rebooted following any patch that requires a
  reboot.

  - Standard checks are performed on rebooted devices to ensure the device is
  operating properly.
tags:
  - patching
path: '/api/v2/tenants/{tenantId}/patches/configurations'
request:
  - post
layout: api-doc
draft: false
---
