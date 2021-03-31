---
slug: tenants-tenantid-schedulemaintenances-search
title: Search scheduled maintenance windows
description: >-
  Gets the scheduled maintenance windows under a specific tenant.


  ##### Notess

  There are special characters that can be used in a query string:

  - (+) represents the next field and must be URL-encoded.

  - (:) represents equals. An example is key : value.

  - Space characters must be URL-encoded.

  - Date format must be yyyy-MM-ddTHH:mm:ssZ (GMT).


  ##### Query Variables

  |Query Variable|Description|

  |-----|-----|

  |uniqueId|Schedule Maintenance window unique ID.|

  |name|Schedule Maintenance name.|

  |startDate|Start date of schedule maintenance.<br>Example: 2016-08-12T10:55:27
  0000|

  |endDate|Expiry date of schedule maintenance.<br>Example: 2016-09-15T18:55:27
  0000|

  |deviceUniqueId|Device ID|

  |Name|Name.|

  |deviceGroupId|Device group ID.|

  |deviceGroupName|Device group name.|

  |siteId|Site ID.|

  |siteName|Site name.|

  |startCreationDate|Filter schedule maintenance windows created within a date
  range. Provide from creation date.<br>Example: 2016-07-24T06:48:40 0000|

  |endCreationDate|Filter schedule maintenance windows created within a date
  range. Provide to creation date.<br>Example: 2016-07-26T06:48:40 0000|

  |startUpdationDate|Filter schedule maintenance windows updated within a date
  range. Provide from update date.<br>Example: 2016-07-24T06:48:40 0000|

  |endUpdationDate|Filter schedule maintenance windows updated within a date
  range. Provide to update date.<br>Example: 2016-07-26T06:48:40 0000|

  |status|Filter with scheduled maintenance window status. For example, to get
  all scheduled maintenance windows that are completed, provide status:
  Completed in the query string.<br>Supported statuses: Active, Pending,
  Suspended, and Completed.|
tags:
  - alerts
path: '/api/v2/tenants/{tenantId}/scheduleMaintenances/search'
request:
  - get
layout: api-doc
draft: false
---
