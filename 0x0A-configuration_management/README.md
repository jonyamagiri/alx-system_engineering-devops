## 0x0A. Configuration management

> This repository contains the tasks for `0x0A. Configuration management` project and a description of what each program or function does:

### Introduction

* Configuration management [CM](https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management) is the act of methodically addressing system changes in a way that ensures the system retains integrity over time.
* In server configuration management, automation is crucial. It's the process by which a server is brought to a desired condition that was previously specified by provisioning scripts written in a particular language and with a certain set of capabilities.
* Numerous configuration management tools are offered on the market. Popular options include Puppet, Ansible, Chef, and Salt. While every tool will have unique traits and operate in somewhat different ways, they are all motivated by the same goal: to confirm that the system's state corresponds to the state specified by your provisioning scripts.

### Tasks

#### Task: 0-create_a_file.pp
Using Puppet, create a file in `/tmp`.
* Requirements: File path is `/tmp/school`. File permission is `0744`. File owner is `www-data`. File group is `www-data`. File contains `I love Puppet`.

#### Task: 1-install_a_package.pp
Using Puppet, install `flask` from `pip3`.
* Requirements: Install `flask`. Version must be `2.1.0`.

#### Task: 2-execute_a_command.pp
Using Puppet, create a manifest that kills a process named `killmenow`.
* Requirements: Must use the `exec` Puppet resource. Must use `pkill`.

___

