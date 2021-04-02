---
slug: tenants-tenantid-managementprofiles-search
title: Search for management profile
description: >-
  Searches for a management profiles.

  ##### Query Variables

  |Variable|Value|Description|

  |---|---|---|

  |id|{id}|The management profile ID.|

  |name|{name}|The management profile name.|

  |type|Agent, Gateway|The anagement profile type. An example is: Agent.|

  |startCreationDate|{startCreationDate}|Search for the management profile
  created within a certain duration. Start indicates the from date. An example
  is: 2016-06-10T10:40:20 0000 (GMT).|

  |endCreationDate|{endCreationDate}|Search for the management profile created
  within a certain duration. End indicates the to date. An Example is:
  2016-06-20T10:40:20 0000 (GMT).|

  ##### Notes

  1. Special characters in the query string
      1. Plus (+) indicates next field and must be URL encoded.
      2. Color (:) indicates Equals. An example is: key: value.
      3. Space characters must be URL encoded.
  2. Date format must use this format: yyyy-MM-ddTHH: mm: ssZ (GMT).
tags:
  - agents-gateways
path: '/api/v2/tenants/{tenantId}/managementProfiles/search'
request:
  - get
layout: api-doc
draft: false
---
