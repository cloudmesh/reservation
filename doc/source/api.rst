**********************************************************************
Python API 
**********************************************************************
.. sidebar:: 
   . 

  .. contents:: Table of Contents
     :depth: 5

..


The Python API contains the following functions to work with the Google Calendar:
Our current version uses only JSON objects to pass to the calendar.

First you need to import the client::

   from reservation.reservation_client import ReservationClent 

Than you decaler a reseration object::

  reservation = ReservationClient(...)


.. note::

   * how do i know which google calendar to use
   * how do i know how to authenticate


Now you can use various api calls

::

  reservation.add (rsv)

Adds a reservatuion.
Argument: A reservation is a JSON object that is passes to his method
to be added to the calendar return value: return ReservationId
(integer) only if reservation does not overlap
  
::

  reservation.remove (rsvId):

Removes a specific reservation from the calendar. Requires the
reservationID
  
::

  reservation.remove_all ():

Removes all the reservations from the calendar.

::

  reservation.get_from_id (rsvId):

Displays the reservation object.

::

  reservation.get_by_user (userId):

Selects all the reservations made by a user returns: all the
reservations events made by the user.

::

  reservation.get_all ():

Selects all reservations in the calendar.
return: Dict containing all the reservations

::

   reservation.list_by_user_and_project (userId, projId, sTime,eTime):

Lists all the users reservations made in a project from a start-time to a end time.

Arguments: userId, ProjectId, Start time, end time

Returns: List of a users reservations made of a project between an interval of time 

::

  reservation.list_by_project (projId):

Lists all the reservations made in a particular project

Argument: projId

Returns: returns all the reservation eventId's of a particular project.
  
:: 

  reservation.duration (rsvId):

Shows the duration of the reservation.

Argument: reservation reservation id.

Returns: returns the duration of that particular reservation.
  
::

  reservation.reschedule (oldRsvId, newRsv):

Used to update or modify an old reservation. Requires old reservation id and new reservation object that will replace the old reservation.

Arguments: oldRsvId (Integer) newEvent (JSON object)

::
          
  reservation.get_from_label (labelStr):

Assuming this label will return only one reservationId.

Return: returns the reservationId (Integer)
  
        
Example
======================================================================

In this example, we will conduct the following steps:
  
#. We will add 3 reservations
#. select all reservations.
#. Reschedule reservation.
#. Remove reservation.
#. Select all reservations.
#. Remove all reservations.
#. Select all reservations

   
Creating 3 reservations
----------------------------------------------------------------------

.. note::

   * why use the name oliver1,2, ... and not reservation 1, 2 in summary
   * why is there a { in description but no } close
   * why do you use inconsistent and illegal python usage of ' in definitions
   * there is no example.py in the code that allows me to run and test
     this exact example
   * we need a link to the example ...
   * in addition to your nice formatted documentation i would give a
     complete example in a .py filr and use a literal include, see
     Aravindhas multi.rst for example 
   * is the reservatiion.json documented?
   * the indentation needs to be space saving 4 spaces is enough
   * code in
     file:///Users/flat/github/reservation/doc/build/html/_modules/reservation/reservation_client.html#check_overlap
     is no nicely formated. e.g. can you try to be closer to 70
     columns, run over where you must, but the other stuff should be
     better formatted
   * is there a better way in python to format this file:///Users/flat/github/reservation/doc/build/html/modules/reservation-gvl.html#reservation.reservation_client.ReservationClient
    * indentation between oliver1,2,3 must be consistent

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

::

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
          }
        })

::

   print reservation.add({
      'summary': 'oliver3',
      'description':'{
      'hosts': '100-103', 
      'kind':'vm-server', 
      'project':'xyz', 
      'userid':'1002', 
      'displayName':'oliverlewis', 
      'email':'lewiso@indiana.edu'
      },

      {
                          
         'start': {
           'dateTime': '2014-05-05T22:50:00.000',
           'timeZone': 'America/New_York'
         },                              
         'end': {
            'dateTime': '2014-05-05T23:51:00.000',
            'timeZone': 'America/New_York'
          }    
      })
         

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
        {'id': u'2slbu96950v62krqh5lmthvc7s', 'label': u'Reservation_3'}, 
       'event0': 
        {'id': u'buta7destbamakidf9lm7agi5k', 'label': u'Reservation_1'}, 
       'event1': 
        {'id': u'5bmlslq006dbv0lampjfeu75ec', 'label': u'Reservation_2'}
      }

     
Removing a specific reservation using a label
----------------------------------------------------------------------

::
     
     reservation.remove(reservation.get_from_label('Reservation_3'))
     print reservation.get_all()
     
Output::

      {'event2': 
        'event0': 
         {'id': u'buta7destbamakidf9lm7agi5k', 'label': u'Reservation_1'}, 
        'event1': 
         {'id': u'5bmlslq006dbv0lampjfeu75ec', 'label': u'Reservation_2'}
      }
      
Rescheduling an event using a label to first retrieve the event::
   
     Rescheduling Reservation_2 to Reservation_X with a new startTime and new endTime
   
      reservation.reschedule(reservation.get_from_label('Reservation_2'), {
                             'summary': 'Reservation_X',
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
    
     {'event0': {'id': u'buta7destbamakidf9lm7agi5k', 'label': u'Reservation_1'}, 
      'event1': {'id': u'5bmlslq006dbv0lampjfeu75ec', 'label': u'Reservation_X'}}
  
Deleting all events::
  
    reservation.remove_all()

     

Google Calendar API                         
======================================================================
 
The specification of the researvation is based on the JSON Calendar
object defined in the google documentation. Additional information is
included as part of the description field.  The Google API
documentation can be found `here
<https://developers.google.com/resources/api-libraries/documentation/calendar/v3/python/latest/calendar_v3.events.html#get>`_.
    
