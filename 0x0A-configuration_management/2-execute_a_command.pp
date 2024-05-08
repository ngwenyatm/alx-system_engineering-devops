# creates a manifest that kills a process named killmenow

exec { 'killmenow':
    command => 'pkill -9 -f killmenow',
    provider => 'shell',
    return => [0,1],
}
