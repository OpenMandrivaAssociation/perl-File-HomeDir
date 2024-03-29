%define	modname	File-HomeDir
%define modver 1.006

Summary:	Get home directory for self or other users
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/File::HomeDir
Source0:	http://search.cpan.org/CPAN/authors/id/R/RE/REHSACK/File-HomeDir-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(File::Which)
BuildRequires:	xdg-user-dirs

%description
A Perl module to get home directory portably for self or other users.

%prep
%setup -qn %{modname}-%{modver}
find lib -name *.pm | xargs chmod 644 
chmod 644 Changes

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# tests require that user dirs exist, which is not the case within bs
#make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/File
%{_mandir}/man3/*
