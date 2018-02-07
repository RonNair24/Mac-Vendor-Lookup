#!/usr/bin/python

#Author: Ron Nair
#Date: 08/02/2018
#Email: joutei@icloud.com
#Version: 1.0


import urllib2, os

while True:

    print('\n >>> Please enter the mac address: ')
    macInput = raw_input()

    print('\n >>> Mac Address Vendor: ')

    os.system('curl http://api.macvendors.com/' + macInput)

    print('\n')
    inp = raw_input('\n >>> Would you like to check another mac address? (y/n): ')
    if(inp == "y" or inp == "Y"):
      continue
    else:
      print '\n Ciao!\n'
      break
