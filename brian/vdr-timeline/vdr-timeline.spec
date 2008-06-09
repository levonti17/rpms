%define pname     timeline
%define plugindir %(vdr-config --plugindir  2>/dev/null || echo ERROR)
%define configdir %(vdr-config --configdir  2>/dev/null || echo ERROR)
%define apiver    %(vdr-config --apiversion 2>/dev/null || echo ERROR)

Name:           vdr-%{pname}
Version:        1.0.141
Release:        1
Summary:        Timeline view for VDR

Group:          Applications/Multimedia
License:        GPL
URL:            http://www.berlios.de/vdr/
Source0:        http://www.berlios.de/vdr/downloads/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  vdr-devel >= 1.3.47 
Requires:       vdr(abi) = %{apiver}

%description
This plugin displays the timeline view of various channels

%prep
%setup -q -n %{pname}-%{version}


%build
#./configure
make %{?_smp_mflags} LIBDIR=. VDRDIR=%{_libdir}/vdr all


%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 $RPM_BUILD_ROOT%{plugindir}
install -dm 755 $RPM_BUILD_ROOT/usr/bin/
install -pm 755 libvdr-%{pname}.so.%{apiver} $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING HISTORY README
%{plugindir}/libvdr-%{pname}.so.%{apiver}


%changelog
