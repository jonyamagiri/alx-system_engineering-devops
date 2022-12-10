# using Puppet to make changes to configuration file
# SSH client configured to use the private key ~/.ssh/school
# SSH client configured to refuse to authenticate using a password

exec { 'echo "PasswordAuthentication no\nIdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config':
        path    => '/bin/'
}
