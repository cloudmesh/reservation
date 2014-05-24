**********************************************************************
Multiworker Devstack for Vagarnt
**********************************************************************

.. sidebar::  
  .
  
  .. contents::
     :depth: 5

..

The procedure below deploys Devstack with multiple workers from devstack source code. The vagrant script below sets up a cluster with the following nodes:

* Controller
* Compute1
* Compute2


Requirements
===============================

VirtualBox
----------------------------------------------------------------------

You must have virtualbox installed. Please follow the documentation at
http://www.virtualbox.org to install it.

Cookiecutter
----------------------------------------------------------------------
You need to have cookiecutter installed, please do this with::

  pip install cookiecutter


Vagrant
----------------------------------------------------------------------

Before you start you need to make sure you have vagrant
installed. Please follow the instructions provided at 
http://www.vagrantup.com/downloads.html. 

Make sure you have at least the version `1.5.4` which you
can find out via::

  vagrant --version

To execute the steps documented her, yo uwill first need to make sure
that you have the vagrant-hostmanage installed::

   vagrant plugin install vagrant-hostmanager



Setup
======================================================================

The setup is easily achieved via cookiecutter, which will
create a new directory with the appropriate scripts and configuration
parameters. It will ask you for a number of parameters such as

* a label, that will be appended to the directory name where the
  scripts are located
* a password for the admin
* a password for the services
* a token for the services

Please do not use the defaults for the passwords and teh tokens, but
define your own strong versions.

To create the directory with the scripts, simply call::

  cookiecutter https://github.com/cloudmesh/cookiecutter-multinode-devstack.git

Than you will find a directory called multinode-<label> 

You can than cd in this directory and inspect the scripts::

  $ cd multidevstack-<TAB>

Run the command:: 

  $ vagrant up


The command will bring up all the nodes: controller, compute1 and compute2.

After the successful instalation, the Horizon dashboard will be
available at::

  http://192.168.236.11 

You can use the username "**admin**" and password that you have
defined with the help of cookiecutter. When the VMs are restarted, we
will need to run the following::
  
  $ cd devstack
  $ ./rejoin-stack.sh

on all the nodes to rejoin the screens started by stack.sh 


Shell Scripts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Controller - install-controller.sh
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`install-controller.sh <https://github.com/cloudmesh/reservation/blob/master/scripts/multinode/install-controller.sh>`_



.. include:: ../../scripts/multinode/install-controller.sh
   :literal:


Compute - install-compute.sh
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`install-compute.sh <https://github.com/cloudmesh/reservation/blob/master/scripts/multinode/install-compute.sh>`_



.. include:: ../../scripts/multinode/install-compute.sh
   :literal:

Vagrantfile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Vagrantfile <https://github.com/cloudmesh/reservation/blob/master/scripts/multinode/Vagrantfile>`_



.. include:: ../../scripts/multinode/Vagrantfile
   :literal:





