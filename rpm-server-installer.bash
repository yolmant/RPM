#!/bin/bash

#install the rpm packages
sudo yum -y install rpm-build

#create a new evironment for rpm
mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
echo '%_topdir %(echo $HOME)/rpmbuild' > ~/.rpmmacros

#install yum tools package
sudo yum -y install yum-utils

#modify the files to enable repo
sudo sed -i 's,enabled=0,enabled=1,g' /etc/yum.repos.d/CentOS-Sources.repo

#try to download rpm packages
#for example yumdowloader --source tree
#to generate an RPM package you need to create a source of the scripts you will package and create the .spec file
#then create an tar.gz file fromm the directory in the /SOURCES with tar czvf file.tar.gz file
#create the RPM rpmbuild -bb SPECS/file.spec or rpmbuild -v -bb --clean SPECS/file.spec
