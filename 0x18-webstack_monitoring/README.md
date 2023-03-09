## 0x18. Webstack monitoring

> This repository contains the tasks for `Webstack monitoring` project and a description of what each program or function does:

### Learning Objectives

    * Why is monitoring needed
    * What are the 2 main area of monitoring
    * What are access logs for a web server (such as Nginx)
    * What are error logs for a web server (such as Nginx)

* In this project, we will implement one of many tools to measure what is going on our servers. Web stack monitoring can be broken down into 2 categories:

1. Application monitoring: getting data about your running software and making sure it is behaving as expected
2. Server monitoring: getting data about your virtual or physical server and making sure they are not overloaded (could be CPU, memory, disk or network overload)


### Tasks

#### Task: 
* Sign up for Datadog. Install datadog-agent on `web-01`
* Create an `application key`
* Your server `web-01` should be visible in Datadog under the host name `XX-web-01`

#### Task: 
* Monitor some metrics. 
    * Set up a monitor that checks the number of read requests issued to the device per second.
    * Set up a monitor that checks the number of write requests issued to the device per second.

#### Task: 2-setup_datadog
* Create a new `dashboard`
* Add at least 4 `widgets` to your dashboard. They can be of any type and monitor whatever you’d like.
* Create the answer file `2-setup_datadog` which has the `dashboard_id` on the first line. 

____


