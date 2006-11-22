Summary:	A reader for the Microsoft Tape Format used by NT Backup
Summary(pl):	Czynik Ta¶m w Formacie Microsoft(R) u¿ywanym przez NT Backup
Name:		mtf
Version:	0.2.1
Release:	1
License:	GPL
Group:		Applications/Dictionaries
Vendor:		D. Alan Stewart, Layton Graphics, Inc. <astewart@layton-graphics.com>
Source0:	http://layton-graphics.com/mtf/%{name}-%{version}.tgz
# Source0-md5:	46f878e1c4cef44ecc7190e851217c2e
URL:		http://layton-graphics.com/mtf/
#Source1:	http://www.seagatesoftware.com/products/sm/library/whitepapers/downloads/mtfv1r18.zip (?)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple reader for tapes recorded w/ MS Backup, version shiped w/ NT
4.0. This program is based on Microsoft Tape Format Specification
Version 1.00a, Document Revision 1.8. This document is available at:
http://www.seagatesoftware.com/products/sm/library/whitepapers/downloads/mtfv1r18.zip


%description -l pl
Prosty czytnik do ta¶m nagranych przez MS Backup, w wersji
dostarczanej z NT 4.0. Ten program bazuje na Microsoft Tape Format
Specification wersja 1.00a, rewizja dokumentu 1.8. Ten dokument jest
dostêpny pod adresem:
http://www.seagatesoftware.com/products/sm/library/whitepapers/downloads/mtfv1r18.zip

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install mtf $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/mtf
