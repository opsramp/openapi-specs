---
title: Resource index and summary
linkTitle: Resource index and summary
weight: 20
description: Lists REST API endpoints by category, alphabetically, with summary information.
type: documentation
---

## Agents and Gateways

{{< table datatable=1  paging=0 searching=0 >}}
    <thead class="thead-dark">
        <tr>
            <th style="width: 50%;">Resource</th>
            <th style="width: 42%;">Description</th>
            <th style="width: 2%;">POST</th>
            <th style="width: 2%;">PUT</th>
            <th style="width: 2%;">GET</th>
            <th style="width: 2%;">DELETE</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>apiTokenGen</td>
            <td>Generates an access token on the gateway.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>applicationservice</td>
            <td>Gets the service status and starts and stops application services.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>download/gateway/{packagename}</td>
            <td>Downloads gateway files from the download server.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>externalproxy</td>
            <td>Configures the external proxy connection on the gateway.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>generalinfo</td>
            <td>Gets general information from the gateway, including appliance details and network information.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>getntpdetails</td>
            <td>Gets NTP details from the gateway.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>gettimezoneinfo</td>
            <td>Gets timezone information from the gateway.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>networksettings</td>
            <td>Specifies the network settings on the gateway.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>nginx</td>
            <td>Gets the NGINX service status and restarts the NGINX service on the gateway.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>ntpmanualconfig</td>
            <td>Manually sets the NTP date and time on the gateway.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>ntpservice</td>
            <td>Starts and stops the gateway NTP service.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>ntpsyncips</td>
            <td>Synchronizes gateway NTP servers time.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>ntpupdateips</td>
            <td>Updates gateway NTP server IP addresses.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>proxy</td>
            <td>Turn the gateway Squid proxy server on and off.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>registration</td>
            <td>Registers the gateway.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>restartnetwork</td>
            <td>Restarts the gateway network service.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>settimezone</td>
            <td>Sets the gateway timezone.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>staticroute</td>
            <td>Sets the gateway static route configuration.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/agentPolicies/{policyId}/devices</td>
            <td>Assigns agent resource policies.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/agentProfiles/{profileId}/devices</td>
            <td>Assigns agent resource profiles.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/agents/{agentversion}/resourcesCountByAgentVersion</td>
            <td>Gets the number of installed agent resources by agent version.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/agents/deployAgentsScript</td>
            <td>Downloads the Linux agent installation script.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/agents/{platform}/download/{package-name}</td>
            <td>Downloads the Linux agents.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/agents/{platform}/info</td>
            <td>Gets the Linux agent. This is usually followed by an API call to Download Linux Agent.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/agents/windows</td>
            <td>Downloads the Windows agent.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/managementProfiles</td>
            <td>Creates a management profile.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/managementProfiles/{id}/attach</td>
            <td>Attaches a gateway to a management profile and generates an activation token. The generated activation token is used in gateway registration.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/managementProfiles/{profileId}</td>
            <td>Gets, updates, and deletes a management profile.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/managementProfiles/{profileId}/detach</td>
            <td>Unmaps, or detaches, the gateway from the management profile and invalidates the activation token.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/managementProfiles/{profileId}/reconnectTunnel</td>
            <td>Reconnects the management profile tunnel.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/managementProfiles/search</td>
            <td>Searches for a management profiles.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
    </tbody>
{{< /table >}}

## Alerts

