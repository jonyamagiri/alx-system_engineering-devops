# manifest configures Nginx server to increase the amount of traffic it can handle

exec { 'fix-nginx-config':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => ['/usr/local/bin/', '/bin/']
}

exec { 'restart-nginx':
  command     => 'nginx restart',
  path        => ['/etc/init.d/'],
  subscribe   => Exec['fix-nginx-config'],
  refreshonly => true
}
