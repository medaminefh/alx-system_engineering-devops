# Create a file in tmp
file { '/tmp/school':
  ensure  => 'file',          # Ensure that it is a file
  mode    => '0744',          # File permissions
  owner   => 'www-data',      # Owner
  group   => 'www-data',      # Group
  content => 'I love Puppet', # Content of the file
}
