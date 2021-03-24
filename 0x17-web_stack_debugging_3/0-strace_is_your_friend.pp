# Using strace, find out why Apache is returning a 500 error
exec { 'settingFix':
  command  => 'sed -i "s/\b.phpp\b/.php/g" /var/www/html/wp-settings.php',
  provider => shell,
}
