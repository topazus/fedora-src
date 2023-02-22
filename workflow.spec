Name:           workflow
Version:        0.10.5
Release:        %autorelease
Summary:        C++ Parallel Computing and Asynchronous Networking Engine
License:        Apache-2.0
URL:            https://github.com/sogou/workflow
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  openssl-devel

%description
As Sogou`s C++ server engine, Sogou C++ Workflow supports almost all back-end
C++ online services of Sogou, including all search services, cloud input
method, online advertisements, etc., handling more than 10 billion requests
every day. This is an enterprise-level programming engine in light and elegant
design which can satisfy most C++ back-end development requirements.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        static
Summary:        Static library for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    static
The %{name}-static package contains the static library for %{name}.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install
rm -rf %{buildroot}%{_docdir}/workflow-%{version}

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/%{name}

%files static
%{_libdir}/libworkflow.a

%changelog
%autochangelog
