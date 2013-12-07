%define	modname	File-HomeDir
%define modver	0.98

Summary:	Get home directory for self or other users
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	8
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/modules/by-module/File/%{modname}-%{modver}.tar.gz
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
%doc README Changes
%{perl_vendorlib}/File
%{_mandir}/man3/*

