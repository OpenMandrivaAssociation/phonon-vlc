%bcond_without qt5
%bcond_without qt6

%define git 20250320

Summary:	Phonon VLC Backend
Name:		phonon-vlc
Version:	0.12.0
Release:	%{?git:0.%{git}.}5
License:	GPLv2+
Group:		Video
Url:		https://www.videolan.org/
%if 0%{?git:1}
Source0:	https://invent.kde.org/libraries/phonon-vlc/-/archive/master/phonon-vlc-master.tar.bz2#/phonon-vlc-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/stable/phonon/phonon-backend-vlc/%{version}/phonon-backend-vlc-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(libvlc)
%if %{with qt5}
BuildRequires:	pkgconfig(phonon4qt5)
BuildRequires:	pkgconfig(Qt5OpenGL)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5X11Extras)
%endif
%if %{with qt6}
BuildRequires:	pkgconfig(phonon4qt6)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6CoreTools)
BuildRequires:	cmake(Qt6GuiTools)
BuildRequires:	cmake(Qt6DBusTools)
BuildRequires:	cmake(Qt6WidgetsTools)
BuildRequires:	cmake(Qt6LinguistTools)
%endif
Provides:	phonon-backend
Requires:	vlc-core
Suggests:	%{name}-translations

%description
This package allows Phonon (the KDE media library) to use VLC for audio and
video playback.

%package translations
Summary:	Translations for the phonon VLC backends (common to all Qt versions)
Group:		Video
BuildArch:	noarch

%description translations
Translations for the phonon VLC backends (common to all Qt versions)

%files translations -f %{name}.lang

%package -n phonon4qt5-vlc
Summary:	Phonon VLC Backend
Provides:	phonon4qt5-backend
Requires:	vlc-core
Suggests:	%{name}-translations

%description -n phonon4qt5-vlc
Phonon4Qt5 VLC Backend.

%files -n phonon4qt5-vlc
%{_libdir}/qt5/plugins/phonon4qt5_backend/phonon_vlc_qt5.so

%package -n phonon4qt6-vlc
Summary:	Phonon VLC Backend
Provides:	phonon4qt6-backend
Requires:	vlc-core
Suggests:	%{name}-translations

%description -n phonon4qt6-vlc
Phonon4Qt6 VLC Backend.

%files -n phonon4qt6-vlc
%{_qtdir}/plugins/phonon4qt6_backend/phonon_vlc_qt6.so

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n phonon%{!?git:-backend}-vlc-%{?git:master}%{!?git:%{version}}
%if %{with qt5}
# The cmake_kde5 macro doesn't currently respect CMAKE_BUILD_DIR,
# so let's make sure the Qt5 build uses the default name
export CMAKE_BUILD_DIR=build
%cmake_kde5 \
	-DPHONON_BUILD_QT5:BOOL=ON \
	-DPHONON_BUILD_QT6:BOOL=OFF \
	-DQT_QMAKE_EXECUTABLE=%{_libdir}/qt5/bin/qmake
cd ..
%endif

%if %{with qt6}
export CMAKE_BUILD_DIR=build-qt6
%cmake \
	-DPHONON_BUILD_QT5:BOOL=OFF \
	-DPHONON_BUILD_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja
cd ..
%endif

%build
%if %{with qt5}
%ninja_build -C build
%endif

%if %{with qt6}
%ninja_build -C build-qt6
%endif

%install
%if %{with qt5}
%ninja_install -C build
%endif

%if %{with qt6}
%ninja_install -C build-qt6
%endif

find %{buildroot}%{_datadir}/locale -name "*.qm" |while read r; do
	L=`echo $r |rev |cut -d/ -f3 |rev`
	echo "%%lang($L) %%{_datadir}/locale/$L/LC_MESSAGES/*.qm" >>%{name}.lang
done
