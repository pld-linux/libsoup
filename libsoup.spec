Summary:	SOAP (Simple Object Access Protocol) implementation in C
Summary(pl.UTF-8):	Implementacja w C SOAP (Simple Object Access Protocol)
Name:		libsoup
Version:	2.2.103
Release:	1
License:	LGPL v2
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libsoup/2.2/%{name}-%{version}.tar.bz2
# Source0-md5:	1ae3c15b35f3d999d203e2361e44559e
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.14.1
BuildRequires:	gnutls-devel >= 1.2.5
BuildRequires:	gtk-doc >= 1.6
BuildRequires:	libgpg-error-devel >= 0.4
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.27
BuildRequires:	pkgconfig
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

%package apidocs
Summary:	libsoup API documentation
Summary(pl.UTF-8):	Dokumentacja API libsoup
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libsoup API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libsoup.

%package devel
Summary:	Include files etc to develop SOAP applications
Summary(pl.UTF-8):	Pliki nagłówkowe, dokumentacja dla SOAP
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.14.1
Requires:	gnutls-devel >= 1.0.6
Requires:	libxml2-devel >= 1:2.6.27

%description devel
Header files, etc you can use to develop SOAP applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe itp. Jednym słowem wszystko czego potrzebujesz aby
samemu tworzyć sobie aplikacje korzystające z SOAP.

%package static
Summary:	SOAP static libraries
Summary(pl.UTF-8):	Biblioteki statyczne SOAP
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
SOAP static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne SOAP.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--enable-ssl \
	--enable-gtk-doc \
	--enable-libgpg-error \
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

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
