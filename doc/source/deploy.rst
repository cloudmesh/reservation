Deployment
======================================================================

Virtualenv
----------------------------------------------------------------------

set up virtualenv as documented in the main cloudmesh documentation

put link here
TBD

Requirements
----------------------------------------------------------------------

After you have set up virtualenv, you instal the requirements with::

  pip install -r requirements.txt



oauth2client library
----------------------------------------------------------------------

Download the oauth2client deb file from the link below via for example
the wget command

::

  wget http://code.google.com/p/google-api-python-client/downloads/detail?name=python-google-oauth2client_1.2.0-1_all.deb&can=2&q=

What is next????



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





Code Development
----------------------------------------------------------------------

We have not yet set up a setup.py environment. Thus for now go into the::

  ./reservation 

directory and modify the code there.

Controling the server
======================================================================

The server can be started from the main repository directory with::

  fab server.start

It can be stapped with::

  fab server.stop


Publishing the Documentation
======================================================================

Developers have the ability to change the documentation in the::

  ./doc/souce

directory. Once done they can create a local updated documenation for
checking with::

  make sphinx

To view it they can say::

  make view

To publish the new documentation to github they can say::

  make gh-pages

.. warning:: the publication is typically done by Gregor von Laszewski
	     upon request from a developer. Please make sure that
	     **all** commits are merged and in the repository. Also
	     the documentation has to be checked with a local make.
