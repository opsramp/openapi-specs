---
slug: tenants-tenantid-notes-search
title: Search for client notes
description: >-
  Searches for client notes.


  |Query Variables|Description|

  |------|-----|

  |searchWord|Search for a note with a specific word provided in the note.|

  |id|Note ID.|

  |startCreationDate|Search for note created within a specific date range.
  startCreationDate denotes the from date.<br>Example: 2016-03-25T09:54:52+0000|

  |endCreationDate|endCreationDate denotes the to date.<br>Example:
  2016-03-27T10:54:52+0000|

  |startUpdationDate|Search for the note updated within a specific date range.
  startUpdationDate denotes the from date.<br>Example: 2016-03-25T09:54:52+0000|

  |endUpdationDate|endUpdationDate denotes the to date.<br>Example:
  2016-03-27T10:54:52+0000|


  ##### Notes

  There are special characters that can be used in a query string:

  - (+) represents the next field and must be URL-encoded.

  - (:) represents equals. An example is `key : value`.

  - Space characters must be URL-encoded.

  - Date format must be yyyy-MM-ddTHH:mm:ssZ (GMT).
tags:
  - tenancy-access-controls
path: '/api/v2/tenants/{tenantId}/notes/search'
request:
  - get
layout: api-doc
draft: false
---
