# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Summary: Advanced, easy to use and extensible WikiEngine
Name: moin
Version: 1.5.7
Release: 1
License: GPL
Group: Applications/Internet
URL: http://moinmoin.wikiwikiweb.de/

Source: http://dl.sf.net/moin/moin-%{version}.tar.gz
Patch0: moin-1.5.2-xml_newline.patch
Patch1: moin-1.5.2-config.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel >= 2.3
Requires: python >= 2.3

Provides: moinmoin = %{version}
Obsoletes: moinmoin <= %{version}-%{release}

%description
MoinMoin is an advanced, easy to use and extensible WikiEngine with a large
community of users. Said in a few words, it is about collaboration on easily
editable web pages.

%prep
%setup
%patch0 -p1 -b .xml_newline
%patch1 -p1 -b .config

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README docs/CHANGES* docs/README* docs/*.html docs/licenses/
%{_bindir}/moin
%{_datadir}/moin/
%{python_sitelib}/MoinMoin/

%changelog
* Sun Mar 11 2007 Dag Wieers <dag@wieers.com> - 1.5.7-1
- Initial package.