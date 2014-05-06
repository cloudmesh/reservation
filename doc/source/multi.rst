Multiworker Devstack for Vagarnt
============================================================================

.. sidebar:: 
   . 

  .. contents:: Table of Contents
     :depth: 5

..


Requirements:

* VirtualBox
* Vagrant
* vagrant-hostmanager plugin


Multi-Node OpenStack Install
----------------------------------------------------------------------

The procedure below deploys Devstack with multiple workers from devstack source code. The vagrant script below sets up a cluster with the following nodes:

* Controller
* Compute1
* Compute2

Prerequisits
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before you start you need to make sure you have vagrant
installed. Make sure you have at least the version `1.5.4` which you
can find out via::

  vagrant --version

To execute the steps documented her, yo uwill first need to make sure
that you have the vagrant-hostmanage installed::

   vagrant plugin install vagrant-hostmanager

Setup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The steps to be followed to create a cluster for the above nodes are 
given below::

  $ mkdir multiworker
  $ cd multiworker

Download the three scripts from the location:
https://github.com/cloudmesh/reservation/tree/master/scripts/multinode::

  $ export GITHUB_DIR=https://github.com/cloudmesh/reservation/tree/master
  $ wget $GITHUB_DIR/scripts/multinode/Vagrantfile
  $ wget $GITHUB_DIR/scripts/multinode/install-compute.sh 
  $ wget $GITHUB_DIR/scripts/multinode/install-controller.sh 

Run the command:: 

  $ vagrant up


The command will bring up all the nodes: controller, compute1 and compute2.

After the successful instalation, the Horizon dashboard will be
available at::

  http://192.168.236.11 

.. note::

   THIS IS WRONG. we want in the exampl to be able to configure
   username and password. and not just take some default values.

The user name is "**admin**" and password is "**labstack**" 
When the VMs are restarted, we need to run::

  rejoin-stack.sh

on all the nodes to rejoin the screens started by stack.sh 

SOMETHING ELSE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Save the Vagranfile
* Run the command: **vagrant up**
* The command will bring up all the nodes: controller, compute1 and compute2.
* Horizon Dashboard should now be available at http://192.168.236.11. The user name is "**admin**" and password is "**labstack**" 
* When the VMs are restarted, we need to run **rejoin-stack.sh** on all the nodes to kind of restart devstack. 




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





