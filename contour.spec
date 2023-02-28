%bcond_without qt6
%global commit 99d6e65ab5ae368be6d951f3f48c725323405978
%global short_commit %(c=%{commit}; echo ${c:0:7})

Name:           contour
Version:        20230226.%{short_commit}
Release:        %autorelease
Summary:        Modern C++ Terminal Emulator
License:        Apache-2.0
URL:            https://github.com/contour-terminal/contour
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  gcc-c++ cmake extra-cmake-modules
BuildRequires:  catch2-devel fmt-devel guidelines-support-library-devel
BuildRequires:  range-v3-devel yaml-cpp-devel libxcb-devel
BuildRequires:  fontconfig-devel freetype-devel harfbuzz-devel libunicode-devel

%if %{with qt6}
BuildRequires:  qt6-qtbase-devel qt6-qtbase-gui qt6-qtdeclarative-devel
BuildRequires:  qt6-qtmultimedia-devel qt6-qtwayland
%else
BuildRequires:  qt5-qtbase-devel qt5-qtbase-gui qt5-qtmultimedia-devel
BuildRequires:  qt5-qtx11extras-devel
%endif

Requires:       fontconfig freetype harfbuzz yaml-cpp
%if %{with qt6}
Requires:       qt6-qtbase qt6-qtbase-gui qt6-qtmultimedia
%else
Requires:       qt5-qtbase qt5-qtbase-gui qt5-qtmultimedia
%endif

%description
Contour is a modern and actually fast, modal, virtual terminal emulator,
for everyday use. It is aiming for power users with a modern feature mindset.

%prep
%autosetup -n %{name}-%{commit} -p1

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

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/contour
%{_datadir}/applications/org.contourterminal.Contour.desktop
%{_datadir}/kservices5/ServiceMenus/*.desktop
%dir %{_datadir}/contour
%{_datadir}/contour/shell-integration/shell-integration.fish
%{_datadir}/contour/shell-integration/shell-integration.tcsh
%{_datadir}/contour/shell-integration/shell-integration.zsh
%{_datadir}/terminfo/c/contour*
%{_datadir}/icons/hicolor/*/apps/org.contourterminal.Contour.png
%{_datadir}/metainfo/org.contourterminal.Contour.metainfo.xml

%changelog
%autochangelog
