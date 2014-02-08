#! /usr/bin/python
#A program to try and make my life easier

from sys import argv

script, filename = argv

print "This will create and potentially destroy %r. Are you sure you want to do this?" % filename
print "Press Ctrl + C anytime to quit"
print "Opening the file..."
target = open(filename, 'w')

#Destroy the file
target.truncate()

#Get input from user
print"What is the group of this server?"
server_group = raw_input('Server group: ')
print "What is the IP address of the server?"
server_ip = raw_input('IP address: ')
print"What is the alias of this server?"
server_alias = raw_input('Server alias: ')
print"What is the hostname of this server?"
server_hostname = raw_input('Server hostname: ')

print "Writing to file now..."

target.write('define host{')
target.write("\n")
target.write('      use                     generic-host            ; Inherit default values from a template')
target.write("\n")
target.write('      host_name               '+server_hostname+'        ; The name we are giving to this host')
target.write("\n")
target.write('      alias                   '+server_alias+'          ; A longer name associated with the host')
target.write("\n")
target.write('      address                 '+server_ip+'             ; IP address of the host')
target.write("\n")
target.write('      hostgroups              '+server_group+'          ; Host groups this host is associated with')
target.write("\n")
target.write('      check_command           check-host-alive')
target.write("\n")
target.write('      max_check_attempts      4')
target.write("\n")
target.write('      check_period            24x7')
target.write("\n")
target.write('      contacts                nagiosadmin')
target.write("\n")
target.write('      contact_groups          admins')
target.write("\n")
target.write('      notification_interval   30')
target.write("\n")
target.write('      notification_period     24x7')
target.write("\n")
target.write('      }')
target.write("\n")
target.write("\n")

target.write('define service{')
target.write("\n")
target.write('  use                     generic-service         ; Inherit default values from a template')
target.write("\n")
target.write('  host_name               '+server_hostname)
target.write("\n")
target.write('  service_description     Uptime')
target.write("\n")
target.write('  check_command           check_snmp!-C public -o sysUpTime.0')
target.write("\n")
target.write('  }')
target.write("\n")
target.write("\n")

target.write('define service{')
target.write("\n")
target.write('  use                     generic-service         ; Inherit default values from a template')
target.write("\n")
target.write('  host_name               '+server_hostname)
target.write("\n")
target.write('  service_description     Hard Drive')
target.write("\n")
target.write('  check_command           check_disk_snmp!-s public -w 85% -c 90% -d C #change this to / for Linux servers')
target.write("\n")
target.write('  }')
target.write("\n")
target.write("\n")

target.write('define service{')
target.write("\n")
target.write('  use                     generic-service         ; Inherit default values from a template')
target.write("\n")
target.write('  host_name               '+server_hostname)
target.write("\n")
target.write('  service_description     CPU Load')
target.write("\n")
target.write('  check_command           check_snmp_load!-C public -w 85% -c 90%')
target.write("\n")
target.write('  }')
target.write("\n")
target.write("\n")


print "Write sucessfully complete!!!"
