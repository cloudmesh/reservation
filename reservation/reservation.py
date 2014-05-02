#! /usr/bin/env python
"""
Usage:
    reservation -h | --help
    reservation --version
    reservation add [--start=TIME_START]
                    [--end=TIME_END]
                    LABEL
                    HOSTS
    reservation add --file=FILE
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
from datetime import datetime, timedelta
from docopt import docopt
import hostlist
from pytimeparse.timeparse import timeparse
# from timestring import Range
# from timestring import Date
from cloudmesh.util.util import parse_time_interval
from cloudmesh.util.util import yn_choice

def not_implemented():
    print "ERROR: not yet implemented"

def rain_command(arguments):

    for list in ["HOSTS", "IDS"]:
        try:
            expanded_list = hostlist.expand_hostlist(arguments[list])
            arguments[list]=expanded_list
        except:
            pass
        
    print(arguments)

    if arguments["add"] and arguments["--file"] is not None:

        print "add file"

    elif arguments["add"]:

        print "add"
        (time_start, time_end) = parse_time_interval(arguments["--start"],
                                                     arguments["--end"])
        print "From:", time_start
        print "To  :", time_end

    elif arguments["list"]:

        print "add"

        (time_start, time_end) = parse_time_interval(arguments["--start"],
                                                     arguments["--end"])
        print "From:", time_start
        print "To  :", time_end
        
    elif arguments["id"]:

        print "id"

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



if __name__ == '__main__':
    arguments = docopt(__doc__)

    rain_command(arguments)
    
