## 0x0B. SSH

> This repository contains the tasks for `SSH` project and a description of what each program or function does:

### Learning Objectives

* What is a server
* Where servers usually live
* What is SSH
* How to create an SSH RSA key pair
* How to connect to a remote host using an SSH RSA key pair
* The advantage of using **#!/usr/bin/env bash** instead of **/bin/bash**

### Tasks

#### Task: 0-use_a_private_key
* Write a Bash script that uses `ssh` to connect to your server using the private key `~/.ssh/school` with the user `ubuntu`.
    * Only use `ssh` single-character flags
    * You cannot use `-l`

#### Task: 1-create_ssh_key_pair
* Write a Bash script that creates an RSA key pair.
    * Name of the created private key must be `school`
    * Number of bits in the created key to be created 4096
    * The created key must be protected by the passphrase `betty`

#### Task: 2-ssh_config
* Your machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.
    * Your SSH client configuration must be configured to use the private key `~/.ssh/school`
    * Your SSH client configuration must be configured to refuse to authenticate using a password

#### Task: 
* Now that you have successfully connected to your server, we would also like to join the party.
    * Add the SSH public key provided to your server so that we can connect using the `ubuntu` user.


___


