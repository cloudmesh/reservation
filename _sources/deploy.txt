Deployment
======================================================================

.. sidebar:: 
   . 

  .. contents:: Table of Contents
     :depth: 5

..

Virtualenv
----------------------------------------------------------------------

Set up `virtual env as described in the main cloudmesh documentation <http://cloudmesh.futuregrid.org/cloudmesh/developer.html#virtualenv>`_.


Requirements
----------------------------------------------------------------------

After you have set up virtualenv, you install the requirements with::

  pip install -r requirements.txt


Install
----------------------------------------------------------------------

As the reservation interface is not yet uploaded to pip, you need to
call in the main directory::

  python setup.py install


Publishing the Documentation
----------------------------------------------------------------------

Developers have the ability to change the documentation in the::

  ./doc/source

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

Steps in a nutshell
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Download repository from github and setup sphinx for documentation::

 mkdir ~/github
 git clone https://github.com/cloudmesh/reservation.git
 cd reservation
 virtualenv ~/ENV
 . ~/ENV/bin/activate
 pip install sphinx
 pip install -r requirements.txt
 make sphinx
 make view
 
Mongo
----------------------------------------------------------------------

To start the mongo db use the command

::

   make start

This will start the db in ~/data. If the data directory is not
existing, it will be created.


To test the service, you can say::

   ./reservation/test.py

To generate some random schedules yo can use the gnerate command,
which is documented in more detail in the manual page::

   put the location here

To clean the reservations (not yet implemented you can say)::

   ./reservation/generate.py clean

Server
----------------------------------------------------------------------

A test server exists that interfaces via http routes to the backend
system. To use it you need sto first start the mongo server in a
terminal with the command describbed in the previous section::

  make mongo

Next you will need to start the server in a different terminal with::

  make server

Now the server and mongo db are started. we assume you have added some
data with for example the test command in yet a different window::

  make test

Now you can open your web browser at::

  http://127.0.0.1:5000

To observe a list of reservations in table form 

To create a random reservation you can use::

  make random
