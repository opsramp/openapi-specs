---
slug: tenants-tenantid-integrations-installed-installedintgid-event
title: Create integration event
description: >-
  Creates an integration event.


  Events are used for sending certain notifications whenever an action is
  performed on OpsRamp entities.


  ###### Notes


  - Provide API payload in Base64 encoding.

  - Integration event for Alert entity is created only using API but can be
  viewed from the OpsRamp Portal.


  Create Event with Alert Entity Type to create an event with alert entity type
  for work flow events only.
tags:
  - integrations
path: '/api/v2/tenants/{tenantId}/integrations/installed/{installedIntgId}/event'
request:
  - post
layout: api-doc
draft: false
---
