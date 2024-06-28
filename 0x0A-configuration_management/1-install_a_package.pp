# Installs the flask package using pip3
exec {'Install flask using pip3':
  command => '/usr/bin/pip3 install Flask==2.1.0',
}
