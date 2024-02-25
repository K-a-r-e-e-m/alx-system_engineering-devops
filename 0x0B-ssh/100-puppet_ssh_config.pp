# This script makes changes to our configuration file with puppet.
class { 'ssh':
    storeconfigs_enabled => false,
    server_options       => {
        PasswordAuthentication => no,
        IdentityFile           => '~/.ssh/school',
    }
}
