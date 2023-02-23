Name:           ensmallen
Version:        2.19.0
Release:        %autorelease
Summary:        A header-only C++ library for numerical optimization
License:        BSD AND BOOST
URL:            https://github.com/mlpack/ensmallen
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  armadillo-devel openblas-devel

%description
Ensmallen is a high-quality C++ library for non-linear numerical optimization.

Ensmallen provides many types of optimizers that can be used for virtually any
numerical optimization task. This includes gradient descent techniques,
gradient-free optimizers, and constrained optimization. ensmallen also allows
optional callbacks to customize the optimization process.

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
cd redhat-linux-build
make ensmallen_tests %{?smp_flags}
./ensmallen_tests --durations yes

%files
%license LICENSE.txt
%doc README.md


%files devel
%{_includedir}/ensmallen.hpp
%{_includedir}/ensmallen_bits
%dir /usr/lib/cmake/ensmallen
/usr/lib/cmake/ensmallen/*.cmake

%changelog
%autochangelog
