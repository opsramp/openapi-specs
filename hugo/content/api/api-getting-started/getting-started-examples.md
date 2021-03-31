---
title: Getting Started Examples
linkTitle: Getting Started Examples
weight: 20
description: A quick start guide to authenticating and using the REST API.
type: documentation
---

## Alert GET

Demonstrates how to get a list of open alerts, using curl, Python, or Java.

### curl

{{< code bash >}}
curl -k -H "Authorization: Bearer {bearer_token}"
	-H "Content-Type: application/json"
	-H "Accept:application/json"
	-X GET "https://{partner_name}.api.ospramp.com/api/v2/tenants/{tenantId}/alerts/search?queryString=actions:OPEN"
{{< /code >}}

### Python

{{< code python >}}
import urllib
import urllib2
import json, sys
import time

API_SERVER = "API_SERVER"
CLIENT_ID  = "CLIENT_ID"
API_KEY    = "API_KEY"
API_SECRET = "API_SECRET"

# Python HTTP client to generate GET/POST requests '''
def httpRequest(url, data=None, headers={}, method='GET',user=None, passwd=None):
    try:
        http_headers = {
            'Content-Type' : 'application/x-www-form-urlencoded',
            'Accept'       : 'text/html, */*',
        }
        http_headers.update(headers)
        req = urllib2.Request(url, data, http_headers)
        req.get_method = lambda: method
        if user and passwd:
            passReq = urllib2.HTTPPasswordMgrWithDefaultRealm()
            passReq.add_password(None, url, user, passwd)
            authhandler = urllib2.HTTPBasicAuthHandler(passReq)
            opener = urllib2.build_opener(authhandler)
            urllib2.install_opener(opener)

        request = urllib2.urlopen(req)
        return request.read()
    except urllib2.HTTPError, emsg:
        _msg = emsg.read()
        print emsg.getcode()
        if emsg.getcode() == 500:
            print _msg
            return _msg
        else:
            print emsg.read()
            raise Exception(emsg.reason)
        raise Exception('httpRequest: HTTPError - ' + str(emsg))
    except urllib2.URLError, emsg:
        raise Exception('httpRequest: URLError - ' + str(emsg))
    except Exception, emsg:
        raise Exception('httpRequest: Exception - ' + str(emsg))


# Get open alerts information from OpsRamp '''
def get_open_alerts(ACCESS_TOKEN, query_string=""):
    headers = {
        "Authorization" : "Bearer " + ACCESS_TOKEN,
        "Content-Type"  : "application/json"
    }
    alerts_search_url = "https://%s/api/v2/tenants/%s/alerts/search?queryString=%s" % (API_SERVER, CLIENT_ID, query_string)

    try:
        response = json.loads(httpRequest(device_search_url, None, headers))
        return response
    except Exception, emsg:
        print emsg
        sys.exit(2)


# Get OpsRamp access token using api key/secret for further communication '''
def get_access_token():
    url = "https://%s/auth/oauth/token" % (API_SERVER)

    data = urllib.urlencode({
        "client_id"     : API_KEY,
        "client_secret" : API_SECRET,
        "grant_type"    : "client_credentials"
    })

    headers = {"Content-Type": "application/x-www-form-urlencoded", "Accept" : "application/json"}
    try:
        result = json.loads(httpRequest(url, data, headers, 'POST'))
        return result['access_token']
    except Exception as emsg:
        raise Exception("Error while getting access token - " + str(emsg))


if __name__ == '__main__':
    try:

        ACCESS_TOKEN = str(get_access_token())

        ''' need to provide the query string based on requirement '''
        query_string = "actions:OPEN"
        open_alerts = get_open_alerts(ACCESS_TOKEN,query_string)

    except Exception as e:
        print ("Failed: {0}".format(e))

    sys.exit(0)
{{< /code >}}


### Java

{{< code java >}}
package com.opsramp.examples.rest;

import java.io.IOException;
import java.util.Date;

import org.apache.http.HttpException;
import org.apache.http.HttpHeaders;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.entity.ContentType;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;

/**
 * Sample program to fetch open alerts within a client
 */
public class GetOpenAlerts {

  /**
   * Main program which invokes get open alerts request
   * @param args
   * @throws HttpException
   * @throws IOException
   */
  public static void main(String[] args) throws HttpException, IOException {
      //Replace the end point and access token accordingly
      String ACCESS_TOKEN = "a0f46d75-534d-4180-b4ec-65a23eb1ae39";

      //Fetching open alerts
      String ENDPOINT = "https://<api-url>/api/v2/tenants/client_99999/alerts/search"
                              + "?queryString=actions:OPEN";
      String response = invokeGetRequest(ACCESS_TOKEN, ENDPOINT, 0);
      System.out.println(response);
  }

  /**
   * Fetches data from given end point
   * @param accessToken
   * @param endPoint
   * @return
   * @throws HttpException
   * @throws IOException
   */
  public static String invokeGetRequest(final String accessToken, final String endPoint, final int currentRetryCount)
          throws HttpException, IOException {
      CloseableHttpClient httpclient = HttpClients.custom().build();
      try {
          HttpGet httpget = new HttpGet(endPoint);
          httpget.setHeader(HttpHeaders.ACCEPT, ContentType.APPLICATION_JSON.toString());
          httpget.setHeader(HttpHeaders.CONTENT_TYPE, ContentType.APPLICATION_JSON.toString());
          httpget.setHeader(HttpHeaders.AUTHORIZATION, "Bearer " + accessToken);

          System.out.println("\n" + httpget.getRequestLine());
          CloseableHttpResponse response = httpclient.execute(httpget);
          try {
              System.out.println("Response " + response.getStatusLine());
              String responseBody = null;
              if(response.getEntity() != null) {
                  responseBody = EntityUtils.toString(response.getEntity());
                  if(response.getStatusLine().getStatusCode() == 429) {
                      if(currentRetryCount > 3) {
                          System.out.println("Retry Max-Limit(3) reached; Dropping API: " + endPoint);
                      }
                      long resetTimeInSeconds = Long.valueOf(response.getFirstHeader("X-RateLimit-Reset").getValue());
                      long retryInSec = resetTimeInSeconds - (new Date().getTime()/1000);
                      System.out.println("\tNext retry in: " + retryInSec + "s" + " | " + endPoint);
                      try {
                          Thread.sleep(retryInSec*1000);
                      } catch(Exception ex) {}
                      invokeGetRequest(accessToken, endPoint, currentRetryCount+1);
                  }
              }
              return responseBody;
          } finally {
              response.close();
          }
      } finally {
          httpclient.close();
      }
  }
}
{{< /code >}}


## Alert POST

Demonstrates how to post alerts on a resourc, using curl, Python, or Java.

### curl

{{< code bash >}}
curl -k https://{api-url}/api/v2/tenants/{tenantId}/alert -H "Authorization: Bearer {bearer_token}" -H "Content-Type: application/json" -H "Accept: application/json" -d '{"serviceName": "{service_name}","device":{"hostName":"{host_name}","resourceUUID":"{resource_id}","providerUUID":"{provider_id}","systemUUID":"{system_id}","macAddress":"{mac_address}","ipAddress":"{id_address}"},"subject":"{subject}", "alertTime":"{alert_time}","currentState":"{surrent_state}", "app":"{app_name}","alertType":"{alert_type}","component": "{component_name}","description":"{description}","monitorName":"{monitor_name}"}'
{{< /code >}}

### Python

{{< code python >}}
import urllib
import urllib2
import json, sys
import time

API_SERVER = "API_SERVER"
CLIENT_ID  = "CLIENT_ID"
API_KEY    = "API_KEY"
API_SECRET = "API_SECRET"

