# $Id$
# Authority: dries
# Upstream: Xavier Guimard <perl+cpan$astola,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lemonldap-NG-Handler

Summary: Apache protection module part of Lemonldap::NG Web-SSO system
Name: perl-Lemonldap-NG-Handler
Version: 0.86
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lemonldap-NG-Handler/

Source: http://www.cpan.org/modules/by-module/Lemonldap/Lemonldap-NG-Handler-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
The Apache protection module part of Lemonldap::NG Web-SSO system.

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

### Clean up docs
find example/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README example/
%doc %{_mandir}/man3/Lemonldap::NG::Handler.3pm*
%doc %{_mandir}/man3/Lemonldap::NG::Handler::*.3pm*
%dir %{perl_vendorlib}/Lemonldap/
%dir %{perl_vendorlib}/Lemonldap/NG/
%{perl_vendorlib}/Lemonldap/NG/Handler/
%{perl_vendorlib}/Lemonldap/NG/Handler.pm

%changelog
* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 0.86-1
- Updated to release 0.86.

* Sun Mar 02 2008 Dag Wieers <dag@wieers.com> - 0.85-1
- Updated to release 0.85.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 0.84-1
- Updated to release 0.84.

* Wed May 02 2007 Dries Verachtert <dries@ulyssis.org> - 0.81-1
- Updated to release 0.81.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.75-1
- Initial package.