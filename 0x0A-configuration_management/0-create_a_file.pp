# Create a normal file if not exists  in /tmp

file { '/tmp/school':
    ensure  => 'present',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet',
}
