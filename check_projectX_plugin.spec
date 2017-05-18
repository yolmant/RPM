Name:		check_projectX_plugin
Version:	1.0
Release:	1%{?dist}
Summary:	this is nagios nrpe plugin

Group:		nti320
License:	GPL
URL:		https://github.com/yolmant/RPM
Source0:	check_projectX_plugin-1.0.tar.gz

Requires:	bash

%description
it will install a new plugin for nagios in the nrpe files 

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/lib64/nagios/plugins
install -m 0755 %{name} %{buildroot}/usr/lib64/nagios/plugins/%{name}

%clean
rm -rf %{buildroot}

%files
/usr/lib64/nagios/plugins/check_projectX_plugin

%post
sudo chown nagios:nagios /usr/lib64/nagios/plugins/check_projectX_plugin
sudo chmod +x /usr/lib64/nagios/plugins/check_projectX_plugin
sudo sed -i "215i command[check_projectX_plugin]=/usr/lib64/nagios/plugins/check_projectX_plugin -w 66 -c 902" /etc/nagios/nrpe.cfg

%doc

%changelog
*Wed May 17 2017 yolman torrez <yojetoga@gmail.com> - 1.0.0
- added support




