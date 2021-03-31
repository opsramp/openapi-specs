---
slug: tenants-tenantid-incidents
title: Create incident
description: >-
  Creates an incident.


  Below are the steps to attach a business impact and urgency to an incident.


  Step 1: Create the business impact and urgency from OpsRamp.


  Instructions to create business impact:

  1. Login to OpsRamp.

  2. Click Setup.

  3. On the left-hand side panel click Service Desk.

  4. Click Business Impacts, select the client, and select the business impact
  status.

  5. Click Add, provide name and description. Click Create.


  Instructions to create Urgency:

  1. Click Setup.

  2. On the left-hand side panel and click Service Desk.

  3. Click Urgencies, select the client and then select the urgency status.

  4. Click Add, provide the name and description and then click Create.


  Step 2: Use Get Business Impacts and Get Urgencies to fetch the business
  impacts and urgencies created.


  Step 3: Provide the IDs in the request payload.
tags:
  - tickets
path: '/api/v2/tenants/{tenantId}/incidents'
request:
  - post
layout: api-doc
draft: false
---
