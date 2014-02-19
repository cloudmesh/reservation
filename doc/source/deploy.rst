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