{{< table datatable=1  paging=0 searching=0 >}}
    <thead class="thead-dark">
        <tr>
            <th style="width: 50%;">Resource</th>
            <th style="width: 42%;">Description</th>
            <th style="width: 2%;">POST</th>
            <th style="width: 2%;">PUT</th>
            <th style="width: 2%;">GET</th>
            <th style="width: 2%;">DELETE</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>alerts/tenants/{tenantId}/alerts/{alertId}</td>
            <td>Gets alert details by alert ID.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>alerts/tenants/{tenantId}/tickets/{ticketId}</td>
            <td>Gets alert details by incident ID.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>alertTypes</td>
            <td>Gets the list of supported alert types.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/alert</td>
            <td>Creates a single alert on a resource.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/alerts/{alertId}/acknowledge</td>
            <td>Acknowledges an alert.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/alerts/{alertId}/actions/{action}</td>
            <td>Posts an action on an alert.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/alerts/{alertId}</td>
            <td>Gets alert details.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/alerts/{alertId}/comments</td>
            <td>Gets alert comments.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/alerts/{alertId}/escalations</td>
            <td>Gets the escalation policy attached to an alert.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/alerts/{alertId}/incidents/{incidentId}/attach</td>
            <td>Attaches an incident to an alert.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/alerts/{alertId}/occurrences</td>
            <td>Gets the alert occurrences based on the alert-triggered time.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/alerts/{alertId}/tickets/{ticketId}/update</td>
            <td>Updates an incident with an alert ID</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/alerts</td>
            <td>Creates multiple alerts on resources.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/alerts/event/{eventId}</td>
            <td>Gets alert details by event ID.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/alerts/search</td>
            <td>Searches alerts.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/alertStatusHistory/{alertId}</td>
            <td>Gets alert status history.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/escalations</td>
            <td>Creates an alert escalation policy. The policy is a predefined action to be taken when an alert is not acknowledged.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/escalations/{id}</td>
            <td>Gets, update, and delete alert escalation policy information.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/escalations/{id}/disable</td>
            <td>Disables an alert escalation policy.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/escalations/{id}/enable</td>
            <td>Enables an alert escalation policy.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/escalations/search</td>
            <td>Gets the alert escalation policies attached to an alert.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/policies/alertCorrelation</td>
            <td>Creates and gets alert correlation policies.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/policies/alertCorrelation/{policyId}/{action}</td>
            <td>Enables, disables, and creates an observed mode on an alert correlation policy.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/policies/alertCorrelation/{policyId}</td>
            <td>Update, gets, and deletes an alert correlation policy by ID.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/policies/firstResponse</td>
            <td>Creates and views first response policydetails.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/policies/firstResponse/{policyId}</td>
            <td>Updates, gets, and deletes a first response policy by ID.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/policies/firstResponse/{policyId}/{status}</td>
            <td>Enables and disables the first response policy.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/rosters</td>
            <td>Creates partner-level and client-level rosters.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/rosters/{id}</td>
            <td>Updates, gets, and deletes rosters.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/rosters/search</td>
            <td>Gets the rosters in an organization.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/scheduleMaintenances</td>
            <td>Creates a daily recurring schedule.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/scheduleMaintenances/search</td>
            <td>Gets the scheduled maintenance windows under a specific tenant.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/scheduleMaintenances/{smId}</td>
            <td>Updates, gets, and deletes scheduled maintenence windows.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/scheduleMaintenances/{smId}/end</td>
            <td>Ends a scheduled maintenance window.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/scheduleMaintenances/{smId}/resources</td>
            <td>Adds and deletes schedule maintenance window resources.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/scheduleMaintenances/{smId}/resources/{resourcesType}</td>
            <td>Gets the list of devices (or device groups or sites) of a scheduled maintenance window.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/scheduleMaintenances/{smId}/resume</td>
            <td>Activates a user.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/scheduleMaintenances/{smId}/suspend</td>
            <td>Suspends a scheduled maintenance window.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/subAlertTypes</td>
            <td>Gets the sub-alert types.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/users/{userId}/alertViews</td>
            <td>Gets a list of alert views.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/users/{userId}/alertViews/{viewId}</td>
            <td>Gets an alert view of a user.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
    </tbody>
{{< /table >}}

## Automation

{{< table datatable=1  paging=0 searching=0 >}}
    <thead class="thead-dark">
        <tr>
            <th style="width: 50%;">Resource</th>
            <th style="width: 42%;">Description</th>
            <th style="width: 2%;">POST</th>
            <th style="width: 2%;">PUT</th>
            <th style="width: 2%;">GET</th>
            <th style="width: 2%;">DELETE</th>
        </tr>
    </thead>
    <tbody>
        # Automation
        <tr>
            <td>tenants/{tenantId}/jobs</td>
            <td>Creates a job.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/jobs/{id}</td>
            <td>Gets, update, and delete the jobs.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/jobs/{id}/run</td>
            <td>Runs a scheduled job.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/jobs/{id}/script/run</td>
            <td>Runs a script.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/jobs/search</td>
            <td>Gets the list of jobs defined by a tenant.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/jobs/types</td>
            <td>Gets the list of job types.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/rba/categories</td>
            <td>Creates and updates an RBA category and gets a list of RBA categories.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/rba/categories/{categoryId}</td>
            <td>Deletes an RBA category.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/rba/categories/{categoryId}/scripts</td>
            <td>Creates and deletes a script and gets a list of scripts for a category.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/rba/categories/{categoryId}/scripts/{scriptId}</td>
            <td>Gets and update the details of a script.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/rba/scripts/{scriptId}/paginatedOutputs</td>
            <td>Gets paginated output logs of a script.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
    </tbody>
{{< /table >}}

## Exports

