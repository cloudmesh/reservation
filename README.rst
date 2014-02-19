Cloudmesh Reservation
======================================================================

This is a project under development.

Goal: Develop a reservation system for cloud virtual machines.

The documentation is maintained at

* http://cloudmesh.github.io/reservation

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
