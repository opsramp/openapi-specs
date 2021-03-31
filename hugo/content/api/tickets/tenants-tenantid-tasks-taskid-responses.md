---
slug: tenants-tenantid-tasks-taskid-responses
title: Add response to task
description: >-
  Adds a response to a task.


  >##### Notes

  >- For attachments, files must be converted to bytes stream with
  base64-encoding.

  >- The default creator (OpsRamp API User) uses id and loginName to change
  default settings.

  >- Make default submission status of a pending request as open, the status of
  the incident which is in Pending status will change to Open status.

  >- The maximum file attachment size is 50MB.
tags:
  - tickets
path: '/api/v2/tenants/{tenantId}/tasks/{taskId}/responses'
request:
  - post
layout: api-doc
draft: false
---
