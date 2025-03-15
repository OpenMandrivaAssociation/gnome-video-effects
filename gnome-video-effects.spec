%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	Collection of GStreamer video effects
Name:		gnome-video-effects
Version:	0.6.0
Release:	5
Group:		System/Libraries
License:	GPLv2
Url:		https://live.gnome.org/GnomeVideoEffects
Source0:	https://ftp.gnome.org/pub/GNOME/sources/gnome-video-effects/%{url_ver}/%{name}-%{version}.tar.xz
Buildarch:	noarch
BuildRequires:  meson
BuildRequires:	intltool

%description
A collection of GStreamer effects to be used in different GNOME Modules.

%package devel
Summary:	Collection of GStreamer video effects
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description devel
A collection of GStreamer effects to be used in different GNOME Modules.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README
%{_datadir}/gnome-video-effects

%files devel
%doc AUTHORS COPYING NEWS
%{_datadir}/pkgconfig/gnome-video-effects.pc

