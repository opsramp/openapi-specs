---
slug: tenants-tenantid-tasks-taskid-close
title: Close task
description: >-
  Closes a task.


  Perform these steps prior to closing a task:


  1. To enable the option to provide reason for closing a task: 
      1. Log into OpsRamp.
      2. Click Setup.
      3. On the left-hand side panel, click Service Desk.
      4. In Configuration, click Settings.
      5. Select client and then click Customize.
      6. In Tasks Settings section, select option Enable reasons to change status Close and then click Save.
  2. Check the status flow transition for Closed.
      1. Click Setup.
      2. On the left-hand side panel, click Service Desk.
      3. In Configuration, click Status Flows.
      4. Check the status flow for the entity Tasks and check the transition of the status Closed. If Closed is unavailable, this indicates the task cannot be closed.
  3. Provide the reason for changing the status:
      1. Click Setup.
      2. On the left-hand side panel, click Service Desk.
      3. In Configuration, click Status Change Reasons.
      4. Click Add,
      5. Select the scope, client, request type and entity status as Closed, provide the reason and click Submit.
  4. Use Get Task API to check if status Closed and reasons to provide for Close
  are enabled. In sample response, in the field allowedStatus if name: Closed
  and reasonsEnabled: true, this indicates reasons should be provided for
  closing a task.

  5. Use the Get status change reasons API to provide reasons to Close. Only
  status: Closed reason is accepted, any other reason would result in an error.
tags:
  - tickets
path: '/api/v2/tenants/{tenantId}/tasks/{taskId}/close'
request:
  - post
layout: api-doc
draft: false
---
