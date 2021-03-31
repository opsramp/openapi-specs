---
slug: tenants-tenantid-timeboundrequests
title: Create time bound request
description: "Creates a time bound request.\n\n## Sample URLs\n```\nhttps://{api-url}/api/v2/tenants/client_7/timeBoundRequests\n```\n\n|Timezones|Timezones|Timezones|\n|--------|\n|Pacific/Asia|Pacific/Honolulu|America/Anchorage|\n|America/Los_Angeles|America/Denver|America/Chicago|\n|America/New_York|America/Puerto_Rico|America/St_Johns|\n|America/Buenos_Aires|Atlantic/Azores|GMT|\n|Europe/Paris|Europe/Istanbul|Africa/Addis_Ababa|\n|Asia/Tehran|Asia/Yerevan|Asia/Karachi|\n|Asia/Calcutta|Asia/Dacca|Asia/Saigon|\n|Asia/Shanghai|Asia/Tokyo|Australia/Darwin|\n|Australia/Sydney|Pacific/Guadalcanal|Pacific/Auckland|\n\n### Schedule Pattern Types\nDefine the time duration for the time bound request to occur once or repeatedly.\n\nDefine the time bound request to occur for one-time only:\n```\n{\n\t\"type\": \"one-time\",\n\t\"startTime\": \"2016-04-10T12:15:00+0000\",\n\t\"endTime\": \"2016-04-10T12:15:00+0000\",\n\t\"timezone\": \"America/Los_Angeles\"\n}\n```\nDefine the time bound request to occur repeatedly:\n```\n{\n\t\"type\": \"recurring\",\n\t\"startTime\": \"2016-04-10T12:15:00+0000\",\n\t\"endTime\": \"2016-04-10T12:15:00+0000\",\n\t\"timezone\": \"America/Los_Angeles\",\n\t\"pattern\": {\n\t\t\"type\": \"daily\",\n\t\t\"dayFrequency\": \"everyday\"\n\t}\n}\n```\nBelow are the recurrence schedule pattern types:\n\n1. Daily\n```\n\"pattern\": {\n\t\t\"type\": \"daily\",\n\t\t\"dayFrequency\": \"everyday\"\n\t}\n```\n2. Weekly\n```\n\"pattern\": {\n\t\t\"type\": \"weekly\",\n\t\t\"weekDays\": \"Monday\"\n}\n```\n3. Monthly\n```\n\"pattern\": {\n\t\t\"type\": \"monthly\",\n\t\t\"dayOfMonth\": \"1\",\n\t\t\"weekIndex\": \"First\",\n\t\t\"dayOfWeek\": \"Monday\"\n}\n```"
tags:
  - tickets
path: '/api/v2/tenants/{tenantId}/timeBoundRequests'
request:
  - post
layout: api-doc
draft: false
---
