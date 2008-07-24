%define real_name IPC-SharedCache

Summary:	IPC-SharedCache module for perl 
Name:		perl-%{real_name}
Version:	1.3
Release:	%mkrel 4
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel, perl-IPC-ShareLite
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module provides a shared memory cache accessed as a tied hash.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README LICENSE ANNOUNCE
%{perl_vendorlib}/IPC/SharedCache.pm
%{_mandir}/*/*


