Summary:	SOAP (Simple Object Access Protocol) implementation in C
Summary(pl.UTF-8):	Implementacja w C SOAP (Simple Object Access Protocol)
Name:		libsoup
Version:	2.33.90
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libsoup/2.33/%{name}-%{version}.tar.bz2
# Source0-md5:	967b0934866be9668a15b64e4f5ff23d
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.9
BuildRequires:	docbook-dtd412-xml
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gobject-introspection-devel >= 0.9.5
BuildRequires:	gtk-doc >= 1.10
BuildRequires:	libgnome-keyring-devel
BuildRequires:	libproxy-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel
Requires:	glib-networking
Requires:	glib2 >= 1:2.28.0
Requires:	gnutls >= 2.1.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It provides an queued asynchronous callback-based mechanism for
sending and servicing SOAP requests, and a WSDL (Web Service
Definition Language) to C compiler which generates client stubs and
server skeletons for easily calling and implementing SOAP methods.

%description -l pl.UTF-8
Pakiet dostarcza interfejs kolejkowalnego, asynchronicznego mechanizmu
do wysyłania i serwowania żądań SOAP oraz WSDL (Web Service Definition
Language) dla kompilatora C, który generuje klienckie stub i szkielety
serwerów dla łatwego wywoływania i implementowania metod SOAP.

%package devel
Summary:	Include files etc to develop SOAP applications
Summary(pl.UTF-8):	Pliki nagłówkowe, dokumentacja dla SOAP
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.28.0
Requires:	gnutls-devel >= 2.1.7
Requires:	libproxy-devel
Requires:	libxml2-devel >= 1:2.6.31

%description devel
Header files, etc you can use to develop SOAP applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe itp. Jednym słowem wszystko czego potrzebujesz aby
samemu tworzyć sobie aplikacje korzystające z SOAP.

%package static
Summary:	SOAP static libraries
Summary(pl.UTF-8):	Biblioteki statyczne SOAP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
SOAP static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne SOAP.

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

%description apidocs
libsoup API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libsoup.

%prep
%setup -q

%build
%{__gtkdocize}
%{__glib_gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	--without-apache-httpd \
	--disable-tls-check \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT/%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post	gnome -p /sbin/ldconfig
%postun	gnome -p /sbin/ldconfig

%files
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

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libsoup-2.4
