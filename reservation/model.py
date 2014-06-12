#
# start mongo with
#
#    mongod --noauth --dbpath . --port 27777
#

from mongoengine import *
import datetime

def reservation_connect():
    try:
        db = connect('reservation', port=27777)
        return db
    except Exception, e:
        print "ERROR: could not establish a connection to mongo db"
        print
        print e
    
class Reservation(Document):

    cm_id = StringField()
    label = StringField()
    summary = StringField()
    host = StringField()
    user = StringField()
    project = StringField()
    start_time = DateTimeField()
    end_time = DateTimeField()
    # date_modified = DateTimeField(default=datetime.datetime.now)

    _order = [
        "label",
        "cm_id",
        "summary",
        "host",
        "user",
        "project",
        "start_time",
        "end_time"
    ]

    def __str__(self):
        d = self.to_json()
        return str(d)

    def to_json(self):
        d = {"label": self.label,
             "cm_id": self.cm_id,
             "summary": self.summary,
             "host": self.host,
             "user": self.user,
             "project": self.project,
             "start_time": str(self.start_time),
             "end_time": str(self.end_time)}
        return d
           
    def find_user(self, username):
        '''Selects all the reservations made by a user

        :param username: the user name
        '''
        return Reservation.objects(user=username)

    def find_all(self):
        '''Selects all reservations in the calendar
        '''
        return Reservation.objects.all()
    
    def find_label(self, label):
        '''Finds all reservations with a given label

        :param label: the label
        '''
        return Reservation.objects(label=label)

    def list(self, user=None, project=None, startTime=None, endTime=None):
        '''Lists all the users reservations made in a project from a
        start time to a end time'''
        try:
            if(user == None):
                reservations = Reservation.objects(project=project,start_time__gte= startTime,end_time__lte= endTime)
            elif(project == None):
                reservations = Reservation.objects(user=user,start_time__gte= startTime,end_time__lte= endTime)
            elif(startTime == None):
                reservations = Reservation.objects(user=user, project=project, end_time__lte= endTime)
            elif(endTime == None):
                reservations = Reservation.objects(user=user, project=project, start_time__gte= startTime)
            elif(user == None and project == None):
                reservations = Reservation.objects(start_time__gte= startTime, end_time__lte= endTime)
            else:
                reservations = Reservation.objects(user=user,project=project,start_time__gte= startTime,end_time__lte= endTime)
        except e:
            print "Query not possible. ", e    
        return reservations
    
    def duration(self, cm_id):
        '''Oliver: this function needs to return the duration 
        of the reservation by searching it from  the cm_id. 
        In this case I think we could do something similar with find_id function '''
        
        '''Shows the duration of the reservation'''

        reservations = Reservation.objects(cm_id=cm_id)
        delta = 0
        print reservations
        for x in reservations:
             delta = x.end_time - x.start_time

        return delta
    
    def delete_all(self):  # done    
        try:
            Reservation.drop_collection()
        except e:
            print "Error in delete all: ", e
        
    def find_id(self, id):
        '''displays the reservation object
        :param id: the cm_id
        '''
        return Reservation.objects(cm_id=id)

if __name__ == "__main__":
    db = reservation_connect()
    reservations = Reservation.objects({})
        
    "Delete all function tested"
    print 70 * "="
    #print reservations
    print 70 * "="
    # reservations = Reservation().delete_all()
    # reservations = Reservation().find_label("exp-0-0")
    #reservation = Reservation().find_all()
    #print reservation
    #rsv = Reservation().duration("cm_reservation-2-7")
    rsv = Reservation().list("gregor", None, None, "2014-06-16")
    #print rsv
    #Reservation().greaterThanStart("2014-06-16")
    for x in rsv:
        print x
        print 70 * "="
    # print Reservation(reservations)
    print 70 * "="
    "find_id function"
    
