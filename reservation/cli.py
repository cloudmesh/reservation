from model import Reservation
from mongoengine import *
from docopt import docopt
import pprint
import json
from cloudmesh_common.tables import array_dict_table_printer

def reservation_connect():
    """establishes connection to the reservation server"""
    try:
        db = connect('reservation', port=27777)
        return db
    except Exception, e:
        print "ERROR: could not establish a connection to mongo db"
        print e
        return None
    
def _print_reservations(reservations, format="table"):
    """prints a reservation"""
    reservation_list = []
    for reservation in reservations:
        reservation_list.append(reservation.to_json())
    if format == "json":
        print json.dumps(reservation_list, indent=4)
    if format == "table":
        print array_dict_table_printer(reservation_list,
                                       ["cm_id",
                                        "label",
                                        "project",
                                        "user",
                                        "host",
                                        "start_time",
                                        "end_time",
                                        "summary",
                                        ]
                                       )
                
def shell_command_reservation(arguments):
    """
      ::
      
        Usage:
            reservation --rst
            reservation --version
            reservation find [all]
                             [--user=USER_ID]
                             [--label=ID]
                             [--cm_id=ID]
                             [--format=FORMAT]                             
            reservation list [--cm_id=CM_ID]
                             [--user=USER_ID]
                             [--project=PROJECT_ID]
                             [--label=STRING]
                             [--start=TIME_START]
                             [--end=TIME_END]
                             [--host=HOST]
                             [--summary=SUMMARY]
                             [--format=FORMAT]
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
            reservation add --cm_id=CM_ID --user=USER_ID --project=PROJECT_ID --label=STRING --start=TIME_START --end=TIME_END --host=HOST --summary=SUMMARY
            reservation add --file=FILE

        Options:
            --rst                 print an rst manul page
            --version             print the version
            --label=STRING        label id reservation
            --cm_id=CM_ID         reservation cloudmesh id
            --user=USER_ID        user id
            --project=PROJECT_ID  project id
            --start=TIME_START    Start time of the reservation, in
                                  YYYY/MM/DD HH:MM:SS format. [default: 1901-01-01]
            --end=TIME_END        End time of the reservation, in
                                  YYYY/MM/DD HH:MM:SS format. In addition a duration
                                  can be specified if the + sign is the first sign.
                                  The duration will than be added to
                                  the start time. [default: 2100-12-31]
            --host=HOST           host number 
            --summary=SUMMARY     summary of the reservation
            --file=FILE           Adding multiple reservations from one file
            --format=FORMAT       Format is either table or jaon
                                  [default: table]
    """

    #print arguments["login"]
    if arguments["--rst"]:

        print 70 * "*"
        print "Manual Pages"
        print 70 * "*"
        print
        print "reservation"
        print 70 * "="
        print "\n::\n"
        lines = shell_command_reservation.__doc__.split("\n")
        for line in lines:
            print "  ", line

    elif arguments["--version"]:
        print reservation.__version__

    elif(arguments["list"]):
        db = Reservation()
        reservations = db.list(cm_id=arguments["--cm_id"],
                               user=arguments["--user"],
                               project=arguments["--project"],
                               label= arguments["--label"],
                               start_time= arguments["--start"],
                               end_time=arguments["--end"],
                               host=arguments["--host"],
                               summary=arguments["--summary"])
        _print_reservations(reservations, arguments["--format"])

    elif(arguments["find"]):
        db = Reservation()
        
        if(arguments["all"]):
            reservations = db.find_all()
        elif(arguments["--user"]):
            reservations = db.find_user(arguments["--user"])
        elif(arguments["--label"]):
            reservations = db.find_label(arguments["--label"])
        elif(arguments["--cm_id"]):
            reservations = db.find_id(arguments["--cm_id"])
        else:
            reservations = db.find_all()

        _print_reservations(reservations, arguments["--format"])
            
    elif(arguments["duration"]):
        db = Reservation()
        print db.duration(arguments["--cm_id"])
    elif(arguments["delete"]):
        if(arguments["all"]):
            db = Reservation()
            db.delete_all()
        else:
            db = Reservation()
            db.delete_selection(cm_id=arguments["--cm_id"],
                                          user=arguments["--user"],
                                          project=arguments["--project"],
                                          label= arguments["--label"],
                                          start_time= arguments["--start"],
                                          end_time=arguments["--end"],
                                          host=arguments["--host"])
    elif(arguments["add"]):

        if arguments["--file"] is None:

            
            db = Reservation(label=arguments["--label"],
                             user=arguments["--user"],
                             project=arguments["--project"],
                             start_time=arguments["--start"],
                             end_time=arguments["--end"],
                             cm_id=arguments["--cm_id"],
                             host=arguments["--host"],
                             summary=arguments["--summary"])
            db.add()
        else:
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
                        db.add()
            except Exception as e:
                print "Error in adding from file. ", e
'''
    elif(arguments["update"]):
          reservations = Reservation()
          fromObj = [str(sys.argv[2]).split("=")[0].replace("--", ""),str(sys.argv[2]).split("=")[1]] 
          toObj = [str(sys.argv[3]).split("=")[0].replace("--", ""),str(sys.argv[3]).split("=")[1]]
          fromBody = {cm_id=101, project = 20, user = "oliver"}
          toBody = {cm_id=101, project = 20, user = "oliver"}
          db.update_selection(cm_id=fromObj[1],project=toObj[1])
          print db.find_all()
'''
        
def main():
    arguments = docopt(shell_command_reservation.__doc__)
    db = reservation_connect()
    shell_command_reservation(arguments)
                                
if __name__ == "__main__":
    main()

