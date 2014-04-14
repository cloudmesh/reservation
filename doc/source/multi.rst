Deploying Openstack from devstack source with multiple workers using Vagrant
============================================================================

Multi-Node OpenStack Install
----------------------------------------------------------------------

The procedure below deploys Devstack with multiple workers from devstack source code. The vagrant script below sets up a cluster with the following nodes:

* Controller
* Compute1
* Compute2


The steps to be followed to create a cluster for the above nodes are 
given below:

* mkdir multiworker
* cd multiworker
* create two scripts **installController.sh** and **installCompute.sh** (Steps are shown below)
* vagrant init

Create a file **installController.sh** with the contents shown below::

  #!/bin/bash

  #################################################################################################################
  # Author        : Aravindh Varadharaju
  # Date          : 6th April 2014
  # Purpose       : Controller Script to setup the controller node
  # Script source : http://stackoverflow.com/questions/16768777/can-i-switch-user-in-vagrant-bootstrap-shell-script
  #################################################################################################################
  case $(id -u) in
      0) 
          sudo ufw disable
          sudo apt-get -q -y update
          sudo apt-get install -y git
          sudo apt-get install -y python-pip
          
          git clone https://github.com/openstack-dev/devstack.git
          chown -R vagrant:vagrant devstack
     
          # When creating the stack deployment for the first time,
          # you are going to see prompts for multiple passwords.
          # Your results will be stored in the localrc file.
          # If you wish to bypass this, and provide the passwords up front,
          # add in the following lines with your own password to the localrc file

          echo '[[local|localrc]]' > local.conf
          echo MULTI_HOST=1 >> local.conf
          echo LOGFILE=/home/vagrant/stack.sh.log >> local.conf
          echo ADMIN_PASSWORD=labstack >> local.conf
          echo MYSQL_PASSWORD=supersecret >> local.conf
          echo RABBIT_PASSWORD=supersecrete >> local.conf
          echo SERVICE_PASSWORD=supersecrete >> local.conf
          echo SERVICE_TOKEN=1qaz2wsx >> local.conf

          mv local.conf /home/vagrant/devstack
          chown vagrant:vagrant /home/vagrant/devstack/local.conf
          
          sudo -u vagrant -i $0  # script calling itself as the vagrant user
          ;;
      *) 
          cd /home/vagrant/devstack
          ./stack.sh
          ;;
  esac

Create a file **installCompute.sh** with the contents shown below::

  #!/bin/bash

  #################################################################################################################
  # Author        : Aravindh Varadharaju
  # Date          : 6th April 2014
  # Purpose       : Compute Script to set up Compute Nodes
  # Script source : http://stackoverflow.com/questions/16768777/can-i-switch-user-in-vagrant-bootstrap-shell-script
  #################################################################################################################
  case $(id -u) in
      0) 
          sudo ufw disable
          sudo apt-get -q -y update
          sudo apt-get install -y git
          sudo apt-get install -y python-pip
          
          git clone https://github.com/openstack-dev/devstack.git
          chown -R vagrant:vagrant devstack
     
          # When creating the stack deployment for the first time,
          # you are going to see prompts for multiple passwords.
          # Your results will be stored in the localrc file.
          # If you wish to bypass this, and provide the passwords up front,
          # add in the following lines with your own password to the localrc file

          echo '[[local|localrc]]' > local.conf
          echo MULTI_HOST=1 >> local.conf
          echo LOGFILE=/home/vagrant/stack.sh.log >> local.conf
          echo ADMIN_PASSWORD=labstack >> local.conf
          echo MYSQL_PASSWORD=supersecret >> local.conf
          echo RABBIT_PASSWORD=supersecrete >> local.conf
          echo SERVICE_PASSWORD=supersecrete >> local.conf
          echo SERVICE_TOKEN=1qaz2wsx >> local.conf
          echo DATABASE_TYPE=mysql >> local.conf
          echo SERVICE_HOST=192.168.236.11 >> local.conf
          echo MYSQL_HOST=192.168.236.11 >> local.conf
          echo RABBIT_HOST=192.168.236.11 >> local.conf
          echo GLANCE_HOSTPORT=192.168.236.11:9292 >> local.conf
          echo ENABLED_SERVICES=n-cpu,n-net,n-api,c-sch,c-api,c-vol >> local.conf

          mv local.conf /home/vagrant/devstack
          chown vagrant:vagrant /home/vagrant/devstack/local.conf
          
          sudo -u vagrant -i $0  # script calling itself as the vagrant user
          ;;
      *) 
          cd /home/vagrant/devstack
          ./stack.sh
          ;;
  esac


Replace the contents of the Vagrantfile generated in the previous step with the contents below::

  ########################################################################
  # Name        : Vagrantfile
  # Author      : Cloudmesh Team
  # Description : The code is based on the setup guide from the URL given: 
  #               http://devstack.org/guides/multinode-lab.html
  # Note        : When new workers need to be added, an entry needs to be
  #             : put under section $script and under workers = [] section
  ########################################################################

  # -*- mode: ruby -*-
  # vi: set ft=ruby :
   
  VAGRANTFILE_API_VERSION = "2"
  $script = <<SCRIPT
  echo root:vagrant | chpasswd
  cat << EOF >> /etc/hosts
  192.168.236.11 controller
  192.168.236.12 compute1
  192.168.236.13 compute2
  EOF
  SCRIPT

  workers = [{name: 'compute1', ip: '192.168.236.12'},
             {name: 'compute2', ip: '192.168.236.13'}]

  Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
   
    config.vm.box = "precise64"
   
    # Turn off shared folders
    config.vm.synced_folder ".", "/vagrant", id: "vagrant-root", disabled: true
   
   # Begin controller
    config.vm.define "controller" do |controller_config|
      controller_config.vm.hostname = "controller"
      controller_config.vm.boot_timeout = 600
      controller_config.vm.provision "shell", inline: $script
      # eth1 configured in the 192.168.236.0/24 network
      controller_config.vm.network "private_network", ip: "192.168.236.11"
      controller_config.vm.provision "shell", path: "installController.sh"
      controller_config.vm.network "forwarded_port", guest: 80, host: 8000
      controller_config.vm.network "forwarded_port", guest: 5000, host: 6000

      controller_config.vm.provider "virtualbox" do |v|
          v.customize ["modifyvm", :id, "--memory", "2048"]
          v.customize ["modifyvm", :id, "--cpus", "1"]
      end
    end
    # End controller

    # Begin Workers
    workers.each do |host|
      config.vm.define host[:name] do |node|
      node.vm.hostname = host[:name]
      node.vm.provision "shell", inline: $script
      node.vm.network :private_network, ip: host[:ip], netmask: '255.255.255.0'
      node.vm.provision "shell", path: "installCompute.sh"
      node.vm.provider "virtualbox" do |v|
        v.customize ["modifyvm", :id, "--memory", "1024"]
        v.customize ["modifyvm", :id, "--cpus", "2"]
        v.customize ["modifyvm", :id, "--nic3", "intnet"]
      end
      end
    end
    # End Workers
  end

* Save the Vagranfile
* Run the command: **vagrant up**
* The command will bring up all the nodes: controller, compute1 and compute2.
* Horizon Dashboard should now be available at https://192.168.236.11. The user name is "**admin**" and password is "**labstack**" 
* When the VMs are restarted, we need to run **rejoin-stack.sh** on all the nodes to kind of restart devstack. 

