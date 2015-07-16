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
Source:         %{name}-%{version}.tar.bz2
Source1:        suse.go
BuildRequires:  
PreReq:         %fillup_prepreq
Provides:
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} %{?_smp_mflags}

%post

%postun

%files
%defattr(-,root,root)
%doc ChangeLog README COPYING


