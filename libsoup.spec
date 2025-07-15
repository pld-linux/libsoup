#
# Conditional build:
%bcond_without	apidocs	# API documentation

Summary:	HTTP client/server library for GNOME
Summary(pl.UTF-8):	Biblioteka klienta/serwera HTTP dla GNOME
Name:		libsoup
Version:	2.74.3
Release:	2
License:	LGPL v2+
Group:		Libraries
Source0:	https://download.gnome.org/sources/libsoup/2.74/%{name}-%{version}.tar.xz
# Source0-md5:	8f657fd301a213629204b3320c35d75a
Patch0:		%{name}-path-override.patch
URL:		https://wiki.gnome.org/Projects/libsoup
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.58
BuildRequires:	gobject-introspection-devel >= 0.10.0
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.20}
BuildRequires:	heimdal-devel
BuildRequires:	libbrotli-devel
BuildRequires:	libpsl-devel >= 0.20.0
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	meson >= 0.50
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	sqlite3-devel
BuildRequires:	sysprof-devel >= 3.38
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	glib2 >= 1:2.58
Requires:	libpsl >= 0.20.0
# for TLS support
Suggests:	glib-networking
# ntlm_auth for NTLM support
Suggests:	samba-winbind
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libsoup is an HTTP client/server library for GNOME. It uses GObjects
and the glib main loop, to integrate well with GNOME applications.

%description -l pl.UTF-8
libsoup to biblioteka klienta/serwera HTTP dla GNOME. Wykorzystuje
typy GObject oraz pętlę główną glib, aby dobrze integrować się z
aplikacjami GNOME.

%package devel
Summary:	Header files for libsoup library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libsoup
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.58
Requires:	libbrotli-devel
Requires:	libpsl-devel >= 0.20.0
Requires:	libxml2-devel >= 1:2.6.31
Requires:	sqlite3-devel
Requires:	sysprof-devel >= 3.38
Requires:	zlib-devel

%description devel
Header files for libsoup library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libsoup.

%package static
Summary:	libsoup static library
Summary(pl.UTF-8):	Biblioteka statyczna libsoup
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libsoup static library.

%description static -l pl.UTF-8
Biblioteka statyczna libsoup.

%package gnome
Summary:	GNOME specific extensions to libsoup library
Summary(pl.UTF-8):	Rozszerzenia GNOME do biblioteki libsoup
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gnome
GNOME specific extensions to libsoup library.

%description gnome -l pl.UTF-8
Rozszerzenia GNOME do biblioteki libsoup.

%package gnome-devel
Summary:	Header files for libsoup-gnome library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libsoup-gnome
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gnome = %{version}-%{release}

%description gnome-devel
Header files for libsoup-gnome library.

%description gnome-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libsoup-gnome.

%package gnome-static
Summary:	Static libsoup-gnome library
Summary(pl.UTF-8):	Statyczna biblioteka libsoup-gnome
Group:		Development/Libraries
Requires:	%{name}-gnome-devel = %{version}-%{release}

%description gnome-static
Static libsoup-gnome library.

%description gnome-static -l pl.UTF-8
Statyczna biblioteka libsoup-gnome.

%package apidocs
Summary:	libsoup API documentation
Summary(pl.UTF-8):	Dokumentacja API libsoup
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
libsoup API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libsoup.

%package -n vala-libsoup
Summary:	libsoup API for Vala language
Summary(pl.UTF-8):	API libsoup dla języka Vala
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala
BuildArch:	noarch

%description -n vala-libsoup
libsoup API for Vala language.

%description -n vala-libsoup -l pl.UTF-8
API libsoup dla języka Vala.

%prep
%setup -q
%patch -P0 -p1

%build
%meson build \
	%{?with_apidocs:-Dgtk_doc=true} \
	-Dntlm=enabled \
	-Dntlm_auth=/usr/bin/ntlm_auth \
	-Dtests=false \
	-Dtls_check=false

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang libsoup

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post	gnome -p /sbin/ldconfig
%postun	gnome -p /sbin/ldconfig

%files -f libsoup.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/libsoup-2.4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsoup-2.4.so.1
%{_libdir}/girepository-1.0/Soup-2.4.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsoup-2.4.so
%{_includedir}/libsoup-2.4
%{_pkgconfigdir}/libsoup-2.4.pc
%{_datadir}/gir-1.0/Soup-2.4.gir

%files static
%defattr(644,root,root,755)
%{_libdir}/libsoup-2.4.a

%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsoup-gnome-2.4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsoup-gnome-2.4.so.1
%{_libdir}/girepository-1.0/SoupGNOME-2.4.typelib

%files gnome-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsoup-gnome-2.4.so
%{_includedir}/libsoup-gnome-2.4
%{_pkgconfigdir}/libsoup-gnome-2.4.pc
%{_datadir}/gir-1.0/SoupGNOME-2.4.gir

%files gnome-static
%defattr(644,root,root,755)
%{_libdir}/libsoup-gnome-2.4.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libsoup-2.4
%endif

%files -n vala-libsoup
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/libsoup-2.4.deps
%{_datadir}/vala/vapi/libsoup-2.4.vapi
