%define    ver     0.3.0
%define    rel     3
%define    prefix  /usr

Summary: Tool for memory profiling and leak detection
Name: memprof
Version: %{ver}
Release: %{rel}
Copyright: GPL
Group: Development/Debuggers
Source: memprof-%{ver}.tar.gz
Requires: libglade >= 0.7-1
BuildRoot: /var/tmp/%{name}-root
Exclusivearch: i386

Patch1: memprof-0.3.0-staticbfd.patch

%description
Memprof is a tool for profiling memory usage and
detecting memory leaks. It can be used with existing
binaries without need for recompilation.
%prep
%setup -q

%patch1 -p1 -b .staticbfd

%build
# The .staticbfd patch changes configure.in
autoconf
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{prefix}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
strip $RPM_BUILD_ROOT%{prefix}/bin/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{prefix}/bin/*
%{prefix}/lib/*
%{prefix}/share/memprof
# FIXME: we need some translations
# %{prefix}/share/locale/*/*/*

%changelog
* Wed Jan 12 2000 Owen Taylor <otaylor@redhat.com>
- Link against libbfd and libiberty statically.

* Wed Oct 27 1999 Owen Taylor <otaylor@redhat.com>
- Initial package