# Python HTTP client to generate GET/POST requests
def httpRequest(url, data=None, headers={}, method='GET',user=None, passwd=None):
    try:
        http_headers = {
            'Content-Type' : 'application/x-www-form-urlencoded',
            'Accept'       : 'text/html, */*',
        }
        http_headers.update(headers)
        req = urllib2.Request(url, data, http_headers)
        req.get_method = lambda: method
        if user and passwd:
            passReq = urllib2.HTTPPasswordMgrWithDefaultRealm()
            passReq.add_password(None, url, user, passwd)
            authhandler = urllib2.HTTPBasicAuthHandler(passReq)
            opener = urllib2.build_opener(authhandler)
            urllib2.install_opener(opener)

        request = urllib2.urlopen(req)
        return request.read()
    except urllib2.HTTPError, emsg:
        _msg = emsg.read()
        print emsg.getcode()
        if emsg.getcode() == 500:
            print _msg
            return _msg
        else:
            print emsg.read()
            raise Exception(emsg.reason)
        raise Exception('httpRequest: HTTPError - ' + str(emsg))
    except urllib2.URLError, emsg:
        raise Exception('httpRequest: URLError - ' + str(emsg))
    except Exception, emsg:
        raise Exception('httpRequest: Exception - ' + str(emsg))


# Post alert using REST API
def post_alert(resource_name, resource_ip, mname, mvalue, poll_time, component=""):
    alert_payload = {
      "serviceName": mname,
      "device": {
        "hostName": resource_name,
        "ipAddress": resource_ip
      },
      "subject": "Critical. %s=%s" % (mname, mvalue),
      "description": "Critical. %s=%s" % (mname, mvalue),
      "alertTime": time.strftime("%F %T", time.gmtime(poll_time)),
      "currentState": "Critical",
      "alertType": "Monitoring",
      "app": "OPSRAMP",
      "component": "%s-%s" % (mname, component)
    }
    headers = {
        "Authorization" : "Bearer " + ACCESS_TOKEN
    }
    alert_url = "https://%s/api/v2/tenants/%s/alert" % (API_SERVER, CLIENT_ID)

    data = str(json.dumps(alert_payload))

    httpRequest(alert_url, data, headers, 'POST')

# Get OpsRamp access token using api key/secret for further communication
def get_access_token():
    url = "https://%s/auth/oauth/token" % (API_SERVER)

    data = urllib.urlencode({
        "client_id"     : API_KEY,
        "client_secret" : API_SECRET,
        "grant_type"    : "client_credentials"
    })

    headers = {"Content-Type": "application/x-www-form-urlencoded", "Accept" : "application/json"}
    try:
        result = json.loads(httpRequest(url, data, headers, 'POST'))
        return result['access_token']
    except Exception as emsg:
        raise Exception("Error while getting access token - " + str(emsg))

if __name__ == '__main__':
    try:
        global ACCESS_TOKEN
        ACCESS_TOKEN = str(get_access_token())

        resource_name = "BVRMLPT057"
        resource_ip = "172.28.102.50"
        mname = "CPU"
        mvalue = "90"
        poll_time = "2014-11-05 11:26:00"

        post_alert(resource_name, resource_ip, mname, mvalue, poll_time)

    except Exception as e:
        print ("Failed: {0}".format(e))

    sys.exit(0)
{{< /code >}}


### Java

{{< code java >}}
    package com.opsramp.examples.rest;

    import java.io.IOException;
    import java.nio.charset.StandardCharsets;
    import java.util.Date;

    import org.apache.http.HttpException;
    import org.apache.http.HttpHeaders;
    import org.apache.http.client.methods.CloseableHttpResponse;
    import org.apache.http.client.methods.HttpPost;
    import org.apache.http.entity.ByteArrayEntity;
    import org.apache.http.entity.ContentType;
    import org.apache.http.impl.client.CloseableHttpClient;
    import org.apache.http.impl.client.HttpClients;
    import org.apache.http.util.EntityUtils;

    /**
     * Sample program to post an alert against a resource
     */
    public class PostAlert {

	/**
	 * Main program which posts an alert against a resource
	 * @param args
	 * @throws HttpException
	 * @throws IOException
	 */
	public static void main(String[] args) throws HttpException, IOException {
		//Replace the end point and access token accordingly
		String ACCESS_TOKEN = "a0f46d75-534d-4180-b4ec-65a23eb1ae39";

		//Posting an alert
		String ENDPOINT = "https://{api-url}/api/v2/tenants/client_99999/alert";
		String PAYLOAD = "{"serviceName": "CPU","device":{"hostName":"HYDLPT220","
				+ ""resourceUUID":"702c19c4-1991-4e99-8c5f-4104c061fe25","systemUUID":"11767","
				+ ""macAddress":"2E:8B:EB:32:7A:F9","ipAddress":"172.2.229.109"},"subject":"Test API Alert","
				+ ""alertTime":"2014-11-05 11:26:00","currentState":"CRITICAL", "app":"OPSRAMP","
				+ ""alertType":"Maintenance","component": "C","description":"Test Alert from API Call","
				+ ""monitorName":"TEST"}";
		String response = invokePostRequest(ACCESS_TOKEN, ENDPOINT, PAYLOAD, 0);
		System.out.println(response);
	}

	/**
	 * Posts data to given end point
	 * @param accessToken
	 * @param endPoint
	 * @param payload
	 * @return
	 * @throws HttpException
	 * @throws IOException
	 */
	public static String invokePostRequest(final String accessToken, final String endPoint,
			final String payload, final int currentRetryCount) throws HttpException, IOException {
		CloseableHttpClient httpclient = HttpClients.custom().build();
		try {
			HttpPost httpPost = new HttpPost(endPoint);
			httpPost.setHeader(HttpHeaders.ACCEPT, ContentType.APPLICATION_JSON.toString());
			httpPost.setHeader(HttpHeaders.CONTENT_TYPE, ContentType.APPLICATION_JSON.toString());
			httpPost.setHeader(HttpHeaders.AUTHORIZATION, "Bearer " + accessToken);
			httpPost.setEntity(new ByteArrayEntity(payload.getBytes(StandardCharsets.UTF_8.toString())));

			System.out.println("\n" + httpPost.getRequestLine());
			CloseableHttpResponse response = httpclient.execute(httpPost);
			try {
				System.out.println("Response " + response.getStatusLine());
				String responseBody = null;
				if(response.getEntity() != null) {
					responseBody = EntityUtils.toString(response.getEntity());
					if(response.getStatusLine().getStatusCode() == 429) {
						if(currentRetryCount } 3) {
							System.out.println("Retry Max-Limit(3) reached; Dropping API: " + endPoint);
						}
						long resetTimeInSeconds = Long.valueOf(response.getFirstHeader("X-RateLimit-Reset").getValue());
						long retryInSec = resetTimeInSeconds - (new Date().getTime()/1000);
						System.out.println("\tNext retry in: " + retryInSec + "s" + " | " + endPoint);
						try {
							Thread.sleep(retryInSec*1000);
						} catch(Exception ex) {}
						invokePostRequest(accessToken, endPoint, payload, currentRetryCount+1);
					}
				}
				return responseBody;
			} finally {
				response.close();
			}
		} finally {
			httpclient.close();
		}
	}
}
{{< /code >}}


## Inventory GET

Demonstrates how to get an inventory of managed client resources, using curl, Python, or Java.

### curl

#### Get list of devices

{{< code bash >}}
curl -k -H "Authorization: Bearer {bearer_token}" -H "Content-Type: application/json" -H "Accept:application/json" -X GET https://{api-url}/api/v2/tenants/{tenantId}/devices/minimal
{{< /code >}}


#### Search device details by name

{{< code bash >}}
curl -k -H "Authorization: Bearer {bearer_token}" -H "Content-Type: application/json" -H "Accept:application/json" -X GET https://{api-url}/api/v2/tenants/{tenantId}/devices/search?queryString=hostName:{host_name}
{{< /code >}}


#### Search devices by UUID

{{< code bash >}}
curl -k -H "Authorization: Bearer {bearer_token}" -H "Content-Type: application/json" -H "Accept:application/json" -X GET https://{api-url}/api/v2/tenants/{tenantId}/devices/search?queryString=resourceUUID:{resource_UUID}
{{< /code >}}



### Python

{{< code python >}}
import urllib
import urllib2
import json, sys
import time

