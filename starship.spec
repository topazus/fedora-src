%global build_timestamp %(date +"%Y.%m.%d")
%global appname starship
%global debug_package %{nil}

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        %autorelease
Summary:        The minimal, blazing-fast, and infinitely customizable prompt for any shell
License:        ISC
URL:            https://starship.rs
Source:         https://github.com/starship/starship/archive/master/%{appname}-master.tar.gz

BuildRequires:  gcc-c++ pkg-config
BuildRequires:  openssl-devel

%description
The minimal, blazing-fast, and infinitely customizable prompt for any shell!

%prep
%autosetup -n %{appname}-master

if [ ! -d $HOME/.cargo ]; then
  curl https://sh.rustup.rs -sSf | sh -s -- --profile minimal -y
fi

%build
$HOME/.cargo/bin/cargo build --release

%install
install -pDm755 target/release/%{appname} %{buildroot}%{_bindir}/%{appname}

mkdir -p %{buildroot}%{_datadir}/bash-completion/completions %{buildroot}%{_datadir}/zsh/site-functions %{buildroot}%{_datadir}/fish/vendor_conf.d

./target/release/starship completions bash > %{buildroot}%{_datadir}/bash-completion/completions/%{appname}
./target/release/starship completions zsh > %{buildroot}%{_datadir}/zsh/site-functions/_%{appname}
./target/release/starship completions fish > %{buildroot}%{_datadir}/fish/vendor_conf.d/%{appname}.fish

%check

%files
%license LICENSE
%doc README.md
%{_bindir}/%{appname}

%{_datadir}/bash-completion/completions/%{appname}
%{_datadir}/zsh/site-functions/_%{appname}
%{_datadir}/fish/vendor_conf.d/%{appname}.fish

%changelog
%autochangelog
