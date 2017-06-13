Name:		plugins
Version:	1.0
Release:	1%{?dist}
Summary:	this is nagios nrpe plugins

Group:		nti320
License:	GPL
URL:		https://github.com/yolmant/RPM
Source0:	plugins-1.0.tar.gz

Requires:	bash

%description
it will install a new pluginis and preparer the host for the nagios server

%prep

%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/lib64/nagios/plugins
install -m 0755 check_Python %{buildroot}/usr/lib64/nagios/plugins/check_Python
install -m 0755 check_django_connection %{buildroot}/usr/lib64/nagios/plugins/check_django_connection
install -m 0755 check_httpd_django %{buildroot}/usr/lib64/nagios/plugins/check_httpd_django

%clean
rm -rf %{buildroot}

%files
/usr/lib64/nagios/plugins/check_httpd_django
/usr/lib64/nagios/plugins/check_django_connection
/usr/lib64/nagios/plugins/check_Python

%post
#installing all the necessary packages
yum -y install httpd nrpe nagios-plugins-all wget

#adding check_mem plugin
sudo cd /usr/lib64/nagios/plugins/
sudo wget https://raw.githubusercontent.com/justintime/nagios-plugins/master/check_mem/check_mem.pl
sudo mv check_mem.pl check_mem
sudo chmod +x check_mem

#modify the nrpe file configuration to connect with the server
sudo sed -i "s/allowed_hosts=127.0.0.1/allowed_hosts=127.0.0.1,10.128.0.0\/24/" /etc/nagios/nrpe.cfg
sudo sed -i "s/dont_blame_nrpe=0/dont_blame_nrpe=1/" /etc/nagios/nrpe.cfg

#adjust nrpe command definitions
sudo sed -i "215i command[check_disk]=\/usr\/lib64\/nagios\/plugins\/check_disk -w 20% -c 10% -p \/dev\/sda1" /etc/nagios/nrpe.cfg
sudo sed -i "216i command[check_procs]=\/usr\/lib64\/nagios\/plugins\/check_procs -w 150 -c 200" /etc/nagios/nrpe.cfg
sudo sed -i "217i command[check_mem]=/usr/lib64/nagios/plugins/check_mem  -f -w 20 -c 10" /etc/nagios/nrpe.cfg

sudo chown nagios:nagios /usr/lib64/nagios/plugins/check_httpd_django
sudo chown nagios:nagios /usr/lib64/nagios/plugins/check_django_connection
sudo chown nagios:nagios /usr/lib64/nagios/plugins/check_Python

sudo chmod +x /usr/lib64/nagios/plugins/check_httpd_django
sudo chmod +x /usr/lib64/nagios/plugins/check_django_connection
sudo chmod +x /usr/lib64/nagios/plugins/check_Python

sudo sed -i "218i command[check_httpd_django]=/usr/lib64/nagios/plugins/check_httpd_django" /etc/nagios/nrpe.cfg
sudo sed -i "218i command[check_django_connection]=/usr/lib64/nagios/plugins/check_django_connection" /etc/nagios/nrpe.cfg
sudo sed -i "218i command[check_Python]=/usr/lib64/nagios/plugins/check_Python" /etc/nagios/nrpe.cfg

#star and enable all the services
sudo systemctl enable nrpe httpd
sudo systemctl start nrpe httpd

%doc

%changelog
*Tue Jun 12 2017 Yolman Torrez <yojetoga@gmail.com> - 1.0
- added support
