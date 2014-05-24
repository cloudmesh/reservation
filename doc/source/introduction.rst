Cloudmesh Reservation
======================================================================

This is a project under development.

Goal: Develop a reservation system for cloud virtual machines.

Design Features
----------------------------------------------------------------------

* REST interface 
* Commandline interface
* User Service: Users can schedule vms based on their own schedule 
* Admin Service: Custom OpenTSack scheduler interfaceing with
  reservations

The system will provide two unique services discussed next.

Code
-----

The code is located at:

* https://github.com/cloudmesh/reservation 

This documentation is located at:

* http://cloudmesh.futuregrid.org/reservation


User calendar based scheduling of VMs
----------------------------------------------------------------------

The first is a user side service, that allows users to use a calendar
service to schedule the creation and management of virtual machines.

.. note:: is this covered by heat?


A system wide reservation system for clouds
----------------------------------------------------------------------

The second service allows users to submit their reservations to a
global service managing also other users reservation. This service is
useful in case of resource starvation or the need to setup special
cloud environments that are needed by the users for a short period of
time.





