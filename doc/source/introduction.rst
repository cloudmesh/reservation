Cloudmesh Reservation
======================================================================

:Goal: 

  Develop a reservation system for the provisioning of virtual
  machines with the possibility to also use it for bare metal
  provisioning.

:Abstract:

  Cloudmesh Resource Reservation is being developed to create and
  manage reservations inside Cloudmesh. Cloudmesh is a project that
  includes the ability to conduct bare metal provisioning. It is
  important that this is supported in a multiuser environment. We will
  be developing for this a time based reservation system in which
  users will have access to resources based on time slices. This
  project will develop such a reservation system as a commandline tool
  and also as a GUI (if time permits while leveraging the work done by
  von Laszewski for this project). As a result we will have a simple
  commandline tool that allows the administrator or user to choose a
  reservation or query the system to find a suitable
  reservation. Limits will be put in place so that users do not
  reserve too many resources and block the systems while not allowing
  others to use it. The system will have an abstract plugin that
  allows the integration of a real bare metal provisioning. However,
  for this project, we will simulate it and focus only on the
  management of the reservation itself and not how they are used or
  how machines are leveraged for the actual bare metal
  provisioning. Convenient tables and views are developed as part of
  the GUI development which is doable as the GUI framework is already
  included in the project developed by von Laszewski.

:Keywords:

   resource reservation, provisioning, baremetal, virtual machines

:Authors:

  Gregor von Laszewski, Oliver Lewis Natiele Bohn

:Code:

  The code and documentation of this project are maintained in github
  at:

  * https://github.com/cloudmesh/reservation 

:Documentation:

   This documentation is located at:

   * http://cloudmesh.futuregrid.org/reservation

:Issues:

  Issues are located are located at:

  * https://github.com/cloudmesh/reservation/issues


Design Features
----------------------------------------------------------------------

The design features of the reservation framework include a number of
convenient interfaces. They include the following

:REST:

   A REST interface is provided to provide easy accessibility of the
   functionality through a variety of frameworks and different
   programming languages

:Commandline:

   A commandline interface is provides to integrate the reservation
   framework easily into scripting environments and allow access from
   a traditional compute terminal.

:Command Shell:

   A command shell is provided to allow the integration with cloudmesh
   so that the reservation framework can easily leverage the rich
   commandline set fro managing virtual machines. Furthermore it
   allows to script repeatable experiments more easily while
   leveraging the state that is contained in the command shell.

:Portal:

   A Web service framework is provided to allow easy access via a
   portal framework. The service can either be hosted in a shared
   environment or run stand allone on a users computer.

In addition the framework allows the exposure of admin and user
controlled features of the service:


:User Services: 

  Users can schedule vm's and bare metal resources based on their own
  scheduling requests

:Admin Services: 

  Administrators can grant access to specific resources to useres and
  projects.

  Administrators can furthermore include custom schedulers into the
  reservation framework to either automatize finding of suitable
  reservations or to adaot them to lead to better resource
  utilization.

The system will provide two unique services discussed next.


User calendar based scheduling of VMs
----------------------------------------------------------------------

The first is a user side service, that allows users to use a calendar
service to schedule the creation and management of virtual machines.


A system wide reservation system for clouds
----------------------------------------------------------------------

The second service allows users to submit their reservations to a
global service managing also other users reservation. This service is
useful in case of resource starvation or the need to setup special
cloud environments that are needed by the users for a short period of
time.





