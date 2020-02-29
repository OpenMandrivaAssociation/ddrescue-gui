#NOT READY YET!

Name:           ddrescue-gui
Version:        2.0.2
Release:        1
Summary:        A simple GUI frontend to make gddrescue easier to use.
Group:          Applications/System
License:        GPLv3+
URL:            https://www.hamishmb.com/html/downloads.php?program_name=ddrescue-gui
Source0:        https://www.hamishmb.com/files/Downloads/ddrescue-gui/%{version}/OtherDistro/ddrescue-gui_%{version}_otherdistro-0ubuntu1_ppa1.tar.gz
BuildArch:      noarch

BuildRequires:  python
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)

Requires: python
#Requires:  python-wxpython4, 
Requires: wxPython
#Not ready
Requires: python3dist(getdevinfo)
Requires: python3dist(requests)
Requires: ddrescue
Requires: psmisc
Requires: coreutils
Requires: kpartx 
Requires: parted 
Requires: util-linux
Requires: libnotify
Requires: bash
Requires: polkit

%description
A simple GUI frontend to make gddrescue easier to use.

%prep
%setup -qn ddrescue-gui-%{version}

%build
%py_build

cp -rv LICENSE tests.py %{buildroot}%{_datadir}/ddrescue-gui/

%install
%py_install

#rm -rf $RPM_BUILD_ROOT
#mkdir -p %{buildroot}%{_datadir}/ddrescue-gui/
#mkdir -p %{buildroot}%{_datadir}/applications
#mkdir -p %{buildroot}%{_datadir}/pixmaps
#mkdir -p %{buildroot}%{_datadir}/polkit-1/actions
#cp -rv LICENSE Tools Tests images docs other DDRescue_GUI.py tests.py %{buildroot}%{_datadir}/ddrescue-gui/
#cp -rv ddrescue-gui.desktop %{buildroot}%{_datadir}/applications
#cp -rv ddrescue-gui.png %{buildroot}%{_datadir}/pixmaps
#cp -rv org.hamishmb.ddrescue-gui.policy %{buildroot}%{_datadir}/polkit-1/actions
#chmod -R a+rx %{buildroot}%{_datadir}/ddrescue-gui/

%files
%{_datadir}/ddrescue-gui/*
%{_datadir}/applications/ddrescue-gui.desktop
%{_datadir}/pixmaps/ddrescue-gui.png
%{_datadir}/polkit-1/actions/org.hamishmb.ddrescue-gui.policy
