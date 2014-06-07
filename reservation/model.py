#
# start mongo with
#
#    mongod --noauth --dbpath . --port 27777
#

from mongoengine import *
import datetime


class Reservation(Document):

    cm_id = StringField()
    label = StringField()
    summmary = StringField()
    host = StringField()
    user = StringField()
    project = StringField()
    start_time = DateTimeField()
    end_time = DateTimeField()
    date_modified = DateTimeField(default=datetime.datetime.now)

    _order = [
        "label",
        "cm_id",
        "summmary",
        "host",
        "user",
        "project",
        "start_time",
        "end_time"
    ]

    def __str__(self):
        d = self.to_json()
        print d
        r = ""
        for key in self._order:
            r = r + key + ": " + d[key] + " "
        return r

    
    def to_json(self):
        d = {"label": self.label,
             "cm_id": self.cm_id,
             "summmary": self.summmary,
             "host": self.host,
             "user": self.user,
             "project": self.project,
             "start_time": str(self.start_time),
             "end_time": str(self.end_time)}
        return d

    
db = connect('reservation', port=27777)

reservation = Reservation(label="res-1",
                          cm_id="reservation-res-1",
                          summmary="Simple reservation",
                          host="i001",
                          user="gregor",
                          project="fg82",
                          start_time=datetime.datetime(
                              2014, 8, 1, 01, 00, 00),
                          end_time=datetime.datetime(2014, 8, 1, 02, 00, 00))
reservation.save()

reservations = Reservation.objects(user="gregor")

for reseravtion in reservations:
    print reservation

print 70 * "="

reservations = Reservation.objects(start_time__gte=datetime.datetime(2014, 8, 1, 01, 00, 00))
for reseravtion in reservations:
    print reservation
