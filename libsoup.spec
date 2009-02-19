Summary:	SOAP (Simple Object Access Protocol) implementation in C
Summary(pl.UTF-8):	Implementacja w C SOAP (Simple Object Access Protocol)
Name:		libsoup
Version:	2.25.91
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libsoup/2.25/%{name}-%{version}.tar.bz2
# Source0-md5:	ef29429708d463057f7eb4b40ec2a92e
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.19.7
BuildRequires:	gnutls-devel >= 1.2.5
BuildRequires:	gtk-doc >= 1.6
BuildRequires:	libproxy-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel
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
Requires:	glib2-devel >= 1:2.19.7
Requires:	gnutls-devel >= 1.2.5
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
%{__glib_gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-ssl \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	pkgconfigdir=%{_pkgconfigdir} \
	m4datadir=%{_aclocaldir} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post	gnome -p /sbin/ldconfig
%postun	gnome -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libsoup-2.4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsoup-2.4.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsoup-2.4.so
%{_libdir}/libsoup-2.4.la
%{_includedir}/libsoup-2.4
%{_pkgconfigdir}/libsoup-2.4.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libsoup-2.4.a

%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsoup-gnome-2.4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsoup-gnome-2.4.so.1

%files gnome-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsoup-gnome-2.4.so
%{_libdir}/libsoup-gnome-2.4.la
%{_includedir}/libsoup-gnome-2.4
%{_pkgconfigdir}/libsoup-gnome-2.4.pc

%files gnome-static
%defattr(644,root,root,755)
%{_libdir}/libsoup-gnome-2.4.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libsoup-2.4
