#!/bin/bash

#install the repo packege and apache
yum -y install createrepo httpd

#turn off enforcement
setenforce 0

#create the following directories
mkdir -p /repos/CentOS/7/Packages/

#create the repo in the directory
createrepo /repos/CentOS/7/Pakages

#enabling ad starting apache
systemctl enable httpd
systemctl start httpd

#link the html website to the directories created
ln -s /var/www/html/centos /repos/CentOS

sed -i 's/^/#/' /etc/httpd/conf.d/welcome.conf

#restart apache
systemctl restart httpd

