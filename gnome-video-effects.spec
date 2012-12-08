Name:           gnome-video-effects
Version:        0.4.0
Release:        %mkrel 1
Summary:        Collection of GStreamer video effects

Group:          System/Libraries
License:        GPLv2
URL:            http://live.gnome.org/GnomeVideoEffects
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
Buildarch:      noarch
BuildRequires:  intltool
BuildRoot: 	%{_tmppath}/%{name}-%{version}-root

%description
A collection of GStreamer effects to be used in different GNOME Modules.

%package devel
Summary:Collection of GStreamer video effects
Group: Development/Other
Requires: %name = %version-%release

%description devel
A collection of GStreamer effects to be used in different GNOME Modules.

%prep
%setup -q

%build
%configure2_5x
%make


%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%doc README
%{_datadir}/gnome-video-effects

%files devel
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS
%{_datadir}/pkgconfig/gnome-video-effects.pc




%changelog
* Mon Dec 06 2010 Götz Waschk <waschk@mandriva.org> 0.2.0-1mdv2011.0
+ Revision: 611945
- import gnome-video-effects

