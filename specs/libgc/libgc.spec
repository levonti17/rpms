# $Id$
# Authority: dag

%define real_name gc

Summary: Conservative garbage collector for C
Name: libgc
Version: 6.8
Release: 1
Epoch: 1
License: BSD
Group: System Environment/Libraries
URL: http://www.hpl.hp.com/personal/Hans_Boehm/gc/

Source: http://www.hpl.hp.com/personal/Hans_Boehm/%{real_name}/gc_source/%{real_name}%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Obsoletes: libgc-6, libgc-6.1alpha5, gc

%description
Boehm's GC is a garbage collecting storage allocator that is
intended to be used as a plug-in replacement for C's malloc.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{epoch}:%{version}-%{release}
Obsoletes: libgc6-devel, gc-devel

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{real_name}%{version}

%build
%configure \
	--enable-threads="pthreads"
%{__make} %{?_smp_mflags} LIBS="-ldl"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_libdir} \
			%{buildroot}%{_includedir}/libgc/ \
			%{buildroot}%{_mandir}/man1/
%makeinstall
#	DESTDIR="%{buildroot}"
#%{__install} -Dp -m0644 include/*.h %{buildroot}%{_includedir}/libgc/
%{__install} -Dp -m0655 doc/gc.man %{buildroot}%{_mandir}/man1/libgc.1

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la
%{__rm} -rf %{buildroot}%{_datadir}/gc/

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README.QUICK
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/*
%doc %{_mandir}/man?/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*.h
%{_includedir}/gc
%{_includedir}/libgc/
#exclude %{_libdir}/*.la

%changelog
* Wed Aug 09 2006 Dries Verachtert <dries@ulyssis.org> - 6.8-1
- Updated to release 6.8.

* Mon Apr 03 2006 Dries Verachtert <dries@ulyssis.org> - 6.7-1
- Updated to release 6.7.

* Sat Jan 14 2006 Dag Wieers <dag@wieers.com> - 6.6-1
- Excluded gc.1 manpage.

* Tue Sep 20 2005 Dries Verachtert <dries@ulyssis.org> - 6.6-0
- Updated to release 6.6.

* Sun Nov 23 2003 Dag Wieers <dag@wieers.com> - 6.2-0
- Updated to release 6.2.

* Mon Mar 17 2003 Dag Wieers <dag@wieers.com> - 6.1-0
- Initial package. (using DAR)
