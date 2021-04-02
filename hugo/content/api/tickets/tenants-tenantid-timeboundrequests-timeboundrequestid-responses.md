---
slug: tenants-tenantid-timeboundrequests-timeboundrequestid-responses
title: Add response to a time bound request
description: >-
  Adds a response to a time bound request.


  >##### Notes

  >- For attachments, files must be converted to bytes stream with
  base64-encoding.

  >- The default creator (OpsRamp API User) can send id and loginName to change
  the default.

  >- Based on the setting Make default submission status of a pending request as
  open, the status of the Pending request will change to Open.

  >- A file attachment is limited to 50MB.

  >- Date format is yyyy-MM-ddTHH:mm:ssZ (GMT).
tags:
  - tickets
path: '/api/v2/tenants/{tenantId}/timeBoundRequests/{timeBoundRequestId}/responses'
request:
  - post
layout: api-doc
draft: false
---
