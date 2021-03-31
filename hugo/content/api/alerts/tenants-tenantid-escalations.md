---
slug: tenants-tenantid-escalations
title: Create alert escalation policy
description: >
  Creates an alert escalation policy. The policy is a predefined action to be
  taken when an alert is not acknowledged.


  ##### Notes

  - resources: Used to define different resources to apply the escalate alert
  policy.

  - escalations: Used to define the users for escalated alerts notifications.

  - escalationType:
      - AUTOMATIC_UNTIL_ACKNOWLEDGED_CLOSED_SUPPRESSED_TICKETED: Automated notifications via recipient users until acknowledged, closed, suppressed, or ticketed.
      - AUTOMATIC_UNTIL_ACKNOWLEDGED_CLOSED_SUPPRESSED: Automated notifications via recipient users until acknowledged, closed, or suppressed.
      - MANUAL – Contact users directly as required.
  - filterCriteria – Use the following request structure for 'Alert : Occurrence
  Frequency'.

  - occurrences – Any integer.

  - frequency – Any integer.

  - frequencyType – hours or days or weeks
tags:
  - alerts
path: '/api/v2/tenants/{tenantId}/escalations'
request:
  - post
layout: api-doc
draft: false
---
