Name:      phonon-vlc
Summary:   Phonon VLC Backend
Group:     Video
Version:   0.4.1
Release:   1
License:   GPLv2+
URL:       http://www.videolan.org/
Source0:   ftp://ftp.kde.org/pub/kde/stable/phonon/phonon-backend-vlc/%{version}/src/phonon-backend-vlc-%{version}.tar.xz
BuildRequires: cmake
BuildRequires: vlc-devel
BuildRequires: automoc4
BuildRequires: phonon-devel >= 2:4.5.0
Provides:  phonon-backend
# as a requires it pulls in vlc when building
Suggests:  vlc-plugin-pulse

%description
This package allows Phonon (the KDE media library) to use VLC
for audio and video playback.

%prep
%setup -qn phonon-backend-vlc-%version

%build
%cmake
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

%files
%{_libdir}/kde4/plugins/phonon_backend/phonon_vlc.so
%{_datadir}/kde4/services/phononbackends/vlc.desktop
