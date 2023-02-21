Name:           workflow
Version:        0.10.5
Release:        %autorelease
Summary:        C++ Parallel Computing and Asynchronous Networking Engine
License:        Apache-2.0 or GPL-2.0-only
URL:            https://github.com/sogou/workflow
Source:         https://github.com/sogou/workflow/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake

%global _description %{expand:
As Sogou`s C++ server engine, Sogou C++ Workflow supports almost all back-end
C++ online services of Sogou, including all search services, cloud input
method, online advertisements, etc., handling more than 10 billion requests
every day. This is an enterprise-level programming engine in light and elegant
design which can satisfy most C++ back-end development requirements.}

%description %{_description}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel %{_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        static
Summary:        Development files for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    devel %{_description}

The %{name}-static package contains libraries for
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
%{_libdir}/*.so.*

%files devel
%doc README.md
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/%{name}

%files static
%{_libdir}/libworkflow.a

%exclude %{_docdir}/workflow-0.10.5/README.md

%changelog
%autochangelog
