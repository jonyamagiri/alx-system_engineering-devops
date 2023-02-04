## 0x14. MySQL

> This repository contains the tasks for `MySQL` project and a description of what each program or function does:

### Learning Objectives

    * What is the main role of a database?
    * What is a database replica?
    * What is the purpose of a database replica?
    * Why database backups need to be stored in different physical locations?
    * What operation should you regularly perform to make sure that your database backup strategy actually works?

* A database is a collection of data stored in an organized way to allow for efficient retrieval and manipulation of the data. The main role of a database is to provide a centralized repository for data that can be easily accessed, managed and updated.
* A database replica is a copy of a database that is stored on a separate server. The purpose of having a replica is to provide a backup of the data in case the primary database fails, as well as to distribute the load of incoming requests to multiple servers, improving performance and ensuring high availability.

### Tasks

#### Task: 0-world_wide_web
* Configure your domain zone so that the subdomain `www` points to your load-balancer IP (`lb-01`). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.

#### Task: 
* First things first, let’s get MySQL installed on both your web-01 and web-02 servers.
* MySQL distribution must be 5.7.x

#### Task: 
* Create a MySQL user named `holberton_user` on both `web-01` and `web-02` with the host name set to `localhost` and the password `projectcorrection280hbtn`. This will allow us to access the replication status on both servers.

#### Task: 
* Create a database named `tyrell_corp`.
* Within the `tyrell_corp` database create a table named `nexus6` and add at least one entry to it.

#### Task: 
* On your primary MySQL server (web-01), create a new user for the replica server.
* The name of the new user should be `replica_user`, with the host name set to `%`, and can have whatever password you’d like.
* `replica_user` must have the appropriate permissions to replicate your primary MySQL server.

#### Task: 4-mysql_configuration_primary, 4-mysql_configuration_replica
* MySQL primary must be hosted on `web-01` - do not use the `bind-address`, just comment out this parameter
* MySQL replica must be hosted on `web-02`
* Setup replication for the MySQL database named `tyrell_corp`
* Provide your MySQL primary configuration as answer file(`my.cnf` or `mysqld.cnf`) with the name `4-mysql_configuration_primary`
* Provide your MySQL replica configuration as an answer file with the name `4-mysql_configuration_replica`

#### Task: 5-mysql_backup
* Write a Bash script that generates a MySQL dump and creates a compressed archive out of it.

___


