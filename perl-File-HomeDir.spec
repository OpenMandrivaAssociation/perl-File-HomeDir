%define	upstream_name	 File-HomeDir
%define upstream_version 0.98

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:	Get home directory for self or other users
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires: perl(File::Which)
BuildRequires: xdg-user-dirs

Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
A Perl module to get home directory portably for self or other users.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
find lib -name *.pm | xargs chmod 644 
chmod 644 Changes

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# tests require that user dirs exist, which is not the case within bs
#make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/File
%{_mandir}/*/*
