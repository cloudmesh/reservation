"""
Usage:
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

"""
import sys
from docopt import docopt
import hostlist
from pprint import pprint
from random import randint
from model import Reservation

def generate(arguments):

    print arguments

    if arguments['clean']:
        print "ERROR: delete all entries is not yet implemented."
        
    else:

        reservations = int(arguments["RESERVATIONS"])
        duration = int( arguments["DURATION"])
        server_string = arguments["SERVERS"]
        servers = hostlist.expand_hostlist(server_string)

        print 70 * "="
        print servers
        print reservations
        print duration
        print 70 * "="

        t_start = {}
        t_end = {}
        for s in xrange(0, len(servers)):
            t_start[s] = []
            t_end[s] = []        
            t_start[s].append(randint(0, duration))
            t_end[s].append(t_start[s][0] + randint(0, duration))

        for s in range(0, len(servers)):
            for n in range(1, reservations):
                t_start[s].append(t_end[s][n - 1] + randint(0, duration))
                t_end[s].append(t_start[s][n] + randint(0, duration))

        for s in range(0, len(servers)):
            for n in range(0, reservations):
                print s, n, t_start[s][n], t_end[s][n]

        pprint ("start: " + str(t_start))
        pprint ("end  : " + str(t_end))    

        for s in range(0, len(servers)):
            for n in range(0, reservations):
                cm_id = "cm_reservation-" + str(s) + "-" + str(n)
                print "server={0}, cm_id={1}, start_time={2}, end_time={3}" \
                  .format(servers[s], cm_id, str(t_start[s][n]), str(t_end[s][n]))
                r = Reservation(label="exp1",
                                cm_id=cm_id,
                                summary = "test1",
                                host=servers[s],
                                user="gregor",
                                project="fg82",
                                start_time=str(t_start[s][n]), 
                                end_time=str(t_end[s][n])
                    )

        print 70 * "A"
        reservations = Reservation.objects(user="gregor")
        print 70 * "B"

        for reservation in reservations:
            print reservation

if __name__ == '__main__':
    print(sys.argv)
    arguments = docopt(__doc__)

    generate(arguments)
