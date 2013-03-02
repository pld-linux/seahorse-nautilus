Summary:	PGP encryption and signing for Nautilus
Summary(pl.UTF-8):	Rozszerzenie Seahorse dla Nautilusa
Name:		seahorse-nautilus
Version:	3.6.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/seahorse-nautilus/3.6/%{name}-%{version}.tar.xz
# Source0-md5:	31e440429f038ebd1d6a6ab0f51ac4b1
URL:		https://live.gnome.org/Seahorse
BuildRequires:	dbus-glib-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gcr-devel
BuildRequires:	gettext-devel
BuildRequires:	gnupg2
BuildRequires:	gpgme-devel >= 1.0
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	libcryptui-devel
BuildRequires:	libgnome-keyring-devel
BuildRequires:	libnotify-devel
BuildRequires:	nautilus-devel
BuildRequires:	pkgconfig
Requires:	glib2 >= 1:2.26.0
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
%doc AUTHORS NEWS README THANKS
%attr(755,root,root) %{_bindir}/seahorse-tool
%{_mandir}/man1/seahorse-tool.1*
%attr(755,root,root) %{_libdir}/nautilus/extensions-3.0/libnautilus-seahorse.so
%{_datadir}/seahorse-nautilus
%{_desktopdir}/seahorse-pgp-encrypted.desktop
%{_desktopdir}/seahorse-pgp-keys.desktop
%{_desktopdir}/seahorse-pgp-signature.desktop
%{_datadir}/GConf/gsettings/org.gnome.seahorse.nautilus.convert
%{_datadir}/glib-2.0/schemas/org.gnome.seahorse.nautilus.*gschema.xml
