Summary:	OpenGL-FreeType Library
Name:		OGLFT
Version:	0.9
Release:	4
License:	LGPL
Group:		Libraries
Source0:	http://downloads.sourceforge.net/oglft/oglft-%{version}.tar.gz
# Source0-md5:	c3a8e0993f98edb7611c20f46631d2a6
Patch0:		link.patch
URL:		http://oglft.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	gle-devel
BuildRequires:	libtool
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ library that supplies an interface between the fonts on a system
and an OpenGL or Mesa application. It uses the excellent FreeType
library to read font faces from their files and renders text strings
as OpenGL primitives. 

%package devel
Summary:	Header files for OGLFT
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for OGLFT.

%package static
Summary:	Static version of OGLFT
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of OGLFT.

%prep
%setup -q -n oglft-%{version}
%patch0 -p1

%build
QTDIR=/usr
CPPFLAGS=-I/usr/include/qt
export QTDIR CPPFLAGS
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libOGLFT.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libOGLFT.so.1.*.*
%attr(755,root,root) %ghost %{_libdir}/libOGLFT.so.1

%files devel
%defattr(644,root,root,755)
%doc doc/html
%{_includedir}/oglft
%attr(755,root,root) %{_libdir}/libOGLFT.so

%files static
%defattr(644,root,root,755)
%{_libdir}/libOGLFT.a
