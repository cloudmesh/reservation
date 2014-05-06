**********************************************************************
Python API 
**********************************************************************

.. sidebar:: Page Contents |video-hadoop|

   .. contents::
      :local:

The Python API contains the following functions to work with the Google Calendar:
Our current version uses only JSON objects to pass to the calendar.

* The add(self,rsv):
      Argument: A reservation is a JSON object that is passes to his method to be added to the calendar
      return value: return ReservationId (integer) only if reservation does not overlap
  
* remove(self,rsvId):
      Removes a specific reservation from the calendar. Requires the reservationID
  
* remove_all(self):
      Removes all the reservations from the calendar

* get_from_id(self,rsvId):
        displays the reservation object

* get_by_user(self,userId):
      Selects all the reservations made by a user
      returns: all the reservations events made by the user.

* get_all(self):
      Selects all reservations in the calendar.
      return: Dict containing all the reservations

* list_by_user_and_project(self, userId, projId, sTime,eTime):
      Lists all the users reservations made in a project from a start-time to a end time
      Arguments: userId, ProjectId, Start time, end time
      returns: List of a users reservations made of a project between an interval of time 

* list_by_project(self, projId):
      Lists all the reservations made in a particular project
      Argument: projId
      return value: returns all the reservation eventId's of a particular project.
  
* duration(self, rsvId):
      Shows the duration of the reservation
      Argument: reservation reservation id.
      returns: returns the duration of that particular reservation.
  
* reschedule(self, oldRsvId, newRsv):
          Used to update or modify an old reservation. Requires old reservation id and new reservation object that will replace the old reservation
          Args: oldRsvId (Integer)
          newEvent (JSON object)
          
* get_from_label(self, labelStr):
      Assuming this label will return only one reservationId.
      return: returns the reservationId (Integer)
  
WorkFlow
======================================================================
  
*  1. We will add 3 reservations
*  2. select all reservations.
*  3. Reschedule reservation.
*  4. Remove reservation.
*  5. Select all reservations.
*  6. Remove all reservations.
*  7. Select all reservations
        
Sample code 
======================================================================

   
Creating 3 reservations
----------------------------------------------------------------------

::
   
     print reservation.add({
                       'summary': 'oliver1',
                        'description':'{
                            'hosts': '100-103', 
                            'kind':'vm-server', 
                            'project':'xyz', 
                            'userid':'1002', 
                            'displayName':'oliverlewis', 
                            'email':'lewiso@indiana.edu'
                        },
                        
                        'start': {
                            'dateTime': '2014-05-05T22:50:00.000',
                            'timeZone': 'America/New_York'
                        },
                        
                        'end': {
                            'dateTime': '2014-05-05T23:51:00.000',
                            'timeZone': 'America/New_York'
                        }
                       })
     print reservation.add({
                       'summary': 'oliver2',
                        'description':'{
                            'hosts': '100-103', 
                            'kind':'vm-server', 
                            'project':'xyz', 
                            'userid':'1001', 
                            'displayName':'oliverlewis', 
                            'email':'lewiso@indiana.edu'
                        },
                        
                        'start': {
                            'dateTime': '2014-05-05T22:50:00.000',
                            'timeZone': 'America/New_York'
                        },
                        
                        'end': {
                            'dateTime': '2014-05-05T23:51:00.000',
                            'timeZone': 'America/New_York'
                        }})
                             print reservation.add('summary': 'oliver3',
                              'description':'{
                                  'hosts': '100-103', 
                                  'kind':'vm-server', 
                                  'project':'xyz', 
                                  'userid':'1002', 
                                  'displayName':'oliverlewis', 
                                  'email':'lewiso@indiana.edu'
                              },
                              
                              'start': {
                                  'dateTime': '2014-05-05T22:50:00.000',
                                  'timeZone': 'America/New_York'
                              },
                              
                              'end': {
                                  'dateTime': '2014-05-05T23:51:00.000',
                                  'timeZone': 'America/New_York'
                              }})
                       
Output ::
    
     buta7destbamakidf9lm7agi5k
     5bmlslq006dbv0lampjfeu75ec
     2slbu96950v62krqh5lmthvc7s
   
Select all reservations
----------------------------------------------------------------------

::

      print reservation.get_all()
      
Output ::

      {'event2': 
        {'id': u'2slbu96950v62krqh5lmthvc7s', 'label': u'Appointment3'}, 
       'event0': 
        {'id': u'buta7destbamakidf9lm7agi5k', 'label': u'Appointment1'}, 
       'event1': 
        {'id': u'5bmlslq006dbv0lampjfeu75ec', 'label': u'Appointment2'}
      }

     
Removing a specific reservation using a label
----------------------------------------------------------------------

::
     
     reservation.remove(reservation.get_from_label('Appointment3'))
     print reservation.get_all()
     
Output::

      {'event2': 
        'event0': 
         {'id': u'buta7destbamakidf9lm7agi5k', 'label': u'Appointment1'}, 
        'event1': 
         {'id': u'5bmlslq006dbv0lampjfeu75ec', 'label': u'Appointment2'}
      }
      
Rescheduling an event using a label to first retrieve the event::
   
     Rescheduling Appointment 2 to AppointmentX with a new startTime and new endTime
   
      reservation.reschedule(reservation.get_from_label('Appointment2'), {
                             'summary': 'AppointmentX',
                              'location': 'Somewherenew',
                              'start': {
                                'dateTime': '2014-06-03T10:00:00.000-07:00',
                                'timeZone': 'America/Los_Angeles'
                              },
                                                                     'end': {
                                'dateTime': '2014-06-03T10:25:00.000-07:00',
                                'timeZone': 'America/Los_Angeles'
                              }})
                              
      print reservation.get_all()
    
Output::
    
     {'event0': {'id': u'buta7destbamakidf9lm7agi5k', 'label': u'Appointment1'}, 
      'event1': {'id': u'5bmlslq006dbv0lampjfeu75ec', 'label': u'AppointmentX'}}
  
Deleting all events::
  
    reservation.remove_all()

     
                         
 
Specification of the entire JSON Calendar object: Referenced from the
google documentation. The Json Object must adhere to the following standard.
      
The complete structure of the object can be viewed from the link below: 
    *  https://developers.google.com/resources/api-libraries/documentation/calendar/v3/python/latest/calendar_v3.events.html#get
    
