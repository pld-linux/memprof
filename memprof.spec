# TODO: update to 0.6
Summary:	Tool for memory profiling and leak detection
Summary(pl.UTF-8):	Narzędzie do profilowania i detekcji wycieków pamięci
Name:		memprof
Version:	0.4.1
Release:	5
Epoch:		1
License:	GPL v2+
Group:		Development/Debuggers
Source0:	http://ftp.gnome.org/pub/GNOME/sources/memprof/0.4/%{name}-%{version}.tar.gz
# Source0-md5:	a3aab0b210bc6a49765e48c93808931c
Patch0:		%{name}-bfdutils.patch
URL:		http://www.gnome.org/projects/memprof/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	binutils-static
BuildRequires:	gettext-tools
BuildRequires:	gnome-libs-devel
BuildRequires:	libglade-gnome-devel >= 0.7
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Memprof is a tool for profiling memory usage and detecting memory
leaks. It can be used with existing binaries without need for
recompilation.

%description -l pl.UTF-8
Memprof jest narzędziem do profilowania pamięci oraz detekcji "memory
leaków". Może być używany z istniejącymi binariami bez konieczności
ich przebudowywania.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Developmentdir=%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_datadir}/memprof
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
