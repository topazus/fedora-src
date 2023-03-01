Name:           abseil
Version:        20230125.1
Release:        %autorelease
Summary:        Abseil Common Libraries (C++)
License:        Apache-2.0
URL:            https://github.com/abseil/abseil-cpp
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
Abseil Common Libraries (C++)

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
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so


%changelog
%autochangelog
