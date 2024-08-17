# Corrects the Internal Server Error on localhost due to misspelt file
exec {'fix-internal-server-error':
command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
path    => '/usr/local/bin/:/bin/'
}