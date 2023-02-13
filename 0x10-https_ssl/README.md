## 0x10. HTTPS SSL

> This repository contains the tasks for `HTTPS SSL` project and a description of what each program or function does:

### Learning Objectives

    * What are the 2 main roles of HTTPS SSL?
    * What is the purpose encrypting traffic?
    * What SSL termination means?

What happens when you don’t secure your website traffic?

* When you don't secure your website traffic, sensitive information transmitted between the user's browser and your website's server can be intercepted and read by unauthorized parties. This information could include login credentials, financial information, and personal information. If this information is intercepted, it can be used for malicious purposes, such as identity theft, financial fraud, and unauthorized access to sensitive information.
* In addition, unsecured websites are vulnerable to attacks such as man-in-the-middle attacks, where an attacker intercepts the traffic between the user and the website and can modify the information being transmitted. This can result in the attacker being able to steal sensitive information, redirect users to a different website, or inject malicious code into the website.
* Moreover, unsecured websites can also be subject to various forms of malware, such as viruses and spyware. These can infect the user's computer, steal sensitive information, or cause other harm.
* Finally, unsecured websites may also be subject to various forms of online fraud, such as phishing attacks, where the attacker poses as a trusted entity in order to steal sensitive information.
* In summary, not securing your website traffic can have serious consequences, including the loss of sensitive information, the compromise of user privacy, and the possibility of being subject to various forms of online fraud and malware.

### Tasks

#### Task: 0-world_wide_web
* Configure your domain zone so that the subdomain `www` points to your load-balancer IP (`lb-01`). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.

#### Task: 1-haproxy_ssl_termination
* Create a certificate using `certbot` and configure `HAproxy` to accept encrypted traffic for your subdomain `www`.

#### Task: 100-redirect_http_to_https
* Configure HAproxy to automatically redirect HTTP traffic to HTTPS.

#### Task: 

___


