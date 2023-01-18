## 0x0C. Web server

> This repository contains the tasks for `Web server` project and a description of what each program or function does:

### Learning Objectives

* What is the main role of a web server
* What is a child process
* Why web servers usually have a parent process and child processes
* What are the main HTTP requests
* What DNS stands for
* What is DNS main role

### Tasks

#### Task: 0-transfer_file
Write a Bash script that transfers a file from our client to a server:
* Accepts 4 parameters
    * The path to the file to be transferred
    * The IP of the server we want to transfer the file to
    * The username `scp` connects with
    * The path to the SSH private key that scp uses
* Display Usage: `0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY` if less than 3 parameters passed
* `scp` must transfer the file to the user home directory `~/`
* Strict host key checking must be disabled when using `scp`

#### Task: 1-install_nginx_web_server
Web servers are the piece of software generating and serving HTML pages:
* Install `nginx` on `web-01` server
* Nginx should be listening on port 80
* When querying Nginx at its root `/` with a GET request (requesting a page) using `curl`, it must return a page that contains the string `Hello World!`
* As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements.
* You can’t use `systemctl` for restarting nginx.

#### Task: 2-setup_a_domain_name
* Set up and provide the domain name only (example: `foobar.tech`), no subdomain (example: `www.foobar.tech`)
* Configure your DNS records with an A entry so that your root domain points to your web-01 IP address.

#### Task: 3-redirection
Configure your Nginx server so that /redirect_me is redirecting to another page.
* The redirection must be a `“301 Moved Permanently”`
* You answer file should be a Bash script containing commands to automatically configure a Ubuntu machine to respect above requirements
* Using what you did with `1-install_nginx_web_server`, write `3-redirection` so that it configures a brand new Ubuntu machine to the requirements asked in this task

#### Task: 4-not_found_page_404
Configure your Nginx server to have a custom 404 page that contains the string `Ceci n'est pas une page`.
* The page must return an HTTP 404 error code
* The page must contain the string `Ceci n'est pas une page`
* Using what you did with `3-redirection`, write `4-not_found_page_404` so that it configures a brand new Ubuntu machine to the requirements asked in this task

#### Task: 7-puppet_install_nginx_web_server.pp
Install and configure an Nginx server using Puppet instead of Bash. You should also include resources in your manifest to perform a 301 redirect when querying /redirect_me.
* Nginx should be listening on port 80
* When querying Nginx at its root `/` with a GET request (requesting a page) using `curl`, it must return a page that contains the string `Hello World!`
* The redirection must be a “301 Moved Permanently”

___


