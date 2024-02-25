# This script makes changes to our configuration file with puppet.
imoprt stdlib

file_line { 'Turn off passwd auth': # Title of puppet resource (uniqe)
    ensure  => present,
    path    => '/etc/ssh/ssh_config', # Path of file will be modefied
    line    => '    PasswordAuthentication no', # Line if exists in file
    replace => true # If PasswordAuthentication yes replace it with no
}

file_line { 'Delare identity file': # Title of puppet resource (uniqe)
    ensure  => 'resent,
    path    => '/etc/ssh/ssh_config',
    line    => '    IdentityFile ~/.ssh/school',
    replace => true
}
