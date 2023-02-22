%global libunicode_git_sha 5987666ea263eb09b03ad57a8cb7601816f85f30
%global ucd_version 15.0.0

Name:           libunicode
Version:        20230219.5987666
Release:        %autorelease
Summary:        Modern C++17 Unicode library
License:        Apache-2.0
URL:            https://github.com/contour-terminal/libunicode
Source0:        %{url}/archive/%{libunicode_git_sha}.tar.gz
Source1:        https://www.unicode.org/Public/%{ucd_version}/ucd/UCD.zip

BuildRequires:  gcc-c++ cmake unzip
BuildRequires:  catch-devel range-v3-devel fmt-devel

%description
The goal of libunicode library is to bring painless unicode support to C++
with simple and easy to understand APIs. The API naming conventions are chosen
to look familiar to those using the C++ standard libary.

%package        static
Summary:        Static library for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    static
The %{name}-static package contains the static library for %{name}.

%prep
#%setup -q -n %{name}-%{libunicode_git_sha} -a0
%autosetup -p1 -n %{name}-%{libunicode_git_sha}

mkdir -p _ucd/ucd-%{ucd_version}
pushd _ucd/ucd-%{ucd_version}
    unzip %{SOURCE1}
popd

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_bindir}/unicode-query

%files static
%{_includedir}/unicode/*.h
%{_libdir}/cmake/%{name}/*.cmake
/usr/lib64/libunicode*.a

%changelog
%autochangelog
