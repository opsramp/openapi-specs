---
slug: tenants-tenantid-alerts-search
title: Search alerts
description: >-
  Searches alerts.


  ##### Query Variables

  |Query Variable|Value|Description|

  |----|---|---|

  |states|Ok, Warning, Critical, Info|Current status of the alert.

  |startDate|yyyy-MM-ddTHH:mm:ssZ|Filter the alert with alert base. startDate
  denotes the from date.<br>Example: 2016-02-24T09:19:47 0000 (GMT)|

  |endDate|yyyy-MM-ddTHH:mm:ssZ|endDate denotes to date.<br>Example:
  2016-02-26T10:20:47 0000 (GMT)|

  |priority|P0, P1, P2, P3, P4, P5|Priority of the alert.<br>Example: P0, P1.
  Separate the values with a comma.|

  |uniqueId|NA|ID of the alert.|

  |deviceStatus|manage, unmanage, all|Status of the device.|

  |resourceType|LOAD_BALANCER, SQS, EBS, DEVICE, SNS, REDSHIFT, SERVICE|Type of
  resource.|

  |resourceIds|NA|ID of a resource.<br>Example:
  DEV0000015754,148e892d-84ce-496c-a123-f91e1a8a3f7d.|

  |actions|ACKNOWLEDGED, TICKETED, CLOSED, IGNORE, SUPPRESSED, OPEN, PURGED,
  CORRELATED|Actions performed on the alert.<br>Example: ACKNOWLEDGED,
  TICKETED.|

  |alertTypes|Monitoring, Maintenance, Appliance, Agent, Scheduled Maintenance,
  Obsolete, Integration Failure, all|Types of Alerts.<br>Example: Maintenance,
  Appliance, Agent.|

  |metrics|NA|Metric type of the alert.<br>Example: PING, SNMP Response.|

  |duration|1, 7, 30|Duration of alert. Duration is represented in Number of
  Days<br>Example: 1, 7.|

  |alertTimeBase|updated, created|Search for the alert based on the updated or
  created time of an alert.<br>Example: updated.|

  |clientIds|NA|ID of clients.<br>Example: client_1, client_2. Separate the IDs
  with a comma.|

  |ticketId|NA|ID of the ticket to which the alert is attached.<br>Example:
  INC0000000001.|

  |apps|NA|Apps from which the alert is generated. Example: Email, Nagios|


  ### Variables for statusHistory

  The statusHistory parameter uses the following variables:


  |Variable|Description|Example|

  |-----|-----|-----|

  |createdBy|Filter alerts based on createdUser.|system|

  |acknowledgedBy|Filter alerts based on acknowledgedUser.|superadmin|

  |suppressedBy|Filter alerts based on suppressedUser.|superadmin|

  |ticketedBy|Filter alerts based on ticketedUser.|opsramp_system_user|

  |closedBy|Filter alerts based on closedUser.|superadmin

  |startAcknowledgedTime||2015-08-10T05:39:51 0000|

  |endAcknowledgedTime||2015-08-10T05:39:51 0000|

  |startSuppressedTime||2015-08-10T05:39:51 0000|

  |endSuppressedTime||2015-08-10T05:39:51 0000|

  |startTicketedTime||2015-08-10T05:39:51 0000|

  |endTicketedTime||2015-08-10T05:39:51 0000|

  |startClosedTime||2015-08-10T05:39:51 0000|

  |endClosedTime||2015-08-10T05:39:51 0000|


  ##### Notes

  - Special characters to use in the query string are:
      - (+) indicates next field and must be URL-encoded.
      - (:) indicates Equals. An example is key: value.
      - (,) indicates multiple values for a key. An example is priority: P0,P1
  - Space characters must be URL-encoded.
tags:
  - alerts
path: '/api/v2/tenants/{tenantId}/alerts/search'
request:
  - get
layout: api-doc
draft: false
---
