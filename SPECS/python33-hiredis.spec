%global pymajor 3
%global pyminor 3
%global pyver %{pymajor}.%{pyminor}
%global iusver %{pymajor}%{pyminor}
%global __python3 %{_bindir}/python%{pyver}
%global python3_sitelib  %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")
%global python3_sitearch %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")
%global srcname hiredis
%global src %(echo %{srcname} | cut -c1)

Name:           python%{iusver}-%{srcname}
Version:        0.2.0
Release:        1.ius%{?dist}
Summary:        Python wrapper for hiredis
Vendor:         IUS Community Project
Group:          Development/Languages
License:        BSD
URL:            https://github.com/redis/hiredis-py
Source0:        https://pypi.python.org/packages/source/%{src}/%{srcname}/%{srcname}-%{version}.tar.gz
BuildRequires:  python%{iusver}-devel
Requires:       python%{iusver}


%description
Python wrapper for hiredis


%prep
%setup -q -n %{srcname}-%{version}


%build
%{__python3} setup.py build


%install
%{__python3} setup.py install --optimize 1 --skip-build --root %{buildroot}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc COPYING
%{python3_sitearch}/*


%changelog
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
