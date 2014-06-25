
%define pybasever 3.3
%define pyver 33

%define upstream_name hiredis

%define name python%{pyver}-%{upstream_name}
%define __python /usr/bin/python%{pybasever}

%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

Name:           %{name}
Version:        0.1.3
Release:        1.ius%{?dist}
Summary:        Python extension that wraps hiredis
Vendor:         IUS Community Project
Group:          Development/Languages
License:        BSD
URL:            http://pypi.python.org/pypi/hiredis
Source0:	http://pypi.python.org/packages/source/h/hiredis/%{upstream_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python%{pyver}-devel

%description
Python extension that wraps hiredis

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING
%{python_sitearch}/%{upstream_name}
%{python_sitearch}/%{upstream_name}-%{version}-*.egg-info

%changelog
* Wed Apr 16 2014 Ben Harper <ben.harper@rackspace.com> - 0.1.3-1.ius
- Latest sources from upstream

* Tue Jan 07 2014 Ben Harper <ben.harper@rackspace.com> - 0.1.2-1.ius
- Latest sources from upstream

* Tue Oct 16 2012 Ben Harper <ben.harper@rackspace.com> - 0.1.1-1.ius
- porting from python32-hiredis

* Thu Sep 20 2012 Jeffrey Ness <jeffrey.ness@rackspace.com> - 0.1.1-1.ius
- New package for IUS
