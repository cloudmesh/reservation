Deployment
======================================================================

For today
------------------------

::
    mkdir ~/github
    git clone https://github.com/cloudmesh/reservation.git

    cd reservation
    virtualenv ~/ENV
    . ~/ENV/bin/activate
    pip install sphinx
    pip install -r requirements.txt
    make sphinx
    sudo pip install sphinxcontrib.exceltable
    sudo pip install sphinx_bootstrap_theme

Virtualenv
----------------------------------------------------------------------

set up virtualenv as documented in the main cloudmesh documentation

put link here
TBD

Requirements
----------------------------------------------------------------------

After you have set up virtualenv, you instal the requirements with::

  pip install -r requirements.txt


Install
----------------------------------------------------------------------

As the reservation interface is not yet uploaded to pip, you need to
call in the main directory::

  python setup.py install


Directory Structure of the project
----------------------------------------------------------------------

The directory structure is as follows::

  -------reservation
               |
               |-----reservation
                         |---reservation.py
                         |---cm_reservation.py
               |-----etc
                         |---researvation_config.json







Publishing the Documentation
----------------------------------------------------------------------

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
