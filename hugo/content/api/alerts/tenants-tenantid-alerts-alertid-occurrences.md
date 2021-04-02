---
slug: tenants-tenantid-alerts-alertid-occurrences
title: Get alerts for alert-triggered time
description: >
  Gets the alert occurrences based on the alert-triggered time.


  ##### Notes

  There are special characters that can be used in a query string:

  - (+) represents the next field and must be URL-encoded.

  - (:) represents equals. An example is key : value.

  - Space characters must be URLencoded.

  - Date format must be yyyy-MM-ddTHH:mm:ssZ (GMT).


  ### The process for pagination

  The API provides the results in descending order of alert-triggered date. The
  latest alert appears first based on the alert-triggered time. The process for
  handling any number of occurrences include the following:

  1. Get all occurrences of an alert.

  2. Get alert occurrences of an alert that is triggered within a specific
  duration.

  3. Traverse through each page of occurrences.


  ### Get All occurrences of an alert

  To fetch all alert occurrences irrespective of the alert-triggered time,
  provide the URI:

  ```

  /tenants/{tenantId}/alerts/{alertId}/occurrences

  ```


  ### Get Alert occurrences of an alert that is triggered within a specific
  duration

  To fetch raw alerts triggered within a specific duration, provide the start
  time and end time. To fetch raw alerts triggered between January 13th 2017 to
  February 13th 2017, provide the startTime of 2017-01-13T00:00:00 0000 and an
  endTime of 2016-02-13T00:00:00 0000. This is the URI for that request:

  ```

  /tenants/{tenantId}/alerts/{alertId}/occurrences?queryString=startTime:2017-01-13T00:00:00
  0000+endTime:2017-02-13T00:00:00 0000

  ```


  ### Traverse through each page of occurrences

  There is a limit of 100 results per page. If an alert has 120 occurrences, the
  latest 100 results will appear in the first page. To traverse to the second
  page, use the endDate from the first page and provide it as the endTime in the
  query string. The second page will return the remaining 20 alerts.


  Use these fields when traversing through additional pages as long as
  `nextPage: true`:


  |Field|Description|

  |-----|-----|

  |results|List of raw alerts data.|

  |pageSize|The page size that represents the total number of results to display
  on the page. The default page size is 100.|

  |nextPage|This flag helps determine when the search is complete. If nextPage:
  false, the search is done. to traverse through the rest of the pages.|

  |descendingOrder|Alerts appear in a descending order. The latest triggered
  alert appears on the top.|

  |startDate|Indicates the alert-triggered time of the first result on the
  page.|

  |endDate|Indicates the alert-triggered time of the last result on the page. To
  traverse through the other pages, provide endDate from previous page and
  provide it as endTime in queryString.|
tags:
  - alerts
path: '/api/v2/tenants/{tenantId}/alerts/{alertId}/occurrences'
request:
  - get
layout: api-doc
draft: false
---
