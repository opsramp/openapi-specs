---
slug: tenants-tenantid-monitoring-templates-search
title: Search templates
description: >-
  Searching for template based on query parameters


  ##### Query Variables

  |Query Variables|Description|

  |-----|-----|

  |id|Template ID.|

  |name|Template name.|

  |scope|Template scope. Example: Global [note 3]|

  |collectorType|Collector type.<br>Supported values are: Agent, Gateway,
  OpsRamp Cloud, AWS, GOOGLE, AZURE|

  |status|Template status.<br>Example: ACTIVE, EOL

  |generation|The generation.<br>Example: 1, 2|

  |startCreationDate|Search for templates created within a certain
  duration.<br>startCreationDate denotes the from date.|

  |endCreationDate|Search for templates created within a certain
  duration.<br>endCreationDate denotes the to date.|

  |startUpdationDate|Search for templates updated within a certain
  duration.<br>startUpdationDate denotes the from update date.|

  |endUpdationDate|Search for templates updated within a certain
  duration.<br>endUpdationDate denotes the to update date.|

  |sourceType|Template source.<br>Supported values are: DEVICE, DATA_CENTER,
  VI_CLUSTER, VI_DATASTORE, JMX_APP_CLUSTER, JMX_APP_INSTANCE,
  DISTRIBUTED_VIRTUAL_SWITCH, CONTRAIL_ANALYTICS_NODE, CONTRAIL_CONFIG_NODE,
  CONTRAIL_CONTROL_NODE, VIRTUVAL_ROUTER, STORAGE_ARRAY_VOLUME|


  ##### Notes

  1. There are special characters that can be used in a query string:

  - (+) represents the next field and must be URL-encoded.

  - (:) represents equals. An example is key : value.

  - Space characters must be URL-encoded.

  2. Date format must be yyyy-MM-ddTHH:mm:ssZ (GMT).

  3. Provide scope: Global, to get gGlobal templates

  4. Provide scope: OpsRamp, to get OpsRamp templates

  5. CLIENT AUTHENTICATION
      1. Provide scope: Partner, to get partner templates
      2. Provide scope: Client, to get client templates
    6. PARTNER AUTHENTICATION
      1. Provide scope: Partner, to get partner templates
      2. Use this API with respective client_id, to get client templates as shown in example URL 1

  Note: queryString not required with scope.


  7. SERVICE PROVIDER AUTHENTICATION
      1. Use this API with respective msp_id, to get partner templates as shown in example URL 3

  Note: queryString not required with scope.

      2. Use this API with respective client_id, to get client templates as shown in example URL 1

    Note: queryString not required with scope.

  8. Provide sourceType = DEVICE, to get available templates at the device
  level.


  Note: This can be useful in assigning templates to a device.
tags:
  - monitoring
path: '/api/v2/tenants/{tenantId}/monitoring/templates/search'
request:
  - get
layout: api-doc
draft: false
---