{{< table datatable=1  paging=0 searching=0 >}}
    <thead class="thead-dark">
        <tr>
            <th style="width: 50%;">Resource</th>
            <th style="width: 42%;">Description</th>
            <th style="width: 2%;">POST</th>
            <th style="width: 2%;">PUT</th>
            <th style="width: 2%;">GET</th>
            <th style="width: 2%;">DELETE</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>exports/tenants/{tenantId}/create</td>
            <td>Creates an on-demand batch export template.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
    </tbody>
{{< /table >}}

## Integrations

{{< table datatable=1  paging=0 searching=0 >}}
    <thead class="thead-dark">
        <tr>
            <th style="width: 50%;">Resource</th>
            <th style="width: 42%;">Description</th>
            <th style="width: 2%;">POST</th>
            <th style="width: 2%;">PUT</th>
            <th style="width: 2%;">GET</th>
            <th style="width: 2%;">DELETE</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>tenants/{tenantId}/integrations/activity</td>
            <td>Gets the installation activity details of an installed integration activity.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/integrations/available/{intgId}/emailProps/{entityType}</td>
            <td>Gets the email properties of an entity.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/integrations/available/{intgId}/mappingAttr/{entityType}</td>
            <td>Gets the integration mappable properties for an entity.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/integrations/available/search</td>
            <td>Searches available integrations.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/integrations/events/placeHolders/{entityType}</td>
            <td>Gets the integration event placeholders of an entity.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/integrations/install/AWS</td>
            <td>These endpoint IDs are used to install third-party integrations.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/integrations/install/AZURE</td>
            <td>These endpoint IDs are used to install third-party integrations.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/integrations/install/CUSTOM</td>
            <td>Installs a custom integration.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/integrations/installed/{installedIntgId}/disable</td>
            <td>Disables an installed integration, temporarily disabling the integration services.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/integrations/installed/{installedIntgId}/enable</td>
            <td>Enables an installed integration.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/integrations/installed/{installedIntgId}/event/{eventId}/activate</td>
            <td>Activates an integration event.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/integrations/installed/{installedIntgId}/event/{eventId}/deactivate</td>
            <td>Deactivates an integration event.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/integrations/installed/{installedIntgId}/event/{eventId}</td>
            <td>Updates, gets, and deletes an integration event.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/integrations/installed/{installedIntgId}/event</td>
            <td>Creates an integration event.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/integrations/installed/{installedIntgId}/events</td>
            <td>Gets installed integration events.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/integrations/installed/{installedIntgId}/inbound/authentication</td>
            <td>Creates and updates installed integration inbound authentication.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/integrations/installed/{installedIntgId}</td>
            <td>Updates, gets, and deletes the installed integration details.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/integrations/installed/{installedIntgId}/mappingAttr</td>
            <td>Creates, updates, and gets installed integration mapping attributes.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/integrations/installed/{installedIntgId}/notifier</td>
            <td>Creates and updates an installed integration base notifier.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/integrations/installed/search</td>
            <td>Searches for installed integrations.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/integrations/install/EMAILALERTS</td>
            <td>Installs email alert integrations. OpsRamp processes all incoming Alert emails.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/integrations/install/EMAILINCIDENTS</td>
            <td>Installs an email request integration.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/integrations/install/GOOGLE</td>
            <td>These endpoint IDs are used to install third-party integrations.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/integrations/install/{intgId}</td>
            <td>Installs the following integrations:</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/integrations/install/OKTA</td>
            <td>Installs a SSO integration.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/policies/discovery/action/scan/{discoveryProfileId}</td>
            <td>Rescans an AWS, Azure, and Google discovery profile.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/policies/discovery/{discoveryId}</td>
            <td>Gets and delete discovery profiles for AWS, Azure, and Google.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/policies/discovery</td>
            <td>Creates and updates AWS, Azure, and Google discovery profiles and gets a list of discovery profiles.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/policies/discovery/search</td>
            <td>Uses a discovery profile name to search for an AWS, Azure, and Google discovery profile.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
    </tbody>
{{< /table >}}

## Knowledge Base

