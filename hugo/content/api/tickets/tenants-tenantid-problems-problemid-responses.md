---
slug: tenants-tenantid-problems-problemid-responses
title: Add response to a problem
description: >-
  Adds a response to a problem.


  ##### Notes

  - For attachments, files must be converted to bytes stream with
  base64-encoding.

  - The default creator (OpsRamp API User) can send id and loginName to change
  the default.

  - Based on the setting Make default submission status of a pending request as
  open, the status of the Pending request will change to Open.

  - A file attachment is limited to 50MB.
tags:
  - tickets
path: '/api/v2/tenants/{tenantId}/problems/{problemId}/responses'
request:
  - post
layout: api-doc
draft: false
---
