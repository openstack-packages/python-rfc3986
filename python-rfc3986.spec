%global pypi_name rfc3986

Name:           python-rfc3986
Version:        XXX
Release:        1%{?dist}
Summary:        general-purpose rfc3986 library,

License:        ASL 2.0
URL:            https://github.com/openstack-packages/python-rfc3986
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr


%description
A Python implementation of `RFC 3986`_ including validation and authority parsing.

%prep
%setup -q -n rfc3986-%{upstream_version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}

%files
%doc README.rst LICENSE
%{python_sitelib}/rfc3986
%{python_sitelib}/rfc3986-*.egg-info

%changelog
* Thu Aug 28 2014 Derek Higgins <derekh@redhat.com> - XXX
- Initial package.
