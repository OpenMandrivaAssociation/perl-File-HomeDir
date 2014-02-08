%define	upstream_name	 File-HomeDir
%define upstream_version 0.98

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Get home directory for self or other users
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(File::Which)
BuildRequires:	xdg-user-dirs

BuildArch:	noarch

%description
A Perl module to get home directory portably for self or other users.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
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
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.980.0-3mdv2012.0
+ Revision: 765244
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.980.0-2
+ Revision: 763758
- rebuilt for perl-5.14.x

* Mon Jul 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.980.0-1
+ Revision: 690259
- update to new version 0.98

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.970.0-2
+ Revision: 667141
- mass rebuild

* Thu Feb 24 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.970.0-1
+ Revision: 639636
- update to new version 0.97

* Tue Feb 01 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.950.0-1
+ Revision: 634682
- update to new version 0.95

* Sat Oct 23 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.930.0-1mdv2011.0
+ Revision: 587626
- new version

* Tue Jul 27 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.910.0-1mdv2011.0
+ Revision: 561549
- skip tests, they require user dirs to exist
- create user desktop dirs if needed
- adding missing buildrequires:
- adding missing buildrequires:
- update to 0.91

* Sun Jan 03 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.890.0-1mdv2010.1
+ Revision: 485803
- update to 0.89

* Tue Nov 24 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.880.0-1mdv2010.1
+ Revision: 469436
- update to 0.88

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.860.0-1mdv2010.0
+ Revision: 403170
- rebuild using %%perl_convert_version

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.86-1mdv2010.0
+ Revision: 370072
- update to new version 0.86

* Thu Mar 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.84-1mdv2009.1
+ Revision: 354156
- update to new version 0.84

* Fri Oct 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.82-1mdv2009.1
+ Revision: 294629
- update to new version 0.82

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.81-1mdv2009.1
+ Revision: 292161
- update to new version 0.81

* Mon Jun 30 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.80-1mdv2009.0
+ Revision: 230269
- update to new version 0.80

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.69-2mdv2009.0
+ Revision: 223751
- rebuild

* Mon Feb 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.69-1mdv2008.1
+ Revision: 162036
- update to new version 0.69

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Dec 07 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.67-1mdv2008.1
+ Revision: 116170
- update to new version 0.67

* Thu Aug 30 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.66-1mdv2008.0
+ Revision: 75221
- update to new version 0.66

* Mon May 21 2007 Michael Scherer <misc@mandriva.org> 0.65-1mdv2008.0
+ Revision: 29097
- Update to new version 0.65

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 0.64-1mdv2008.0
+ Revision: 20093
- 0.64


* Wed May 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.58-1mdv2007.0
- new release
- fix sources URL

* Thu May 04 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.57-1mdk
- New release 0.57
- Change Source URL

* Sun Mar 12 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.56-1mdk
- New release 0.56

* Mon Mar 06 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.54-1mdk
- New release 0.54

* Fri Jan 20 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.52-1mdk
- new version
- spec cleanup
- %%mkrel
- rpmbuildupdate aware

* Wed Nov 09 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.07-1mdk
- 0.07
- Remove patch1 (disable windows-only code)
- Fix permissions and line encodings

* Mon May 02 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.06-1mdk
- 0.06

* Thu Jan 29 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.05-2mdk
- 0.05

* Wed Jan 28 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.05-1mdk
- from Robin Rosenberg <robin.rosenberg@dewire.com> :
	- initial contrib import. Needed for building Captive-NTFS

