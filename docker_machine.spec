#
# spec file for package docker-machine
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define         go_arches %ix86 x86_64
Name:           docker_machine
Version:        0.3.0
Release:        0
License:        Apache-2.0
Summary:        Machine management for container-centric world
Url:            https://docs.docker.com/machine
Group:          System/Management
Source:         %{name}-%{version}.tar.gz
Source1:        suse.go
BuildRequires:  bash-completion
BuildRequires:  device-mapper-devel >= 1.2.68
BuildRequires:  glibc-devel-static
%ifarch %go_arches
BuildRequires:  go >= 1.4
BuildRequires:  go-go-md2man
%else
BuildRequires:  gcc5-go >= 5.0
BuildRequires:  libapparmor-devel
BuildRequires:  procps
BuildRequires:  sqlite3-devel
BuildRequires:  zsh
Requires:       e2fsprogs
Requires:       procps
Requires:       bash-completion
Requires:       tar >= 1.26
Requires:       xz  >= 4.9
PreReq:         %fillup_prepreq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
blah blah
%prep
%setup -q -n docker_machine%{version}

%build
%ifnarch %go_arches
mkdir /tmp/dirty-hack
ln -s /usr/bin/go-5 /tmp/dirty-hack/go
export PATH=/tmp/dirty-hack:$PATH
%endif

%install
install -d %{buildroot}%{go_contribdir}
install -d %{buildroot}%{_bindir} 

%defattr(-,root,root)
