Summary:	OpenGL-FreeType Library
Summary(pl.UTF-8):	Biblioteka OpenGL-FreeType
Name:		OGLFT
Version:	0.9
Release:	4
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/oglft/oglft-%{version}.tar.gz
# Source0-md5:	c3a8e0993f98edb7611c20f46631d2a6
Patch0:		link.patch
URL:		http://oglft.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	freetype-devel >= 2
BuildRequires:	gle-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	qt-devel >= 3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ library that supplies an interface between the fonts on a system
and an OpenGL or Mesa application. It uses the excellent FreeType
library to read font faces from their files and renders text strings
as OpenGL primitives. 

%description -l pl.UTF-8
Bibllioteka C++ zapewniająca interfejs pomiędzy fontami w systemie
oraz aplikacjami OpenGL/Mesy. Wykorzystuje świetną bibliotekę FreeType
do odczytu wyglądu fontów z plików, natomiast łańcuchy tekstu rysuje
jako figury OpenGL.

%package devel
Summary:	Header files for OGLFT
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki OGLFT
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL-GLU-devel
Requires:	freetype-devel >= 2
Requires:	gle-devel
Requires:	libstdc++-devel
Requires:	qt-devel >= 3

%description devel
Header files for OGLFT.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki OGLFT.

%package static
Summary:	Static version of OGLFT library
Summary(pl.UTF-8):	Statyczna wersja biblioteki OGLFT
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of OGLFT library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki OGLFT.

%prep
%setup -q -n oglft-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	CPPFLAGS="%{rpmcppflags} -I/usr/include/qt" \
	QTDIR=/usr
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
%attr(755,root,root) %{_libdir}/libOGLFT.so
%{_includedir}/oglft

%files static
%defattr(644,root,root,755)
%{_libdir}/libOGLFT.a
