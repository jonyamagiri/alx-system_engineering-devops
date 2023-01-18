# Puppet manifest that installs and configures Nginx web server

# install Nginx
package { 'nginx':
  ensure => installed,
}

# configure welcome page
file { '/var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World!',
}

# configure redirection
file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => "listen 80 default_server;\nrewrite ^/redirect_me https://www.youtube.com permanent;",
}

# Nginx restart
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
