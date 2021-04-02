---
slug: tenants-tenantid-problems-categories-uniqueid
title: Update problem category
description: >-
  Updates a category of the entity type problem.


  Provide the unique ID of the category you would like to update. Use the get
  categories API to get the list of categories of the problem entity type.


  In this API, the following actions can be performed on a category:

  - Rename a category

  - Assign child categories to a parent category

  - Change the status of a parent category to a child category

  >A child category cannot be changed to a parent category using this API.


  Do the following to change the status:

  1. Log into OpsRamp.

  2. On the left-hand side panel. Select Service Desk and then Categories.

  3. Select entity select Change from the drop-down.

  4. Click on the category name to view the category page.

  5. Click Edit, select category type Parent, and then click Update.

  6. The category is now updated as a parent category.
tags:
  - tickets
path: '/api/v2/tenants/{tenantId}/problems/categories/{uniqueId}'
request:
  - post
layout: api-doc
draft: false
---
