Name:           yyjson
Version:        0.6.0
Release:        %autorelease
Summary:        A high performance JSON library written in ANSI C
License:        Apache-2.0
URL:            https://github.com/ibireme/yyjson
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake

%description
The yyjson library is a high performance JSON library written in ANSI C.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup

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

%files devel
%{_includedir}/*

%changelog
%autochangelog
