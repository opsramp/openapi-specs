---
slug: tenants-tenantid-integrations-install-vmware
title: Install VMWARE integration
description: |-
  These endpoint IDs are used to install compute integrations
  - Pre-requistes:
    - User needs to use the set credentials for the VMware infra. To set credentials https://docs.opsramp.com/api/tenancy-access-controls/tenants-tenantid-credentialsets/
    - User needs gateway profile ids, which can be known using search endpoint at https://docs.opsramp.com/api/agents-gateways/tenants-tenantid-managementprofiles-search/
    - Supported values are not case-sensitive. 'All' & 'all' both are valid.
    - For "schedule" attributes in payload refer https://docs.opsramp.com/api/integrations/tenants-tenantid-policies-discovery-search/

  The following compute integrations are supported:
    - VMWARE
  These are only for private cloud discovery configurations
tags:
  - integrations
path: '/api/v2/tenants/{tenantId}/integrations/install/VMWARE'
request:
  - post
layout: api-doc
draft: false
---
