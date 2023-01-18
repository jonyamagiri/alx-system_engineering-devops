# Puppet manifest that installs and configures Nginx web server

package { 'nginx':
  ensure => installed,
}

file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => "listen 80 default_server;\nrewrite ^/redirect_me https://www.youtube.com permanent;",
}

file { '/var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World!',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
