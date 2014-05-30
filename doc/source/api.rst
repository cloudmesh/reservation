**********************************************************************
Google Calendar API
**********************************************************************
.. sidebar:: 
   . 

  .. contents:: Table of Contents
     :depth: 5

..


Steps to follow to set up the environment
======================================================================
Before starting with the example it is necessary to prepare the environment.

Step 1: `Create a Google Account <https://accounts.google.com/SignUp>`_.

Step 2: Register the project on Google to run the sample example
        1) `Create a Project <https://console.developers.google.com/project>`_.
	2) Select the project then under the Api's & Auth Tab select API.
	3) In the sidebar on the left, select APIs & auth. In the list of APIs, make sure the status is ON for the Google Calendar API.

Step 3: Authorization- Get Client Secrets JSON file
	1) Go to the Google Developers Console that can be found `here <https://console.developers.google.com/project>`_.
	2) Select a project.
	3) In the sidebar on the left, select Credentials.
	4) Download the JSON file and rename the file as client_secrets.json.
	5) move clients_secrets.json file to ~/.futuregrid/cloudmesh/. If the directory isn't present create the directory using : mkdir ~/.futuregrid/cloudmesh/ and then run the move : mv client_secrets.json ~/.futuregrid/cloudmesh/

Step 4: Running the Python Reservation command line
	1) After doing a git clone of the project run the command line arguments given in the example in the same order.
	2) New reservations can be added to the reservation_json_files folder using the `JSON Template <https://github.com/cloudmesh/reservation/blob/master/reservation_json_files/reservation_template>`_.


Command-line commands                         
======================================================================
	1) reservation.py add --file=FILE
    	2) reservation.py remove --reservation_id=RESERVATION_ID
    	3) reservation.py remove_all
    	4) reservation.py get_all
    	5) reservation.py get_from_label --label=LABEL
    	6) reservation.py get_by_user --user_id=USER_ID
    	7) reservation.py reschedule --reservation_id=RESERVATION_ID --file=FILE
    	8) reservation.py get_from_id --reservation_id=RESERVATION_ID
    	9) reservation.py duration --reservation_id=RESERVATION_ID
    	10) reservation.py list_by_project --proj_id=PROJ_ID
    	11) reservation.py list_by_user_and_project --user_id=USER_ID --proj_id=PROJ_ID --start=TIME_START --end=TIME_END
    
Example                         
======================================================================

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

Step1: Adding the 3 reservations to the google calendar

::

     /github/reservation/reservation$ python reservation.py add --file=../reservation_json_files/reservation1.json
     /github/reservation/reservation$ python reservation.py add --file=../reservation_json_files/reservation2.json
     /github/reservation/reservation$ python reservation.py add --file=../reservation_json_files/reservation3.json
     
Step2: Get all the reservation from the calendar
  
::

  /github/reservation/reservation$ python reservation.py get_all
   
Step3: Reschedule reservation 1 with reservation 2

::

     /github/reservation/reservation$ python reservation.py reschedule --reservation_id=c19qpuhq7g63urslvhi39d82h0 --file=../reservation_json_files/reservation2.json
   

Step4: Remove reservation 1

::

     /github/reservation/reservation$ python reservation.py remove --reservation_id=c19qpuhq7g63urslvhi39d82h0
   
Step5: Get the reservations by user id

::

     /github/reservation/reservation$ python reservation.py get_by_user --user_id=1001

Step6: Remove all reservations

::

     /github/reservation/reservation$ python reservation.py remove_all
   
Step7: Get the reservations by user id

::

     /github/reservation/reservation$ python reservation.py get_by_user --user_id=1001


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


Python API 
======================================================================
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

Google Calendar Event Object
======================================================================
 
The specification of the researvation is based on the JSON Calendar
object defined in the google documentation. Additional information is
included as part of the description field.  The Google API
documentation can be found `here
<https://developers.google.com/resources/api-libraries/documentation/calendar/v3/python/latest/calendar_v3.events.html#get>`_.
  
