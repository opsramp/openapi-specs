---
slug: tenants-tenantid-timeboundrequests-timeboundrequestid-close
title: Close time bound request
description: >-
  Closes a time bound request.


  Follow the steps before closing a time bound request:


  Step 1: To enable the option to provide reason for closing a time bound
  request.

  1. Log into OpsRamp.

  2. Click Setup.

  3. On the left-hand side panel, click Service Desk.

  4. In Configuration, click Settings.

  5. Select client and then click Customize.

  6. In the Time Bound Request section, select option Enable reasons to change
  status Close and then click Save.


  Step 2: Check the status flow transition for Closed.

  1. Click Setup.

  2. On the left-hand panel, click Service Desk.

  3. In Configuration, click Status Flows.

  4. Check the status flow for the entity Time Bound and check the transition of
  the status Closed.

  5. If Closed is unavailable, this indicates the time bound request cannot be
  closed.


  Step 3: Provide the reason for changing the status.

  1. Click Setup.

  2. On the left-hand side panel, click Service Desk.

  3. In Configuration, click Status Change Reasons.

  4. Click Add, select the scope, client, request type, entity status as Closed
  and provide the reason and then click Submit.


  >##### Notes

  >- Use the get time bound request to check if status Closed and reasons to
  provide for Close are enabled. If under the field allowedStatus if name:
  Closed and reasonsEnabled: true, this indicates reasons should be provided for
  closing a time bound request.

  >- Use the get status change reasons to provide the reasons to Close. The
  reasons configured in status: Closed are accepted, but a new provided reason
  would result in an error.
tags:
  - tickets
path: '/api/v2/tenants/{tenantId}/timeBoundRequests/{timeBoundRequestId}/close'
request:
  - post
layout: api-doc
draft: false
---