API_SERVER = "api.opsramp.com"
CLIENT_ID  = "CLIENT_ID"
API_KEY    = "API_KEY"
API_SECRET = "API_SECRET"


''' Python HTTP client to make GET/POST requests '''
def httpRequest(url, data=None, headers={}, method='GET',user=None, passwd=None):
    try:
        http_headers = {
            'Content-Type' : 'application/x-www-form-urlencoded',
            'Accept'       : 'text/html, */*',
        }
        http_headers.update(headers)
        req = urllib2.Request(url, data, http_headers)
        req.get_method = lambda: method
        if user and passwd:
            passReq = urllib2.HTTPPasswordMgrWithDefaultRealm()
            passReq.add_password(None, url, user, passwd)
            authhandler = urllib2.HTTPBasicAuthHandler(passReq)
            opener = urllib2.build_opener(authhandler)
            urllib2.install_opener(opener)

        request = urllib2.urlopen(req)
        return request.read()
    except urllib2.HTTPError, emsg:
        _msg = emsg.read()
        print emsg.getcode()
        if emsg.getcode() == 500:
            print _msg
            return _msg
        else:
            print emsg.read()
            raise Exception(emsg.reason)
        raise Exception('httpRequest: HTTPError - ' + str(emsg))
    except urllib2.URLError, emsg:
        raise Exception('httpRequest: URLError - ' + str(emsg))
    except Exception, emsg:
        raise Exception('httpRequest: Exception - ' + str(emsg))


''' Get resource/device information from OpsRamp '''
def get_resources(ACCESS_TOKEN, query_string="", pageSize=500, pageNo=None):
    headers = {
        "Authorization" : "Bearer " + ACCESS_TOKEN,
        "Content-Type"  : "application/json"
    }
    device_search_url = "https://%s/api/v2/tenants/%s/devices/search?pageSize=%s&queryString=%s"
                          % (API_SERVER, CLIENT_ID, pageSize, query_string)
    if pageNo:
        device_search_url += "&pageNo=" + str(pageNo)
    try:
        response = json.loads(httpRequest(device_search_url, None, headers))
        print "\t" + device_search_url
        ''' Capture full devices information using response'''
        ''' print "\t" + json.dumps(response)'''
        return response
    except Exception, emsg:
        print emsg
        print 'Resource does not exist in OPSRAMP, Please create new Resource'
        sys.exit(2)


def get_devices_data(ACCESS_TOKEN, pageSize=500, query_string=""):
    devices = {}

    def get_device_data(rsrcInfo):
        for resource in rsrcInfo['results']:
            devices[resource['id']] = resource['generalInfo']['hostName']

        if rsrcInfo['nextPage']:
            rsrcs = get_resources(ACCESS_TOKEN, query_string, pageSize, rsrcInfo['pageNo'] + 1)
            get_device_data(rsrcs)

    resources = get_resources(ACCESS_TOKEN, query_string, pageSize)
    get_device_data(resources)
    return devices


''' Get OpsRamp access token using api key/secret for further communication '''
def get_access_token():
    url = "https://%s/auth/oauth/token" % (API_SERVER)

    data = urllib.urlencode({
        "client_id"     : API_KEY,
        "client_secret" : API_SECRET,
        "grant_type"    : "client_credentials"
    })

    headers = {"Content-Type": "application/x-www-form-urlencoded", "Accept" : "application/json"}
    try:
        result = json.loads(httpRequest(url, data, headers, 'POST'))
        print "\n\tAccessToken: " + result['access_token'] + "\n";
        return result['access_token']
    except Exception as emsg:
        raise Exception("Error while getting access token - " + str(emsg))


''' Execution starts here'''
if __name__ == '__main__':
    try:

        ACCESS_TOKEN = str(get_access_token())

        pageSize=500
        query_string = ""

        devices = get_devices_data(ACCESS_TOKEN, pageSize, query_string)

        ''' All Device ids & names are available in devices dictionary'''
        print json.dumps(devices)
    except Exception as e:
        print ("Failed: {0}".format(e))

    sys.exit(0)
{{< /code >}}

### Java

{{< code java >}}
package com.opsramp.examples.rest;

import java.io.IOException;
import java.util.Date;

import org.apache.http.HttpException;
import org.apache.http.HttpHeaders;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.entity.ContentType;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;

/**
 * Sample program to fetch devices within a client
 */
public class GetDevices {

	/**
	 * Main program which invokes get devices request
	 * @param args
	 * @throws HttpException
	 * @throws IOException
	 */
	public static void main(String[] args) throws HttpException, IOException {
		//Replace the end point and access token accordingly
		String ACCESS_TOKEN = "a0f46d75-534d-4180-b4ec-65a23eb1ae39";

		//Fetching devices minimal list
		String ENDPOINT = "https://<api-url>/api/v2/tenants/client_99999/devices/minimal";
		String response = invokeGetRequest(ACCESS_TOKEN, ENDPOINT, 0);
		System.out.println(response);

		//Performing device search using host name
		ENDPOINT = "https://<api-url>/api/v2/tenants/client_99999/devices/search"
						+ "?queryString=hostName:HYDLPT323";
		response = invokeGetRequest(ACCESS_TOKEN, ENDPOINT, 0);
		System.out.println(response);

		//Performing device search using unique id
		ENDPOINT = "https://<api-url>/api/v2/tenants/client_99999/devices/search"
						+ "?queryString=resourceUUID:5486c82c-d5fc-4e40-b238-a4f00cb387da";
		response = invokeGetRequest(ACCESS_TOKEN, ENDPOINT, 0);
		System.out.println(response);
	}

	/**
	 * Fetches data from given end point
	 * @param accessToken
	 * @param endPoint
	 * @return
	 * @throws HttpException
	 * @throws IOException
	 */
	public static String invokeGetRequest(final String accessToken, final String endPoint, final int currentRetryCount)
			throws HttpException, IOException {
		CloseableHttpClient httpclient = HttpClients.custom().build();
		try {
			HttpGet httpget = new HttpGet(endPoint);
			httpget.setHeader(HttpHeaders.ACCEPT, ContentType.APPLICATION_JSON.toString());
			httpget.setHeader(HttpHeaders.CONTENT_TYPE, ContentType.APPLICATION_JSON.toString());
			httpget.setHeader(HttpHeaders.AUTHORIZATION, "Bearer " + accessToken);

			System.out.println("\n" + httpget.getRequestLine());
			CloseableHttpResponse response = httpclient.execute(httpget);
			try {
				System.out.println("Response " + response.getStatusLine());
				String responseBody = null;
				if(response.getEntity() != null) {
					responseBody = EntityUtils.toString(response.getEntity());
					if(response.getStatusLine().getStatusCode() == 429) {
						if(currentRetryCount > 3) {
							System.out.println("Retry Max-Limit(3) reached; Dropping API: " + endPoint);
						}
						long resetTimeInSeconds = Long.valueOf(response.getFirstHeader("X-RateLimit-Reset").getValue());
						long retryInSec = resetTimeInSeconds - (new Date().getTime()/1000);
						System.out.println("\tNext retry in: " + retryInSec + "s" + " | " + endPoint);
						try {
							Thread.sleep(retryInSec*1000);
						} catch(Exception ex) {}
						invokeGetRequest(accessToken, endPoint, currentRetryCount+1);
					}
				}
				return responseBody;
			} finally {
				response.close();
			}
		} finally {
			httpclient.close();
		}
	}
}
{{< /code >}}


## Metric GET

Demonstrates how to get metric data for a managed resource, using curl, Python, or Java.

### curl
The following sample code gets resource ID and resource type using the Search Devices API.
The resource ID and resource type are captured from the response.

{{< code bash >}}
curl -k -H "Authorization: Bearer {bearer_token}" -H "Content-Type: application/json" -H "Accept:application/json" -X GET "https://{api-url}/api/v2/tenants/{tenantId}/devices/search?queryString=hostName:{host_name}"
{{< /code >}}

The following sample code gets metric name from the list of available metrics on a device.

