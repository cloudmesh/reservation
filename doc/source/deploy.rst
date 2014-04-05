Deployment
======================================================================

Multi-Node OpenStack Install
----------------------------------------------------------------------

The vagrant script below uses the cookbooks from Rackspace to setup a 
cluster with the following nodes:

* Chef
* Controller
* Compute1
* Compute2
* Cinder

The steps to be followed to create a cluster for the above nodes are 
given below:

* mkdir havana
* cd havana
* vagrant init
* Replace the contents of the Vagrantfile generated in the previous step with the contents below::

  # -*- mode: ruby -*-
  # vi: set ft=ruby :
 
  VAGRANTFILE_API_VERSION = "2"
  $script = <<SCRIPT
  echo root:vagrant | chpasswd
  cat << EOF >> /etc/hosts
   192.168.236.10 chef
   192.168.236.11 controller
   192.168.236.12 compute1
   192.168.236.13 compute2
   192.168.236.14 cinder
  EOF
  SCRIPT
  Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
 
  config.vm.box = "precise64"
 
  # Turn off shared folders
  config.vm.synced_folder ".", "/vagrant", id: "vagrant-root", disabled: true
 
  # Begin chef
  config.vm.define "chef" do |chef_config|
   chef_config.vm.hostname = "chef"
   chef_config.vm.provision "shell", inline: $script
   # eth1 configured in the 192.168.236.0/24 network
   chef_config.vm.network "private_network", ip: "192.168.236.10"
 
   chef_config.vm.provider "virtualbox" do |v|
    v.customize ["modifyvm", :id, "--memory", "512"]
    v.customize ["modifyvm", :id, "--cpus", "1"]
   end
  end
  # End chef
 
 # Begin controller
  config.vm.define "controller" do |controller_config|
   controller_config.vm.hostname = "controller"
   controller_config.vm.boot_timeout = 600
   controller_config.vm.provision "shell", inline: $script
   # eth1 configured in the 192.168.236.0/24 network
   controller_config.vm.network "private_network", ip: "192.168.236.11"

   controller_config.vm.provider "virtualbox" do |v|
    v.customize ["modifyvm", :id, "--memory", "2048"]
    v.customize ["modifyvm", :id, "--cpus", "1"]
   end
  end
  # End controller
 
  # Begin compute1
  config.vm.define "compute1" do |compute1_config|
   compute1_config.vm.hostname = "compute1"
   compute1_config.vm.provision "shell", inline: $script
   # eth1 configured in the 192.168.236.0/24 network
   compute1_config.vm.network "private_network", ip: "192.168.236.12"
 
   compute1_config.vm.provider "virtualbox" do |v|
    v.customize ["modifyvm", :id, "--memory", "1024"]
    v.customize ["modifyvm", :id, "--cpus", "2"]
    # eth2 left unconfigured so the Chef Cookbooks can configure it
    v.customize ["modifyvm", :id, "--nic3", "intnet"]
   end
  end
  # End compute1
  
  # Begin compute2
  config.vm.define "compute2" do |compute2_config|
   compute2_config.vm.hostname = "compute2"
   compute2_config.vm.provision "shell", inline: $script
   # eth1 configured in the 192.168.236.0/24 network
   compute2_config.vm.network "private_network", ip: "192.168.236.13"
 
   compute2_config.vm.provider "virtualbox" do |v|
    v.customize ["modifyvm", :id, "--memory", "1024"]
    v.customize ["modifyvm", :id, "--cpus", "2"]
    # eth2 left unconfigured so the Chef Cookbooks can configure it
    v.customize ["modifyvm", :id, "--nic3", "intnet"]
   end
  end
  # End compute2
  # Begin cinder
  config.vm.define "cinder" do |cinder_config|
   cinder_config.vm.hostname = "cinder"
   cinder_config.vm.provision "shell", inline: $script
   # eth1 configured in the 192.168.236.0/24 network
   cinder_config.vm.network "private_network", ip: "192.168.236.14"

   cinder_config.vm.provider "virtualbox" do |v|
    v.customize ["modifyvm", :id, "--memory", "512"]
    v.customize ["modifyvm", :id, "--cpus", "1"]
   end
  end
  # End cinder
end

* Save the Vagranfile
* Run the command: vagrant up 

For today
------------------------

Download repository and setup sphinx for documentation::
  mkdir ~/github
  git clone https://github.com/cloudmesh/reservation.git
  cd reservation
  virtualenv ~/ENV
  . ~/ENV/bin/activate
  pip install sphinx
  pip install -r requirements.txt
  make sphinx
  pip install sphinxcontrib-exceltable
  pip install sphinx_bootstrap_theme

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
