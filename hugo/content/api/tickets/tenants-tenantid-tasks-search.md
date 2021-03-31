---
slug: tenants-tenantid-tasks-search
title: Search tasks
description: >-
  Searches tasks.


  >##### Notes

  The request parameter include is required to get the following information in
  the response:

  >- Custom fields

  >- Status flow

  Example: include=customFields, statusFlow


  ##### Query Variables


  |Field|Default Value|

  |----|----|

  |uniqueId|ID of the task.<br>Example: CHG0000002401|

  |status|Current status of task.<br>Supported values: New, Open, Pending,
  Resolved, Closed, and On Hold.<br>Example: Closed, Resolved|

  |priority|Current priority of task.<br>Supported values: Low, Normal, High,
  Urgent, and Very Low<br>Example: High, Urgent|

  |subject|A short summary of task.<br>Example: task from Alert.|

  |assignedTo|User who has been assigned task.<br>Example: USR0000000129|

  |requester|User who requests the task.<br>Example: USR0000000129|

  |startCreationDate|Filter task with the creation date. Provide the from
  date.<br>Example: 2016-07-26T14:49:44 0000 (GMT)|

  |endCreationDate|Provide the to date.<br>Example: 2016-07-28T07:12:19 0000
  (GMT)|

  |startUpdationDate|Filter task with the updation date.<br>Example:
  2016-08-12T06:54:59 0000 (GMT)|

  |endUpdationDate|Provide the to date.<br>Example: 2016-08-15T10:40:20 0000
  (GMT)|

  |oldStatus|Previous status of task.<br>Supported values: New, Open, Pending,
  Resolved, and On Hold<br>Example: Resolved|

  |oldPriority|Previous priority of task.<br>Supported values: Low, Normal,
  High, Urgent, and Very Low<br>Example: Urgent|

  |deviceId|Unique ID of the device.<br>Example:
  481af404-33a6-4d61-af77-c483ca6641fa|

  |source|Source of the task.<br>Supported values: PORTAL, INTEGRATION, MOBILE,
  EMAIL|

  |sourcePolicyType|Source policy type of the task.<br>Supported values:
  AUTOINCIDENT, INTEGRATION|

  |firstContactFix|Problem fixed without assigning to another group.<br>Example:
  true, false|

  |startResponseBreachDate|Filter task with response breach date. Provide from
  date.<br>Example: 2016-08-25T08:12:19+0000 (GMT)|

  |endResponseBreachDate|Provide to date.<br>Example: 2016-09-28T10:40:20 0000
  (GMT)|

  |startResolutionBreachDate|Filter task with resolution breach date. Provide
  from date.<br>Example: 2016-08-25T08:12:19 0000 (GMT)|

  |endResolutionBreachDate|Provide to date.<br>Example: 2016-09-29T10:40:20 0000
  (GMT)|

  |responseBreach|Response to task beyond the time limit.<br>Example: false|

  |resolutionBreach|task fixed within the time limit.<br>Example: true|

  |assigneeGroupIds|ID of the group to which the task is assigned.<br>Example:
  1, 2, 3|

  |minResponseTime|Minimum response time of task.<br>Example: 300 (time in
  seconds)|

  |maxResponseTime|Maximum response time of task.<br>Example: 600 (time in
  seconds)|

  |minResolutionTime|Minimum resolution time of task.<br>Example: 3600 (time in
  seconds)|

  |maxResolutionTime|Maximum resolution time of task.<br>Example: 7200 (time in
  seconds)|

  |minReOpens|Minimum number of times task is reopened.<br>Example: 5|

  |maxReOpens|Maximum number of times task is reopened.<br>Example: 8|

  |startClosedDate|Filter tasks with the closed date. Provide the from closed
  date.<br>Example: 2016-08-12T06:54:59 0000 (GMT)|

  |endClosedDate|Provide to closed date.<br>Example: 2016-08-15T06:54:59 0000
  (GMT)|

  |startResolvedDate|Filter tasks with the resolved date. Provide from resolved
  date.<br>Example: 2016-08-12T06:49:59 0000 (GMT)|

  |endResolvedDate|Provide to resolved date.<br>Example: 2016-08-14T07:49:59
  0000 (GMT)|

  |extTicketId|External ticket ID.|


  >##### Notes

  >To view tickets created within a given date range, provide both
  startCreationDate and endCreationDate. Otherwise, the tickets created in the
  last month would be returned.

  >There are special characters that can be used in a query string:

  >- (+) represents the next field and must be URL-encoded.

  >- (:) represents equals. An example is `key : value`.

  >- Space characters must be URL-encoded.

  >- Date format must be yyyy-MM-ddTHH:mm:ssZ (GMT)
tags:
  - tickets
path: '/api/v2/tenants/{tenantId}/tasks/search'
request:
  - get
layout: api-doc
draft: false
---
