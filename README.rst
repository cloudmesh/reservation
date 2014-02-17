Cloudmesh Reservation
======================================================================

This is a project under development.

Goal: Develop a reservation system for cloud virtual machines.

Deasign Features
----------------------------------------------------------------------

* REST interface 
* Commandline interface
* User Service: Users can schedule vms based on their own schedule 
* Admin Service: Custom OpenTSack scheduler interfaceing with
  reservations

The system will provide two unique services discussed next.

User calanedar based scheduling of VMs
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


Design
========

REST interfaces
----------------------------------------------------------------------

Initial starting point::

  cm/v1.0/reservation/

  def list
	lists the reservation

  cm/v1.0/reservation/<label>

  def get (label)
        gets the reservation with the given label

  cm/v1.0/reservation/add/<label>/<resource>/<from>/<to>
  
  def get (label)
        gets the reservation with the given label

  cm/v1.0/reservation/delete/<label>/<resource>/<from>/<to>

  def get (label)
        gets the reservation with the given label


  cm/v1.0/reservation/delete/<label>/<cell><cloud>/<region>/<aggregate>/<numberofvms>/<from>/<to>

  def get (label)
        gets the reservation with the given label


.. list-table:: REST Interface
   :widths: 15 10 30
   :header-rows: 1

   * - HTTP Method
     - URI
     - Action
   * - GET
     - cm/v1.0/reservation/
     - list all available reservations
   * - GET
     - cm/v1.0/reservation/<label>
     - List all reservations with a given label
   * - ...
     - ...
     - ...
