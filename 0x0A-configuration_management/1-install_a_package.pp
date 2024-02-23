#!/usr/bin/puppet
# We use shebang because script will be executed
# This file install flask from pip3 with Puppet
# With a specific version of flask

package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
}