{{< code bash >}}
curl -k -H "Authorization: Bearer {bearer_token}" -H "Content-Type: application/json" -H "Accept:application/json" -X GET "https://{api-url}/api/v2/metric/tenants/{tenantId}/rtypes/DEVICE/resources/{resource_id}/metrics"
{{< /code >}}

The following sample code gets the time series response for the resource ID,
resource type and metric (startTime and endTime are UNIX timestamps).

{{< code bash >}}
curl -k -H "Authorization: Bearer {bearer_token}" -H "Content-Type: application/json" -H "Accept:application/json" -X GET "https://{api-url}/api/v2/metric/search?tenant={client_id}&rtype=DEVICE&resource={resource_id}&metric={metric_name}&startTime={start_time}&endTime={end_time}"
{{< /code >}}

{{< alert title="Coding notes" >}}
- Sample metric and start/end times are `metric=system.cpu.utilization&startTime=1444973469&endTime=1463772116049`
- Start/end dates from the curl from Linux
  - date +%s #Current time:
  - date -d "1 hour ago" +%s #1 Hour ago
  - date -d "1 day ago" +%s #1 Day ago
  - date -d "1 month ago" +%s #1 Month ago
- Start/end dates from the curl from OS X (macOS):
  - date +%s #Current time
  - date -v-1H +%s #1 Hour ago
  - date -v-1d +%s #1 Day ago
  - date -v-1m +%s #1 Month ago
 {{< /alert >}}

### Python

{{< code python >}}
import urllib
import urllib2
import json, sys
import time

API_SERVER = "api.opsramp.com"
CLIENT_ID  = "CLIENT_ID"
API_KEY    = "API_KEY"
API_SECRET = "API_SECRET"

# Python HTTP client to generate GET/POST requests
def httpRequest(url, data=None, headers={}, repeat_count=None, method='GET',user=None, passwd=None):
    try:
        http_headers = {
            'Content-Type' : 'application/x-www-form-urlencoded',
            'Accept'       : 'text/html, */*',
        }
        http_headers.update(headers)
        req = urllib2.Request(url, data, http_headers)
        req.get_method = lambda: method
        if user and passwd:
            passReq = urllib2.HTTPPasswordMgrWithDefaultRealm()
            passReq.add_password(None, url, user, passwd)
            authhandler = urllib2.HTTPBasicAuthHandler(passReq)
            opener = urllib2.build_opener(authhandler)
            urllib2.install_opener(opener)

        request = urllib2.urlopen(req)
        return request.read()
    except urllib2.HTTPError, emsg:
        _msg = emsg.read()
        print emsg.getcode()
        if emsg.getcode() == 429:
            time.sleep(60)
            if repeat_count != None and repeat_count < 3:
                httpRequest(url, data, headers, repeat_count+1, method)
            print _msg
            return _msg
        elif emsg.getcode() == 500:
            print _msg
            return _msg
        else:
            print emsg.read()
            raise Exception(emsg.reason)
        raise Exception('httpRequest: HTTPError - ' + str(emsg))
    except urllib2.URLError, emsg:
        raise Exception('httpRequest: URLError - ' + str(emsg))
    except Exception, emsg:
        raise Exception('httpRequest: Exception - ' + str(emsg))

# Get metrics
def get_available_metrics(rsrc_id, rsrc_type):
    try:
        headers = {
            "Authorization" : "Bearer " + ACCESS_TOKEN,
            "Content-Type"  : "application/json",
            "Accept"        : "application/json"
        }
        available_metrics_url = "https://{0}/api/v2/metric/tenants/{1}/rtypes/{2}/resources/{3}/metrics"
        % (API_SERVER, CLIENT_ID, rsrc_type, rsrc_id)

        return httpRequest(available_metrics_url, None, headers, 0, 'GET')
    except Exception as emsg:
        print 'Failed to get metric data %s' % (emsg)

# Time Series metrics data
def get_timeseries_metrics_data(rsrc_id, rsrc_type,metric_name,start_time,end_time):
    try:
        headers = {
            "Authorization" : "Bearer " + ACCESS_TOKEN,
            "Content-Type"  : "application/json",
            "Accept"        : "application/json"
        }

        timeseries_metrics_url = "https://{0}/api/v2/metric/search?tenant={1}&rtype={2}&resource={3}&metric={4}&startTime={5}&endTime={6}"
         % (API_SERVER, CLIENT_ID, rsrc_type, rsrc_id, metric_name,start_time,end_time)

        return httpRequest(timeseries_metrics_url, None, headers, 0, 'GET')
    except Exception as emsg:
        print 'Failed to post metric data %s' % (emsg)

# Get OpsRamp access token using api key/secret for further communication
def get_access_token():
    url = "https://%s/auth/oauth/token" % (API_SERVER)

    data = urllib.urlencode({
        "client_id"     : API_KEY,
        "client_secret" : API_SECRET,
        "grant_type"    : "client_credentials"
    })

    headers = {"Content-Type": "application/x-www-form-urlencoded", "Accept" : "application/json"}
    try:
        result = json.loads(httpRequest(url, data, headers, None, 'POST'))
        return result['access_token']
    except Exception as emsg:
        raise Exception("Error while getting access token - " + str(emsg))

if __name__ == '__main__':
    try:
        global ACCESS_TOKEN
        ACCESS_TOKEN = str(get_access_token())

        RESOURCE_TYPE = "DEVICE"
        RESOURCE_ID = "702c19c4-1991-4e99-8c5f-4104c061fe25"

        available_metrics = get_available_metrics(RESOURCE_ID, RESOURCE_TYPE)

        ''' Fetching time series metric data for the resource '''

        METRIC_NAME = 'opsramp.agent.status'

        ''' start time and end time in epoch time '''
        start_time = "1444973469"
        end_time = "1467980181"
        timeseries_data = get_timeseries_metrics_data(RESOURCE_ID, RESOURCE_TYPE, METRIC_NAME,start_time,end_time)

    except Exception as e:
        print ("Failed: {0}".format(e))

    sys.exit(0)
{{< /code >}}

### Java

{{< code java >}}
package com.opsramp.examples.rest;

import java.io.IOException;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.Date;

import org.apache.http.HttpException;
import org.apache.http.HttpHeaders;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.entity.ContentType;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;

import com.google.gson.JsonElement;
import com.google.gson.JsonParser;

/**
 * Sample program to get time series metric data of a resource
 */
public class GetTimeSeriesMetricData {

	/**
	 * Main program which invokes time series metric data request
	 * @param args
	 * @throws HttpException
	 * @throws IOException
	 */
	public static void main(String[] args) throws HttpException, IOException {
		//Replace the end point and access token accordingly
		String ACCESS_TOKEN = "a0f46d75-534d-4180-b4ec-65a23eb1ae39";

		//Performing device search using host name
		String ENDPOINT = "https://<api-url>/api/v2/tenants/client_99999/devices/search"
					+ "?queryString=" + URLEncoder.encode("hostName:HYDLPT220", StandardCharsets.UTF_8.toString());
		URLEncoder.encode(ENDPOINT, StandardCharsets.UTF_8.toString());
		String response = invokeGetRequest(ACCESS_TOKEN, ENDPOINT, 0);
		if(response == null || response.isEmpty()) {
			return;
		}
		System.out.println(response);

		//Capturing resource id and type from response
		JsonElement json = new JsonParser().parse(response);
		JsonElement count = json.getAsJsonObject().get("totalResults");
		if(count == null || count.isJsonNull()) {
			return;
		}
		if(count.getAsInt() == 0) {
			return;
		}
		JsonElement resourceJson = json.getAsJsonObject().get("results")
										.getAsJsonArray().get(0);
		String resourceUID = null, resourceType = null;
		if(resourceJson.getAsJsonObject().get("id") != null) {
			resourceUID = resourceJson.getAsJsonObject().get("id").getAsString();
		}
		if(resourceJson.getAsJsonObject().get("type") != null) {
			resourceType = resourceJson.getAsJsonObject().get("type").getAsString();
		}
		System.out.println("Total Results: " + count.getAsInt());
		System.out.println("Resource Id: " + resourceUID);
		System.out.println("Resource Type: " + resourceType);

		if(resourceUID == null || resourceUID.isEmpty()
				|| resourceType == null || resourceType.isEmpty()) {
			return;
		}

		//Fetching available metrics list of the resource
		ENDPOINT = "https://<api-url>/api/v2/metric/tenants/client_99999"
						+ "/rtypes/" + resourceType+ "/resources/" + resourceUID+ "/metrics";
		response = invokeGetRequest(ACCESS_TOKEN, ENDPOINT, 0);
		if(response == null || response.isEmpty()) {
			return;
		}
		System.out.println(response);

		//Capturing metric name from response
		json = new JsonParser().parse(response);
		if(!json.isJsonArray() || json.getAsJsonArray().size() == 0) {
			return;
		}

		JsonElement metricJson = json.getAsJsonArray().get(0);

		String metricName = null;
		if(metricJson.getAsJsonObject().get("metricName") != null) {
			metricName = metricJson.getAsJsonObject().get("metricName").getAsString();
		}
		if(metricName == null || metricName.isEmpty()) {
			return;
		}
		System.out.println("Metric Name: " + metricName);

		//Fetching time series metric data for the resource
		ENDPOINT = "https://<api-url>/api/v2/metric/search?tenant=client_99999"
						+ "&rtype=" + resourceType + "&resource=" + resourceUID +
						"&metric=" + metricName + "&startTime=1444973469&endTime=1467980181";
		response = invokeGetRequest(ACCESS_TOKEN, ENDPOINT, 0);
		System.out.println(response);
	}

