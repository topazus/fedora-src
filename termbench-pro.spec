%global termbench_pro_git_sha a4feadd3a698e4fe2d9dd5b03d5f941534a25a91

Name:           termbench-pro
Version:        20230219.a4feadd
Release:        %autorelease
Summary:        Terminal Benchmarking as CLI and library
License:        Apache-2.0
URL:            https://github.com/contour-terminal/termbench-pro
Source0:        %{url}/archive/%{termbench_pro_git_sha}.tar.gz

BuildRequires:  gcc-c++ cmake

%description
Termbench Pro is the interim name for a project to benchmark the terminal
emulators backend bandwidth throughput.

%prep
%autosetup -n %{name}-%{termbench_pro_git_sha}

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE.txt
%doc README.md

%changelog
%autochangelog
