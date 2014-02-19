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
