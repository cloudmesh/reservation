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

Than you declare a reseration object::

  reservation = ReservationClient(...)

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
  
        
Google Client Secrets
======================================================================

To authenticate with the google calendar follow the steps listed below::

Go to the Google Developers Console that can be found `here
<https://console.developers.google.com/project>`_.
   * Select a project.
   * In the sidebar on the left, select APIs & auth. In the list of APIs, make sure the status is ON for the Google Calendar API.
   * In the sidebar on the left, select Credentials.
   * Find the correct set of OAuth 2.0 credentials in the list, and then find the Client ID and Client secret for those credentials.
   * Download the JSON file and then place it on the same directory level as the reservation.py class



Google Calendar API                         
======================================================================
 
The specification of the researvation is based on the JSON Calendar
object defined in the google documentation. Additional information is
included as part of the description field.  The Google API
documentation can be found `here
<https://developers.google.com/resources/api-libraries/documentation/calendar/v3/python/latest/calendar_v3.events.html#get>`_.
    
Example                         
======================================================================

Reservation made by user1:

`reservation1.json <https://github.com/cloudmesh/reservation/blob/master/reservation_json_files/reservation1.json>`_

.. include:: ../../reservation_json_files/reservation1.json
   :literal:
   
`reservation2.json <https://github.com/cloudmesh/reservation/blob/master/reservation_json_files/reservation2.json>`_

.. include:: ../../reservation_json_files/reservation2.json
   :literal:
   
Reservation made by User2:
   
`reservation3.json <https://github.com/cloudmesh/reservation/blob/master/reservation_json_files/reservation3.json>`_

.. include:: ../../reservation_json_files/reservation3.json
   :literal:

Reservation client api file:

`reservation_client.py <https://github.com/cloudmesh/reservation/blob/master/reservation/reservation_client.py>`_

.. include:: ../../reservation/reservation_client.py
   :literal:

Reservation Main Controller:

`reservation.py <https://github.com/cloudmesh/reservation/blob/master/reservation/reservation.py>`_

.. include:: ../../reservation/reservation.py
   :literal:


In this example, we will conduct the following steps:
  
#. We will add 3 reservations
#. select all reservations.
#. Reschedule reservation.
#. Remove reservation.
#. Select all reservations by user id.
#. Remove all reservations.
#. Select all reservations by user id.

.. note ::
  
  All the commands are executed via the command line

Step1: Adding the 3 reservations to the google calendar::
     /github/reservation/reservation$ python reservation.py add --file=../reservation_json_files/reservation1.json
     /github/reservation/reservation$ python reservation.py add --file=../reservation_json_files/reservation2.json
     /github/reservation/reservation$ python reservation.py add --file=../reservation_json_files/reservation3.json
     
Step2: Get all the reservation from the calendar

::
  /github/reservation/reservation$ python reservation.py get_all
   
Step3: Reschedule reservation 1 with reservation 2::
     /github/reservation/reservation$ python reservation.py reschedule --reservation_id=c19qpuhq7g63urslvhi39d82h0 --file=../reservation_json_files/reservation2.json
   

Step4: Remove reservation 1::
     /github/reservation/reservation$ python reservation.py remove --reservation_id=c19qpuhq7g63urslvhi39d82h0
   
Step5: Get the reservations by user id::
     /github/reservation/reservation$ python reservation.py get_by_user --user_id=1001

Step6: Remove all reservations::
     /github/reservation/reservation$ python reservation.py remove_all
   
Step7: Get the reservations by user id::
     /github/reservation/reservation$ python reservation.py get_by_user --user_id=1001
