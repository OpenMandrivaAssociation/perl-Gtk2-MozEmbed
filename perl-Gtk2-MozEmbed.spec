%define upstream_name    Gtk2-MozEmbed
%define upstream_version 0.08

%if %{?xulrunner_libname:0}%{?!xulrunner_libname:1}
%define xulrunner_libname libxulrunner
%endif

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:    Perl module for the Gecko engine
License:    GPL+ or Artistic
Group:      Development/GNOME and GTK+
Url:        http://gtk2-perl.sf.net/
Source0:    http://prdownloads.sourceforge.net/gtk2-perl/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires: glib2-devel
BuildRequires: gtk+2-devel
BuildRequires: perl-ExtUtils-Depends 
BuildRequires: perl-ExtUtils-PkgConfig
BuildRequires: perl-Gtk2 >= 1.081
# ensure we link/requires the right browser:
BuildConflicts: mozilla-devel
%if %mdkversion < 200900
BuildRequires: mozilla-firefox-devel
%elif %mdvver < 201000
BuildRequires: xulrunner-devel-unstable
%else 
BuildRequires: xulrunner-devel
%endif
%if %mdkversion < 200900
%define firefox_version %(rpm -q mozilla-firefox --queryformat %{VERSION})
Requires: %mklibname mozilla-firefox %{firefox_version}
%else
Requires: %xulrunner_libname
%endif
BuildRequires: perl-devel 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

Requires: perl-Gtk2 

%description
This package adds perl support for the Gecko engine.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
find -type d -name CVS | rm -rf 

%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
export GTK2_PERL_CFLAGS="$RPM_OPT_FLAGS"
perl Makefile.PL INSTALLDIRS=vendor
make OPTIMIZE="$RPM_OPT_FLAGS"
#%make test || :

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc examples/*
%{_mandir}/*/*
%{perl_vendorarch}/Gtk2/*
%{perl_vendorarch}/auto/*
