Summary:	Tool for memory profiling and leak detection
Summary(pl):	Narzêdzie do profilowania i detekcji wycieków pamiêci
Name:		memprof
Version:	0.4.1
Release:	5
Epoch:		1
License:	GPL
Group:		Development/Debuggers
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/memprof/0.4/%{name}-%{version}.tar.gz
# Source0-md5:	a3aab0b210bc6a49765e48c93808931c
Patch0:		%{name}-bfdutils.patch
URL:		http://www.gnome.org/projects/memprof/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	binutils-static
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	libglade-gnome-devel >= 0.7
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Memprof is a tool for profiling memory usage and detecting memory
leaks. It can be used with existing binaries without need for
recompilation.

%description -l pl
Memprof jest narzêdziem do profilowania pamiêci oraz detekcji "memory
leaków". Mo¿e byæ u¿ywany z istniej±cymi binariami bez konieczno¶ci
ich przebudowywania.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
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
	Developmentdir=%{_applnkdir}/Development

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
%{_pixmapsdir}/*
