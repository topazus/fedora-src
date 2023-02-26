%global debug_package %{nil}
%global appname vscode
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%bcond_without check

Name:           %{appname}
Version:        %{build_timestamp}
Release:        %autorelease
Summary:        a code editor redefined and optimized for building and debugging modern web and cloud applications.
License:        MIT
URL:            https://code.visualstudio.com/
Source0:        https://update.code.visualstudio.com/%{version}/linux-x64/stable
Source1:        https://raw.githubusercontent.com/topazus/fedora-copr/main/vscode/vscode.desktop

Requires:       libxkbfile xdg-utils

%description
Visual Studio Code (vscode): Editor for building and debugging modern web and cloud applications (official binary version)

%prep
%autosetup -n VSCode-linux-x64

%build


%install
mkdir -p %{buildroot}/opt/vscode
cp -r * %{buildroot}/opt/vscode

#install -pDm755 bin/code %{buildroot}%{_bindir}/code
install -pDm644 ./resources/app/resources/linux/code.png %{buildroot}/usr/share/icons/code.png

install -pDm644 ./resources/completions/bash/code %{buildroot}/usr/share/bash-completion/completions/code
install -pDm644 ./resources/completions/zsh/_code %{buildroot}/usr/share/zsh/site-functions/_code

install -pDm644 %{SOURCE1} %{buildroot}/usr/share/applications/vscode.desktop

%check

%files
%dir /opt/vscode
/opt/vscode/*
/usr/share/icons/code.png
/usr/share/bash-completion/completions/code
/usr/share/zsh/site-functions/_code
/usr/share/applications/vscode.desktop

%ghost /usr/bin/code

%post
ln -s /opt/vscode/bin/code /usr/bin/code

%changelog
%autochangelog
