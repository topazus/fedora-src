%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname gcc

Name:           %{appname}-stable
Version:        12.2.0
Release:        1%{?dist}
Summary:        GNU Compiler Collection (GCC)
License:        GPL
URL:            http://gcc.gnu.org/
Source:  	https://ftp.gnu.org/gnu/gcc/gcc-12.2.0/gcc-%{version}.tar.xz

BuildRequires:  zlib-devel bison flex
BuildRequires:  gmp-devel mpfr-devel libmpc-devel
BuildRequires:  python3-devel
BuildRequires:  gcc gcc-c++ make
BuildRequires:  git wget
BuildRequires:  dblatex dejagnu docbook5-style-xsl gcc-gdc
BuildRequires:  gcc-gnat gdb glibc-static hostname libgnat
BuildRequires:  libgphobos-static python3-sphinx sharutils

%description
Powerful yet simple to use screenshot software.

%prep
%autosetup -n gcc-%{version}

%build
./configure \
	--enable-languages=c,c++,fortran \
	--prefix=/opt/gcc \
	--enable-checking=release --with-system-zlib \
	--without-isl --disable-multilib --enable-bootstrap --host=x86_64-pc-linux-gnu
make bootstrap %{?_smp_mflags}

%install
%make_install

%check

%files
/opt/gcc/

%changelog
