---
slug: tenants-tenantid-customfields-classcode-customfieldid
title: Get custom field
description: >-
  Gets the details of a custom field.


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

  >Custom fields are user defined fields to include additional information of
  the entity.
tags:
  - tickets
path: '/api/v2/tenants/{tenantId}/customFields/{classCode}/{customFieldId}'
request:
  - get
layout: api-doc
draft: false
---
