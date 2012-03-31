Name:		webapp
Version:	1
Release:	%{gitbuild}.1%{?dist}
Summary:	Adds phing channel to PEAR

Group:		Development/Languages
License:	LGPLv2
URL:		http://example.com/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source0:		%{name}-%{gitbuild}.tgz

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

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%post


%postun

%files
%defattr(-,root,root,-)
/var/www/%{name}


%changelog
