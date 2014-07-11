from mongoengine import *
import datetime
import sys
import csv
import os
import pprint

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
        
    def duration(self, cm_id):
        '''Shows the duration of the reservation'''

        reservations = Reservation.objects(cm_id=cm_id)
        delta = 0
        #print reservations
        for x in reservations:
             delta = x.end_time - x.start_time

        return delta
    
    def list(self, **kwargs):
        '''Lists all the users reservations made in a project from a
        start time to a end time'''        
        start_time ="1901-01-01"
        end_time = "2100-12-31"
        empty_keys = [k for k,v in kwargs.iteritems() if not v]
        for k in empty_keys:
            del kwargs[k]
        if("start_time" in kwargs):
            start_time = kwargs['start_time']
            del kwargs['start_time']
        if("end_time" in kwargs):
            end_time = kwargs['end_time']
            del kwargs['end_time']
        '''test change'''
        #pp.pprint(kwargs)
        #print "laughing: ", start_time, "__", end_time
        reservations = Reservation.objects(__raw__=kwargs, start_time__gte=start_time, end_time__lte=end_time)
        
        return reservations
    
    def delete_all(self):
        Reservation.drop_collection()
    
    def delete_selection(self, **kwargs):  # done    
        start_time ="1901-01-01"
        end_time = "2100-12-31"
        empty_keys = [k for k,v in kwargs.iteritems() if not v]
        for k in empty_keys:
            del kwargs[k]
        if("start_time" in kwargs):
            start_time = kwargs['start_time']
            del kwargs['start_time']
        if("end_time" in kwargs):
            end_time = kwargs['end_time']
            del kwargs['end_time']
        try:
            Reservation.objects(__raw__=kwargs, start_time__gte=start_time, end_time__lte=end_time).delete()
        except Exception as e:
            print "Error in delete all: ", e
            
    def update_selection(self, **kwargs):  # done  
        start_time ="1901-01-01"
        end_time = "2100-12-31"
        empty_keys = [k for k,v in kwargs.iteritems() if not v]
        for k in empty_keys:
            del kwargs[k]
        if("start_time" in kwargs):
            start_time = kwargs['start_time']
            del kwargs['start_time']
        if("end_time" in kwargs):
            end_time = kwargs['end_time']
            del kwargs['end_time']
        try:                                            
            print Reservation.objects(__raw__=kwargs)
        except Exception as e:
            print "Error in update. ", e
            
    '''def update_selection(self, fromObj, toObj):
        #print fromObj, toObj
        rsvs = {}
        if("project" == fromObj[0]):
            if("project" == toObj[0]):
                Reservation.objects(project=fromObj[1]).update(set__project=toObj[1])
            elif("cm_id" == toObj[0]):
                Reservation.objects(project=fromObj[1]).update(set__cm_id=toObj[1])
            elif("user" == toObj[0]):
                Reservation.objects(project=fromObj[1]).update(set__user=toObj[1])
            elif("host" == toObj[0]):
                Reservation.objects(project=fromObj[1]).update(set__host=toObj[1])
            elif("end_time" == toObj[0]):
                Reservation.objects(project=fromObj[1]).update(set__end_time=toObj[1])
            elif("start_time" == toObj[0]):
                Reservation.objects(project=fromObj[1]).update(set__start_time=toObj[1])
            elif("label" == toObj[0]):
                Reservation.objects(project=fromObj[1]).update(set__label=toObj[1])
            elif("summary" == toObj[0]):
                Reservation.objects(project=fromObj[1]).update(set__summary=toObj[1])
        elif("cm_id" == fromObj[0]):
            if("project" == toObj[0]):
                Reservation.objects(cm_id=fromObj[1]).update(set__project=toObj[1])
            elif("cm_id" == toObj[0]):
                Reservation.objects(cm_id=fromObj[1]).update(set__cm_id=toObj[1])
            elif("user" == toObj[0]):
                Reservation.objects(cm_id=fromObj[1]).update(set__user=toObj[1])
            elif("host" == toObj[0]):
                Reservation.objects(cm_id=fromObj[1]).update(set__host=toObj[1])
            elif("end_time" == toObj[0]):
                Reservation.objects(cm_id=fromObj[1]).update(set__end_time=toObj[1])
            elif("start_time" == toObj[0]):
                Reservation.objects(cm_id=fromObj[1]).update(set__start_time=toObj[1])
            elif("label" == toObj[0]):
                Reservation.objects(cm_id=fromObj[1]).update(set__label=toObj[1])
            elif("summary" == toObj[0]):
                Reservation.objects(cm_id=fromObj[1]).update(set__summary=toObj[1])
        elif("user" == fromObj[0]):
            if("project" == toObj[0]):
                Reservation.objects(user=fromObj[1]).update(set__project=toObj[1])
            elif("cm_id" == toObj[0]):
                Reservation.objects(user=fromObj[1]).update(set__cm_id=toObj[1])
            elif("user" == toObj[0]):
                Reservation.objects(user=fromObj[1]).update(set__user=toObj[1])
            elif("host" == toObj[0]):
                Reservation.objects(user=fromObj[1]).update(set__host=toObj[1])
            elif("end_time" == toObj[0]):
                Reservation.objects(user=fromObj[1]).update(set__end_time=toObj[1])
            elif("start_time" == toObj[0]):
                Reservation.objects(user=fromObj[1]).update(set__start_time=toObj[1])
            elif("label" == toObj[0]):
                Reservation.objects(user=fromObj[1]).update(set__label=toObj[1])
            elif("summary" == toObj[0]):
                Reservation.objects(user=fromObj[1]).update(set__summary=toObj[1])
        elif("host" == fromObj[0]):
            if("project" == toObj[0]):
                Reservation.objects(host=fromObj[1]).update(set__project=toObj[1])
            elif("cm_id" == toObj[0]):
                Reservation.objects(host=fromObj[1]).update(set__cm_id=toObj[1])
            elif("user" == toObj[0]):
                Reservation.objects(host=fromObj[1]).update(set__user=toObj[1])
            elif("host" == toObj[0]):
                Reservation.objects(host=fromObj[1]).update(set__host=toObj[1])
            elif("end_time" == toObj[0]):
                Reservation.objects(host=fromObj[1]).update(set__end_time=toObj[1])
            elif("start_time" == toObj[0]):
                Reservation.objects(host=fromObj[1]).update(set__start_time=toObj[1])
            elif("label" == toObj[0]):
                Reservation.objects(host=fromObj[1]).update(set__label=toObj[1])
            elif("summary" == toObj[0]):
                Reservation.objects(host=fromObj[1]).update(set__summary=toObj[1])
        elif("end_time" == fromObj[0]):
            if("project" == toObj[0]):
                Reservation.objects(end_time=fromObj[1]).update(set__project=toObj[1])
            elif("cm_id" == toObj[0]):
                Reservation.objects(end_time=fromObj[1]).update(set__cm_id=toObj[1])
            elif("user" == toObj[0]):
                Reservation.objects(end_time=fromObj[1]).update(set__user=toObj[1])
            elif("host" == toObj[0]):
                Reservation.objects(end_time=fromObj[1]).update(set__host=toObj[1])
            elif("end_time" == toObj[0]):
                Reservation.objects(end_time=fromObj[1]).update(set__end_time=toObj[1])
            elif("start_time" == toObj[0]):
                Reservation.objects(end_time=fromObj[1]).update(set__start_time=toObj[1])
            elif("label" == toObj[0]):
                Reservation.objects(end_time=fromObj[1]).update(set__label=toObj[1])
            elif("summary" == toObj[0]):
                Reservation.objects(end_time=fromObj[1]).update(set__summary=toObj[1])
        elif("start_time" == fromObj[0]):
            if("project" == toObj[0]):
                Reservation.objects(start_time=fromObj[1]).update(set__project=toObj[1])
            elif("cm_id" == toObj[0]):
                Reservation.objects(start_time=fromObj[1]).update(set__cm_id=toObj[1])
            elif("user" == toObj[0]):
                Reservation.objects(start_time=fromObj[1]).update(set__user=toObj[1])
            elif("host" == toObj[0]):
                Reservation.objects(start_time=fromObj[1]).update(set__host=toObj[1])
            elif("end_time" == toObj[0]):
                Reservation.objects(start_time=fromObj[1]).update(set__end_time=toObj[1])
            elif("start_time" == toObj[0]):
                Reservation.objects(start_time=fromObj[1]).update(set__start_time=toObj[1])
            elif("label" == toObj[0]):
                Reservation.objects(start_time=fromObj[1]).update(set__label=toObj[1])
            elif("summary" == toObj[0]):
                Reservation.objects(start_time=fromObj[1]).update(set__summary=toObj[1])
        elif("label" == fromObj[0]):
            if("project" == toObj[0]):
                Reservation.objects(label=fromObj[1]).update(set__project=toObj[1])
            elif("cm_id" == toObj[0]):
                Reservation.objects(label=fromObj[1]).update(set__cm_id=toObj[1])
            elif("user" == toObj[0]):
                Reservation.objects(label=fromObj[1]).update(set__user=toObj[1])
            elif("host" == toObj[0]):
                Reservation.objects(label=fromObj[1]).update(set__host=toObj[1])
            elif("end_time" == toObj[0]):
                Reservation.objects(label=fromObj[1]).update(set__end_time=toObj[1])
            elif("start_time" == toObj[0]):
                Reservation.objects(label=fromObj[1]).update(set__start_time=toObj[1])
            elif("label" == toObj[0]):
                Reservation.objects(label=fromObj[1]).update(set__label=toObj[1])
            elif("summary" == toObj[0]):
                Reservation.objects(label=fromObj[1]).update(set__summary=toObj[1])
        elif("summary" == fromObj[0]):
            if("project" == toObj[0]):
                Reservation.objects(summary=fromObj[1]).update(set__project=toObj[1])
            elif("cm_id" == toObj[0]):
                Reservation.objects(summary=fromObj[1]).update(set__cm_id=toObj[1])
            elif("user" == toObj[0]):
                Reservation.objects(summary=fromObj[1]).update(set__user=toObj[1])
            elif("host" == toObj[0]):
                Reservation.objects(summary=fromObj[1]).update(set__host=toObj[1])
            elif("end_time" == toObj[0]):
                Reservation.objects(summary=fromObj[1]).update(set__end_time=toObj[1])
            elif("start_time" == toObj[0]):
                Reservation.objects(summary=fromObj[1]).update(set__start_time=toObj[1])
            elif("label" == toObj[0]):
                Reservation.objects(summary=fromObj[1]).update(set__label=toObj[1])
            elif("summary" == toObj[0]):
                Reservation.objects(summary=fromObj[1]).update(set__summary=toObj[1])
              
        #print Reservation.objects(cm_id=fromObj[1])'''
        
    def find_id(self, id):
        '''displays the reservation object
        :param id: the cm_id
        '''
        return Reservation.objects(cm_id=id)

    def time_string(date_time):
        return datetime.datetime.strptime(self.start_time, "%Y-%m-%d %H:%M:%S")
            
    def add(self):
        if(self.check_overlap() == True):
            flag = True
            print "Reservations overlap: cannot schedule at this time"
            while flag:
                self.start_time = str(self.time_string(self.start_time) + datetime.timedelta(minutes=30))
                self.end_time = str(self.time_string(self.end_time)+ datetime.timedelta(minutes=30))
                if(self.check_overlap()==False):
                    flag = False
            return "Reservations can be scheduled at :", str(self.start_time)
        else:            
            Reservation.save(self)
            print "Reservation added successfully."
            
    def check_overlap(self):
        #print self.start_time, self.end_time
        flag = False
        rsvs= self.find_all()
        start_time = self.time_string(self.start_time)
        end_time = self.time_string(self.end_time)
        for rsv in rsvs:
            if((rsv['start_time'] <= start_time and
                rsv['end_time'] >= start_time and
                (self.host == rsv['host'])) or
                (end_time <= rsv['end_time']
                 and rsv['start_time'] <= end_time
                and (self.host == rsv['host']))):
                flag = True
                break;
        return flag