{{< table datatable=1  paging=0 searching=0 >}}
    <thead class="thead-dark">
        <tr>
            <th style="width: 50%;">Resource</th>
            <th style="width: 42%;">Description</th>
            <th style="width: 2%;">POST</th>
            <th style="width: 2%;">PUT</th>
            <th style="width: 2%;">GET</th>
            <th style="width: 2%;">DELETE</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>tenants/{tenantId}/kb/article/{articleId}/comment</td>
            <td>Adds comments to a KB article.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/kb/article/{articleId}/comments/{commentId}/resources/{resourceId}</td>
            <td>Downloads KB article attachment or comment.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/kb/article/{articleId}/comments</td>
            <td>Gets a list of comments for a KB article.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/kb/article/{articleId}/delete</td>
            <td>Deletes a KB category.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/kb/article/{articleId}</td>
            <td>Gets and updates a KB article.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/kb/article/{articleId}/resources/{resourceId}</td>
            <td>Downloads a KB article attachment.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/kb/article/{articleId}/share</td>
            <td>Shares KB article.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/kb/{articleId}/activitylog</td>
            <td>Gets KB article activity log with provided details.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/kb/article</td>
            <td>Creates a KB article.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/kb/articlesList</td>
            <td>Gets a list of KB articles.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/kb/articles/search</td>
            <td>Searchs for the list of articles in a KB category.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/kb/category/{categoryId}</td>
            <td>Gets a knowledge base category.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/kb/category/create</td>
            <td>Creates a KB category.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/kb/category/delete/{categoryId}</td>
            <td>Deletes a KB category.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/kb/categorylist/{categoryId}</td>
            <td>Gets the list of sub-categories of a knowledge base category.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/kb/categorylist</td>
            <td>Gets list of knowledge base categories.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/kb/category/restore/{categoryId}</td>
            <td>Gets a knowledge base category from TRASH.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/kb/category/update/{categoryId}</td>
            <td>Updates a KB category.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/kb/template</td>
            <td>Creates a KB template.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/kb/templatesList</td>
            <td>Gets the list of KB templates.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/kb/template/{templateId}/delete</td>
            <td>Deletes a KB template.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/kb/template/{templateId}</td>
            <td>Gets KB article template details.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
    </tbody>
{{< /table >}}

## Metrics

{{< table datatable=1  paging=0 searching=0 >}}
    <thead class="thead-dark">
        <tr>
            <th style="width: 50%;">Resource</th>
            <th style="width: 42%;">Description</th>
            <th style="width: 2%;">POST</th>
            <th style="width: 2%;">PUT</th>
            <th style="width: 2%;">GET</th>
            <th style="width: 2%;">DELETE</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>metric/search</td>
            <td>Gets the details of metric behavior at a certain time period.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>metric/tenants/{tenantId}/metrics/{metric}/metricType</td>
            <td>Updates and gets metric type details.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>metric/tenants/{tenantId}/{tenantId}/metrictype</td>
            <td>The endpoint to assign agent policy for resources.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>metric/tenants/{tenantId}/rtypes/{rtype}/resources/{resource}/metrics</td>
            <td>Updates and gets resource metrics.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
    </tbody>
{{< /table >}}

## Monitoring

{{< table datatable=1  paging=0 searching=0 >}}
    <thead class="thead-dark">
        <tr>
            <th style="width: 50%;">Resource</th>
            <th style="width: 42%;">Description</th>
            <th style="width: 2%;">POST</th>
            <th style="width: 2%;">PUT</th>
            <th style="width: 2%;">GET</th>
            <th style="width: 2%;">DELETE</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>tenants/{tenantId}/monitoring/templates/search</td>
            <td>Activates a user.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/resources/{resourceId}/templates</td>
            <td>Assigns, unassigns, and updates resource templates.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/resources/{resourceId}/templates/search</td>
            <td>Gets templates assigned to a resource.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/resourceMonitors</td>
            <td>Creates resource monitors.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
    </tbody>
{{< /table >}}

## Patching

