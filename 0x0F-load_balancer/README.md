## 0x0F. Load balancer

> This repository contains the tasks for `Load balancer` project and a description of what each program or function does:

### Learning Objectives

* We have been given 2 additional servers:
    * gc-[STUDENT_ID]-web-02-XXXXXXXXXX
    * gc-[STUDENT_ID]-lb-01-XXXXXXXXXX
    
* We'll improve our web stack so that there is redundancy for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

* For this project, I'll write Bash scripts to automate the work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.

### Tasks

#### Task: 0-custom_http_response_header
You need to configure `web-02` to be identical to `web-01`:
* Configure Nginx so that its HTTP response contains a custom header (on `web-01` and `web-02`)
    * The name of the custom HTTP header must be `X-Served-By`
    * The value of the custom HTTP header must be the hostname of the server Nginx is running on

#### Task: 1-install_load_balancer
Install and configure HAproxy on your `lb-01` server.
* Configure HAproxy so that it send traffic to `web-01` and `web-02`
* Distribute requests using a roundrobin algorithm
* Make sure that HAproxy can be managed via an init script
* Make sure that your servers are configured with the right hostnames: `[STUDENT_ID]-web-01` and `[STUDENT_ID]-web-02`.
* Write a Bash script that configures a new Ubuntu machine to respect above requirements

#### Task: 2-puppet_custom_http_response_header.pp
Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.
* The name of the custom HTTP header must be `X-Served-By`
* The value of the custom HTTP header must be the hostname of the server Nginx is running on
* Write `2-puppet_custom_http_response_header.pp` so that it configures a brand new Ubuntu machine to the requirements asked in this task

___


