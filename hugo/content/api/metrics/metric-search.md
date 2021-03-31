---
slug: metric-search
title: Get metric (time series) on resources
description: >-
  Gets the details of metric behavior at a certain time period.

  There are three common examples that show how to get metric data based on a
  specific time series.


  1. Time series type (RealTime):

  ```

  https://{api-url}/api/v2/metric/search?tenant=client_20&rtype=DEVICE&resource=ab342123-5bfb-434c-aae4-03611ca020d9&metric=system.cpu.utilization&startTime=1536643494&endTime=1536661494&timeseries_type=RealTime

  ```

  2. Time series type (CHANGE_DETECTION):

  ```

  https://{api-url}/api/v2/metric/search?tenant=client_20&rtype=DEVICE&resource=ab342123-5bfb-434c-aae4-03611ca020d9&metric=system.cpu.utilization&startTime=1536643494&endTime=1536661494&timeseries_type=CHANGE_DETECTION

  ```

  3. Time series type (FORECAST):

  ```

  https://{api-url}/api/v2/metric/search?tenant=client_20&rtype=DEVICE&resource=ab342123-5bfb-434c-aae4-03611ca020d9

  ```


  ### Data resolution

  OpsRamp retains the raw metrics data for the most recent seven. Metric
  roll-ups are computed every half-hour, hourly, and daily. Calculations
  performed include average, minimum, maximum, and latest. Based on the selected
  time range, data is dynamically served in raw and rolled-up formats.


  |Time Range|Resolution|Time Series Sections|

  |----|----|----|

  |Up to 24 hours|Raw|data (RAW)|

  |Greater than 24 hours to 3 days|30-minute rollup|data (AVG), minVals (MIN),
  maxVals(MAX) and lastVals(LATEST / LAST)|

  |Greater than 3 days to 30 days|1-hour rollup|data (AVG), minVals (MIN),
  maxVals(MAX) and lastVals(LATEST / LAST)|

  |Greater than 30 days|1-day rollup|data (AVG), minVals (MIN), maxVals(MAX) and
  lastVals(LATEST / LAST)|

  |Using "data=raw" query param|Raw (up to 7 days)|data (RAW)|


  ### Sample responses

  To get metric behavior at multiple time series patterns:
  example-multiple-time-series


  To get metric behavior at current time stamp in real time:
  example-current-real-time


  To get significant changes on a metric (using CHANGE_DETECTION):
  example-change-detection


  To forecast values of a metric (using FORECAST): example-forecast


  Roll-ups enables the viewing of metric behavior in wider time spans.


  >When OpsRamp receives data points for a given time series, this data is
  accumulated for specific periods of time. This data is stored in four roll-ups
  for each interval: average, minimum, maximum, and latest.


  To get metric data for a roll-up time series: example-roll-up
tags:
  - metrics
path: /api/v2/metric/search
request:
  - get
layout: api-doc
draft: false
---
