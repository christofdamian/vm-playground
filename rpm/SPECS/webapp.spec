Name:		webapp
Version:	1
Release:	%{gitbuild}.1%{?dist}
Summary:	Adds phing channel to PEAR

Group:		Development/Languages
License:	LGPLv2
URL:		http://example.com/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source0:	%{name}-%{gitbuild}.tgz
Source1:	%{name}-httpd.conf

Requires:	httpd
Requires:	php
Requires:	systemd-units

BuildArch:	noarch

%description
webapp

%prep
mkdir -p %{name}-%{version}
cd %{name}-%{version}

%build

%install
cd %{name}-%{version}

mkdir -p $RPM_BUILD_ROOT/var/www/%{name}
tar xvfz %{SOURCE0} -C $RPM_BUILD_ROOT/var/www/%{name}

mkdir -p $RPM_BUILD_ROOT/etc/httpd/conf.d
install %{SOURCE1} $RPM_BUILD_ROOT/etc/httpd/conf.d/%{name}.conf

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%post
systemctl enable httpd.service

%postun

%files
%defattr(-,root,root,-)
/var/www/%{name}
/etc/httpd/conf.d/%{name}.conf

%changelog
