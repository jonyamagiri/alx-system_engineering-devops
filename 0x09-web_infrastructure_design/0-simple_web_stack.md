# Simple web stack

## Description

This is a basic web infrastructure hosting a website that can be accessed by typing "www.foobar.com" into the address bar. The network of the server is not secured by SSL certificates or firewalls. The server's resources (CPU, RAM, and SSD) must be shared by each component (database, application server).

## Specifics of the infrastructure

**What is a server?**
* The term "server" refers to a piece of computer hardware or software that offers services to other computers, often known as clients.

**What is the role of the domain name?**
* The purpose of domain names is to give text-based labels—rather to the numerical addresses used in Internet protocols—to identify Internet resources, such as computers, networks, and services.

**What type of DNS record `www` is in `www.foobar.com`?**
* `www.foobar.com` uses an A record. This can be checked by running `dig www.foobar.com` (the results might be different but for the infrastructure in this design, an A record is used). A hostname and its matching IPv4 address are stored in an Address Mapping record (A Record), commonly referred to as a DNS host record.

**What is the role of the web server?**
* A web server's main responsibility is to store, process, and transmit to end users any requested data or webpages. It employs Physical Storage: To maintain the security of website data, all data is kept on a physical web server.

**What is the role of the application server?**
* Application servers serve as hosts (or containers) for user business logic, easing access to and performance of the business application.

**What is the role of the database?**
* To maintain a collection of organized information that can easily be accessed, managed and updated

**What is the server using to communicate with the computer of the user requesting the website?**
* The TCP/IP protocol suite is used to facilitate communication between the client and the server via the internet network.


## Issues with the infrastructure

**SPOF**
* This infrastructure contains several SPOFs (Single Points of Failure). For example, failure of the application server leads to inaccessibility of the site.

**Downtime when maintenance needed (like deploying new code web server needs to be restarted)**
* The server must be shut down or any component shut down when we need to do maintenance checks on it. There is just one server, thus there would be a downtime on the website.

**Cannot scale if too much incoming traffic**
* Because all the necessary components are on a single server, scaling this system would be challenging. When the server starts getting a lot of requests, it may rapidly run out of resources or begin to slow down.


