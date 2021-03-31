---
slug: tenants-tenantid-alert
title: Create alert on a resource
description: >-
  Creates a single alert on a resource.


  ##### Notes

  - A list of event IDs is generated when alerts are created. This list is valid
  for 30 days.

  - Use the event IDs to search and get alert details.


  Creation of a new resource depends on the following:


  - A new resource is created and new device group, service group, and location
  are assigned.

  - A new resource is created and existing device group, service group, and
  location are assigned.

  - An already existing resource cannot be assigned to a new or existing Device
  Group, Service Group and Location.
tags:
  - alerts
path: '/api/v2/tenants/{tenantId}/alert'
request:
  - post
layout: api-doc
draft: false
---
