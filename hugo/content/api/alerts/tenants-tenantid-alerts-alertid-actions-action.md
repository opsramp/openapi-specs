---
slug: tenants-tenantid-alerts-alertid-actions-action
title: Post action on an alert
description: >-
  Posts an action on an alert.


  ##### Notes

  When unacknowledge or unsuppress is specified, the alert status becomes either
  open or ticketed (if there is an incident ID associated with the alert).
tags:
  - alerts
path: '/api/v2/tenants/{tenantId}/alerts/{alertId}/actions/{action}'
request:
  - post
layout: api-doc
draft: false
---
