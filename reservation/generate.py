"""
Usage:
    generate [--json|--table|--calendar] SERVERS RESERVATIONS DURATION
    generate clean
    
Arguments:
    SERVERS       Number of servers for which we generate reservations
    RESERVATIONS  Number of reservations per server
    DURATION      The maximum duration of a reservation (determined randomly)
    
"""
import sys
from docopt import docopt
import hostlist
from pprint import pprint
from random import randint
from model import Reservation

def generate(arguments):

    print arguments

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
            print "server={0}, cm_id={1}, start_time={2}, end_time={3}" \
              .format(servers[s], "cm_reservation-" + str(s) + "-" + str(n), str(t_start[s][n]), str(t_end[s][n]))
            r = Reservation(label="exp1",
                            cm_id="cm_reservation-" \
                                   + str(s) + "-" + str(n), 
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
