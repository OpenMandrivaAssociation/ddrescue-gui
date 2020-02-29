Name:           ddrescue-gui
Version:        2.0.2
Release:        1%{?dist}
Summary:        A simple GUI frontend to make gddrescue easier to use.
Group:          Applications/System
License:        GPLv3+
URL:            https://www.hamishmb.com/html/downloads.php?program_name=ddrescue-gui
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       python3, python3-wxpython4, python3-getdevinfo, python3-requests, ddrescue, psmisc, coreutils, kpartx, parted, util-linux, libnotify, bash, polkit

%description
A simple GUI frontend to make gddrescue easier to use.

%prep
%autosetup -c ddrescue-gui

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/ddrescue-gui/
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/polkit-1/actions
cp -rv LICENSE Tools Tests images docs other DDRescue_GUI.py tests.py %{buildroot}%{_datadir}/ddrescue-gui/
cp -rv ddrescue-gui.desktop %{buildroot}%{_datadir}/applications
cp -rv ddrescue-gui.png %{buildroot}%{_datadir}/pixmaps
cp -rv org.hamishmb.ddrescue-gui.policy %{buildroot}%{_datadir}/polkit-1/actions
chmod -R a+rx %{buildroot}%{_datadir}/ddrescue-gui/

%files
/usr/share/ddrescue-gui/*
/usr/share/applications/ddrescue-gui.desktop
/usr/share/pixmaps/ddrescue-gui.png
/usr/share/polkit-1/actions/org.hamishmb.ddrescue-gui.policy
