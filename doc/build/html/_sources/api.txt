**********************************************************************
Python API 
**********************************************************************

.. sidebar:: Page Contents |video-hadoop|

   .. contents::
      :local:

The Python API contains the following functions to work with the Google Calendar:
Our current version uses only JSON objects to pass to the calendar.

* The addEventToCalendar(event):
      Arguments: event object
      return value: return EventId (integer) only if event does not overlap
  
* removeEventFromCalendar(eventId):
      Argument: EventId (Integer)
  
* removeAllEvents():
      This removes all the events from the primary calendar.

* viewEventFromId(eventId):
      returns the entire event object that is stored in the calendar.

* selectEventIdsFromUser(userId):
      Argument: user id (integer)
      returns: all the reservations events made by the user.

* selectAllEvents():
      This lists all the events from the primary calendar.
      return: Dict containing all the events

* lstUsrProjRsvSTimeETime(userId, projId, sTime, eTime):
      Arguments: userId, ProjectId, Start time, end time
      returns: List of a users reservations made of a project between an interval of time 

* lstRsvProj(projId):
      Argument: projId
      return value: returns all the reservation eventId's of a particular project.
  
* durationOfRsv(rsvId):
      Argument: reservation event id.
      returns: returns the duration of that particular event.
  
* rescheduleEvent(oldEventId, newEvent):
      Used to update or modify an old event.
          Args: oldEventId (Integer)
          newEvent (JSON object)
          
* selectEventIdFromLabel(label):
      args: label which will be compared with the summary from the event
      return: returns the eventId (Integer)
  
WorkFlow
======================================================================
  
*  1. We will add 3 events
*  2. select all events.
*  3. Reschedule event.
*  4. Remove event.
*  5. Select all events.
*  6. Remove all events.
*  7. Select all events
        
Sample code 
======================================================================

   
Creating 3 events
----------------------------------------------------------------------

::
   
     print reservation.addEventToCalendar({
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
     print reservation.addEventToCalendar({
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
                             print reservation.addEventToCalendar('summary': 'oliver3',
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
   
Select all events
----------------------------------------------------------------------

::

      print reservation.selectAllEvents()
      
Output ::

      {'event2': 
        {'id': u'2slbu96950v62krqh5lmthvc7s', 'label': u'Appointment3'}, 
       'event0': 
        {'id': u'buta7destbamakidf9lm7agi5k', 'label': u'Appointment1'}, 
       'event1': 
        {'id': u'5bmlslq006dbv0lampjfeu75ec', 'label': u'Appointment2'}
      }

     
Removing a specific event using a label
----------------------------------------------------------------------

::
     
     reservation.removeEventFromCalendar(reservation.selectEventIdFromLabel('Appointment3'))
     print reservation.selectAllEvents()
     
Output::

      {'event2': 
        'event0': 
         {'id': u'buta7destbamakidf9lm7agi5k', 'label': u'Appointment1'}, 
        'event1': 
         {'id': u'5bmlslq006dbv0lampjfeu75ec', 'label': u'Appointment2'}
      }
      
Rescheduling an event using a label to first retrieve the event::
   
     Rescheduling Appointment 2 to AppointmentX with a new startTime and new endTime
   
      reservation.rescheduleEvent(reservation.selectEventIdFromLabel('Appointment2'), {
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
                              
      print reservation.selectAllEvents()
    
Output::
    
     {'event0': {'id': u'buta7destbamakidf9lm7agi5k', 'label': u'Appointment1'}, 
      'event1': {'id': u'5bmlslq006dbv0lampjfeu75ec', 'label': u'AppointmentX'}}
  
Deleting all events::
  
    reservation.removeAllEvents()

     
                         
 
Specification of the entire JSON Calendar object: Referenced from the
google documentation. The Json Object must adhere to the following standard.
      
The complete structure of the object can be viewed from the link below: 
    *  https://developers.google.com/resources/api-libraries/documentation/calendar/v3/python/latest/calendar_v3.events.html#get
    
