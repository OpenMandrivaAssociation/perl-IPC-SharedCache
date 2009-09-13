%define upstream_name       IPC-SharedCache
%define upstream_version    1.3

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Summary:    Manage a cache in SysV IPC shared memory
License:	GPL or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:     http://www.cpan.org/modules/by-module/IPC/%{upstream_name}-%{upstream_version}.tar.gz
Patch:      0001-Wrap-IPC-ShareLite-new-calls-inside-eval-block.patch 
BuildRequires:	perl-IPC-ShareLite
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module provides a shared memory cache accessed as a tied hash.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 
%patch -p 1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README LICENSE ANNOUNCE
%{perl_vendorlib}/IPC
%{_mandir}/*/*


