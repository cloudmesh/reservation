#! /usr/bin/env python
"""
Usage:
    reservation -h | --help
    reservation login
    reservation --rst
    reservation --version
    reservation add [--start=TIME_START]
                    [--end=TIME_END]
                    LABEL
                    HOSTS
    reservation add --file=FILE
    reservation remove --reservation_id=RESERVATION_ID
    reservation remove_all
    reservation get_all
    reservation get_from_label --label=LABEL
    reservation get_by_user --user_id=USER_ID
    reservation reschedule --reservation_id=RESERVATION_ID --file=FILE
    reservation get_from_id --reservation_id=RESERVATION_ID
    reservation duration --reservation_id=RESERVATION_ID
    reservation list_by_project --proj_id=PROJ_ID
    reservation list_by_user_and_project --user_id=USER_ID --proj_id=PROJ_ID --start=TIME_START --end=TIME_END
    reservation list [--start=TIME_START]
                     [--end=TIME_END]
                     [--format=FORMAT]
    reservation id (LABELS|IDS)
    reservation [-i] rm (LABELS|IDS)
    reservation [-i] delete (LABELS|IDS)     
    
Arguments:
    ID        the unique ID of the reservation
    LABEL     the label of a host
    
Options:
    --label=LABEL  the label pf the reservation
    -f FILE, --file=FILE  file to be specified
    --reservation_id=RESERVATION_ID                RESERVATION_ID
    --user_id=USER_ID                USER_ID
    --proj_id=PROJ_ID                PROJ_ID
    -i           interactive mode adds a yes/no 
                 question for each host specified
    --start=TIME_START     Start time of the reservation, in 
                           YYYY/MM/DD HH:MM:SS format. [default: current_time]
    --end=TIME_END         End time of the reservation, in 
                           YYYY/MM/DD HH:MM:SS format. In addition a duration
                           can be specified if the + sign is the first sign.
                           The duration will than be added to
                           the start time. [default: +1d]
    --format=FORMAT        Format of the output json, cfg. [default:json]
"""

from cloudmesh_install import config_file


from datetime import datetime, timedelta
from docopt import docopt
from reservation_client import ReservationClient
import hostlist
from pytimeparse.timeparse import timeparse
# from timestring import Range
# from timestring import Date

from cloudmesh_common.tables import parse_time_interval
from cloudmesh_common.util import yn_choice
import textwrap
import argparse
import os
import sys  
import httplib2
import json
from apiclient import discovery
from oauth2client import file
from oauth2client import client
from oauth2client import tools



def not_implemented():
    print "ERROR: not yet implemented"

def rain_command(arguments):
    if arguments["--rst"]:

        print 70*"*"
        print "Manual Pages"
        print 70*"*"
        print
        print "reservation"        
        print 70*"="
        print "\n::\n"        
        lines = __doc__.split("\n")
        for line in lines:
            print "  ", line

    elif arguments["--version"]:

        not_implemented()
    elif arguments["login"]:
        try:
            os.system('cm-reservation-login')
        except Exception, e:
            print "Could not find the command cm-reservation-login. Make sure the cloudmesh code is properly installed."

    else:
        
        for list in ["HOSTS", "IDS"]:
            try:
                expanded_list = hostlist.expand_hostlist(arguments[list])
                arguments[list]=expanded_list
            except:
                pass

        #print(arguments)

        try:
            
            reservation = get_service_object()

        except Exception, e:
            print "ERROR: could not connect to the calendar service"

            print
            print e
            print
            sys.exit(1)
            
        if arguments["add"] and arguments["--file"] is not None:

            print "add file"
            try:
                with open(arguments["--file"]) as json_file:
                    json_data = json.load(json_file)
                    reservation.add(json_data)
            except:
                print "File doesn't exist"
            print reservation.get_all()
        elif arguments["add"]:

            print "add"
            (time_start, time_end) = parse_time_interval(arguments["--start"],
                                                         arguments["--end"])
            print "From:", time_start
            print "To  :", time_end

        elif arguments["list"]:

            print "list"

            (time_start, time_end) = parse_time_interval(arguments["--start"],
                                                         arguments["--end"])
            print "From:", time_start
            print "To  :", time_end

        elif arguments["id"]:

            print "id"
            
        elif arguments["remove_all"]:
            print "Remove all reservations from calendar"
            reservation.remove_all()
            
        elif arguments["remove"]:
            print "Removed the reservation from calendar"
            reservation.remove(arguments["--reservation_id"])
            
        elif arguments["get_from_id"]:
            print "Reservation object from calendar by id"
            print reservation.get_from_id(arguments["--reservation_id"])
            
        elif arguments["get_from_label"]:
            print "Reservation object from calendar by label"
            print reservation.get_from_label(arguments["--label"])
            
        elif arguments["get_by_user"]:
            print "Reservation object from calendar by user"
            print reservation.get_by_user(arguments["--user_id"])
            
        elif arguments["list_by_project"]:
            print "Reservation object from calendar by project"
            print reservation.list_by_project(arguments["--proj_id"])
            
        elif arguments["list_by_user_and_project"]:
            print "Lists all the users reservations made in a project from a start-time to a end time"
            list = reservation.list_by_user_and_project(arguments["--user_id"], arguments["--proj_id"], arguments["--start"], arguments["--end"])
            for value in list:
                print value
                print "************************************************************"
            
        elif arguments["get_all"]:

            print "Get all reservations from calendar"
            list = reservation.get_all()
            for value in list:
                for key, value in value.iteritems():
                    if isinstance(value, dict):
                        for key, value in value.iteritems():
                            print key,'\t', value
                    else:
                        print key,'\t\t', value
                            #print value
                        print "************************************************************"

        elif arguments["reschedule"]:
            print "Reschedule reservation"
            try:
                with open(arguments["--file"]) as json_file:
                    json_data = json.load(json_file)
                    reservation.reschedule(arguments["--reservation_id"], json_data)
            except:
                print "File doesn't exist"
                
        elif arguments["duration"]:
            print "Shows the duration of the reservation"
            print reservation.duration(arguments["--reservation_id"])
            

        elif arguments["delete"] or arguments["rm"] :
            """rain [-i] delete LABELS"""
            """rain [-i] rm LABELS"""            

            interactive = arguments["-i"]

            print "delete", interactive

            for label in arguments["LABELS"]:
                if interactive:
                    keep = yn_choice("Do you want to delete the reservation <%s>?" % label)
                    if keep:
                        print "delete %s" % label
                    else:
                        print "keeping %s" % label
            not_implemented()


def get_service_object():
    '''Get calendar object'''
    storage = file.Storage('reservation_config.dat')
    credentials = storage.get()
    # Create an httplib2.Http object to handle our HTTP requests and authorize it
    # with our good Credentials.
    http = httplib2.Http()
    http = credentials.authorize(http)
    
    # Construct the service object for the interacting with the Calendar API.
    service = discovery.build('calendar', 'v3', http=http)
    reservation = ReservationClient(service)
    return reservation


if __name__ == '__main__':
    print(sys.argv)
    arguments = docopt(__doc__)

    rain_command(arguments)
    
