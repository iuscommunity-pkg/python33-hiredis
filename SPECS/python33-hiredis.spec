%global ius_suffix 33
%global __python33 %{_bindir}/python3.3
%global python33_sitearch %(%{__python33} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")

Name:           python%{ius_suffix}-hiredis
Version:        0.2.0
Release:        2.ius%{?dist}
Summary:        Python wrapper for hiredis
License:        BSD
URL:            https://github.com/redis/hiredis-py
Source0:        https://pypi.python.org/packages/source/h/hiredis/hiredis-%{version}.tar.gz
BuildRequires:  python%{ius_suffix}-devel
BuildRequires:  python%{ius_suffix}-setuptools


%description
Python extension that wraps protocol parsing code in hiredis. It primarily
speeds up parsing of multi bulk replies.


%prep
%setup -q -n hiredis-%{version}


%build
%{__python33} setup.py build


%install
%{__python33} setup.py install --optimize 1 --skip-build --root %{buildroot}


%files
%doc COPYING
%{python33_sitearch}/hiredis*


%changelog
* Fri Apr 15 2016 Carl George <carl.george@rackspace.com> - 0.2.0-2.ius
- Macro clean up
- Build with setuptools, not distutils

* Mon Apr 06 2015 Ben Harper <ben.harper@rackspace.com> - 0.2.0-1.ius
- Latest upstream

* Mon Feb 09 2015 Carl George <carl.george@rackspace.com> - 0.1.6-1.ius
- Latest upstream

* Mon Oct 06 2014 Ben Harper <ben.harper@rackspace.com> - 0.1.5-1.ius
- Latest sources from upstream

* Wed Jun 25 2014 Carl George <carl.george@rackspace.com> - 0.1.4-1.ius
- Latest sources from upstream
- Update vendor, summary, description, and url
- Implement python and ius macros

* Wed Apr 16 2014 Ben Harper <ben.harper@rackspace.com> - 0.1.3-1.ius
- Latest sources from upstream

* Tue Jan 07 2014 Ben Harper <ben.harper@rackspace.com> - 0.1.2-1.ius
- Latest sources from upstream

* Tue Oct 16 2012 Ben Harper <ben.harper@rackspace.com> - 0.1.1-1.ius
- porting from python32-hiredis

* Thu Sep 20 2012 Jeffrey Ness <jeffrey.ness@rackspace.com> - 0.1.1-1.ius
- New package for IUS