	/**
	 * Fetches data from given end point
	 * @param accessToken
	 * @param endPoint
	 * @return
	 * @throws HttpException
	 * @throws IOException
	 */
	public static String invokeGetRequest(final String accessToken, final String endPoint, final int currentRetryCount)
			throws HttpException, IOException {
		CloseableHttpClient httpclient = HttpClients.custom().build();
		try {
			HttpGet httpget = new HttpGet(endPoint);
			httpget.setHeader(HttpHeaders.ACCEPT, ContentType.APPLICATION_JSON.toString());
			httpget.setHeader(HttpHeaders.CONTENT_TYPE, ContentType.APPLICATION_JSON.toString());
			httpget.setHeader(HttpHeaders.AUTHORIZATION, "Bearer " + accessToken);

			System.out.println("\n" + httpget.getRequestLine());
			CloseableHttpResponse response = httpclient.execute(httpget);
			try {
				System.out.println("Response " + response.getStatusLine());
				String responseBody = null;
				if(response.getEntity() != null) {
					responseBody = EntityUtils.toString(response.getEntity());
					if(response.getStatusLine().getStatusCode() == 429) {
						if(currentRetryCount > 3) {
							System.out.println("Retry Max-Limit(3) reached; Dropping API: " + endPoint);
						}
						long resetTimeInSeconds = Long.valueOf(response.getFirstHeader("X-RateLimit-Reset").getValue());
						long retryInSec = resetTimeInSeconds - (new Date().getTime()/1000);
						System.out.println("\tNext retry in: " + retryInSec + "s" + " | " + endPoint);
						try {
							Thread.sleep(retryInSec*1000);
						} catch(Exception ex) {}
						invokeGetRequest(accessToken, endPoint, currentRetryCount+1);
					}
				}
				return responseBody;
			} finally {
				response.close();
			}
		} finally {
			httpclient.close();
		}
	}
}
{{< /code >}}


## Metric POST

Demonstrates how to POST metric data on a managed resource, using curl, Python, or Java.

### curl

{{< code bash >}}
curl -k https://{api-url}/api/v2/metric/tenants/{tenantId}/rtypes/DEVICE/resources/{resource_id}/metrics -H "Authorization: Bearer {bearer_token}" -H "Content-Type: application/json" -H "Accept: application/json" -d '[{"metricName" : "{metric_name}","instanceName" : "{instance_name}","instanceVal" : "13.50","ts" : "1448274610"}]' -X POST
{{< /code >}}

### Python

{{< code python >}}
import urllib
import urllib2
import json, sys
import time

API_SERVER = "API_SERVER"
CLIENT_ID  = "CLIENT_ID"
API_KEY    = "API_KEY"
API_SECRET = "API_SECRET"

# Python HTTP client to generate GET/POST requests
def httpRequest(url, data=None, headers={}, method='GET',user=None, passwd=None):
    try:
        http_headers = {
            'Content-Type' : 'application/x-www-form-urlencoded',
            'Accept'       : 'text/html, */*',
        }
        http_headers.update(headers)
        req = urllib2.Request(url, data, http_headers)
        req.get_method = lambda: method
        if user and passwd:
            passReq = urllib2.HTTPPasswordMgrWithDefaultRealm()
            passReq.add_password(None, url, user, passwd)
            authhandler = urllib2.HTTPBasicAuthHandler(passReq)
            opener = urllib2.build_opener(authhandler)
            urllib2.install_opener(opener)

        request = urllib2.urlopen(req)
        return request.read()
    except urllib2.HTTPError, emsg:
        _msg = emsg.read()
        print emsg.getcode()
        if emsg.getcode() == 500:
            print _msg
            return _msg
        else:
            print emsg.read()
            raise Exception(emsg.reason)
        raise Exception('httpRequest: HTTPError - ' + str(emsg))
    except urllib2.URLError, emsg:
        raise Exception('httpRequest: URLError - ' + str(emsg))
    except Exception, emsg:
        raise Exception('httpRequest: Exception - ' + str(emsg))

# Post metrics
def post_metrics(rsrc_id, metric_data):
    try:
        headers = {
            "Authorization" : "Bearer " + config.access_token,
            "Content-Type"  : "application/json",
            "Accept"        : "application/json"
        }
        post_metrics_url = "https://%s/api/v2/metric/tenants/%s/rtypes/DEVICE/resources/%s/metrics" % (API_SERVER, CLIENT_ID, rsrc_id)
        data = str(json.dumps(metric_data))

        httpRequest(post_metrics_url, data, headers, 'POST')
    except Exception as emsg:
        print 'Failed to post metric data %s' % (emsg)

# Get OpsRamp access token using api key/secret for further communication
def get_access_token():
    url = "https://%s/auth/oauth/token" % (API_SERVER)

    data = urllib.urlencode({
        "client_id"     : API_KEY,
        "client_secret" : API_SECRET,
        "grant_type"    : "client_credentials"
    })

    headers = {"Content-Type": "application/x-www-form-urlencoded", "Accept" : "application/json"}
    try:
        result = json.loads(httpRequest(url, data, headers, 'POST'))
        return result['access_token']
    except Exception as emsg:
        raise Exception("Error while getting access token - " + str(emsg))

if __name__ == '__main__':
    try:
        global ACCESS_TOKEN
        ACCESS_TOKEN = str(get_access_token())

        RESOURCE_ID = "702c19c4-1991-4e99-8c5f-4104c061fe25"

        metric_data = [{
            "metricName"   : "system.ping.rta",
            "instanceVal"  : "16.50",
            "instanceName" : "rta",
            "ts"           : "1467983770"
        }]

        post_metrics(RESOURCE_ID, metric_data)

    except Exception as e:
        print ("Failed: {0}".format(e))

    sys.exit(0)
{{< /code >}}

### Java

{{< code java >}}
package com.opsramp.examples.rest;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.Date;

import org.apache.http.HttpException;
import org.apache.http.HttpHeaders;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.ByteArrayEntity;
import org.apache.http.entity.ContentType;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;

/**
 * Sample program to post metric against a resource
 */
public class PostMetric {

