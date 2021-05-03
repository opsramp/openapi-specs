---
slug: tenants-tenantid-resources-search
title: Search resources
description: >
  Gets the resources of a partner or a client.


  ##### Query Variables


  |Query Variables|Description|

  |-----|-----|

  |hostName|Name of the host.|

  |dnsName|Domain service name.|

  |resourceName|Name of the resource.|

  |aliasName|Other name of resource.|

  |id|Resource unique ID.<br>Example: d5bce6fe-d19f-4ad7-8c50-5f639f2dd321|

  |serialNumber|Resource serial number.<br>Example:
  d7bce6fe-d19f-4ad7-8c50-2f639f2dd778|

  |ipAddress|Resource IP address.|

  |systemUID|System Unique ID.<br>Example: 10.10.10.10|

  |state|Resource state supported values: active, inactive, discovered, all.
  Filter devices based on the device state.<br>Example: discovered|

  |type|Values accepted as Resource Type:DEVICE, AUTO_SCALING, EBS,
  LOAD_BALANCER, SQL_DATABASE, SQL_SERVER, SYNTHETIC<br>Example: DEVICE|

  |deviceType|Filter resources based on device type. This parameter is required
  if the resource type is a device. Use Get Device Types API to get the names of
  supported device types. Enumerate multiple device type names with
  comma-separated strings.<br>Example: Windows, Linux|

  |resourceType|Filter resources based on a resource type. Use Get Device Types
  API to get a list of supported resource types supported by OpsRamp. Enumerate
  multiple resource types with comma-separated strings.<br>Example: DEVICE,
  DOCUMENT_DB|

  |startCreationDate|Indicates the date to search the creation date of a
  resource. Start indicates from date.<br>Example: 2017-01-01T00:00:00 0000|

  |endCreationDate|Indicates the date to search for the last date of resource
  creation. End indicates to date.<br>Example: 2017-01-31T00:00:00 0000|

  |startUpdationDate|Search for a resource updated within a specific duration.
  Start indicates from date.<br>Example: 2017-01-01T00:00:00 0000|

  |endUpdationDate|Search for a resource updated within a specific duration.
  End  indicates to date.<br>Example: 2017-01-31T00:00:00 0000|

  |tags|Custom attribute tag names. Enumerate multiple tags, by separating each
  tag with a comma.<br>Example: Admin|

  |template|Monitoring template ID used to get the list of devices assigned on a
  particular template.|

  |agentProfile|Agent profile ID.|

  |gatewayProfile|Gateway profile ID.|

  |instanceId|Cloud instance ID.|

  |accountNumber|Cloud provider's account number.<br>Example: 290642135901|

  |installedIntgId|Installed integration ID.<br>Example:
  INTG-6dcbc22c-5436-5eb8-5e7c-8db0319938a4|

  |agentInstalled|Filter for agent-installed resources:<br>- agentInstalled:
  true gets agent-installed resources.<br>- agentInstalled: false gets non-agent
  resources.<br>Example: true|

  |deviceGroup|Fetch resources that are part of a specific device/child group.
  Provide a device group name.<br>Example: Windows Servers|

  |serviceGroup|Fetch resources that are part of a specific service group.
  Provide service group name.<br>Example: Admin Group|

  |deviceLocation|Fetch resources that are at a specific location. Provide a
  location name.<br>Example: West-SJ|

  |isEquals|To search for the exact match of a variable.<br>- isEquals: true ,
  to search for the exact match of a variable.<br>- isEquals: false to search
  for a similar match of a variable.<br>For example, to fetch list of resources
  in location West Valley and resource group, provide the query variable
  respectively as:<br>- deviceLocation: West Valley%2BisEquals: true<br>-
  deviceGroup: Windows Servers%2BisEquals:true<br>Note: This is an optional
  parameter for deviceGroup/deviceLocation/serviceGroup|

  |assetManagedTime|The most recent time a resource is managed. The asset
  managed time gets updated whenever a resource is managed or
  unmanaged.<br>Example: 2017-01-01T00:00:00 0000|

  |firstAssetManagedTime|The first time a resource is managed.<br>Example:
  2017-01-31T00:00:00 0000|

  |aliasIp|Alias IP address of the network you have.|

  |appRoles|Filter for resources based on applications running on the
  resources.List of supported applications:|

  |osArchitecture|Filter for supported architecture 32 bit or 64 bit|


  |appRoles|appRoles|appRoles|appRoles|

  |-----|-----|-----|-----|

  activemq|hbase|mongodb|rabbitmq

  apache|hdfs-datanode|monitdMemoryStats|redis

  cassandra|hdfs-namenode|moxi-server|riak

  ceph|iptable|mysql|solr

  couchbase|jboss|nfsiostat|spark

  couchdb|kafka|nginx|squid

  DNS-Server|kubernetes|ntp|tomcat

  docker|kvm|openvpn|varnish

  docker-container|lighttpd|oracle|weblogic

  elasticsearch|mesosmaster|postfix|websphere

  haproxy|mesosslave|postgresql|zookeeper


  ##### Notes

  There are special characters that can be used in a query string:

  - (+) represents the next field and must be URL-encoded.

  - (:) represents equals. An example is key : value.

  - Space characters must be URL-encoded.

  - Date format must be yyyy-MM-ddTHH:mm:ssZ (GMT).
tags:
  - resource-management
path: '/api/v2/tenants/{tenantId}/resources/search'
request:
  - get
layout: api-doc
draft: false
---
