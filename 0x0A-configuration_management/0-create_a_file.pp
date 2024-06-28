# Creates the file '/tmp/school' with permissions 744 and writes the content 'I love Puppet'
file {'/tmp/school':
  ensure  => 'present',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}