{{< table datatable=1  paging=0 searching=0 >}}
    <thead class="thead-dark">
        <tr>
            <th style="width: 50%;">Resource</th>
            <th style="width: 42%;">Description</th>
            <th style="width: 2%;">POST</th>
            <th style="width: 2%;">PUT</th>
            <th style="width: 2%;">GET</th>
            <th style="width: 2%;">DELETE</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>tenants/{tenantId}/patches/baselines/{baselineId}/{action}</td>
            <td>Activates and deactivates a patch baseline.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/patches/baselines/{baselineId}/{patchId}/{action}</td>
            <td>Adds and removes patches from a baseline.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/patches/baselines/{baselineId}</td>
            <td>Gets, updates, and deletes patch baselines.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/patches/baselines</td>
            <td>Creates and gets patch baselines.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/patches/compliance/{complianceId}/baselines/{baselineId}/{action}</td>
            <td>Assigns and unassigns a patch baseline attached for a patch compliance check.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/patches/compliance/{complianceId}/baselines</td>
            <td>Gets the baselines attached to a patch compliance.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/patches/compliance/{complianceId}/deviceGroups/{deviceGrpId}/{action}</td>
            <td>Assigns and unassigns a device group for a patch compliance.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/patches/compliance/{complianceId}/deviceGroups</td>
            <td>Gets the device groups attached to a patch compliance.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/patches/compliance/{complianceId}/devices/{deviceId}/{action}</td>
            <td>Assigns and unassigns devices for patch compliance.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/patches/compliance/{complianceId}/devices</td>
            <td>Gets the list of devices attached to a patch compliance.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/patches/compliance/{complianceId}</td>
            <td>Update sand deletes a patch compliance</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/patches/compliance/{complianceId}/run</td>
            <td>Runs a patch compliance, checking all devices and device groups for compliance.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/patches/compliance</td>
            <td>Creates a patch compliance and gets the list of patch compliance checks.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/patches/configurations/{id}</td>
            <td>Updates, gets, and deletes a patch configuration.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/patches/configurations/{id}/run</td>
            <td>Runs a patch configuration.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/patches/configurations</td>
            <td>Creates a patch configuration and executes patches on the resources.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/patches/configurations/search</td>
            <td>Searches for patch configurations by a client.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/patches</td>
            <td>Gets a tenant’s list of patches.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/patches/rating/{intgId}/feed/{patchId}</td>
            <td>Gets patch details and delete a patch qualification.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/patches/{resourceId}/install/status</td>
            <td>Gets the patching status of all devices in a patch configuration and display paginated output.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/patches/{resourceId}/scan/status</td>
            <td>Gets the patch scan status of all devices assigned to a missing patch job and display paginated output.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/resources/patches</td>
            <td>Gets the details of installed, missing, or installation-failed patches for a client’s resources.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/resources/{resourceId}/baselines/{baselineId}/patches</td>
            <td>Checks the compliance of a resource against a patch baseline.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/resources/{resourceId}/patches/install/status</td>
            <td>Gets the patching status of a device.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/resources/{resourceId}/patches/{patchId}/{approvalType}</td>
            <td>Approves and disapproves a patch.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/resources/{resourceId}/patches/scan/status</td>
            <td>Gets the details of patch scan status of a device.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
    </tbody>
{{< /table >}}

## Resource Management

