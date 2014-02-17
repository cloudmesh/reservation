#!/usr/bin/env python

"""Example of program with many options using docopt.

Usage:
  reservation_client.py list
  reservation_client.py list --label=LABEL
  reservation_client.py add --label=LABEL --from=FROM --to=TO --service=SERVICE
  reservation_client.py delete --label=LABEL
  
Arguments:
  FROM     date from which the reservation lasts
  TO       date to which the reservation lasts
  LABEL    label associated with the reservation
  SERVICE  the name of the service
  
Options:
  -h --help            show this help message and exit
  --version            show version and exit
  -v --verbose         print status messages
  -q --quiet           report only file names
  --server=SERVER      speifies the server
  --to=TO              speifies the date to which the reservation is set
  --from=FROM          speifies the date from which the reservation is set
  --label=LABEL        speifies the label for the reservation
  --delete=LABEL    deletes all reservations with the given LABEL

Description:

  describe here what the commands do
   
  reservation_client.py list
    
    prints out all reservations
        
  reservation_client.py list myRes
    
    prints out all reservations with the lable myRes
        
  reservation_client.py delete --label=myRes
  
      deletes all reservations with the label myRes
      
  reservation_client.py add --label=myRes --from="01/01/2014:13:00:30" --to="02/01/2014:13:00:45" --service=SERVICE
   
      adds a reservation with the label myRes starting January 1st 2013 1pm and 30 seconds till February 1st, 2014 1pm and 45 seconds
    
"""

from docopt import docopt
import requests
import pprint

class ReservationClient:
    
    def __init__(self, argdict):
        print "not yet implemented"
        
    def run(self):
        print "not yet implemented"

    def add(self,
            res_from,
            res_to,
            res_label,
            res_service):
        """adding a reservation"""
        print "not yet implemented"

    def delete(self,
            res_label):
        """adding a reservation"""
        print "not yet implemented"
            
if __name__ == '__main__':
    arguments = docopt(__doc__, version='1.0')
    gclient = ReservationClient(arguments)
    gclient.run()