  /**
   * Main program which posts a metric against a resource
   * @param args
   * @throws HttpException
   * @throws IOException
   */
  public static void main(String[] args) throws HttpException, IOException {
      //Replace the end point and access token accordingly
      String ACCESS_TOKEN = "a0f46d75-534d-4180-b4ec-65a23eb1ae39";

      //Posting a metric
      String ENDPOINT = "https://<api-url>/api/v2/metric/tenants/client_99999"
                              + "/rtypes/DEVICE/resources/702c19c4-1991-4e99-8c5f-4104c061fe25/metrics";
      String PAYLOAD = "[{"metricName" : "system.ping.rta","instanceName": "rta","
                              + ""instanceVal" : "16.50","ts" : "1467983770"}]";
      String response = invokePostRequest(ACCESS_TOKEN, ENDPOINT, PAYLOAD, 0);
      System.out.println(response);
  }

  /**
   * Posts data to given end point
   * @param accessToken
   * @param endPoint
   * @param payload
   * @return
   * @throws HttpException
   * @throws IOException
   */
  public static String invokePostRequest(final String accessToken, final String endPoint,
          final String payload, final int currentRetryCount) throws HttpException, IOException {
      CloseableHttpClient httpclient = HttpClients.custom().build();
      try {
          HttpPost httpPost = new HttpPost(endPoint);
          httpPost.setHeader(HttpHeaders.ACCEPT, ContentType.APPLICATION_JSON.toString());
          httpPost.setHeader(HttpHeaders.CONTENT_TYPE, ContentType.APPLICATION_JSON.toString());
          httpPost.setHeader(HttpHeaders.AUTHORIZATION, "Bearer " + accessToken);
          httpPost.setEntity(new ByteArrayEntity(payload.getBytes(StandardCharsets.UTF_8.toString())));

          System.out.println("\n" + httpPost.getRequestLine());
          CloseableHttpResponse response = httpclient.execute(httpPost);
          try {
              System.out.println("Response " + response.getStatusLine());
              String responseBody = null;
              if(response.getEntity() != null) {
                  responseBody = EntityUtils.toString(response.getEntity());
                  if(response.getStatusLine().getStatusCode() == 429) {
                      if(currentRetryCount > 3) {
                          System.out.println("Retry Max-Limit(3) reached; Dropping API: " + endPoint);
                      }
                      long resetTimeInSeconds = Long.valueOf(response.getFirstHeader("X-RateLimit-Reset").getValue());
                      long retryInSec = resetTimeInSeconds - (new Date().getTime()/1000);
                      System.out.println("\tNext retry in: " + retryInSec + "s" + " | " + endPoint);
                      try {
                          Thread.sleep(retryInSec*1000);
                      } catch(Exception ex) {}
                      invokePostRequest(accessToken, endPoint, payload, currentRetryCount+1);
                  }
              }
              return responseBody;
          } finally {
              response.close();
          }
      } finally {
          httpclient.close();
      }
  }
}
{{< /code >}}


## Response payload

A response payload example.

A new field, `wsusSettings: enabled`, is added to sample response payload.

{{< code json >}}
{
	"id": "43d49023-4c47-4dbf-a59b-9c40610e1ab8",
	"generalInfo": {
		"osName": "Microsoft Windows 7 Professional Service Pack 1, 64-bit",
		"ipAddresses": "172.24.102.169",
		"make": "LENOVO",
		"description": "PhoenixBIOSSC-Tv2.1",
		"hostName": "SJLPT044",
		"dns": "sjlpt044.myoragnization.com",
		"deviceType": "Work Station",
		"domainRole": "1",
		"macAddress": "68:94:23:9B:E1:25",
		"keyboardType": "US104",
		"encodingType": "UTF8",
		"physicalMemory": "7.72",
		"aliasName": "sjlpt311.organization.com",
		"createdTime": "2016-07-24T09:44:56+0000",
		"updatedTime": "2016-12-05T05:33:48+0000",
		"agentDeploytime": "2016-07-24T09:44:56+0000"
	},
	"bios": {
		"biosName": "PhoenixBIOSSC-Tv2.1",
		"biosVersion": "J9ET58WW(1.58)",
		"smBiosVersion": "J9ET58WW(1.58)",
		"smBiosMajorVersion": "2",
		"smBiosMinorVersion": "7",
		"smBiosPresent": "True",
		"systemSerial": "PF00XNRM",
		"systemModel": "20C600AAUS",
		"systemManufacturer": "MicrosoftCorporation"
	},
	"consoles": [{
			"ipAddress": "127.0.0.1",
			"port": "3389",
			"consoleConnector": "Agent",
			"consoleAuthType": "PASSWORD",
			"consoleProtocol": "RDP",
			"type": "MANAGEMENTCONSOLE"
		},
		{
			"ipAddress": "127.0.0.1",
			"port": "0",
			"consoleConnector": "Agent",
			"consoleAuthType": "PASSWORD",
			"consoleProtocol": "FTRANSFER",
			"type": "MANAGEMENTCONSOLE"
		},
		{
			"ipAddress": "127.0.0.1",
			"port": "0",
			"consoleConnector": "Agent",
			"consoleAuthType": "PASSWORD",
			"consoleProtocol": "RMSHELL",
			"type": "MANAGEMENTCONSOLE"
		}
	],
	"drives": [{
			"id": 9,
			"total": 117,
			"free": 68,
			"fileSystem": "NTFS",
			"name": "C:",
			"description": "Local Fixed Disk"
		},
		{
			"id": 10,
			"total": 170,
			"free": 54,
			"fileSystem": "NTFS",
			"name": "D:",
			"description": "Local Fixed Disk"
		}
	],
	"networkCardDetails": [{
			"id": 38065,
			"networkName": "GigabitEthernet3/23",
			"status": "UP",
			"ifName": "GigabitEthernet3/23",
			"ifAlias": "GigabitEthernet3/23",
			"ifDescription": "GigabitEthernet3/23",
			"ipAddress": "172.20.200.50",
			"macAddress": "00:16:C7:6F:06:A0",
			"speed": "AUTO",
			"linkMode": "MGNT_MODE_LINK",
			"confLinkSpeed": "AUTO",
			"adminStatus": "UP",
			"operationalStatus": "UP"
		},
		{
			"id": 38066,
			"networkName": "GigabitEthernet3/25",
			"status": "UP",
			"ifName": "GigabitEthernet3/25",
			"ifAlias": "GigabitEthernet3/25",
			"ifDescription": "GigabitEthernet3/25",
			"ipAddress": "172.20.200.50",
			"macAddress": "00:16:C7:6F:06:AC",
			"speed": "10 Mbps",
			"linkMode": "MGNT_MODE_LINK",
			"confLinkSpeed": "10 Mbps",
			"adminStatus": "UP",
			"operationalStatus": "UP"
		},
		{
			"id": 38067,
			"networkName": "GigabitEthernet3/24",
			"status": "UP",
			"ifName": "GigabitEthernet3/24",
			"ifAlias": "GigabitEthernet3/24",
			"ifDescription": "GigabitEthernet3/24",
			"ipAddress": "172.20.200.50",
			"macAddress": "00:16:C7:6F:06:AC",
			"speed": "1 Gbps",
			"linkMode": "MGNT_MODE_LINK",
			"confLinkSpeed": "10 Mbps",
			"adminStatus": "UP",
			"operationalStatus": "UP"
		},
		{
			"id": 38068,
			"networkName": "GigabitEthernet3/27",
			"status": "UP",
			"ifName": "GigabitEthernet3/27",
			"ifAlias": "GigabitEthernet3/27",
			"ifDescription": "GigabitEthernet3/27",
			"ipAddress": "172.20.200.50",
			"macAddress": "00:16:C7:6F:06:AC",
			"speed": "100 Bbps",
			"linkMode": "MGNT_MODE_WLAN_LINK",
			"confLinkSpeed": "10 Mbps",
			"adminStatus": "UP",
			"operationalStatus": "UP"
		}
	],
	"location": {
		"id": 4,
		"name": "MYORGANIZATION-SJ",
		"description": "Resource in San Jose",
		"address": "Parkway, San Jose"
	},
	"deviceWarranty": {
		"purchaseDate": "2014-12-01T10:10:00+0000",
		"warrantyExpireDate": "2015-12-01T10:10:00+0000"
	},
	"antivirusDetails": {
		"vendor": "McAfee, Inc.",
		"productName": "McAfee Agent",
		"productVersion": "5.0.4.283",
		"currentDefinition": "8521",
		"lastScannedTime": "2017-05-08T11:45:00+0000",
		"status": "Upto Date",
		"supported": "Not Supported"
	},
	"status": "UP",
	"state": "active",
	"clientUniqueId": "client_8",
	"servicePackage": "Services",
	"ipAddress": "172.24.102.169",
	"type": "DEVICE",
	"applicationTypes": "AD,MSSQL,IIS,EXCHANGE",
	"agentInstalled": true,
	"agentVersion": "5.98.0000",
	"agentConnectivity": "DIRECT",
	"source": "Agent",
	"deviceGroups": [{
			"id": "DGP-876f73a7-c0e4-409c-a757-5c64205ff97a",
			"name": "SJ-WINDOWS",
			"description": "Windows Systems at SJ"
		},
		{
			"id": "DGP-420a80f4-5fba-46d5-a1c1-20e2df4a326a",
			"name": "SJ-Linux",
			"description": "Linux Devices in SJ"
		}
	],
	"serviceGroups": [{
			"id": "SGP-d4ad6f5f-c788-4747-b62c-17b59c89ca06",
			"name": "Agents"
		},
		{
			"id": "SGP-c2af3866-fc89-47dd-b83f-bcc8df0b2a0a",
			"name": "VTH Services"
		}
	],
	"managementProfile": {
		"id": 4,
		"name": "Agent Management Profile",
		"description": "Management profile",
		"type": "Agent"
	},
	"components": [
		"pbxCircuitCards",
		"pbxPorts",
		"pbxRegistrations",
		"pbxTrunks",
		"pbxLicense",
		"disks"
	],
	"metricTypes": [{
			"metricName": "system.memory.usage.physical.percent",
			"displayName": "Memory Utilization (%)",
			"description": "Memory Utilization in Percentage",
			"unit": "%",
			"unitLabel": "Utilization"
		},
		{
			"metricName": "system.disk.used.util.percent",
			"displayName": "Disk Utilization (%)",
			"description": "Disk Utilization in Percentage",
			"unit": "%",
			"unitLabel": "Utilization"
		},
		{
			"metricName": "system.memory.usage.virtual",
			"displayName": "Memory Utilization",
			"description": "Amount of physical memory  immediately available for allocation to a process or for system use",
			"unit": "GB",
			"unitLabel": "Utilization"
		}
	],
	"cpus": [{
		"processor": "CPU0",
		"processorName": "Intel(R) Core(TM) i7-4770HQ CPU @ 2.20GHz",
		"processorVersion": "",
		"manufacturer": "GenuineIntel",
		"family": "2",
		"powerManagementSupported": false,
		"l2CacheSize": 0,
		"maxClockSpeed": 2193,
		"dataWidth": 64,
		"numberOfCores": 1
	}],
	"wsusSettings": "enabled"
}
{{< /code >}}

