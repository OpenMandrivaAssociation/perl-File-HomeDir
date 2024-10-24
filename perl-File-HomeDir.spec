%define	modname	File-HomeDir

Summary:	Get home directory for self or other users
Name:		perl-%{modname}
Version:	1.006
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/File::HomeDir
Source0:	http://search.cpan.org/CPAN/authors/id/R/RE/REHSACK/File-HomeDir-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(File::Which)
BuildRequires:	xdg-user-dirs

%description
A Perl module to get home directory portably for self or other users.

%prep
%autosetup -p1 -n %{modname}-%{version}
find lib -name *.pm | xargs chmod 644 
chmod 644 Changes

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
# tests require that user dirs exist, which is not the case within bs
#make test

%install
%make_install

%files
%doc Changes
%{perl_vendorlib}/File
%{_mandir}/man3/*
