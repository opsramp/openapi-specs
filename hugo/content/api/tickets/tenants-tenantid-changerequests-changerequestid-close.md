---
slug: tenants-tenantid-changerequests-changerequestid-close
title: Close change request
description: >-
  Closes a change request.


  Follow the steps before closing a change request:


  Step 1: Check the status flow transition for Closed.

  1. Login to OpsRamp.

  2. Click Setup.

  3. On the left-hand side panel, click Service Desk.

  4. In Configuration, click Status Flows.

  5. Check the status flow for the entity Change Request.

  6. Check the transition of the status Closed. If Closed is available this
  indicates the change request can be closed; otherwise, the change request
  cannot be closed.


  Step 2: Provide the reason for changing the status.

  1. Click Setup.

  2. On the left-hand side panel, click Service Desk.

  3. In Configuration, click Status Change Reasons and then click Add.

  4. Select the scope, client, request type and entity status as Closed, provide
  the reason and then click Submit.


  Step 3: Enable the option to provide reason for closing a change request.

  This is normally an optional step. However, this step is required to provide a
  reason for closing the change request.

  1. Click Setup.

  2. On the left-hand side panel, click Service Desk.

  3. In Configuration, click Settings.

  4. Select client and then click Customize.

  5. In Incident Request section, select option Enable reasons to change status
  Close and then click Save.


  ##### Notes

  - Use the get change request API to check if status Closed and reasons to
  provide for Close are enabled. If under the field allowedStatus if name:
  Closed and reasonsEnabled: true, this indicates reasons should be provided for
  closing an incident.

  - Use the get status change reasons API to provide the reasons to Close. The
  reasons configured in status: Closed are accepted, but a new provided reason
  would result in an error.

  - Date format must be yyyy-MM-ddTHH:mm:ssZ (GMT).
tags:
  - tickets
path: '/api/v2/tenants/{tenantId}/changeRequests/{changeRequestId}/close'
request:
  - post
layout: api-doc
draft: false
---
