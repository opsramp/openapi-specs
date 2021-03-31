---
slug: tenants-tenantid-users-search
title: Search tenant users
description: >-
  Gets users for a tenant.


  ##### Notes

  - This API provides minimal user details.

  - To get the complete details of a user, use the Get User API.


  ##### Query Variables


  |Query Variables|Description|

  |----|----|

  |uniqueId|ID of user.|

  |loginName|Login name of user.|

  |firstName|First name of user.|

  |lastName|Last name of user.|

  |mailId|User email.|

  |startCreationDate|Filter the users created within a date range. Provide the
  from date.<br>Example: 2016-11-01T11:54:24 0000|

  |endCreationDate|Filter the users created within a date range. Provide the to
  date.<br>Example: 2016-11-03T11:54:24 0000|

  |startUpdationDate|Filter the users updated within a date range. Provide the
  to date.<br>Example: 2016-11-01T11:54:24 0000|

  |endUpdationDate|Filter the users updated within a date range. Provide the to
  date.<br>Example: 2016-11-03T11:54:24 0000|

  |status|- To get a list of active users, provide status: active.<br>- To fetch
  list of inactive users, provide status: inactive.|


  ##### Notes

  There are special characters that can be used in a query string:

  - (+) represents the next field and must be URL-encoded.

  - (:) represents equals. An example is `key : value`.

  - Space characters must be URL-encoded.

  - Date format must be yyyy-MM-ddTHH:mm:ssZ (GMT).
tags:
  - tenancy-access-controls
path: '/api/v2/tenants/{tenantId}/users/search'
request:
  - get
layout: api-doc
draft: false
---
