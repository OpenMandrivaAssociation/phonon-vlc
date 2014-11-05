Summary:	Phonon VLC Backend
Name:		phonon-vlc
Version:	0.8.1
Release:	1
License:	GPLv2+
Group:		Video
Url:		http://www.videolan.org/
Source0:	ftp://ftp.kde.org/pub/kde/stable/phonon/phonon-backend-vlc/%{version}/src/phonon-backend-vlc-%{version}.tar.xz
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	pkgconfig(libvlc)
BuildRequires:	pkgconfig(phonon)
Provides:	phonon-backend
# as a requires it pulls in vlc when building
Suggests:	vlc-plugin-pulse

%description
This package allows Phonon (the KDE media library) to use VLC for audio and
video playback.

%files
%doc COPYING.LIB
%{_libdir}/kde4/plugins/phonon_backend/phonon_vlc.so
%{_datadir}/kde4/services/phononbackends/vlc.desktop

#----------------------------------------------------------------------------

%prep
%setup -qn phonon-backend-vlc-%{version}

%build
%cmake
%make


%install
%makeinstall_std -C build

