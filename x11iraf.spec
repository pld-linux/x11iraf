Summary:	X11IRAF - utilities and applications developed by the IRAF project
Summary(pl.UTF-8):   X11IRAF - narzędzia i aplikacje stworzone w ramach projektu IRAF
Name:		x11iraf
Version:	1.3.1
Release:	0.1
License:	?
Group:		X11/Applications
Source0:	ftp://iraf.noao.edu/iraf/x11iraf/%{name}-v%{version}-src.tar.gz
# Source0-md5:	77870465d792b0a3a61c34e6bc077224
Patch0:		%{name}-errno.patch
Patch1:		%{name}-system-libs.patch
Patch2:		%{name}-noism.patch
URL:		http://iraf.noao.edu/iraf/web/projects/x11iraf/x11iraf.html
BuildRequires:	XFree86-devel
BuildRequires:	Xaw3d-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	/usr/X11R6/lib/X11/app-defaults

%description
X11IRAF - X11/GUI development utilities and applications developed by
the IRAF Project, National Optical Astronomy Observatories.

%description -l pl.UTF-8
X11IRAF to narzędzia programistyczne i aplikacje X11/GUI stworzone w
ramach projektu IRAF w obserwatoriach National Optical Astronomy.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
xmkmf -a
%{__make} -C obm \
	CDEBUGFLAGS="%{rpmcflags}"

%{__make} -C cdl \
	CDEBUGFLAGS="%{rpmcflags}"

%{__make} \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_appdefsdir}}

install bin.linux/[!r]* $RPM_BUILD_ROOT%{_bindir}
install man/[!r]* $RPM_BUILD_ROOT%{_mandir}/man1
install app-defaults/* $RPM_BUILD_ROOT%{_appdefsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Notes-V1.3 Revisions doc/*.ps
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_appdefsdir}/*
