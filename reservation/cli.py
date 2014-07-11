from model import Reservation
from mongoengine import *
from docopt import docopt

def reservation_connect():
    try:
        db = connect('reservation', port=27777)
        return db
    except Exception, e:
        print "ERROR: could not establish a connection to mongo db"
        print e
    

def rain_command(arguments):
    """
    Usage:
        reservation find [all]
                         [--user=USER_ID]
                         [--label=ID]
                         [--cm_id=ID]
        reservation list [--cm_id=CM_ID]
                         [--user=USER_ID]
                         [--project=PROJECT_ID]
                         [--label=STRING]
                         [--start=TIME_START]
                         [--end=TIME_END]
                         [--host=HOST]
                         [--summary=SUMMARY]
        reservation duration [--cm_id=CM_ID]
        reservation delete [all]
                           [--cm_id=CM_ID]
                           [--user=USER_ID]
                           [--project=PROJECT_ID]
                           [--label=STRING]
                           [--start=TIME_START]
                           [--end=TIME_END]
                           [--host=HOST]
        reservation update [--cm_id=CM_ID]
                           [--user=USER_ID]
                           [--project=PROJECT_ID]
                           [--label=STRING]
                           [--start=TIME_START]
                           [--end=TIME_END]
                           [--host=HOST]
                           [--summary=SUMMARY]
                           [--cm_id=CM_ID]
                           [--user=USER_ID]
                           [--project=PROJECT_ID]
                           [--label=STRING]
                           [--start=TIME_START]
                           [--end=TIME_END]
                           [--host=HOST]
                           [--summary=SUMMARY]
        reservation add --cm_id=CM_ID
                        --user=USER_ID
                        --project=PROJECT_ID
                        --label=STRING
                        --start=TIME_START
                        --end=TIME_END
                        --host=HOST
                        --summary=SUMMARY
        reservation addFile --file=FILE

    Arguments:
        --label=STRING    label id reservation
        --cm_id=CM_ID    reservation cloudmesh id
        --user=USER_ID    user id
        --project=PROJECT_ID    project id
        --start=TIME_START     Start time of the reservation, in
                               YYYY/MM/DD HH:MM:SS format. [default: 1901-01-01]
        --end=TIME_END         End time of the reservation, in
                               YYYY/MM/DD HH:MM:SS format. In addition a duration
                               can be specified if the + sign is the first sign.
                               The duration will than be added to
                               the start time. [default: 2100-12-31]
        --host=HOST            host number 
        --summary=SUMMARY        summary of the reservation
        --file=FILE            Adding multiple reservations from one file
    Options:

"""

        #print arguments["login"]
    if(arguments["list"]):
        reservations = Reservation()
        rsv= reservations.list(cm_id=arguments["--cm_id"],
                               user=arguments["--user"],
                               project=arguments["--project"],
                               label= arguments["--label"],
                               start_time= arguments["--start"],
                               end_time=arguments["--end"],
                               host=arguments["--host"],
                               summary=arguments["--summary"])
        for x in rsv:
            print x
            print 70 * "="
    elif(arguments["find"]):
        reservations = Reservation()
        if(arguments["all"]):
            print reservations.find_all()
        elif(arguments["--user"]):
            print reservations.find_user(arguments["--user"])
        elif(arguments["--label"]):
            print reservations.find_label(arguments["--label"])
        elif(arguments["--cm_id"]):
            print reservations.find_id(arguments["--cm_id"])
    elif(arguments["duration"]):
        reservations = Reservation()
        print reservations.duration(arguments["--cm_id"])
    elif(arguments["delete"]):
        if(arguments["all"]):
            reservations = Reservation()
            reservations.delete_all()
        else:
            reservations = Reservation()
            reservations.delete_selection(cm_id=arguments["--cm_id"],
                                          user=arguments["--user"],
                                          project=arguments["--project"],
                                          label= arguments["--label"],
                                          start_time= arguments["--start"],
                                          end_time=arguments["--end"],
                                          host=arguments["--host"])
    elif(arguments["add"]):
        reservations = Reservation(label=arguments["--label"],
                                   user=arguments["--user"],
                                   project=arguments["--project"],
                                   start_time=arguments["--start"],
                                   end_time=arguments["--end"],
                                   cm_id=arguments["--cm_id"],
                                   host=arguments["--host"],
                                   summary=arguments["--summary"])
        reservations.add()
    elif(arguments["addFile"] and arguments["--file"] is not None):
        try:
            with open(os.path.join(sys.path[0], arguments["--file"])) as file:
                reader = csv.reader(file)
                for row in reader:
                    reservations = Reservation(cm_id=row[0],
                                               label=row[1],
                                               user=row[2],
                                               project=row[3],
                                               start_time=row[4],
                                               end_time=row[5],
                                               host=row[6],
                                               summary=row[7])
                    reservations.add()
        except Exception as e:
            print "Error in adding from file. ", e
'''    elif(arguments["update"]):
          reservations = Reservation()
          fromObj = [str(sys.argv[2]).split("=")[0].replace("--", ""),str(sys.argv[2]).split("=")[1]] 
          toObj = [str(sys.argv[3]).split("=")[0].replace("--", ""),str(sys.argv[3]).split("=")[1]]
          fromBody = {cm_id=101, project = 20, user = "oliver"}
          toBody = {cm_id=101, project = 20, user = "oliver"}
          reservations.update_selection(cm_id=fromObj[1],project=toObj[1])
          print reservations.find_all()    '''

                                
if __name__ == "__main__":
    arguments = docopt(rain_command.__doc__)
    db = reservation_connect()
    rain_command(arguments)
    
