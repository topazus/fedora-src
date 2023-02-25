%bcond_without qt6
%global libunicode_git_sha df619a0f2ba45297de346e2c0c7af53a954901b4
%global termbench_pro_git_sha a4feadd3a698e4fe2d9dd5b03d5f941534a25a91
%global ucd_version 15.0.0

Name:           contour
Version:        0.3.10.257
Release:        %autorelease
Summary:        Modern C++ Terminal Emulator
License:        Apache-2.0
URL:            https://github.com/contour-terminal/contour
Source0:        https://github.com/contour-terminal/contour/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/contour-terminal/libunicode/archive/%{libunicode_git_sha}.tar.gz
Source2:        https://github.com/contour-terminal/termbench-pro/archive/%{termbench_pro_git_sha}.tar.gz
Source3:        https://www.unicode.org/Public/%{ucd_version}/ucd/UCD.zip

Patch0:         https://gist.githubusercontent.com/topazus/8e0ab94f380733e5bb97f3654d66bb4d/raw/56617b721942eee3718f0d37728bb8635f33bec9/fix-header-change.patch
Patch1:         https://gist.githubusercontent.com/topazus/b067d22c6ac22787ac594fd828ff459d/raw/918b67e2209a0d0c76ca85bf9e682ff6f309ebdf/use-3rdparty.patch
#Patch2:         libunicode-fix-header-change.patch

BuildRequires:  gcc-c++ cmake extra-cmake-modules
BuildRequires:  catch-devel fmt-devel guidelines-support-library-devel
BuildRequires:  range-v3-devel yaml-cpp-devel libxcb-devel
BuildRequires:  fontconfig-devel freetype-devel harfbuzz-devel

%if %{with qt6}
BuildRequires:  qt6-qtbase-devel qt6-qtdeclarative-devel qt6-qtmultimedia-devel
%else
BuildRequires:  qt5-qtbase-devel qt5-qtdeclarative-devel qt5-qtmultimedia-devel
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
%setup -a0
%setup -a1 -a2
%autopatch -p0 -p1

mkdir -p 3rdparty
mv libunicode-%{libunicode_git_sha} 3rdparty/libunicode
mv termbench-pro-%{termbench_pro_git_sha} 3rdparty/termbench-pro

mkdir -p 3rdparty/libunicode/_ucd/ucd-%{ucd_version}
pushd 3rdparty/libunicode/_ucd/ucd-%{ucd_version}
    unzip %{SOURCE3}
popd

echo 'macro(ContourThirdParties_Embed_libunicode)
    add_subdirectory(${ContourThirdParties_SRCDIR}/libunicode EXCLUDE_FROM_ALL)
endmacro()
macro(ContourThirdParties_Embed_termbench_pro)
    add_subdirectory(${ContourThirdParties_SRCDIR}/termbench-pro EXCLUDE_FROM_ALL)
endmacro()' > 3rdparty/CMakeLists.txt

%build
%if %{with qt6}
%cmake \
    -DBUILD_SHARED_LIBS:BOOL=Off \
    -DCONTOUR_BUILD_WITH_QT6=On
%else
%cmake \
    -DBUILD_SHARED_LIBS:BOOL=Off \
    -DCONTOUR_BUILD_WITH_QT6=Off
%endif
%cmake_build

%install
%cmake_install

rm %{buildroot}%{_datadir}/contour/LICENSE.txt
rm %{buildroot}%{_datadir}/contour/README.md

./redhat-linux-build/src/contour/contour generate config to %{buildroot}%{_datadir}/contour/contour.yml

%check
%ctest

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/contour
%{_datadir}/applications/org.contourterminal.Contour.desktop
%{_datadir}/kservices5/ServiceMenus/*.desktop
%dir %{_datadir}/contour
%{_datadir}/contour/shell-integration.zsh
%{_datadir}/contour/contour.yml
%{_datadir}/terminfo/c/contour*
%{_datadir}/icons/hicolor/*/apps/org.contourterminal.Contour.png
%{_datadir}/metainfo/org.contourterminal.Contour.metainfo.xml

%changelog
%autochangelog