{{< table datatable=1  paging=0 searching=0 >}}
    <thead class="thead-dark">
        <tr>
            <th style="width: 50%;">Resource</th>
            <th style="width: 42%;">Description</th>
            <th style="width: 2%;">POST</th>
            <th style="width: 2%;">PUT</th>
            <th style="width: 2%;">GET</th>
            <th style="width: 2%;">DELETE</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>tenants/{mspId}/decommission/{action}</td>
            <td>Enables and disables resource decommission at partner level.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/customAttributes/{attributeId}/assignedEntities/search</td>
            <td>Searches for the assigned entities by attribute.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/customAttributes/{attributeId}</td>
            <td>Updates, gets, and deletes tenant custom attributes.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/customAttributes/{attributeId}/values/{valueId}/devices</td>
            <td>Assigns and unassigns custom attributes for devices</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/customAttributes/{attributeId}/values/{valueId}</td>
            <td>Updates a custom attribute value description.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/customAttributes/{attributeId}/values/{valueId}/serviceGroups</td>
            <td>Assigns and unassigns custom attributes for service groups</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/customAttributes</td>
            <td>Creates a tenant custom attribute type and the list of values</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/customAttributes/search</td>
            <td>Searches for tenant custom attribute types and respective values.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/dependencies/{resourceuuid}</td>
            <td>Creates, gets, and deletes resource dependency.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/deviceGroups/{deviceGroupId}/childs</td>
            <td>Assigns and unassigns a child resources for device groups.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/deviceGroups/{deviceGroupId}/childs/search</td>
            <td>Gets the child resources or child device groups within a parent device group.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/deviceGroups/{deviceGroupId}</td>
            <td>Gets device group details and delete sdevice groups.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/deviceGroups/minimal</td>
            <td>Gets minimal details of device groups.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/deviceGroups</td>
            <td>Creates and updates device groups.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/deviceGroups/search</td>
            <td>Gets the root level device groups.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/devices/{deviceId}/customAttributes</td>
            <td>Gets device custom attributes.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/devices/{deviceId}/deviceWarranty</td>
            <td>Creates a device warranty and gets device warranty details.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/devices/wsussettings/{action}</td>
            <td>The endpoint to assign agent policy for resources.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/deviceWarranties</td>
            <td>Gets the details of multiple device warranties.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/history/resources/{resourceId}</td>
            <td>Gets the data of a decommissioned resource.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/history/resources</td>
            <td>Gets the list of decommissioned resources.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/policies/management/{id}/action/run</td>
            <td>Runs a device management policy.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/policies/management/{id}</td>
            <td>The endpoint is used to get device management policy details and unassign agent policy for resources.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/policies/management</td>
            <td>Creates and updates device management policies, and gets tenant device management policies, without pagination.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/policies/management/search</td>
            <td>Searches for a device management policy with a policy name.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/resources/antivirus/search</td>
            <td>Gets the latest antivirus definitions installed on resources.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/resources/minimal</td>
            <td>Gets minimal resource details.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/resources/{resourceId}/applications</td>
            <td>Gets the list of applications running on a resource.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/resources/{resourceId}/availability</td>
            <td>Gets the availability details of a resource within a specific time frame.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/resources/{resourceId}/availability/rule</td>
            <td>Updates and gets the availability rule defined on a resource.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/resources/{resourceId}/decommission</td>
            <td>Decommissions a resource.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/resources/{resourceId}/notes/{noteId}</td>
            <td>Updates a resource note.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/resources/{resourceId}/notes</td>
            <td>Creates a resource note.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/resources/{resourceId}/notes/search</td>
            <td>Gets the latest antivirus definitions installed on resources.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/resources/{resourceId}</td>
            <td>Gets resource information, update resource details, and delete a resource using a resource ID.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/resources</td>
            <td>Creates a generic resource.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/resources/Resourcetype/{resourceType}/{identity}</td>
            <td>Deletes a resource based on resource type.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/resources/search</td>
            <td>Gets the resources of a partner or a client.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/resourceType/minimal</td>
            <td>Gets minimal resource type details.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/serviceGroups/link</td>
            <td>Links or shares an existing service group with other service groups.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/serviceGroups/minimal</td>
            <td>Gets minimal details (including service group ID and name) of service groups.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/serviceGroups</td>
            <td>Creates or updates a service group.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/serviceGroups/search</td>
            <td>Gets root-level, parent service groups.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/serviceGroups/{serviceGroupId}/customAttributes</td>
            <td>Gets service group custom attributes.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/serviceGroups/{sgId}/childs</td>
            <td>Assigns and unassigns child resources for a service group.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/serviceGroups/{sgId}/childs/search</td>
            <td>Gets the child entities (resources or service groups) of a parent service group.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/serviceGroups/{sgId}</td>
            <td>Gets and delete service groups.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/serviceGroups/unLink/{parentSgId}/{childSgId}</td>
            <td>Unlinks a child service group from a parent service group.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/services/{serviceId}/availability</td>
            <td>Gets availability details of a service.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/sites/minimal</td>
            <td>Gets minimal details of sites.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/sites</td>
            <td>Creates a site to organize devices based on location.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/sites/search</td>
            <td>Searches sites.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/sites/{siteId}</td>
            <td>Updates and gets site details, and deletes a site.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/topology/{resourceUUID}</td>
            <td>Gets topology data by providing relationship information about resources.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{varId}/clients/{clientId}/customAttributes</td>
            <td>Gets client custom attributes.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{varId}/customAttributes/{attributeId}/values/{valueId}/clients</td>
            <td>Assigns and unassigns client custom attributes.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
    </tbody>
{{< /table >}}

## Tenancy and Access Controls

