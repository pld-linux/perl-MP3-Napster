#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	MP3
%define		pnam	Napster
Summary:	MP3::Napster Perl module - interface to the Napster MP3 search and distribution servers
Summary(pl):	Modu³ Perla MP3::Napster - interfejs do serwerów wyszukiwania i dystrubucji plików MP3 Napstera
Name:		perl-MP3-Napster
Version:	2.04
Release:	8
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b3e253997909882b09013f6557aadc48
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-MP3-Info
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is MP3::Napster, a pure-Perl interface to the Napster MP3 file
search and distribution servers (www.napster.com). With this module,
you can connect to Napster servers, participate in online chat
channels, search the Napster virtual library of MP3 sound files, and
exchanged selected MP3s with other users.

%description -l pl
To jest MP3::Napster, interfejs do serwerów wyszukiwania i dystrubucji
plików MP3 - Napstera (www.napster.com), napisany w czystym Perlu. Z
tym modu³em mo¿esz pod³±czyæ siê do serwerów Napstera, zostaæ
uczestnikiem kana³ów pogawêdkowych, przeszukiwaæ wirtualn± bibliotekê
plików MP3 Napstera, i wymieniaæ wybrane pliki z innymi u¿ytkownikami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/MP3/Napster.pm
%{perl_vendorlib}/MP3/Napster
%{perl_vendorlib}/MP3/TkNapster
%{_mandir}/man3/*
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
