#! /usr/bin/env python
"""
Usage:
    generate -h | --help | --rst
    generate clean
    generate SERVERS RESERVATIONS DURATION START
    generate list [--json|--table|--calendar]

Arguments:
    SERVERS       Number of servers for which we generate 
                  reservations
    RESERVATIONS  Number of reservations per server
    DURATION      The maximum duration of a reservation 
    		      (determined randomly)
    START         The start date. if now is specified, the current
    		      time is used, otherwise an offset is used in the
    		      form of 1m, or 1h, or 1w[default: now]

Description:

    This program generates a number of reservations so they can be
    used to test the reservation package.

    generate clean
        deletes all reservations from the reservation database

    generate SERVERS RESERVATIONS DURATION
        generates a number of reservations where the servers are
        specified as hostlist (e.g. i[001-003]. The reservations
        specifies how many reservations there will be for each
        server. The duration is a random number between [0,duration]
        that specified not only a duration, but also the time delta
        between two reservations on the same host.

    generate list
        retiurns the list of reservations in the specified
        format. Thoe format can be list, table, or calendar

Bugs:
    Not implemented:

    * clean 
    * list
    * the generation function does not yet have a start date

See Also:
    * https://pypi.python.org/pypi/pytimeparse/1.1.0

"""
import sys
from docopt import docopt
import hostlist
from pprint import pprint
from random import randint
from pytimeparse.timeparse import timeparse
import datetime
from model import Reservation
from model import reservation_connect

def generate(arguments):

    if arguments['clean']:

        db = reservation_connect()
        reservations = Reservation.objects({})
        print "deleting:"
        for reservation in reservations:
            print reservation.label,
            reservation.delete()
        print
        
    elif arguments["--rst"]:

        print "generate"
        print 70 * "="
        print "\n::\n"
        lines = __doc__.split("\n")
        for line in lines:
            print "  ", line

    else:

        reservations = int(arguments["RESERVATIONS"])
        duration = int(arguments["DURATION"])
        server_string = arguments["SERVERS"]
        servers = hostlist.expand_hostlist(server_string)
        if arguments["START"] in ["now"]:
            first_time = datetime.datetime.now()
        else:
            first_time = timeparse(arguments("START"))

        print 70 * "="
        print "Servers:     ", servers
        print "Reservations:", reservations
        print "Duration:    ", duration
        print "First date:  ", first_time
        print 70 * "="

        db = reservation_connect()        

        def random_delta(duration):
            r = randint(0, duration)
            return datetime.timedelta(seconds=timeparse("{0} h".format(r)))
        
        t_start = {}
        t_end = {}
        for s in xrange(0, len(servers)):
            t_start[s] = []
            t_end[s] = []
            
            t_start[s].append(first_time + random_delta(duration))
            t_end[s].append(t_start[s][0] + random_delta(duration))

        for s in range(0, len(servers)):
            for n in range(1, reservations):
                t_start[s].append(t_end[s][n - 1] + random_delta(duration))
                t_end[s].append(t_start[s][n] +  random_delta(duration))

        #for s in range(0, len(servers)):
        #    for n in range(0, reservations):
        #        print s, n, t_start[s][n], t_end[s][n]

        #pprint("start: " + str(t_start))
        #pprint("end  : " + str(t_end))

        for s in range(0, len(servers)):
            for n in range(0, reservations):
                entry = {
                    "cm_id": "cm_reservation-{0}-{1}".format(s,n),
                    "label": "exp-{0}-{1}".format(s,n),
                    "summary": "task-{0}-{1}".format(s,n),
                    "host": servers[s],
                    "user": "gregor",
                    "project" : "fg82",
                    "start_time": str(t_start[s][n]),
                    "end_time": str(t_end[s][n]),
                    }

                print entry
                r = Reservation(
                    cm_id=entry["cm_id"],
                    host=entry["host"],
                    label=entry["label"],
                    user=entry["user"],
                    summary=entry["summary"],                    
                    project=entry["project"],
                    start_time=entry["start_time"],
                    end_time=entry["end_time"]
                    )
                r.save()

        print 70 * "A"
        reservations = Reservation.objects()
        print len(reservations)
        for reservation in reservations:
           pprint(reservation)
        print 70 * "B"

        for reservation in reservations:
            print reservation

if __name__ == '__main__':
    arguments = docopt(__doc__)

    generate(arguments)