{{< table datatable=1  paging=0 searching=0 >}}
    <thead class="thead-dark">
        <tr>
            <th style="width: 50%;">Resource</th>
            <th style="width: 42%;">Description</th>
            <th style="width: 2%;">POST</th>
            <th style="width: 2%;">PUT</th>
            <th style="width: 2%;">GET</th>
            <th style="width: 2%;">DELETE</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>cfg/alertSource/available/custIntg/{intgId}</td>
            <td>Gets the list of available custom (and email alert integration) alert sources.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>cfg/countries</td>
            <td>Gets the list of countries based on country code.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>cfg/tenants/channels</td>
            <td>Gets the list of channels.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>cfg/tenants/nocs</td>
            <td>Gets the list of NOCs of a tenant.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>cfg/timezones</td>
            <td>Gets the list of timezones.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{orgId}/users/minimal</td>
            <td>Gets the minimal details of the users.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{orgId}/users</td>
            <td>Creates a user.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{orgId}/users/{userId}/changePassword</td>
            <td>Changes the password.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{orgId}/users/{userId}</td>
            <td>Updates and gets user details.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/credentialSets/{credentialSetId}</td>
            <td>Updates, gets, and deletes a credential set by ID.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/credentialSets/minimal</td>
            <td>Gets the minimal details of client credential sets.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/credentialSets</td>
            <td>Creates and gets a credential set.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/devices/{deviceId}/credentialSets/minimal</td>
            <td>Gets the minimal details of client credential sets.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/notes/{noteId}/</td>
            <td>Updates, gets, and deletes a client note.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/notes/search</td>
            <td>Searches for client notes.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/notes</td>
            <td>Creates client notes.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/permissionSets</td>
            <td>Gets the list of permission sets assigned to a tenant.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/roles/{roleId}</td>
            <td>Updates, gets, and deletes roles.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/roles/search</td>
            <td>Gets roles under a partner or client.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/roles</td>
            <td>Creates a partner- or client-level role.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/userGroups</td>
            <td>Creates a partner- or client-level user group, and searches user groups.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/userGroups/{userGroupId}</td>
            <td>Updates, gets, and deletes user groups.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/userGroups/{userGroupId}/users</td>
            <td>Adds, gets, and deletes users for a user group.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/users/loginHistory/search</td>
            <td>Gets the user login history.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/users/search</td>
            <td>Gets users for a tenant.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/users/{userId}/{action}</td>
            <td>The endpoint to assign agent policy for resources.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{varId}/clients/{clientId}/{action}</td>
            <td>Activates and deactivates a client.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{varId}/clients/{clientId}</td>
            <td>Updates and gets client details.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{varId}/clients/minimal</td>
            <td>Gets the minimal details of clients.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{varId}/clients/search</td>
            <td>Searches for clients.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{varId}/clients</td>
            <td>Creates a client.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{varId}</td>
            <td>This API is used to get details of a partner.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
    </tbody>
{{< /table >}}

## Tickets

