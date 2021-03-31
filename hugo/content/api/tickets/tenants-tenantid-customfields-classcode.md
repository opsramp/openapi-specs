---
slug: tenants-tenantid-customfields-classcode
title: Get custom fields
description: >-
  Gets details of custom fields attached to an entity.


  Use the supported entities along with their class code:


  |Entity|Class Code|

  |----|----|

  |Service request|SERVICEREQUEST|

  |Time-bound request|ACSTICKET|

  |Task|TASK|

  |Incident|INCIDENT|

  |Problem|PROBLEM|

  |Change request|CHANGE|

  |Scheduled tasks|SCHEDULEDTASK|

  |User|USER|

  |Knowledge base article|KBARTICLE|


  Create custom fields for the entity and then use this endpoint to get the list
  of configured custom fields.


  To create an ITSM entity, both Subject and Description are mandatory fields.
  Requested By, Assignee Group, and the other fields are optional. To include
  additional information, create custom fields for the respective entity from
  the following types of custom fields:

  - Drop-down

  - Text

  - Multi-line text

  - Numeric

  - Checkbox

  - Date

  - Date-time
tags:
  - tickets
path: '/api/v2/tenants/{tenantId}/customFields/{classCode}'
request:
  - get
layout: api-doc
draft: false
---
