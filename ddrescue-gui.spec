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
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)

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
%autosetup -p1

%build
%py_build

%install
# setup.py is REALLY REALLY broken...
# So let's do what they do in the Debian packaging info
cat debian/install |while read r; do
	SRC="`echo $r |cut -d' ' -f1`"
	DEST="`echo $r |cut -d' ' -f2`"
	mkdir -p "%{buildroot}$DEST"
	cp -a "$SRC" "%{buildroot}$DEST"
done

%files
%{_datadir}/ddrescue-gui/*
%{_datadir}/applications/ddrescue-gui.desktop
%{_datadir}/pixmaps/ddrescue-gui.png
%{_datadir}/polkit-1/actions/org.hamishmb.ddrescue-gui.policy
