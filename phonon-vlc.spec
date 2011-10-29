Summary:   VLC Backend for Phonon
Name:      phonon-vlc
Version:   0.4.1
Release:   1
Source0:   ftp://ftp.kde.org/pub/kde/stable/phonon/phonon-backend-vlc/%version/src/phonon-backend-vlc-%version.tar.xz
License:   GPLv2+
Group:     Video
URL:       http://www.videolan.org/

Provides:  phonon-backend
# as a requires it pulls in vlc when building
Suggests:  vlc-plugin-pulse
BuildRequires: vlc-devel
BuildRequires: kde4-macros
BuildRequires: automoc4
BuildRequires: phonon-devel >= 2:4.5.0

%description
This package allows Phonon (the KDE media library) to use VLC
for audio and video playback.

%prep
%setup -qn phonon-backend-vlc-%version

%build
%cmake_kde4
%make

%install
rm -rf %buildroot

%makeinstall_std -C build
%clean
rm -fr %buildroot

%files
%defattr(-,root,root)
%_libdir/kde4/plugins/phonon_backend/phonon_vlc.so
%_datadir/kde4/services/phononbackends/vlc.desktop
