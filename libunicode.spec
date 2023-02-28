%global commit dc246b8a6804d3f265c67d573d484550c38652f9
%global short_commit %(c=%{commit}; echo ${c:0:7})
%global ucd_version 15.0.0

Name:           libunicode
Version:        20230226.%{short_commit}
Release:        %autorelease
Summary:        Modern C++17 Unicode library
License:        Apache-2.0
URL:            https://github.com/contour-terminal/libunicode
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
Source1:        https://www.unicode.org/Public/%{ucd_version}/ucd/UCD.zip

BuildRequires:  gcc-c++ cmake unzip
BuildRequires:  catch2-devel range-v3-devel fmt-devel

%description
The goal of libunicode library is to bring painless unicode support to C++
with simple and easy to understand APIs. The API naming conventions are chosen
to look familiar to those using the C++ standard libary.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tools
Summary:       Tools for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description tools
The %{name}-tools package contains tools about %{name}.

%prep
%autosetup -n %{name}-%{commit}

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
%{_libdir}/%{name}*.so.*

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%dir %{_libdir}/cmake/%{name}
%{_libdir}/cmake/%{name}/*.cmake
%{_libdir}/%{name}*.so

%files tools
%{_bindir}/unicode-query

%changelog
%autochangelog
