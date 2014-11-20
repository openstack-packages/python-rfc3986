# Created by pyp2rpm-1.1.0b
%global pypi_name rfc3986

Name:           python-%{pypi_name}
Version:        XXX
Release:        XXX{?dist}
Summary:        Validating URI References per RFC 3986

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/rfc3986
Source0:        https://pypi.python.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel


%description
A Python implementation of RFC 3986 including validation and authority parsing.


%prep
%setup -q -n %{pypi_name}-%{upstream_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}


%files
%doc README.rst LICENSE
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Mon Sep 15 2014 Alan Pevec <apevec@redhat.com> - 0.2.0-1
- Initial package.
