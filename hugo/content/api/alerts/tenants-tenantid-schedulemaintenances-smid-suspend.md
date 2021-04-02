---
slug: tenants-tenantid-schedulemaintenances-smid-suspend
title: Suspend scheduled maintenance window
description: >-
  Suspends a scheduled maintenance window.


  ##### Notes

  - Only active schedule maintenance windows can be suspended.

  - Dates in date range consider date as yyyy-MM-dd and ignore the time HH: mm:
  ss.

  - Send dates (start date & end date) in GMT format.
tags:
  - alerts
path: '/api/v2/tenants/{tenantId}/scheduleMaintenances/{smId}/suspend'
request:
  - post
layout: api-doc
draft: false
---
