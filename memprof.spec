Summary:	Tool for memory profiling and leak detection
Name:		memprof
Version:	0.3.0
Release:	5
License:	GPL
Group:		Development/Debuggers
Group(pl):	Programowanie/Odpluskwiacze
Source:		%{name}-%{version}.tar.gz
Patch:		memprof-applnk.patch
BuildRequires:	libglade-devel >= 0.7-1
BuildRequires:	gettext-devel
BuildRequires:	automake
BuildRequires:	binutils
BuildRequires:	gnome-libs-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6
%define		_applnkdir	%{_datadir}/applnk

%description
Memprof is a tool for profiling memory usage and detecting memory leaks. It
can be used with existing binaries without need for recompilation.

%prep
%setup -q
%patch -p1

%build
gettextize --copy --force
automake
LDFLAGS="-s"; export LDFLAGS
%configure \
	--disable-static

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so

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
