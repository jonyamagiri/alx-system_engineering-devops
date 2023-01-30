## 0x13. Firewall

> This repository contains the tasks for `Firewall` project and a description of what each program or function does:

### Learning Objectives

* A firewall is a network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules. It acts as a barrier between a private internal network and the public Internet, protecting the network from unauthorized access and potential cyber threats.

### Tasks

#### Task: 0-block_all_incoming_traffic_but
Install the `ufw` firewall and setup a few rules on `web-01`.
* Configure `ufw` so that it blocks all incoming traffic, except the following TCP ports:
	*  `22` (SSH)
	*  `443` (HTTPS SSL)
	*  `80` (HTTP)
Share the `ufw` commands that you used in your answer file

#### Task: 100-port_forwarding
Firewalls can not only filter requests, they can also forward them.
* Configure `web-01` so that its firewall redirects port `8080/TCP` to port `80/TCP`.
* Your answer file should be a copy of the `ufw` configuration file that you modified to make this happen

___


