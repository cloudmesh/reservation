
REST interfaces
==============================

test
----------------------------------------------------------------------
.. autoflask:: reservation.server:app
   :undoc-static:


test2
----------------------------------------------------------------------
.. http:get:: /users/(int:user_id)/posts/(tag)

   The posts tagged with `tag` that the user (`user_id`) wrote.

   **Example request**:

   .. sourcecode:: http

      GET /users/123/posts/web HTTP/1.1
      Host: example.com
      Accept: application/json, text/javascript

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: text/javascript

      [
        {
          "post_id": 12345,
          "author_id": 123,
          "tags": ["server", "web"],
          "subject": "I tried Nginx"
        },
        {
          "post_id": 12346,
          "author_id": 123,
          "tags": ["html5", "standards", "web"],
          "subject": "We go to HTML 5"
        }
      ]

   :query sort: one of ``hit``, ``created-at``
   :query offset: offset number. default is 0
   :query limit: limit number. default is 30
   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :reqheader Authorization: optional OAuth token to authenticate
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: no error
   :statuscode 404: there's no user



Initial starting point. This text will be removed and put into the
list-table::

  cm/v1.0/reservation/

  def list
	lists the reservation

  cm/v1.0/reservation/<label>

  def get (label)
        gets the reservation with the given label

  cm/v1.0/reservation/add/<label>/<resource>/<from>/<to>
  
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


