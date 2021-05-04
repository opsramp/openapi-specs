---
slug: tenants-orgid-clients-clientid-action
title: Activate or deactivate client
description: >-
  Activates and deactivates a client.


  The action specified in the URL is the action to be performed on the client
  profile.


  ### Supported action types


  |Action|Description|

  |----|----|

  |activate|All clients operations are activated.|

  |suspend|Disable the client account and temporarily stop all client
  operations.|

  |terminate|Terminating the client will stop its operations, remove all agents,
  and uninstall all integrations|
tags:
  - tenancy-access-controls
path: '/api/v2/tenants/{orgId}/clients/{clientId}/{action}'
request:
  - post
layout: api-doc
draft: false
---