{{< table datatable=1  paging=0 searching=0 >}}
    <thead class="thead-dark">
        <tr>
            <th style="width: 50%;">Resource</th>
            <th style="width: 42%;">Description</th>
            <th style="width: 2%;">POST</th>
            <th style="width: 2%;">PUT</th>
            <th style="width: 2%;">GET</th>
            <th style="width: 2%;">DELETE</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>tenants/{tenantId}/changeRequests/categories</td>
            <td>Creates categories for the change request entity type.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/changeRequests/categories/{uniqueId}</td>
            <td>Updates a category of the change request entity type.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/changeRequests/{changeRequestId}/activitylog</td>
            <td>Gets user activities on a change request.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/changeRequests/{changeRequestId}/close</td>
            <td>Closes a change request.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/changeRequests/{changeRequestId}/responses/{responseId}/resources/{resourceId}</td>
            <td>Downloads the response attachment attached to a change request.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/changeRequests/{changeRequestId}/responses/search</td>
            <td>Gets responses of a change request.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/changeRequests/{changeRequestId}/responses</td>
            <td>Adds a response to a change request.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/changeRequests/{changeRequestId}</td>
            <td>Gets and update change requests.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/changeRequests/customForm</td>
            <td>Gets the custom form for a change request.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/changeRequests/search</td>
            <td>Searches for change requests.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/changeRequests</td>
            <td>Creates a change request.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/customFields/{classCode}/{customFieldId}</td>
            <td>Gets the details of a custom field.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/customFields/{classCode}</td>
            <td>Gets details of custom fields attached to an entity.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/incidents/businessImpacts</td>
            <td>Creates and gets an incident business impact.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/incidents/businessImpacts/{uniqueId}</td>
            <td>Updates incident business impact.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/incidents/categories</td>
            <td>Creates categories for the incident entity type.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/incidents/categories/{uniqueId}</td>
            <td>Updates a category of entity type incident.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/incidents/customForm</td>
            <td>Gets the custom form for an incident.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/incidents/forwardMapping</td>
            <td>Creates, updates, and gets forward mapping.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/incidents/{incidentId}/activitylog</td>
            <td>Gets user activities on an incident.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/incidents/{incidentId}/close</td>
            <td>Closes an incident.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/incidents/{incidentId}/responses/{responseId}/resources/{resourceId}</td>
            <td>Downloadsthe response attached to an incident.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/incidents/{incidentId}/responses/search</td>
            <td>Gets responses of an incident.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/incidents/{incidentId}/responses</td>
            <td>Adds a response to an incident.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/incidents/{incidentId}</td>
            <td>Updates and Gets incidents.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/incidents/reverseMapping</td>
            <td>Creates, updates, and gets reverse mappings.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/incidents/search</td>
            <td>Searches for incidents.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/incidents</td>
            <td>Creates an incident.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/incidents/urgencies</td>
            <td>Create and gets urgencies for an incident.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/incidents/urgencies/{uniqueId}</td>
            <td>Updates urgency.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/problems/categories</td>
            <td>Creates categories for the problem entity type.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/problems/categories/{uniqueId}</td>
            <td>Updates a category of the entity type problem.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/problems/customForm</td>
            <td>Gets the custom form for a problem.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/problems/{problemId}/activitylog</td>
            <td>Gets user activities on a problem.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/problems/{problemId}/close</td>
            <td>Closes a problem.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/problems/{problemId}/responses/{responseId}/resources/{resourceId}</td>
            <td>Downloads the response attached to a problem.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/problems/{problemId}/responses/search</td>
            <td>Gets responses of a problem.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/problems/{problemId}/responses</td>
            <td>Adds a response to a problem.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/problems/{problemId}</td>
            <td>Updates and gets a problem</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/problems/search</td>
            <td>Searches problems.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/problems</td>
            <td>Creates a problem.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/serviceRequests/categories</td>
            <td>Creates categories for the service request entity type.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/serviceRequests/categories/{uniqueId}</td>
            <td>Updates a category of entity type service request.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/serviceRequests/customForm</td>
            <td>Gets the custom form for a service request.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/serviceRequests/search</td>
            <td>Searches for service requests.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/serviceRequests/{serviceRequestId}/activitylog</td>
            <td>Gets user activities on a service request.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/serviceRequests/{serviceRequestId}/close</td>
            <td>Closes a service request.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/serviceRequests/{serviceRequestId}/responses/{responseId}/resources/{resourceId}</td>
            <td>Downloads the response attached to a service request.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/serviceRequests/{serviceRequestId}/responses/search</td>
            <td>Gets responses of a service request.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/serviceRequests/{serviceRequestId}/responses</td>
            <td>Adds a response to a service request.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/serviceRequests/{serviceRequestId}</td>
            <td>Updates and gets a service request.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/serviceRequests</td>
            <td>Creates a service request.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/tasks/search</td>
            <td>Searches tasks.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/tasks/{taskId}/activitylog</td>
            <td>Gets a list of user activities on a task..</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/tasks/{taskId}/close</td>
            <td>Closes a task.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/tasks/{taskId}/responses/{responseId}/resources/{resourceId}</td>
            <td>Downloads the response attached to a task.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/tasks/{taskId}/responses/search</td>
            <td>Gets responses of a task.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/tasks/{taskId}/responses</td>
            <td>Adds a response to a task.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/tasks/{taskId}</td>
            <td>Updates and gets tasks.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/tasks</td>
            <td>Creates a task.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/{ticketType}/categories/{parentCategoryId}</td>
            <td>Gets the list of categories for an entity type.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/{ticketType}/slaPolicies/{id}</td>
            <td>Gets the details of a service level agreement policy.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/{ticketType}/slaPolicies/search</td>
            <td>Gets a list of all service level agreement policies along with their details.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/{ticketType}/statusReasons</td>
            <td>Gets ticket status change reasons.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/{ticketType}/{ticketId}/notes/{noteId}</td>
            <td>Updates, gets, and deletes ticket notes by ID.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;">&xcirc;</td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/{ticketType}/{ticketId}/notes</td>
            <td>Creates and gets ticket notes.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/timeBoundRequests/customForm</td>
            <td>Gets the custom form for a time-bound request.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/timeBoundRequests/search</td>
            <td>Searches for time bound requests.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/timeBoundRequests</td>
            <td>Creates a time bound request.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/timeBoundRequests/{timeBoundRequestId}/activitylog</td>
            <td>Gets user activities on a time bound request.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/timeBoundRequests/{timeBoundRequestId}/close</td>
            <td>Closes a time bound request.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/timeBoundRequests/{timeBoundRequestId}/responses/{responseId}/resources/{resourceId}</td>
            <td>Downloads the response attached to a time bound request.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/timeBoundRequests/{timeBoundRequestId}/responses/search</td>
            <td>Gets responses of a time bound request.</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/timeBoundRequests/{timeBoundRequestId}/responses</td>
            <td>Adds a response to a time bound request.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;"></td>
        </tr>
        <tr>
            <td>tenants/{tenantId}/timeBoundRequests/{timeBoundRequestId}</td>
            <td>Updates and gets time bound requests.</td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
            <td style="text-align: center;">&xcirc;</td>
            <td style="text-align: center;"></td>
        </tr>
    </tbody>
{{< /table >}}
