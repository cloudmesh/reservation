Changing the scheduler in openstack
=============================

This section expects a devstack deployment. So if you have not
deployed devstack you should first take a look at the devstack
deployment.

The a scheduler in openstack can be make scheduling decisions in one
of the following ways:

#. Creating a new Scheduler from scratch:- Here we create new a brand
   new scheduler. The advantage of this approach is that we have
   complete freedom to create the scheduler in whatever way need. The
   disadvantage is that the openstack schedulers have a lot already
   built into them. We can not benefit from them.

#. Using the filtered scheduler provided by openstack and creating
   custom filters: Openstack has an inbuilt filtered scheduler. This
   filtered scheduler uses filters which tell if a host is available
   for booting the instance or not. Openstack already provides a
   number of filters and also a provision to create new filters. The
   advantage of this method is that any new filters can be combined
   with the existing filters as multiple filters can be specified to
   the filter scheduler. The disadvantage is that we are restricted to
   the filter based framework.

Important directories/files
----------------------------------------------------------------------

When you openstack is setup is setup(at least using dev-stack)q these
are some important directories::

   /opt/stack/nova

This is the nova project directory. This is the base folder for the
nova project. All your code has to be somewhere within this path. For
creating schedulers we are specifically interested in nova.scheduler
module and sub modules (/opt/stack/nova/nova/scheduler). Though the
filters can be placed anywhere within the nova project folder it would
be easier if we kept it within the scheduler module.

The nova configuration file::

  /etc/nova/nova.conf

Most of the configuration is kept in the configuration file called
nova.conf.

Changing the scheduler: As discussed above the for changing how
openstack schedules vm instances either a brand new scheduler can be
written or a new filter can be created and used with the existing
filtered_scheduler. In the further part of the document an example is
given for both.


Creating a brand new scheduler.
---------------------------------------------------------------------------------

This section is based on This openstack tutorial on creating a new
scheduler. For more reference the tutorial can be referred.  For
creating a new scheduler the nova.scheduler.driver.Scheduler has to be
implemented. This class has the following methods

#. update_service_capabilities
#. hosts_up
#. group_hosts
#. *schedule_run_instance - This is the method which schedules an
   instance. It contains a remote procedure call.
#. *select_destinations - This gives a list of destination hosts that
   can be used.

The methods with the * need to be implemented. The others have a
default implementation.

The code can be looked up from the
scripts/scheduler/ip_scheduler.py. Here the scheduler is implemented
as a random node selector based on IP and hostname. This file must be
placed in the /opt/stack/nova/nova/scheduler directory.  Also
host_name prefixes may have to be changed as per the names of your
host nodes. My host node is named ‘sridhar’ so I made changed the
hostname_prefix value to ‘sridhar’

Changes to the configuration file: 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Add the following to the nova.conf file (located under /etc/nova)::
    
    scheduler_driver=nova.scheduler.ip_scheduler.IPScheduler

Testing the scheduler
-------------------------

In dev stack the output is shown on different screens. Out of the
various screens we are interested in the n-sch screen (screen 10). If
you have your devstack running then the following command brings up
the screens::

	screen -r stack

This would not work if you already have screens open somewhere. Now
you need to go to screen 10. You could go to screen 9( Ctrl + A + 9)
and then do a next (Ctrl + A + N). All the output related to the
booting vms would be in on this screen.

Also after every change to either the filter/scheduler class or config
file, you need to exit(Ctrl + C) on this terminal and re-run the last
command. This will update to the latest version of the scheduler/
conf. *Do not forget to do this*.

To test the scheduler you will have to boot a new instance. But before
that you need to sort of provide the user information. The easy way to
do this is to go to where you have the devstack source files and enter
the devstack project. Once you have done that::
 
	$ source openrc ‘admin’

Now you will be working as admin. You can boot an instance. FOr
booting the instance do the following::

	$ nova boot <instance_name> --image=<image_id> --flavor=<flavor_id>

The available images and flavors can be looked up as follows.::

	$ nova image-list
	$ nova flavor-list

