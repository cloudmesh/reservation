import datetime
import json
from mongoengine import connect
from model import Reservation

class ReservationClient(object):

    _collection_name = "cm_reservation"
    _db = None
    
    def __init__(self, collection=None):
        if collection:
            self._db = connection(collection)
        else
            self._db = connection(self._collection_name)
            

    def add(self, reservation):
        '''Adds a reservation

        :param reservation: a dict containing the reservation
        '''
        rsv = Researvation(reservation)
                
        if(check_overlap(self.service, reservation) == True):
            print "ERROR: Reservations overlap: cannot schedule at this time"
            return False
            # bug rase exception
        else:
            rsv.save()
            return True


    def remove_all(self):
        '''Removes all the reservations from the calendar'''
        for reservation in Reervations.objects:
            reservation.delete()

    def remove(self, id):
        '''Removes a specific reservation from the calendar.

        :param id: the cm_id of the reservation 
        '''
        # find the reservation
        # delete it 

    def find_id(self, id):
        '''displays the reservation object

        :param id: the cm_id
        '''
        reservation = Reservation.objects(cm_id=id)
        return reservation

    def find_user(self, username):
        '''Selects all the reservations made by a user

        :param username: the user name
        '''
        reservations = Reservation.objects(user=username)
        return reservations

    def find_all(self):
        '''Selects all reservations in the calendar
        '''
        return Reservation.objects


    def find_label(self, label):
        '''Finds all reservations with a given label

        :param label: the label
        '''
        reservations = Reservation.objects(label=label)
        return reservations



    def list_by_user_and_project(self, user, project, start_time, end_time):
        '''Lists all the users reservations made in a project from a
        start-time to a end time'''
        reservations = self.find(user=user,
                                 project=project,
                                 start_time __gt__ start_time,
                                 end_time __lt__ end_time)
        return reservations


    def duration(self, cm_id):
        '''Shows the duration of the reservation'''

        reservation = self.find(cm_id=cm_id)
        delta = reservation.end_tome - reservation.start_time

        return delta


def check_overlap(reservation):

    t_start = reservation.start_time
    t_end = reservation.end_tome
    reservations = Reservatione(start_time __gt__ t_start, end_time _lt_ t_end 
    return reservations.count() > 0

def reschedule(self, cm_id, d):
        '''Used to update or modify an old reservation.
        Requires old reservation id and new reservation
        object that will replace the old reservation'''

        reservation = cself.find(cm_id)
        d["cm_id"] = cm_id

        Reservation.update(d)
        
