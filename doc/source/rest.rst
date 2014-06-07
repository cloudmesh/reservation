
REST interfaces
==============================

The Server has the following routes

.. autoflask:: reservation.server:app
   :undoc-static:



Initial starting point. This text will be removed and put into the
list-table::



  cm/v1.0/reservation/
  
  def add (label)
        adds the reservation with the given label

  cm/v1.0/reservation/delete/<label>

  def get (label)
        gets the reservation with the given label


  cm/v1.0/reservation/delete/<label>/<cell><cloud>/<region>/<aggregate>/<numberofvms>/<from>/<to>

  def get (label)
        gets the reservation with the given label


.. list-table:: REST Interface
   :widths: 15 10 30 15
   :header-rows: 1

   * - HTTP Method
     - URI
     - Action
     - Python Client
   * - GET
     - cm/v1.0/reservation/
     - List all available reservations
     - list()
   * - GET
     - cm/v1.0/reservation/<label>
     - List all reservations with a given label
     - list(label)
   * - ...
     - ...
     - ...
     - ...
       

References for REST
----------------------------------------------------------------------

* Designing Flask REST Interfaces:
  http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
* Designing Flask REST Interfaces, part2:
http://blog.miguelgrinberg.com/post/designing-a-restful-api-using-flask-restful
* Requests: http://requests.readthedocs.org/en/latest/


