#!/usr/bin/pup
# install flask from pip3 Using puppet

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
