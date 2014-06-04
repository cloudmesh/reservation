"""
Usage:
    generate SERVERS RESERVATIONS DURATION

Arguments:
    SERVERS       Number of servers for which we generate reservations
    RESERVATIONS  Number of reservations per server
    DURATION      The maximum duration of a reservation (determined randomly)
    
"""

def generate(arguments):

    print arguments

    servers = arguments["SERVERS"]
    reservations = arguments["RESERVATIONS"]
    duration = arguments["DURATION"]

    for s in range(0,servers):
        t_start[s] = []
	    t_start[s][0] = random (0,duration)
       	t_end[s][0] = t_stat[s][0] + random (0,duration)
    for s in range(0,servers):
        for n in range(1,reservations):
            t_start[s][n] = t_end_[r,n-1] + random (0,duration)
            t_end[[s[n] = t_start[r][n] + random (0,duration)

	for s in range(0,servers):
        for n in range(0,reservations):
            print s, n, t_start[s][n], t_end[s][n]

    
if __name__ == '__main__':
    print(sys.argv)
    arguments = docopt(__doc__)

    generate(arguments)
