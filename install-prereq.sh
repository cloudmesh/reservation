#!/bin/bash
echo "------------------------------------------------"
echo "Installing VirtualBox......Please be patient...."
echo "------------------------------------------------"
sudo sh -c "echo 'deb http://download.virtualbox.org/virtualbox/debian '$(lsb_release -cs)' contrib non-free' > /etc/apt/sources.list.d/virtualbox.list"
wget -q http://download.virtualbox.org/virtualbox/debian/oracle_vbox.asc -O- | sudo apt-key add -
sudo apt-get update
sudo apt-get install virtualbox-4.3 dkms
echo "------------------------------------------------"
echo "Installing Vagrant........Please be patient....."
echo "------------------------------------------------"
wget https://dl.bintray.com/mitchellh/vagrant/vagrant_1.6.2_x86_64.deb
dpkg -i vagrant_1.6.2_x86_64.deb
vagrant plugin install vagrant-hostmanager
echo "------------------------------------------------"
echo "Installing Virtualenv.....Please be patient....."
echo "------------------------------------------------"
apt-get install python-virtualenv
echo "------------------------------------------------"
echo "Installing Git........Please be patient........."
echo "------------------------------------------------"
apt-get install git
apt-get install python-dev
echo "------------------------------------------------"
echo "Installed VirtualBox Version: " && vboxmanage --version
echo "Installed Vagrant Version: " && vagrant --version
echo "Installed Virtualenv Version: " && virtualenv --version
echo "Installed Git Version: " && git --version
echo "Installation complete!!"
echo "------------------------------------------------"
