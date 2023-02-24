
%global git_date    20230222
%global git_commit  f59f3a2135af3c60fb55c742835e0346bba9370b
%global git_commit_short  %(c="%{git_commit}"; echo ${c:0:8})

Name:           elmerfem
Version:        %{git_date}.git%{git_commit_short}
Release:        %autorelease
Summary:        a finite element software for numerical solution of partial differential equations
License:        GPL-2.0-only AND LGPL-2.1-only
URL:            https://github.com/ElmerCSC/elmerfem
Source:         %{url}/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz

BuildRequires:  gcc-c++ gcc-gfortran
BuildRequires:  cmake
BuildRequires:  openmpi-devel openblas-devel lapack-devel
BuildRequires:  netcdf-devel MUMPS-devel

%description
Elmer is a finite element software for numerical solution of partial
differential equations. Elmer is capable of handling any number of equations
and is therefore ideally suited for the simulation of multiphysical problems.
It includes models, for example, of structural mechanics, fluid dynamics, heat
transfer and electromagnetics. Users can also write their own equations that
can be dynamically linked with the main program.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{git_commit}

%build
%cmake \
  -DWITH_OpenMP=True \
  -DWITH_MPI=True \
  -DWITH_ElmerIce=True \
  -DWITH_Mumps=True
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc README.adoc


%files devel


%changelog
%autochangelog
