You need 3 libraries to set up the Calendar API.
=========================================================

    The google python client libraries
    oauth2client library
    httplib2 library

* Step 1: Install Client Libraries
  * **pip install --upgrade google-api-python-client

* Step 2: Download the oauth2client deb file from the link below:
  * **http://code.google.com/p/google-api-python-client/downloads/detail?name=python-google-oauth2client_1.2.0-1_all.deb&can=2&q=

* Step 3: Download the httplib2 from the URL below.

  * **http://code.google.com/p/httplib2/downloads/list

  * **run 'python setup.py install' to install﻿﻿

----------------------------------------------------------
The project structure is as follows:
-------Reservation
               |
               |
               |------lib
                         |---google-api-python-client
                         |---oauth2client
                         |---httplib2
               |
               |-----src
                         |---client_secrets.json
                         |---Main.dat
                         |---Main.py
                         |---ReservationServiceEvents.py
