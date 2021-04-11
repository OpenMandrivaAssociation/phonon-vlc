%bcond_with qt4

Summary:	Phonon VLC Backend
Name:		phonon-vlc
Version:	0.11.3
Release:	1
License:	GPLv2+
Group:		Video
Url:		http://www.videolan.org/
Source0:	http://download.kde.org/stable/phonon/phonon-backend-vlc/%{version}/phonon-backend-vlc-%{version}.tar.xz
%if %{with qt4}
BuildRequires:	automoc4
BuildRequires:	pkgconfig(phonon)
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(libvlc)
BuildRequires:	pkgconfig(phonon4qt5)
BuildRequires:	pkgconfig(Qt5OpenGL)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5X11Extras)
Provides:	phonon-backend
# as a requires it pulls in vlc when building
Suggests:	vlc-plugin-pulse

%description
This package allows Phonon (the KDE media library) to use VLC for audio and
video playback.

%if %{with qt4}
%files
%{_libdir}/kde4/plugins/phonon_backend/phonon_vlc.so
%{_datadir}/kde4/services/phononbackends/vlc.desktop
%endif

%package -n phonon4qt5-vlc
Summary:	Phonon VLC Backend
Provides:	phonon4qt5-backend
# as a requires it pulls in vlc when building
Suggests:	vlc-plugin-pulse

%description -n phonon4qt5-vlc
Phonon4Qt5 VLC Backend.

%files -n phonon4qt5-vlc -f %{name}.lang
%{_libdir}/qt5/plugins/phonon4qt5_backend/phonon_vlc.so

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n phonon-backend-vlc-%{version}

%if %{with qt4}
mkdir Qt4
mv `ls -1 |grep -v Qt4` Qt4
cp -a Qt4 Qt5
%endif

%build
%if %{with qt4}
pushd Qt4
%cmake -DPHONON_BUILD_PHONON4QT5:BOOL=OFF \
	-DQT_QMAKE_EXECUTABLE=%{_prefix}/lib/qt4/bin/qmake
%make
popd

pushd Qt5
%endif

%cmake_kde5 -DPHONON_BUILD_PHONON4QT5:BOOL=ON \
	-DQT_QMAKE_EXECUTABLE=%{_libdir}/qt5/bin/qmake
%ninja


%install
%if %{with qt4}
%makeinstall_std -C Qt4/build

%ninja_install -C Qt5/build
%else
%ninja_install -C build
%endif

find %{buildroot}%{_datadir}/locale -name "*.qm" |while read r; do
	L=`echo $r |rev |cut -d/ -f3 |rev`
	echo "%%lang($L) %%{_datadir}/locale/$L/LC_MESSAGES/*.qm" >>%{name}.lang
done
