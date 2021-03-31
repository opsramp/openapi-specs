---
slug: tenants-tenantid-roles
title: Create role
description: >-
  Creates a partner- or client-level role.


  A role defines permission sets to user and -user groups on devices and device
  groups. A user (or user group) can be assigned to one or more roles


  ### Create a Role with Scope: MSP and Provide Visibility of Specific Clients

  - Create a role that is applicable only for partners.

  - Users in this role can view only specific clients:


  ### Create a Role with Scope: MSP and Provide Visibility of All Clients,
  Devices, and Credentials

  - Create a role that applies only for a partner.

  - Users in this role can view all clients (under the partner)


  ### Create a Role with Scope: Client and Provide Visibility of All Devices and
  Credentials

  Create a role that is applicable only for a partner:


  - Users in the role can view all clients under the partner.

  - Users in the role can view all client devices and credentials.


  ### Create a Role with Scope: Client and Provide Visibility of Specific
  Devices, and Credentials

  Create a role that is applicable for client:


  - Users in the role can view all client devices.

  - Users in the role can view all client credential sets.
tags:
  - tenancy-access-controls
path: '/api/v2/tenants/{tenantId}/roles'
request:
  - post
layout: api-doc
draft: false
---