## Scheduled maintenance

Generates a request to manage the schedule maintenance window, using curl, Python, or Java.

### curl

#### Create window

Create a schedule maintenance window:

{{< code bash >}}
curl -k -H "Authorization: Bearer {bearer_token}" -H "Content-Type: application/json" -H "Accept:application/json" -X POST https://{api-url}/api/v2/tenants/{tenantId}/scheduleMaintenances -d
{{< /code >}}

{{< code json >}}
{
	"name": "{scheduleMaintenance_name}",
	"description": "{scheduleMaintenance_description}",
	"dontRunRBA": "false",
	"dontInstallPatch": "false",
	"devices": [{
		"hostName": "{host_name}"
	}],
	"schedule": {
		"type": "{schedule_type}",
		"startTime": "{start_time}",
		"endTime": "{end_time}",
		"timezone": "{time_zone}"
	}
}
{{< /code >}}

#### Search for window

Search for a schedule maintenance window by name:

{{< code bash >}}
curl -H "Authorization: Bearer {bearer_token}" -H "Content-Type: application/json" -H "Accept:application/json" -X GET https://{api-url}/api/v2/tenants/{tenantId}/scheduleMaintenances/search?queryString=name:{scheduleMaintenance_name}}
{{< /code >}}


#### Suspend window

Suspend a schedule maintenance window:

{{< code bash >}}
curl -H "Authorization: Bearer {bearer_token}" -H "Content-Type: application/json" -H "Accept:application/json" -X POST https://{api-url}/api/v2/tenants/{tenantId}/scheduleMaintenances/{scheduleMaintenance_id}/suspend
{{< /code >}}

#### Resume window

Resume a schedule maintenance window:

{{< code bash >}}
curl -H "Authorization: Bearer {bearer_token}" -H "Content-Type: application/json" -H "Accept:application/json" -X POST https://{api-url}/api/v2/tenants/{tenantId}/scheduleMaintenances/{scheduleMaintenance_id}/resume
{{< /code >}}

#### Delete window

Delete a schedule maintenance window:

{{< code bash >}}
curl -H "Authorization: Bearer {bearer_token}" -H "Content-Type: application/json" -H "Accept:application/json" -X DELETE https://{api-url}/api/v2/tenants/{tenantId}/scheduleMaintenances/{scheduleMaintenance_id}
{{< /code >}}

### Python

{{< code python >}}
import urllib
import urllib2
import json, sys
import time

API_SERVER = "api.opsramp.com"
CLIENT_ID  = "CLIENT_ID"
API_KEY    = "API_KEY"
API_SECRET = "API_SECRET"

# Python HTTP client to generate GET/POST requests
def httpRequest(url, data=None, headers={}, repeat_count=None, method='GET',user=None, passwd=None):
    try:
        http_headers = {
            'Content-Type' : 'application/x-www-form-urlencoded',
            'Accept'       : 'text/html, */*',
        }
        http_headers.update(headers)
        req = urllib2.Request(url, data, http_headers)
        req.get_method = lambda: method
        if user and passwd:
            passReq = urllib2.HTTPPasswordMgrWithDefaultRealm()
            passReq.add_password(None, url, user, passwd)
            authhandler = urllib2.HTTPBasicAuthHandler(passReq)
            opener = urllib2.build_opener(authhandler)
            urllib2.install_opener(opener)

        request = urllib2.urlopen(req)
        return request.read()
    except urllib2.HTTPError, emsg:
        _msg = emsg.read()
        print emsg.getcode()
        if emsg.getcode() == 429:
            time.sleep(60)
            if repeat_count != None and repeat_count < 3:
                httpRequest(url, data, headers, repeat_count+1, method)
            print _msg
            return _msg
        elif emsg.getcode() == 500:
            print _msg
            return _msg
        else:
            print emsg.read()
            raise Exception(emsg.reason)
        raise Exception('httpRequest: HTTPError - ' + str(emsg))
    except urllib2.URLError, emsg:
        raise Exception('httpRequest: URLError - ' + str(emsg))
    except Exception, emsg:
        raise Exception('httpRequest: Exception - ' + str(emsg))

def schedule_maintenance_actions(URL, DATA):
    headers = {
        "Authorization" : "Bearer " + ACCESS_TOKEN,
        "Content-Type"  : "application/json"
    }
    try:
        response = json.loads(httpRequest(URL, DATA, headers, 0, 'GET'))
    except Exception, emsg:
        print emsg
        sys.exit(2)

# Get OpsRamp access token using api key/secret for further communication
def get_access_token():
    url = "https://%s/auth/oauth/token" % (API_SERVER)

    data = urllib.urlencode({
        "client_id"     : API_KEY,
        "client_secret" : API_SECRET,
        "grant_type"    : "client_credentials"
    })

    headers = {"Content-Type": "application/x-www-form-urlencoded", "Accept" : "application/json"}
    try:
        result = json.loads(httpRequest(url, data, headers, None, 'POST'))
        return result['access_token']
    except Exception as emsg:
        raise Exception("Error while getting access token - " + str(emsg))

