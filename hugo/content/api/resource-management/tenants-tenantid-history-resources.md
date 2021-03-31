---
slug: tenants-tenantid-history-resources
title: Search decommissioned resources
description: >-
  Gets the list of decommissioned resources.


  Notes

  There are special characters that can be used in a query string:

  - (+) represents the next field and must be URL-encoded.

  - (:) represents equals. An example is `key : value`.

  - Space characters must be URL-encoded.

  - Date format must be `yyyy-MM-ddTHH:mm:ssZ (GMT)`.


  ##### Query Variables


  |Query Variables|Description|

  |----|----|

  |id|Resource ID.<br>Example: d7bce6fe-d19f-4ad7-8c50-2f639f2dd778|

  |state|Resource state.Supported value: DECOMMISSIONED|

  |hostName|Resource host name.<br>Example: SJKT1212|

  |ipAddress|Resource IP Address.<br>Example: 10.23.89.226|

  |instanceId|Cloud instance ID.|

  |tags|Additional information of a resource, preferably, a custom attribute
  name.|

  |startDate|Search for resources decommissioned within a specific duration.
  startDate indicates the from date. For example, to fetch list resources
  decommissioned between 14th Aug 2018 to 18th Aug 2018, provide startDate as
  2018-08-14T10:20:20 0000 and endDate as 2018-08-18T12:10:20 0000Note: Date
  format: yyyy-MM-ddTHH:mm:ssZ (GMT).|

  |endDate|Search for resources decommissioned within a specific duration.
  endDate indicates the to date.Note: Date format: yyyy-MM-ddTHH:mm:ssZ (GMT).|

  |type|Resource type.<br>Example: DEVICE|

  |accountNumber|Instance account number. This varies for each provider:<br>-
  AWS: Account number<br>- Azure: Subscription ID<br>- Google: Project ID|

  |provider|Cloud provider name.<br>Example: AWS|

  |owner|Owner ID.<br>Example: 23422135901|

  |instanceType|Cloud instance type.|

  |instanceState|Cloud instance state.Supported Value: DECOMMISSIONED|

  |zone|Zone name in which instance is located.<br>Example: virgina-east|

  |region|Geographical location in which instance is located.<br>Example:
  US-EAST|

  |ami|Amazon Machine image.|

  |hostedServiceName|Domain role.|

  |startLaunchDate|Search for decommissioned cloud instances launched within a
  specific duration.Provide from date.<br>Example: 2018-07-11T10:05:20 0000|

  |endLaunchDate|Search for decommissioned cloud instances launched within a
  specific duration.Provide to date.<br>Example: 2018-08-20T11:10:20 0000|
tags:
  - resource-management
path: '/api/v2/tenants/{tenantId}/history/resources'
request:
  - get
layout: api-doc
draft: false
---
