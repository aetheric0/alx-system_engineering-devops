# Kills the process with name 'killmenow'
exec {'Kills process killmenow':
  command => '/usr/bin/pkill killmenow',
}