While selecting a flavor keep in mind how much memory you have on your
host machines. If the host machines do not have memory, it will cause
problems. For purpose of ease and testing you can use flavor = 1. If
boot is asynchronous and will give a details of the instance it is
trying to boot. Now to check the boot status you can do::

	$ nova list

Also if you look into the n-sch screen you will have log information
about the booting of the new instance.

Using the filtered scheduler and building a new custom filter: 
------------------------------------------------------------------------------

All filters need to do the following:

#. Inherit nova.scheduler.filters.BaseHostFilter
#. Implement host_passes method: This method for a given set of inputs
   returns a boolean value corresponding to whether the host passes
   the criteria posed by the filter. All the hosts that pass the
   criteria return true.

The code provided scripts/scheduler/temp.py is a cooked up example
which uses some pseudo data to check if the host passes the criteria
or no. You may have to change the host_names to correspond to the
values you have in your hosts list. Copy this file to
/opt/stack/nova/nova/scheduler/filters/ directory. This filter looks
up the temperature for the specific host from a made-up dictionary and
also the threshold value and passes the host if the temperature is
less than the threshold.

Modifying the Config file 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following lines need to be added to the nova.conf file::

    scheduler_driver = nova.scheduler.filter_scheduler.FilterScheduler
    scheduler_available_filters = nova.scheduler.filters.temp.BasicTempFilter
    scheduler_default_filters = BasicTempFilter

Here the first line tells that we would like to use the
filtered_scheduler. The second line tells us where to look for
available filters. There can be multiple lines for multiple
filters. Many examples talk about all the standard filters being
present under “nova.scheduler.filters.standard_filters”.  However with
my devstack version I could not find it. However we can add any of the
filters we need using the scheduler_available_filters. The
default_filters tells what default_filters you would like to use by
default. This can be a comma separated string if you want to specify
multiple filters. However it is necessary that the default filters are
included using available filters.

Testing
^^^^^^^

Testing can be done a way similar to the one explained in the
section where the scheduler is created from scratch.


Code
--------------------------------------------------------------------

The source files used in this example are

#. A new scheduler: scripts/scheduler/ip_scheduler.py

#. A filter for the filtered scheduler: scripts/scheduler/temp.py

Summary
---------------------------------------------------------------------

This tutorial assumes that the user has a devstack deployment.

Deployment: Building a new scheduler 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Copy scripts/scheduler/ip_scheduler.py file to the /opt/stack/nova/nova/scheduler

#. Make changes to the hostname in the file. Find the word ‘sridhar’
   and replace it with the hostname of your devstack node.

#. Add the following to the configuration file( /etc/nova/nova.conf)::

   scheduler_driver=nova.scheduler.ip_scheduler.IPScheduler

Deployment - Using existing filtered scheduler with new filters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Copy scripts/scheduler/temp.py file and place it in
/opt/stack/nova/nova/scheduler/filters/
https://drive.google.com/file/d/0B_8o1u7Zt7aWZFJPajhvZ3dUQTg/edit?usp=sharing

#. Change the host_name in the downloaded file to whatever your
   host_name. Search for the occurrence of the word ‘sridhar’. You can
   also add other hosts you have to the dictionary.

#. Add the following to the configuration(( /etc/nova/nova.conf))
   scheduler_driver = nova.scheduler.filter_scheduler.FilterScheduler
   scheduler_available_filters =
   nova.scheduler.filters.temp.BasicTempFilter scheduler_default_filters
   = BasicTempFilter

Testing:
^^^^^^^^^^^^^^^

#. If you dont have the screen running start them::
	
    $ screen -r stack

#. Navigate to the n-sch screen(screen 10). All your output regarding
   booting instances can be seen on this terminal::

	Ctrl + A + 9
	Ctrl + A + N

#. If the screen was already running after you made changes do the
   following. Do this every time you change the configuration file or
   code::

	Ctrl + C				exit
	Run the last command.		(up arrow and return)

#. On a new terminal go to the devstack source directory and run::

	$ source openrc admin

#. Copy the image id of favorite image. Image-ids can be obtained by::

	$ nova image-list

#. Boot instance using::

	$ nova boot <instance_name> --image=<image_id> --flavor=1

#. View status(gives status of all instances booted)::

	$ nova list

#. See the n-sch screen if there were any errors

