Summary: Condor EC2 Node configuration script
Name: condor-ec2-node
Version: 0.1
Release: 1%{?dist}
License: ASL 2.0
Group: Applications/System
URL: none
Source0: condor-ec2-node.tar.gz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Requires: condor >= 7.4.4-0.8

%description
An init script to configure Condor on an EC2 instance.

It provides PUBLIC_IP to Condor configuration, and reads a user
specified configuration from the EC2 instance's user data.


%prep
%setup -q -n condor-ec2-node


%build


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE-2.0.txt README
%_initrddir/condor-ec2-node


%changelog
* Mon Aug  9 2010  <matt@redhat> - 0.1-1
- Initial release

