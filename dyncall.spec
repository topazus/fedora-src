Name:           dyncall
Version:        1.3
Release:        %autorelease
Summary:        A Generic Dynamic FFI package
License:        ISC
URL:            https://dyncall.org/
Source0:        https://dyncall.org/r%{version}/dyncall-%{version}.tar.gz

BuildRequires:  gcc make

%description
The dyncall library encapsulates architecture-, OS- and compiler-specific function call semantics
in a virtual bind argument parameters from left to right and then call interface allowing 
programmers to call C functions in a completely dynamic manner.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup

%build
./configure --prefix=%{buildroot}%{_prefix}
%make_build

%install
%make_install

%files
%{_prefix}/lib/libdyncall*.a
%{_prefix}/lib/libdynload_s.a

%files devel
%{_includedir}/dyncall*.h
%{_includedir}/dynload.h

%changelog
%autochangelog
