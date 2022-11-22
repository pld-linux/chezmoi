Summary:	Manage your dotfiles across multiple diverse machines, securely
Name:		chezmoi
Version:	2.27.1
Release:	1
License:	MIT
Group:		Applications/Networking
Source0:	https://github.com/twpayne/chezmoi/releases/download/v%{version}/%{name}_%{version}_linux_amd64.tar.gz
# Source0-md5:	b7da1e16598d1ffc2bff2ac5bd27aa5d
URL:		https://syncthing.net/
ExclusiveArch:	%{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Manage your dotfiles across multiple diverse machines, securely.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install -p %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/%{name}
