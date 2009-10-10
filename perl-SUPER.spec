#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	SUPER
Summary:	SUPER - control superclass method dispatch
Summary(pl.UTF-8):	SUPER - przekazywanie sterowania do metod klasy nadrzędnej
Name:		perl-SUPER
Version:	1.17
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/SUPER/%{pdir}-%{version}.tar.gz
# Source0-md5:	aa54aa7e9148c368091e34559587f3b2
URL:		http://search.cpan.org/dist/SUPER/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-Sub-Identify
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
When subclassing a class, you occasionally want to dispatch control to
the superclass -- at least conditionally and temporarily. The Perl
syntax for calling your superclass is ugly and unwieldy:

$self->SUPER::method(@_);

especially when compared to its Ruby equivalent:

super;

It's even worse in that the normal Perl redispatch mechanism only
dispatches to the parent of the class containing the method at compile
time. That doesn't work very well for mixins and roles.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}//*.pm
%{_mandir}/man3/*
