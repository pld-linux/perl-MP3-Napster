%define	pdir	MP3
%define	pnam	Napster
%include	/usr/lib/rpm/macros.perl
Summary:	MP3-Napster perl module
Summary(pl):	Modu³ perla MP3-Napster
Name:		perl-MP3-Napster
Version:	2.04
Release:	5

License:	GPL
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(da):	Udvikling/Sprog/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(is):	Þróunartól/Forritunarmál/Perl
Group(it):	Sviluppo/Linguaggi/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(no):	Utvikling/Programmeringsspråk/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Group(sl):	Razvoj/Jeziki/Perl
Group(sv):	Utveckling/Språk/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-MP3-Info
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is MP3-Napster, a pure-Perl interface to the Napster MP3 file
search and distribution servers (www.napster.com). With this module,
you can connect to Napster servers, participate in online chat
channels, search the Napster virtual library of MP3 sound files, and
exchanged selected MP3s with other users.

%description -l pl
To jest MP3-Napster, interfejs do serwerów wyszukiwania i dystrubucji
plików MP3 - Napstera (www.napster.com), napisany w czystym Perlu. Z
tym modu³em mo¿esz pod³±czyæ siê do serwerów Napstera, zostaæ
uczestnikiem kana³ów pogawêdkowych, przeszukiwaæ wirtualn± bibliotekê
plików MP3 Napstera, i wymieniaæ wybrane pliki z innymi u¿ytkownikami.

%prep
%setup -q -n MP3-Napster-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz eg
%{perl_sitelib}/MP3/Napster.pm
%{perl_sitelib}/MP3/Napster
%{perl_sitelib}/MP3/TkNapster
%{_mandir}/man3/*
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/*
