# This manifest installs flask package 2.1.0 from pip3.

package { 'Python3.8':
  ensure   => '3.8.10',
  provider => 'pip3',
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Package['Flask'],
}
