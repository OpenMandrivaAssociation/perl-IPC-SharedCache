%define upstream_name       IPC-SharedCache
%define upstream_version    1.3

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2
Summary:	Manage a cache in SysV IPC shared memory
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source:		http://www.cpan.org/modules/by-module/IPC/%{upstream_name}-%{upstream_version}.tar.gz
Patch:		0001-Wrap-IPC-ShareLite-new-calls-inside-eval-block.patch 

BuildRequires:	perl-devel
BuildRequires:	perl(IPC::ShareLite)
BuildArch:	noarch


%description
This module provides a shared memory cache accessed as a tied hash.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 
%patch -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README LICENSE ANNOUNCE
%{perl_vendorlib}/IPC
%{_mandir}/*/*

%changelog
* Sun Sep 13 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.300.0-1mdv2010.0
+ Revision: 438672
- use new perl_version macro
- fix API change in IPC::Sharelite (RT patch)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.3-5mdv2009.0
+ Revision: 257373
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.3-4mdv2009.0
+ Revision: 245404
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1.3-2mdv2008.1
+ Revision: 135856
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.3-2mdv2008.0
+ Revision: 86512
- rebuild


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3-1mdv2007.0
- rebuild

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3-1mdk
- initial Mandriva package

