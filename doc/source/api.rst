Prerequisit
=============

Instructions currently only working for debian, whatabout OSX????

::

  pip install -r requirements.txt

Google python client libraries
----------------------------------------------------------------------

::

  pip install --upgrade google-api-python-client

oauth2client library
----------------------------------------------------------------------

Download the oauth2client deb file from the link below via for example
the wget command

::

  wget http://code.google.com/p/google-api-python-client/downloads/detail?name=python-google-oauth2client_1.2.0-1_all.deb&can=2&q=

What is next????


httplib2 library
----------------------------------------------------------------------

  cd /tmp
  mkdir httplib2
  wget http://code.google.com/p/httplib2/downloads/list
  gzip -xvf ....
  cd ???
  python setup.py install' to install﻿﻿


Directory Structure of the project
----------------------------------------------------------------------

The directory structure is as follows::

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
