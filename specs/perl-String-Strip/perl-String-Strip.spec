# $Id$
# Authority: dries
# Upstream: Brent B. Powers <cpan$B2Pi,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name String-Strip

Summary: Fast, commonly used, string operations
Name: perl-String-Strip
Version: 1.01
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/String-Strip/

Source: http://search.cpan.org/CPAN/authors/id/B/BP/BPOWERS/String-Strip-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
String::Strip is an XS extension that implements four white space
removal routines: StripSpace (remove all white space), StripLSpace
(strip leading white space), StripTSpace (strip trailing white space),
and StripLTSpace (strip leading and trailing white space). All four of
these routines work directly on the input argument, rather than
passing back a result. The routines tend to be roughly 30% faster than
equivalent function regex code.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/String/
%{perl_vendorarch}/String/Strip.pm
%dir %{perl_vendorarch}/auto/String/
%{perl_vendorarch}/auto/String/Strip/

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Initial package.
