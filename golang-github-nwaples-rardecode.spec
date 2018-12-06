%global goipath  github.com/nwaples/rardecode
%global commit   e06696f847aeda6f39a8f0b7cdff193b7690aef6
Version: 0

%global common_description %{expand:
A go package for reading RAR archives.}

%gometa

Name: %{goname}
Release: 0.2%{?dist}
Summary: A go package for reading RAR archives
License: BSD
URL: %{gourl}
Source0: %{gosource}

%description
%{common_description}

%package devel
Summary: %{summary}
BuildArch: noarch

%description devel
%{common_description}

This package contains the source code needed for building packages that import
the %{goipath} Go namespace.

%prep
%gosetup -q

%install
%goinstall

%check
%gochecks

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gite06696f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 27 2018 Dominik Mierzejewski <dominik@greysector.net> - 0-0.1.20180327gite06696f
- First package for Fedora
