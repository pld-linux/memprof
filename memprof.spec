Summary:	Tool for memory profiling and leak detection
Summary(pl):	Narzêdzie do profilowania i detekcji leak'ów pamiêci
Name:		memprof
Version:	0.4.1
Release:	4
Epoch:		1
License:	GPL
Group:		Development/Debuggers
Group(de):	Entwicklung/Debugger
Group(pl):	Programowanie/Odpluskwiacze
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/memprof/%{name}-%{version}.tar.gz
URL:		http://people.redhat.com/~otaylor/memprof/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	binutils-static
BuildRequires:	libglade-devel >= 0.7
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Memprof is a tool for profiling memory usage and detecting memory
leaks. It can be used with existing binaries without need for
recompilation.

%description -l pl
Memprof jest narzêdziem do profilowania pamiêci oraz detekcji 
"memory leak'ów". Mo¿e byæ u¿ywany z istniej±cymi binariami bez
konieczno¶ci ich przebudowywania.

%prep
%setup -q

%build
rm -f missing
gettextize --copy --force
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Developmentdir=%{_applnkdir}/Development

%find_lang %{name}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_datadir}/memprof
%{_applnkdir}/Development/*
%{_pixmapsdir}/*
