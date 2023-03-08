# manifest enables the user 'holberton' to login and open files without error

exec { 'update-hard-file-limit':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => ['/usr/local/bin/', '/bin/']
}

exec { 'update-soft-file-limit':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => ['/usr/local/bin/', '/bin/']
}
