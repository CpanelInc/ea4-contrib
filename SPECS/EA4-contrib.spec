Name: cpanel-ea4-contrib-release
Version: 0.1
# Doing release_prefix this way for Release allows for OBS-proof versioning, See EA-4602 for more details
%define release_prefix 2
Release: %{release_prefix}%{?dist}.cpanel
Summary: Access the EA4-contrib repository

Group: Development/Tools
License: BSD 2-Clause
Vendor: cPanel, Inc.
Requires: yum

%description
This package puts in please the EA4-contrib.repo file needed to use the software related to EA4 from outside contributors of cPanel.

%install
rm -rf %{buildroot}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -m 644 %_sourcedir/EA4-contrib.repo $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/EA4-contrib.repo

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_sysconfdir}/yum.repos.d/EA4-contrib.repo

%changelog
* Thu Apr 13 2023 Dan Muey <dan@cpanel.net> - 0.1-2
- ZC-10895: make `From repo` have OS info akin to `APT-Sources`

* Wed Mar 01 2017 Jacob Perkins <jacob.perkins@cpanel.net> - 0.1-1
- Initial creation
