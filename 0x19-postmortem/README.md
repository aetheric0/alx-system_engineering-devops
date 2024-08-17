![image](https://github.com/user-attachments/assets/9d92d214-f14d-491c-8009-04b939619080)


**Summary**
- There was an outage of our service between the hours 9:00 to 16:00 UTC+3.
- During these hours users experienced very slow responses to their request and there were infrequent downtimes. 70% of our users were affected
- The root cause of the problems was insufficient memory on our servers to process requests from clients hence the reduced response rate and infrequent downtimes

**Timeline**
- The issue was detected at 13:00 UTC+3
- Several of our customer based reached out to complain about the issue
- We were able to diagnose our servers by running commands to check their performance, then discovered the root cause
- Originally we investigated our internet connectivity but discovered it was fine, before turning to the servers themselves
- The incident was escalated to our SRE engineering specialists immediately the problem was reported
- We have been able to scale horizontally through clustering with new servers to mitigate the failure. The web service has returned back to normalcy.

**Root Cause and Resolution**
- The root cause was the memory of our two servers were overloaded as our web service has seen more use in recent months, coupled with the fact that the timeline the incident was reported is when our users are most active on the site.
- We decided to scale horizontally as it is the most efficient solution and fastest to implement by adding two additional servers to manage the web resources. This has led to even improved response time to users request overall

**Corrective and Preventative Measures**
To avert such incidence from occurring in the future by ensuring that our system is built on the principle of High Availability, we have decided to include a monitoring system for our cluster of servers that will monitor the state of the system at all times. This system would give alerts when over 50% of a server memory has been used as well as an analytical system that can measure the trend in rise of our user activity to help us take preemptive actions and ensure that our service is fully available all the time.

This is a list of implementations the team has decided on to include to our system:
A monitoring service on each server
A mother monitoring service that aggregates the performance of all servers on our system
Ensuring two extra backup servers are available to ensure fast scaling of the servers should our monitoring system raise errors.
Automated monitoring system that alerts the SREs when an issue arises to ensure we do not miss any critical information that may be happening on the backend
