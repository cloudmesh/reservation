"""
Usage:
    reservation --label=ID

Arguments:
    --label=ID    label id reservation
    
Options:
    
"""
from mongoengine import *
from docopt import docopt
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

    def list(self, **kwargs):
        '''Lists all the users reservations made in a project from a
        start time to a end time'''        
        start_time ="1901-01-01"
        end_time = "2100-12-31"
        if("start_time" in kwargs):
            start_time = kwargs['start_time']
            del kwargs['start_time']
        if("end_time" in kwargs):
            end_time = kwargs['end_time']
            del kwargs['end_time']
        reservations = Reservation.objects(__raw__=kwargs, start_time__gte=start_time, end_time__lte=end_time)
        return reservations
        
    def duration(self, cm_id):
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

    def add(self):
        if(self.check_overlap() == True):
            print "Reservations overlap: cannot schedule at this time"
        else:            
            Reservation.save(self)
            print "Reservation added successfully."
            
    def check_overlap(self):
        #print self.start_time, self.end_time
        flag = False
        rsvs= self.list()
        start_time = datetime.datetime.strptime(self.start_time, "%Y-%m-%d %H:%M:%S.%f")
        end_time = datetime.datetime.strptime(self.end_time, "%Y-%m-%d %H:%M:%S.%f")
        for rsv in rsvs:
            if((rsv['start_time'] <= start_time and rsv['end_time'] >= start_time and (self.host == rsv['host'])) or (end_time <= rsv['end_time'] and rsv['start_time'] <= end_time and (self.host == rsv['host']))):
                flag = True
                break;
        return flag

def test(arguments):
    #print arguments["login"]
    print "in here"
    
if __name__ == "__main__":
    arguments = docopt(__doc__)
    test(arguments)
    #db = reservation_connect()
    
    print arguments
    #reservation_command(arguments)
    
    #reservations = Reservation.objects({})
        
    "Delete all function tested"
    print 70 * "="
    #print reservations
    print 70 * "="
    # reservations = Reservation().delete_all()
    # reservations = Reservation().find_label("exp-0-0")
    #reservation = Reservation().find_all()
    #print reservation
    #rsv = Reservation().duration("cm_reservation-2-7")
    #rsv = Reservation.objects(user="gregor")
    #reservations = Reservation(label="oli-exp", user="Nat", project="fg82", start_time="2014-06-18 21:06:16.642000", end_time="2014-06-20 21:06:16.642000", cm_id="ol_reservation-1-6", host="ol02", summary="rubbish data")
    #reservations = Reservation()
    #reservations.delete_all()
    #rsv= reservations.list(user="Nat")
    
    #rsv = reservations.add()
    #print rsv
    #Reservation().greaterThanStart("2014-06-16")
    '''if rsv is not None:
        for x in rsv:
            print x
            print 70 * "="'''#
    # print Reservation(reservations)
    print 70 * "="
    "find_id function"
    
