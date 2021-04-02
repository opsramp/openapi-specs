---
slug: tenants-tenantid-devicegroups
title: Create and update device groups
description: |-
  Creates and updates device groups.

  ### Update Group
  Updates the details of a device group with one of these actions:

  - Rename a device group
  - Change the set of devices residing in a device group
  - Change knowledge base articles assigned to a device group
  - Add a device group as a child under an existing device group (the parent)

  ### Add a device group as a child in an existing device group
  The existing device group becomes the parent of the child device group.
tags:
  - resource-management
path: '/api/v2/tenants/{tenantId}/deviceGroups'
request:
  - post
layout: api-doc
draft: false
---
