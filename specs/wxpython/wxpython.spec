# $Id$

# Authority: dries
# Screenshot: http://drpython.sourceforge.net/linuxclassbrowser.2.x.jpg
# ScreenshotURL: http://drpython.sourceforge.net/screenshots.html

Summary: Python bindings for wxWindows
Name: wxpython
Version: 2.6.1.0
Release: 2.2
License: GPL
Group: Development/Tools
URL: http://www.wxpython.org/

Source: http://dl.sf.net/wxpython/wxPythonSrc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: wxGTK-devel, python, python-devel, gcc-c++

%description
wxPython is a GUI toolkit for the Python programming language. It allows
Python programmers to create programs with a robust, highly functional
graphical user interface, simply and easily. It is implemented as a Python
extension module (native code) that wraps the popular wxWidgets cross
platform GUI library, which is written in C++.

Like Python and wxWidgets, wxPython is Open Source which means that it is
free for anyone to use and the source code is available for anyone to look
at and modify. Or anyone can contribute fixes or enhancements to the
project.

wxPython is a cross-platform toolkit. This means that the same program will
run on multiple platforms without modification. Currently supported
platforms are 32-bit Microsoft Windows, most Unix or unix-like systems, and
Macintosh OS X.

%prep
%setup -n wxPythonSrc-%{version}

%build
cd wxPython
python setup.py build

%install
%{__rm} -rf %{buildroot}
cd wxPython
python setup.py install --root %{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_libdir}/python*/site-packages/wxPython
%{_libdir}/python*/site-packages/wx
%{_bindir}/helpviewer
%{_bindir}/img2png
%{_bindir}/img2xpm
%{_bindir}/img2py
%{_bindir}/xrced
%{_bindir}/pyshell
%{_bindir}/pycrust
%{_bindir}/pywrap
%{_bindir}/pyalacarte
%{_bindir}/pyalamode


%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.6.1.0-2.2
- Rebuild for Fedora Core 5.

* Thu Dec 01 2005 Dries Verachtert <dries@ulyssis.org> - 2.7.1.0-2
- Rebuild.

* Fr Jul 01 2005 Dries Verachtert <dries@ulyssis.org> 2.6.1.0-1
- Update to release 2.6.1.0.

* Mon May 24 2004 Dries Verachtert <dries@ulyssis.org> 2.5.1.5-1
- update to 2.5.1.5

* Wed Jan 28 2004 Dries Verachtert <dries@ulyssis.org> 2.1.4-1
- first packaging for Fedora Core 1