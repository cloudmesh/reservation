#! /usr/bin/env python

from reservation.model import Reservation
import datetime
from mongoengine import *
from reservation.cli import reservation_connect


db = reservation_connect()

reservation = Reservation(label="res-1",
                          cm_id="reservation-res-1",
                          summary="Simple reservation",
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

reservations = Reservation.objects(
    start_time__gte=datetime.datetime(2014, 8, 1, 01, 00, 00))
for reseravtion in reservations:
    print reservation