if __name__ == '__main__':
    try:
        ACCESS_TOKEN = str(get_access_token())

        ''' Creating a schedule maintenance window '''
        url = "https://{0}/api/v2/tenants/{1}/scheduleMaintenances".format(API_SERVER, CLIENT_ID)
        data = {
                "name"              : "Test Maintenance from API",
                "description"       : "Test Maintenance from API",
                "dontRunRBA"        :"false",
                "dontInstallPatch"  :"false",
                "devices"           : [{
                                        "uniqueId": "702c19c4-1991-4e99-8c5f-4104c061fe25"
                                      }],
                "schedule"          : {
                                         "type":"One-Time",
                                         "startTime": "2016-07-07T08:21:00+0000",
                                         "endTime": "2016-07-09T08:45:00+0000",
                                         "timezone":"America/Los_Angeles"
                                      }
                }


        # Searching a schedule maintenance window by name
        url = """https://%s/api/v2/tenants/%s/scheduleMaintenances/search?queryString="""
        + urllib.encode("name:Test Maintenance from API") %(API_SERVER, CLIENT_ID)
        data = None

        # Suspending a schedule maintenance window
        url = "https://{0}/api/v2/tenants/{1}/scheduleMaintenances/123456/suspend".format(API_SERVER, CLIENT_ID)
        data = {"pattern" : "now"}

        # Resuming a schedule maintenance window
        url = "https://{0}/api/v2/tenants/{1}/scheduleMaintenances/123456/resume".format(API_SERVER, CLIENT_ID)
        data = None

        # Deleting a schedule maintenance window
        url = "https://{0/api/v2/tenants/{1}/scheduleMaintenances/123456".format(API_SERVER, CLIENT_ID)
        data = None

        schedule_maintenance_actions(url, data)
    except Exception as e:
        print ("Failed - " + str(e))
{{< /code >}}

### Java

{{< code java >}}
package com.opsramp.examples.rest;

import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.Date;

import org.apache.http.HttpException;
import org.apache.http.HttpHeaders;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpDelete;
import org.apache.http.client.methods.HttpEntityEnclosingRequestBase;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.client.methods.HttpRequestBase;
import org.apache.http.entity.ByteArrayEntity;
import org.apache.http.entity.ContentType;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;

/**
 * Sample program to do schedule maintenance actions
 */
public class ScheduleMaintenanceActions {

	/**
	 * Main program which performs schedule maintenance actions
	 * @param args
	 * @throws HttpException
	 * @throws IOException
	 */
	public static void main(String[] args) throws HttpException, IOException {
		//Replace the end point and access token accordingly
		String ACCESS_TOKEN = "a0f46d75-534d-4180-b4ec-65a23eb1ae39";

		//Creating a schedule maintenance window
		String ENDPOINT = "https://<api-url>/api/v2/tenants/client_99999/scheduleMaintenances";
		String PAYLOAD = "{"name":"Test Maintenance from API","description":"Test Maintenance from API","
				+ ""dontRunRBA":"false","dontInstallPatch":"false", "devices":[{"uniqueId":"
				+ ""702c19c4-1991-4e99-8c5f-4104c061fe25"}],"schedule":{"type":"One-Time","startTime":"
				+ ""2016-07-07T08:21:00+0000","endTime":"2016-07-09T08:45:00+0000","timezone":"
				+ ""America/Los_Angeles"}}";
		String response = invokePostRequest(ACCESS_TOKEN, ENDPOINT, PAYLOAD);
		System.out.println(response);

		//Searching a schedule maintenance window by name
		ENDPOINT = "https://<api-url>/api/v2/tenants/client_99999/scheduleMaintenances/search"
			 + "?queryString=" + URLEncoder.encode("name:Test Maintenance from API", StandardCharsets.UTF_8.toString());
		response = invokeGetRequest(ACCESS_TOKEN, ENDPOINT);
		System.out.println(response);

		//Suspending a schedule maintenance window
		ENDPOINT = "https://<api-url>/api/v2/tenants/client_99999/scheduleMaintenances/123456/suspend";
		PAYLOAD = "{"pattern": "now"}";
		response = invokePostRequest(ACCESS_TOKEN, ENDPOINT, PAYLOAD);
		System.out.println(response);

		//Resuming a schedule maintenance window
		ENDPOINT = "https://<api-url>/api/v2/tenants/client_99999/scheduleMaintenances/123456/resume";
		response = invokePostRequest(ACCESS_TOKEN, ENDPOINT, null);
		System.out.println(response);

		//Deleting a schedule maintenance window
		ENDPOINT = "https://<api-url>/api/v2/tenants/client_99999/scheduleMaintenances/123456";
		response = invokeDeleteRequest(ACCESS_TOKEN, ENDPOINT);
		System.out.println(response);
	}

	/**
	 * Fetches data from given end point
	 * @param accessToken
	 * @param endPoint
	 * @return
	 * @throws HttpException
	 * @throws IOException
	 */
	public static String invokeGetRequest(final String accessToken, final String endPoint)
			throws HttpException, IOException {
		return invokeRequest(accessToken, endPoint, null, new HttpGet(), 0);
	}

	/**
	 * Deletes data at given end point
	 * @param accessToken
	 * @param endPoint
	 * @return
	 * @throws HttpException
	 * @throws IOException
	 */
	public static String invokeDeleteRequest(final String accessToken, final String endPoint)
			throws HttpException, IOException {
		return invokeRequest(accessToken, endPoint, null, new HttpDelete(), 0);
	}

	/**
	 * Posts data to given end point
	 * @param accessToken
	 * @param endPoint
	 * @param payload
	 * @return
	 * @throws HttpException
	 * @throws IOException
	 */
	public static String invokePostRequest(final String accessToken, final String endPoint,
			final String payload) throws HttpException, IOException {
		return invokeRequest(accessToken, endPoint, payload, new HttpPost(), 0);
	}

	/**
	 * Invokes an OAuth2 API request
	 * @param accessToken
	 * @param endPoint
	 * @param payload
	 * @param httpRequest
	 * @return
	 * @throws HttpException
	 * @throws IOException
	 */
	public static String invokeRequest(final String accessToken, final String endPoint,
			final String payload, HttpRequestBase httpRequest, final int currentRetryCount) throws HttpException, IOException {
		CloseableHttpClient httpclient = HttpClients.custom().build();
		try {
			httpRequest.setURI(URI.create(endPoint));
			httpRequest.setHeader(HttpHeaders.ACCEPT, ContentType.APPLICATION_JSON.toString());
			httpRequest.setHeader(HttpHeaders.CONTENT_TYPE, ContentType.APPLICATION_JSON.toString());
			httpRequest.setHeader(HttpHeaders.AUTHORIZATION, "Bearer " + accessToken);
			if(httpRequest instanceof HttpEntityEnclosingRequestBase && payload != null) {
				((HttpEntityEnclosingRequestBase) httpRequest)
					.setEntity(new ByteArrayEntity(payload.getBytes(StandardCharsets.UTF_8.toString())));
			}

			System.out.println("\n" + httpRequest.getRequestLine());
			CloseableHttpResponse response = httpclient.execute(httpRequest);
			try {
				System.out.println("Response " + response.getStatusLine());
				String responseBody = null;
				if(response.getEntity() != null) {
					responseBody = EntityUtils.toString(response.getEntity());
					if(response.getStatusLine().getStatusCode() == 429) {
						if(currentRetryCount > 3) {
							System.out.println("Retry Max-Limit(3) reached; Dropping API: " + endPoint);
						}
						long resetTimeInSeconds = Long.valueOf(response.getFirstHeader("X-RateLimit-Reset").getValue());
						long retryInSec = resetTimeInSeconds - (new Date().getTime()/1000);
						System.out.println("\tNext retry in: " + retryInSec + "s" + " | " + endPoint);
						try {
							Thread.sleep(retryInSec*1000);
						} catch(Exception ex) {}
						invokeRequest(accessToken, endPoint, payload, httpRequest, currentRetryCount+1);
					}
				}
				return responseBody;
			} finally {
				response.close();
			}
		} finally {
			httpclient.close();
		}
	}
}
{{< /code >}}
