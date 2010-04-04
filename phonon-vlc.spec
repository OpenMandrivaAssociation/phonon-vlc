%define name    phonon-vlc
%define version 0.0.0
%define git     20100404
%define rel     1
%if %git
%define release %mkrel 0.%git.%rel
%else
%define release %mkrel %rel
%endif

%if %git
%define fname %name-snapshot-%git
%else
%define fname %name-%version
%endif

%define git_url git://git.videolan.org/vlc/bindings/phonon.git

Summary:   VLC Backend for Phonon
Name:      %{name}
Version:   %{version}
Release:   %{release}
%if %git
Source0:   http://nightlies.videolan.org/build/source/%fname.tar.bz2
%else
Source0:   http://download.videolan.org/pub/videolan/%name/%{version}/%{fname}.tar.bz2
%endif
License:   GPLv2+
Group:     Video
URL:       http://www.videolan.org/
BuildRoot: %_tmppath/%name-%version-%release-root
Provides:  phonon-backend

BuildRequires: vlc-devel
BuildRequires: kde4-macros
BuildRequires: kdelibs4-devel
BuildRequires: phonon-devel


Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description
This package allows Phonon (the KDE media library) to use VLC
for audio and video playback.


%prep
%if %git
%setup -q -n %name
%else
%setup -q -n %fname
%endif
%apply_patches

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
