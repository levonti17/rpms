# $Id$
# Authority: dag
# Upstream: Leon Brocard <acme$astray,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-WWW-Mechanize-Catalyst

Summary: Test::WWW::Mechanize for Catalyst
Name: perl-Test-WWW-Mechanize-Catalyst
Version: 0.42
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-WWW-Mechanize-Catalyst/

Source: http://www.cpan.org/modules/by-module/Test/Test-WWW-Mechanize-Catalyst-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Test::WWW::Mechanize for Catalyst.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES MANIFEST META.yml README
%doc %{_mandir}/man3/Test::WWW::Mechanize::Catalyst.3pm*
%dir %{perl_vendorlib}/Test/
%dir %{perl_vendorlib}/Test/WWW/
%dir %{perl_vendorlib}/Test/WWW/Mechanize/
#%{perl_vendorlib}/Test/WWW/Mechanize/Catalyst/
%{perl_vendorlib}/Test/WWW/Mechanize/Catalyst.pm

%changelog
* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 1.42-1
- Updated to release 1.42.

* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.41-1
- Initial package. (using DAR)