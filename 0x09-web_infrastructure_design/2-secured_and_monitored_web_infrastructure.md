# Secured and monitored web infrastructure

![image](https://user-images.githubusercontent.com/95341497/201714914-39eb7a3b-b9d3-492d-b93e-e86e447b2548.png)

[Secured and monitored web infrastructure](https://imgur.com/x6iXek7)

## Description

This web architecture has three servers. It is secured, monitored, and serves encrypted traffic.

## Specifics of the infrastructure

**What are firewalls for?**
* By serving as an intermediary between the internal network and the external network and restricting incoming traffic that meets the aforementioned requirements, firewalls help to safeguard the network (or web servers, in any case) from unauthorized and undesired users.

**Why is the traffic served over HTTPS?**
* The SSL certificate is used to encrypt communication between web servers and the outside network in order to avoid man-in-the-middle attacks (MITM) and network sniffers from examining the traffic and revealing sensitive data. The SSL certificates guarantee identity, privacy, and integrity.

**What monitoring is used for?**
* Web servers perform a variety of crucial tasks. As a result, there are several things to monitor, such as connections to clients and other servers on the network, traffic flowing to and from the server at any given moment, demands for host resources like CPU, RAM, and disk access, and the accessibility of other web servers for proxying requests.

**How the monitoring tool is collecting data?**
**Explain what to do if you want to monitor your web server QPS**
* The monitoring tool observes the servers and provides key metrics about the servers' operations to the administrators. It automatically tests the accessibility of the servers, measures response time, and alerts for errors such as corrupt/missing files, security vulnerabilities/violations, and many other issues. 
* In regard to a network that serves a Web domain, the number of queries per second indicates the volume of traffic passing through a certain server. This measurement is crucial for determining if systems are scalable enough to meet the evolving demands of a user community as it expands and how support infrastructures handle fluctuating volumes of Web traffic.


## Issues with the infrastructure

**Why terminating SSL at the load balancer level is an issue?**
* If SSL was off at the load balancer level, communication between the load balancer and the web servers would no longer be encrypted.

**Why having only one MySQL server capable of accepting writes is an issue?**
* A problem with only having one MySQL server is that it might be a single point of failure for the web architecture and is not scalable.

**Why having servers with all the same components (database, web server and application server) might be a problem?**
* When all the components on a server are the same, they compete for resources like CPU, memory, I/O and other resources., which can result in subpar performance and make it challenging to identify the problem's root cause. An arrangement like this is difficult to scale.


