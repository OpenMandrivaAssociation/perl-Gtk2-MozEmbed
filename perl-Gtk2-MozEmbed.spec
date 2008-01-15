%define module Gtk2-MozEmbed
%define fmodule MozEmbed

Summary: Perl module for the Gecko engine
Name:    perl-%module
Version: 0.06
Release: %mkrel 14
License: GPL or Artistic
Group:   Development/GNOME and GTK+
Source:  http://prdownloads.sourceforge.net/gtk2-perl/%module-%version.tar.bz2
URL: http://gtk2-perl.sf.net/
BuildRequires: perl-devel 
BuildRequires: perl-ExtUtils-Depends 
BuildRequires: perl-Gtk2 >= 1.081
BuildRequires: perl-ExtUtils-PkgConfig
# ensure we link/requires the right browser:
BuildConflicts: mozilla-devel
BuildRequires: mozilla-firefox-devel
BuildRequires: glib2-devel
BuildRequires: gtk+2-devel
%define firefox_version %(rpm -q mozilla-firefox --queryformat %{VERSION})
Requires: %mklibname mozilla-firefox %{firefox_version}



Requires: perl-Gtk2 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This package adds perl support for the Gecko engine.

%prep
%setup -q -n %module-%version
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



