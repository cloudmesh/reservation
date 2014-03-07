DevStack
---------------------------------------------------------------------

We asume you have virtualbox and vagrant installed. This procedure will guide you to install OpenStack using DevStack. The procedure will be carried out using Shell Script Provisioner available with Vagrant. There are other standard Provisioning tools such as Chef and Puppet available. For now we will use the Shell Script Provisioner for ease of use. The steps to be followed in a nutshell is given below:

* Have Virtual Box and Vagrant installed
* Create Vagrantfile using **vagrant init** command
* Create a shell script named **install.sh** (or a different name) with the steps to install OpenStack
* Amend the Vagrantfile to call the script

The install.sh script is shown below::

 #! /usr/bin/env bash

 echo "Installing git ...."
 apt-get update >/dev/null 2>&1
 apt-get install -y git >/dev/null 2>&1
 echo "Cloning devstack from devstack ...."
 git clone https://github.com/openstack-dev/devstack.git
 echo "Deploying OpenStack Cloud ...."
 echo "This will take a while to setup ...."
 echo " "
 echo "####################################"
 echo "#        PLEASE BE PATIENT         #"
 echo "####################################"
 echo " "
 cd /home/vagrant/devstack/tools
 chmod +x create-stack-user.sh
 ./create-stack-user.sh
 chown -R stack:stack /home/vagrant/devstack
 cd /home/vagrant/devstack
 sudo -u stack ./stack.sh

The above script needs to be placed in the project directory where the Vagrantfile is present. The next task is to modify the Vagrant file to call the shell script just created.

Add the following line to the Vagrantfile::

  config.vm.provision "shell", path: "install.sh"

Once the file is saved, run the following commands to rebuilt the VM through Vagrant::

 vagrant destroy
 vagrant up

This would take some time to run as OpenStack installation takes around 10 - 15 minutes.
