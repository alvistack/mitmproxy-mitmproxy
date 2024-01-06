# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-mitmproxy
Epoch: 100
Version: 8.0.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Interactive, SSL/TLS-capable intercepting proxy
License: MIT
URL: https://github.com/mitmproxy/mitmproxy/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
mitmproxy is an interactive, SSL/TLS-capable intercepting proxy with a
console interface for HTTP/1, HTTP/2, and WebSockets.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%package -n mitmproxy
Summary: Interactive, SSL/TLS-capable intercepting proxy
Requires: python3
Requires: python3-asgiref >= 3.2.10
Requires: python3-blinker >= 1.4
Requires: python3-brotli >= 1.0
Requires: python3-certifi >= 2019.9.11
Requires: python3-cryptography >= 36
Requires: python3-flask >= 1.1.1
Requires: python3-h11 >= 0.11
Requires: python3-h2 >= 4.1
Requires: python3-hyperframe >= 6.0
Requires: python3-kaitaistruct >= 0.7
Requires: python3-ldap3 >= 2.8
Requires: python3-msgpack >= 1.0.0
Requires: python3-passlib >= 1.6.5
Requires: python3-protobuf >= 3.14
Requires: python3-publicsuffix2 >= 2.20190812
Requires: python3-pyOpenSSL >= 21.0
Requires: python3-pyparsing >= 2.4.2
Requires: python3-pyperclip >= 1.6.0
Requires: python3-ruamel.yaml >= 0.16
Requires: python3-sortedcontainers >= 2.3
Requires: python3-tornado >= 6.1
Requires: python3-urwid >= 2.1.1
Requires: python3-wsproto >= 1.0
Requires: python3-zstandard >= 0.11
Provides: python3-mitmproxy = %{epoch}:%{version}-%{release}
Provides: python3dist(mitmproxy) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-mitmproxy = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(mitmproxy) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-mitmproxy = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(mitmproxy) = %{epoch}:%{version}-%{release}

%description -n mitmproxy
mitmproxy is an interactive, SSL/TLS-capable intercepting proxy with a
console interface for HTTP/1, HTTP/2, and WebSockets.

%files -n mitmproxy
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*

%changelog
