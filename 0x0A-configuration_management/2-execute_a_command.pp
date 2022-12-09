# creates a manifest that kills a process named killmenow; 
# must use the exec Puppet resource and pkill

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
  path     => '/usr/bin';
}
