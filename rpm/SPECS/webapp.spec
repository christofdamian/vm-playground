Name:		webapp
Version:	1
Release:	%{git_build_number}.1%{?dist}
Summary:	Adds phing channel to PEAR

Group:		Development/Languages
License:	LGPLv2
URL:		http://example.com/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch

%description
webapp

%prep


%build

%install

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%post


%postun

%files
%defattr(-,root,root,-)


%changelog
