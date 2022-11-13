# Distributed web infrastructure

![image](https://user-images.githubusercontent.com/95341497/201543412-0ef1b81a-0d33-4415-bba6-5bc16e83941f.png)

[distributed_web_infrastructure image](https://imgur.com/we0ehHc)

## Description

With the help of a server that balances the load between the two servers, this distributed web architecture tries to minimize the amount of traffic to the primary server by spreading some of the burden to a replica server (primary and replica).

## Specifics of the infrastructure

**What distribution algorithm your load balancer is configured with and how it works**
* The Round Robin distribution technique is specified in the HAProxy load balancer. According to their weights, the load balancer behind each server is used in turn by this method. Due to the fact that the servers' processing time is allocated equally, it is also likely the smoothest and most equitable method. Round Robin is a dynamic method that enables real-time modification of server weights.

**Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both?**
* An *Active-Passive* arrangement rather than a *Active-Active* setup is enabled by the HAProxy load-balancer. The load balancer divides workloads across all nodes in a *Active-Active* configuration to avoid any one node from becoming overwhelmed. There will also be a noticeable boost in throughput and response times since there will be more nodes ready to serve. On the other hand, not all nodes will be active in a "Active-Passive" arrangement (capable of receiving workloads at all times). When there are two nodes, the second node must be passive or in standby mode, for instance, if the first node is currently operational. If the preceding node is inactive, the second or following passive node may turn active.

**How a database Primary-Replica (Master-Slave) cluster works**
* In a "Primary-Replica" configuration, one server serves as the "Primary" server while the second server serves as a "Replica" of the "Primary" server. However, whereas the "Replica" server can only handle read requests, the "Primary" server can handle both read and write requests. When the *Primary* server performs a write operation, data is synced across the *Primary* 

**What is the difference between the Primary node and the Replica node in regard to the application?**
* The *Primary* node handles all of the site's write activities, while the *Replica* node may handle read operations, which reduces read traffic to the *Primary* node.

## Issues with the infrastructure

**Where are SPOF**
* There are several SPOFs (Single Point Of Failure). For instance, the entire site would be unable to make updates if the Primary MySQL database server went down (including adding or removing users). The load balancer server and the application server that connects to the main database server are both SPOFs.

**Security issues (no firewall, no HTTPS)**
* Due to the lack of an SSL certificate, hackers can monitor the network because the data being carried over it is not encrypted. No server has a firewall installed, thus there is no method to prevent illegitimate IP addresses from being used.

**No monitoring**
* Since they are not being watched, we have no means of knowing how each server is doing.


