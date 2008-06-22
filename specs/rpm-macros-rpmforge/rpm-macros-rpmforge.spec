# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

Summary: RPM macros used by the RPMForge project
Name: rpm-macros-rpmforge
Version: 0
Release: 1.2
License: GPL
Group: Development/Tools
URL: http://rpmforge.net/

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
RPM macros used by the RPMForge project.

%prep

%{__cat} <<EOF >macros.rpmforge
### RPM macros for RPMForge project (http://rpmforge.net/)
###
### Add to /etc/rpmrc: "macrofiles: /etc/rpm/macros.rpmforge"

%%packager RPMForge authority <%%{name}@package.rpmforge.net>
%%vendor RPMForge project (http://rpmforge.net/)


%if %{?dtag:1}0
%%dtag %dtag
%%%dtag 1
%else
### Current distribution undefined in original buildsystem
#%%dtag ???
#%%??? 1
%endif

%if "%dtag" == "fc2"
### Fedora Core 2
%%distribution RPMForge repository for Fedora Core 2
%%errata 120
%endif
%if "%dtag" == "fc1"
### Fedora Core 1
%%distribution RPMForge repository for Fedora Core 1
%%errata 110
%%_without_alsa 1
%%_without_theora 1
%endif
%if "%dtag" == "el3"
### Red Hat Enterprise Linux 3
%%distribution RPMForge repository for Red Hat Enterprise Linux 3
%%errata 91
%%_without_alsa 1
%%_without_fribidi 1
%%_without_theora 1
%endif
%if "%dtag" == "rh9"
### Red Hat Linux 9
%%distribution RPMForge repository for Red Hat Linux 9
%%errata 90
%%_without_alsa 1
%%_without_fribidi 1
%%_without_theora 1
%endif
%if "%dtag" == "rh8"
### Red Hat Linux 8.0
%%distribution RPMForge repository for Red Hat Linux 8.0
%%errata 80
%%_without_alsa 1
%%_without_fribidi 1
%%_without_theora 1
%endif
%if "%dtag" == "rh7"
### Red Hat Linux 7.3
%%distribution RPMForge repository for Red Hat Linux 7.X
%%errata 73
%%_without_alsa 1
%%_without_autoconf213 1
%%_without_freedesktop 1
%%_without_fribidi 1
%%_without_gnomevfs2 1
%%_without_gtk2 1
%%_without_theora 1
%endif
%if "%dtag" == "el2"
### Red hat Enterprise Linux 2.1
%%distribution RPMForge repository for Red Hat Enterprise Linux 2.1
%%errata 72
%%_without_alsa 1
%%_without_autoconf213 1
%%_without_freedesktop 1
%%_without_fribidi 1
%%_without_gnomevfs2 1
%%_without_gtk2 1
%%_without_theora 1
%endif
%if "%dtag" == "rh6"
### Red Hat Linux 6.2
%%distribution RPMForge repository for Red Hat Linux 6.2
%%errata 62
%%_without_alsa 1
%%_without_autoconf213 1
%%_without_freedesktop 1
%%_without_fribidi 1
%%_without_gnomevfs2 1
%%_without_gtk2 1
%%_without_theora 1
%endif

%ifarch x86_64
### Architecture: x86_64
%%_without_mjpeg 1
%%_without_nasm 1
%%_without_quicktime 1
%endif
EOF

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0644 macros.rpmforge %{buildroot}%{_sysconfdir}/rpm/macros.rpmforge

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%config %{_sysconfdir}/rpm/macros.rpmforge

%changelog
* Tue Jun 08 2004 Dag Wieers <dag@wieers.com> - 0-1
- Initial package. (using DAR)