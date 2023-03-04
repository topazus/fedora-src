%bcond_without qt6

Name:           contour-terminal
Version:        0.3.11.258
Release:        %autorelease
Summary:        Modern C++ Terminal Emulator
License:        Apache-2.0
URL:            https://github.com/contour-terminal/contour
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++ cmake extra-cmake-modules
BuildRequires:  fmt-devel guidelines-support-library-devel
BuildRequires:  range-v3-devel yaml-cpp-devel libxcb-devel
BuildRequires:  fontconfig-devel freetype-devel harfbuzz-devel
BuildRequires:  libunicode-devel
%if %{?fedora} <= 38
BuildRequires:  catch-devel
%else
BuildRequires:  catch2-devel
%endif

%if %{with qt6}
BuildRequires:  qt6-qtbase-devel qt6-qtdeclarative-devel
BuildRequires:  qt6-qtmultimedia-devel
%else
BuildRequires:  qt5-qtbase-devel qt5-qtdeclarative-devel
BuildRequires:  qt5-qtmultimedia-devel
%endif

Requires:       fontconfig freetype harfbuzz yaml-cpp
Requires:       libunicode
%if %{with qt6}
Requires:       qt6-qtbase qt6-qtbase-gui qt6-qtmultimedia
%else
Requires:       qt5-qtbase qt5-qtbase-gui qt5-qtmultimedia
%endif

%description
Contour is a modern and actually fast, modal, virtual terminal emulator,
for everyday use. It is aiming for power users with a modern feature mindset.

%prep
%autosetup -n contour-%{version}

%build
%cmake \
%if %{with qt6}
    -DCONTOUR_BUILD_WITH_QT6=ON
%else
    -DCONTOUR_BUILD_WITH_QT6=OFF
%endif
%cmake_build

%install
%cmake_install

rm %{buildroot}%{_datadir}/contour/LICENSE.txt
rm %{buildroot}%{_datadir}/contour/README.md

%check
%ctest

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/contour
%{_datadir}/applications/*.desktop
%{_datadir}/kservices5/ServiceMenus/*.desktop
%dir %{_datadir}/contour
%dir %{_datadir}/contour/shell-integration
%{_datadir}/contour/shell-integration/shell-integration.fish
%{_datadir}/contour/shell-integration/shell-integration.tcsh
%{_datadir}/contour/shell-integration/shell-integration.zsh
%{_datadir}/terminfo/c/contour*
%{_datadir}/icons/hicolor/*/apps/*.png
%{_metainfodir}/*.xml

%changelog
%autochangelog
