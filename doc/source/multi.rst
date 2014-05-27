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

Install the requirements::
----------------------------------------------------------------------

  $ mkdir ~/github
  $ cd ~/github
  $ git clone https://github.com/cloudmesh/reservation.git
  $ cd reservation
  $ pip install -r requirements.txt

Install VirtualBox and Vagrant::
----------------------------------------------------------------------

  $ ./install-prereq.sh

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

After the successful installation, the Horizon dashboard will be available at::

  http://192.168.236.11 

You can use the username "**admin**" and password that you have
defined with the help of cookiecutter. When the VMs are restarted, we
will need to run the following on all the nodes to rejoin the screens started by stack.sh::
  
  $ cd devstack
  $ ./rejoin-stack.sh



.. note ::
  
  The section below shows the contents of the three scripts that would be created when you do "cookiecutter https://github.com/cloudmesh/cookiecutter-multinode-devstack.git".

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





