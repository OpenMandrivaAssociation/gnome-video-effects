Name:           gnome-video-effects
Version:        0.3.0
Release:        1
Summary:        Collection of GStreamer video effects
Group:          System/Libraries
License:        GPLv2
URL:            http://live.gnome.org/GnomeVideoEffects
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Buildarch:      noarch
BuildRequires:  intltool

%description
A collection of GStreamer effects to be used in different GNOME Modules.

%package devel
Summary:Collection of GStreamer video effects
Group: Development/Other
Requires: %{name} = %{version}-%{release}

%description devel
A collection of GStreamer effects to be used in different GNOME Modules.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%doc README
%{_datadir}/gnome-video-effects

%files devel
%doc AUTHORS COPYING NEWS
%{_datadir}/pkgconfig/gnome-video-effects.pc

