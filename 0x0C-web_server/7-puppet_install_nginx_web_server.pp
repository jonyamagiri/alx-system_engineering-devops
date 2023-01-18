# Puppet manifest that installs and configures Nginx web server

package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

file_line { 'redirect':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com permanent;',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
