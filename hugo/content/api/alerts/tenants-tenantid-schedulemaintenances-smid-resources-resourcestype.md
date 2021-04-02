---
slug: tenants-tenantid-schedulemaintenances-smid-resources-resourcestype
title: End scheduled maintenance window
description: >-
  Ends a scheduled maintenance window.


  ##### Notes

  - User can end only active schedule maintenance windows.

  - Active schedule maintenance windows that are one-time maintenance windows
  move to a completed state. Recurring maintenance windows move to pending
  state.
tags:
  - alerts
path: >-
  /api/v2/tenants/{tenantId}/scheduleMaintenances/{smId}/resources/{resourcesType}
request:
  - post
layout: api-doc
draft: false
---
