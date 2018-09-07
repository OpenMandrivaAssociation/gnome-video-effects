%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	Collection of GStreamer video effects
Name:		gnome-video-effects
Version:	0.4.3
Release:	1
Group:		System/Libraries
License:	GPLv2
Url:		http://live.gnome.org/GnomeVideoEffects
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-video-effects/%{url_ver}/%{name}-%{version}.tar.xz
Buildarch:	noarch
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
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc README
%{_datadir}/gnome-video-effects

%files devel
%doc AUTHORS COPYING NEWS
%{_datadir}/pkgconfig/gnome-video-effects.pc

