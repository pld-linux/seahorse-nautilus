Summary:	PGP encryption and signing for Nautilus
Summary(pl.UTF-8):	Rozszerzenie Seahorse dla Nautilusa
Name:		seahorse-nautilus
Version:	3.10.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/seahorse-nautilus/3.10/%{name}-%{version}.tar.xz
# Source0-md5:	1f33cf9f56ac46b2a2363d022ea7969f
URL:		https://wiki.gnome.org/Apps/Seahorse
BuildRequires:	dbus-glib-devel >= 0.35
BuildRequires:	desktop-file-utils
BuildRequires:	gcr-devel >= 3.4.1
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.10.0
BuildRequires:	gnupg2
BuildRequires:	gpgme-devel >= 1.0.0
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libcryptui-devel >= 3.10
BuildRequires:	libgnome-keyring-devel
BuildRequires:	libnotify-devel >= 0.3
BuildRequires:	nautilus-devel >= 3.0
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	dbus-glib >= 0.35
Requires:	gcr >= 3.4.1
Requires:	glib2 >= 1:2.26.0
Requires:	gpgme >= 1.0.0
Requires:	gnupg2 >= 2.0
Requires:	libcryptui >= 3.10
Requires:	libnotify >= 0.3
Requires:	nautilus >= 3.0
Obsoletes:	nautilus-extension-seahorse < 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Seahorse nautilus is an extension for nautilus which allows encryption
and decryption of OpenPGP files using GnuPG.

%description -l pl.UTF-8
Rozszerzenie do podpisywania i szyfrowania plików.

%prep
%setup -q

%build
%configure \
	--disable-gpg-check \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-3.0/libnautilus-seahorse.la

desktop-file-validate $RPM_BUILD_ROOT%{_desktopdir}/seahorse-pgp-encrypted.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_desktopdir}/seahorse-pgp-keys.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_desktopdir}/seahorse-pgp-signature.desktop

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README THANKS
%attr(755,root,root) %{_bindir}/seahorse-tool
%attr(755,root,root) %{_libdir}/nautilus/extensions-3.0/libnautilus-seahorse.so
%{_datadir}/GConf/gsettings/org.gnome.seahorse.nautilus.convert
%{_datadir}/glib-2.0/schemas/org.gnome.seahorse.nautilus.*gschema.xml
%{_datadir}/seahorse-nautilus
%{_desktopdir}/seahorse-pgp-encrypted.desktop
%{_desktopdir}/seahorse-pgp-keys.desktop
%{_desktopdir}/seahorse-pgp-signature.desktop
%{_mandir}/man1/seahorse-tool.1*
