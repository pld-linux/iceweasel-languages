# TODO:
#   - do something with *.rdf file, there if file conflict with other lang packages
Summary:	Language packs for Iceweasel
Name:		iceweasel-languages
Version:	3.5.5
Release:	0.1
License:	MPL 1.1 or GPL v2+ or LGPL v2.1+
Group:		I18n
Source0:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ca.xpi
# Source0-md5:	8fd39539b161200f80efed98ed227e9e
Source1:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/cs.xpi
# Source1-md5:	fba8336f735fb47b99b24a59da70f5b4
Source2:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/da.xpi
# Source2-md5:	b6d00eb16403b828d67168dd2c04ba3a
Source3:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/de.xpi
# Source3-md5:	f3329017e32dfa1eb1f0d3429c722baa
Source4:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/el.xpi
# Source4-md5:	f4d7c2d3dabe337c53bdca1c112b33fc
Source5:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-ES.xpi
# Source5-md5:	69690daf3c75b8acfe64e837bc210f72
Source6:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fi.xpi
# Source6-md5:	684e795e3ea1ff31e9b1d8d2e6ae153f
Source7:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fr.xpi
# Source7-md5:	9ebf0b96472e89c21f7806f41d8cc11e
Source8:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hu.xpi
# Source8-md5:	d06585e665a49a704d554e107e2b7fb9
Source9:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/it.xpi
# Source9-md5:	d0462d590ef8dd900204fd6d36328e91
Source10:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ja.xpi
# Source10-md5:	6cea045fd5880aacd52a14923c1ed545
Source11:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ka.xpi
# Source11-md5:	8e9d1bfd088217fd3c3ae9913f56619a
Source12:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ku.xpi
# Source12-md5:	53aad6d08a92a539b0eb3aac4080bfc2
Source13:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/lt.xpi
# Source13-md5:	d01db7e23b28e8b28121b87880bd1e76
Source14:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pl.xpi
# Source14-md5:	a15635ccfc3fd7ec25a31aeba2842d4b
Source15:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ro.xpi
# Source15-md5:	1910d674d15377d5a1bf6d643010f0d0
Source16:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ru.xpi
# Source16-md5:	a9422a665365fb424ce6f93149382198
Source17:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sk.xpi
# Source17-md5:	f4a39b27819d04d68ce781b07913b152
Source18:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sl.xpi
# Source18-md5:	e3e23e1b2b490299c9c60d96c9300df1
Source19:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sv-SE.xpi
# Source19-md5:	ae7fba4eb4aff51faa2e0ad44de62cb6
URL:		http://www.mozilla.org/
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
BuildRequires:	zip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		iceweaseldir	%{_datadir}/iceweasel
%define		chromedir		%{iceweaseldir}/chrome

%description
Language packs for Iceweasel.

%package -n iceweasel-lang-ca
Summary:	Catalan resources for Iceweasel
Summary(ca.UTF-8):	Recursos catalans per Iceweasel
Summary(es.UTF-8):	Recursos catalanes para Iceweasel
Summary(pl.UTF-8):	Katalońskie pliki językowe dla Iceweasela
Group:		I18n
URL:		http://www.softcatala.org/projectes/mozilla/
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-ca

%description -n iceweasel-lang-ca
Catalan resources for Iceweasel.

%description -n iceweasel-lang-ca -l ca.UTF-8
Recursos catalans per Iceweasel.

%description -n iceweasel-lang-ca -l es.UTF-8
Recursos catalanes para Iceweasel.

%description -n iceweasel-lang-ca -l pl.UTF-8
Katalońskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-cs
Summary:	Czech resources for Iceweasel
Summary(pl.UTF-8):	Czeskie pliki językowe dla Iceweasela
Group:		I18n
URL:		http://www.mozilla.org/
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-cs

%description -n iceweasel-lang-cs
Czech resources for Iceweasel.

%description -n iceweasel-lang-cs -l pl.UTF-8
Czeskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-da
Summary:	Danish resources for Iceweasel
Summary(pl.UTF-8):	Duńskie pliki językowe dla Iceweasela
Group:		I18n
URL:		http://www.mozilla.org/
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-da

%description -n iceweasel-lang-da
Danish resources for Iceweasel.

%description -n iceweasel-lang-da -l pl.UTF-8
Duńskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-de
Summary:	German resources for Iceweasel
Summary(pl.UTF-8):	Niemieckie pliki językowe dla Iceweasela
Group:		I18n
URL:		http://www.mozilla.org/
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-de

%description -n iceweasel-lang-de
German resources for Iceweasel.

%description -n iceweasel-lang-de -l pl.UTF-8
Niemieckie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-el
Summary:	Greek resources for Iceweasel
Summary(pl.UTF-8):	Greckie pliki językowe dla Iceweasela
Group:		I18n
URL:		http://www.mozilla.org/
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-el

%description -n iceweasel-lang-el
Greek resources for Iceweasel.

%description -n iceweasel-lang-el -l pl.UTF-8
Greckie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-es
Summary:	Spanish resources for Iceweasel
Summary(ca.UTF-8):	Recursos espanyols per Iceweasel
Summary(es.UTF-8):	Recursos españoles para Iceweasel
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Iceweasela
Group:		I18n
URL:		http://www.mozilla.org/
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-es

%description -n iceweasel-lang-es
Spanish resources for Iceweasel.

%description -n iceweasel-lang-es -l ca.UTF-8
Recursos espanyols per Iceweasel.

%description -n iceweasel-lang-es -l es.UTF-8
Recursos españoles para Iceweasel.

%description -n iceweasel-lang-es -l pl.UTF-8
Hiszpańskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-fi
Summary:	Finnish resources for Iceweasel
Summary(pl.UTF-8):	Fińskie pliki językowe dla Iceweasela
Group:		I18n
URL:		http://www.mozilla.org/
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-fi

%description -n iceweasel-lang-fi
Finnish resources for Iceweasel.

%description -n iceweasel-lang-fi -l pl.UTF-8
Fińskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-fr
Summary:	French resources for Iceweasel
Summary(pl.UTF-8):	Francuskie pliki językowe dla Iceweasela
Group:		I18n
URL:		http://www.mozilla.org/
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-fr

%description -n iceweasel-lang-fr
French resources for Iceweasel.

%description -n iceweasel-lang-fr -l pl.UTF-8
Francuskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-hu
Summary:	Hungarian resources for Iceweasel
Summary(hu.UTF-8):	Magyar nyelv Iceweasel-hez
Summary(pl.UTF-8):	Węgierskie pliki językowe dla Iceweasela
Group:		I18n
URL:		http://www.mozilla.org/
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-hu

%description -n iceweasel-lang-hu
Hungarian resources for Iceweasel.

%description -n iceweasel-lang-hu -l hu.UTF-8
Magyar nyelv Iceweasel-hez.

%description -n iceweasel-lang-hu -l pl.UTF-8
Węgierskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-it
Summary:	Italian resources for Iceweasel
Summary(pl.UTF-8):	Włoskie pliki językowe dla Iceweasela
Group:		I18n
URL:		http://www.mozilla.org/
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-it

%description -n iceweasel-lang-it
Italian resources for Iceweasel.

%description -n iceweasel-lang-it -l pl.UTF-8
Włoskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-ja
Summary:	Japanese resources for Iceweasel
Summary(pl.UTF-8):	Japońskie pliki językowe dla Iceweasela
Group:		I18n
URL:		http://www.mozilla.org/
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-ja

%description -n iceweasel-lang-ja
Japanese resources for Iceweasel.

%description -n iceweasel-lang-ja -l pl.UTF-8
Japońskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-ka
Summary:	Georgian resources for Iceweasel
Summary(pl.UTF-8):	Gruzińskie pliki językowe dla Iceweasela
Group:		I18n
URL:		http://www.mozilla.org/
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-ka

%description -n iceweasel-lang-ka
Georgian resources for Iceweasel.

%description -n iceweasel-lang-ka -l pl.UTF-8
Gruzińskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-ku
Summary:	Kurdish resources for Iceweasel
Summary(pl.UTF-8):	Kurdyjskie pliki językowe dla Iceweasela
Group:		I18n
URL:		http://www.mozilla.org/
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-ku

%description -n iceweasel-lang-ku
Kurdish resources for Iceweasel.

%description -n iceweasel-lang-ku -l pl.UTF-8
Kurdyjskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-lt
Summary:	Lithuanian resources for Iceweasel
Summary(pl.UTF-8):	Litewskie pliki językowe dla Iceweasela
Group:		I18n
URL:		http://www.mozilla.org/
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-lt

%description -n iceweasel-lang-lt
Lithuanian resources for Iceweasel.

%description -n iceweasel-lang-lt -l pl.UTF-8
Litewskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-pl
Summary:	Polish resources for Iceweasel
Summary(pl.UTF-8):	Polskie pliki językowe dla Iceweasela
Group:		I18n
URL:		http://www.firefox.pl/
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-pl

%description -n iceweasel-lang-pl
Polish resources for Iceweasel.

%description -n iceweasel-lang-pl -l pl.UTF-8
Polskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-ro
Summary:	Romanian resources for Iceweasel
Summary(pl.UTF-8):	Rumuńskie pliki językowe dla Iceweasela
Group:		I18n
URL:		http://www.mozilla.org/
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-ro

%description -n iceweasel-lang-ro
Romanian resources for Iceweasel.

%description -n iceweasel-lang-ro -l pl.UTF-8
Rumuńskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-ru
Summary:	Russian resources for Iceweasel
Summary(pl.UTF-8):	Rosyjskie pliki językowe dla Iceweasela
Group:		I18n
URL:		http://www.mozilla.org/
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-ru

%description -n iceweasel-lang-ru
Russian resources for Iceweasel.

%description -n iceweasel-lang-ru -l pl.UTF-8
Rosyjskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-sk
Summary:	Slovak resources for Iceweasel
Summary(pl.UTF-8):	Słowackie pliki językowe dla Iceweasela
Group:		I18n
URL:		http://www.mozilla.org/
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-sk

%description -n iceweasel-lang-sk
Slovak resources for Iceweasel.

%description -n iceweasel-lang-sk -l pl.UTF-8
Słowackie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-sl
Summary:	Slovene resources for Iceweasel
Summary(pl.UTF-8):	Słoweńskie pliki językowe dla Iceweasela
Group:		I18n
URL:		http://www.mozilla.org/
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-sl

%description -n iceweasel-lang-sl
Slovene resources for Iceweasel.

%description -n iceweasel-lang-sl -l pl.UTF-8
Słoweńskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-sv
Summary:	Swedish resources for Iceweasel
Summary(pl.UTF-8):	Szwedzkie pliki językowe dla Iceweasela
Group:		I18n
URL:		http://www.mozilla.org/
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-sv

%description -n iceweasel-lang-sv
Swedish resources for Iceweasel.

%description -n iceweasel-lang-sv -l pl.UTF-8
Szwedzkie pliki językowe dla Iceweasela.

%prep
unpack() {
    local args="$1" file="$2"
	local lang=$(basename $file .xpi)
	%{__unzip} $args -d $lang $file

	locale=$(awk -vl=$lang '$1 == l{print $2}' %{_builddir}/locales.txt)
	cd $lang
	install -d defaults/profile
	sed -i -e "s@chrome/$lang@$locale@" chrome.manifest
	[ $lang = $locale ] || mv chrome/$lang.jar chrome/$locale.jar
	mv chrome.manifest chrome/$locale.manifest
	mv install.rdf defaults/profile

	# rebrand locale for Iceweasel
	cd chrome
	unzip -q $locale.jar locale/branding/brand.{dtd,properties} locale/browser/appstrings.properties
	sed -i -e 's/Mozilla Firefox/Iceweasel/g; s/Firefox/Iceweasel/g;' locale/branding/brand.{dtd,properties}
	sed -i -e 's/Firefox/Iceweasel/g;' locale/browser/appstrings.properties
	zip -q0 $locale.jar locale/branding/brand.{dtd,properties} locale/browser/appstrings.properties
	rm -rf locale
	cd ../..
}
%define __unzip unpack
# LANGUAGE LOCALE
cat <<'EOF' > locales.txt
ca ca-ES
cs cs
da da
de de
el el
es-ES es-ES
fi fi
fr fr
hu hu
it it
ja ja
ka ka
ku ku
lt lt
pl pl-PL
ro ro
ru ru
sk sk
sl sl
sv-SE sv-SE
EOF
%setup -qcT %(seq -f '-a %g' 0 19 | xargs)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{chromedir}
for a in */chrome; do
	cp -a $a/* $RPM_BUILD_ROOT%{chromedir}
done

%clean
rm -rf $RPM_BUILD_ROOT

%files -n iceweasel-lang-ca
%defattr(644,root,root,755)
%{chromedir}/ca-ES.jar
%{chromedir}/ca-ES.manifest

%files -n iceweasel-lang-cs
%defattr(644,root,root,755)
%{chromedir}/cs.jar
%{chromedir}/cs.manifest

%files -n iceweasel-lang-da
%defattr(644,root,root,755)
%{chromedir}/da.jar
%{chromedir}/da.manifest

%files -n iceweasel-lang-de
%defattr(644,root,root,755)
%{chromedir}/de.jar
%{chromedir}/de.manifest

%files -n iceweasel-lang-el
%defattr(644,root,root,755)
%{chromedir}/el.jar
%{chromedir}/el.manifest

%files -n iceweasel-lang-es
%defattr(644,root,root,755)
%{chromedir}/es-ES.jar
%{chromedir}/es-ES.manifest

%files -n iceweasel-lang-fi
%defattr(644,root,root,755)
%{chromedir}/fi.jar
%{chromedir}/fi.manifest

%files -n iceweasel-lang-fr
%defattr(644,root,root,755)
%{chromedir}/fr.jar
%{chromedir}/fr.manifest

%files -n iceweasel-lang-hu
%defattr(644,root,root,755)
%{chromedir}/hu.jar
%{chromedir}/hu.manifest

%files -n iceweasel-lang-it
%defattr(644,root,root,755)
%{chromedir}/it.jar
%{chromedir}/it.manifest

%files -n iceweasel-lang-ja
%defattr(644,root,root,755)
%{chromedir}/ja.jar
%{chromedir}/ja.manifest

%files -n iceweasel-lang-ka
%defattr(644,root,root,755)
%{chromedir}/ka.jar
%{chromedir}/ka.manifest

%files -n iceweasel-lang-ku
%defattr(644,root,root,755)
%{chromedir}/ku.jar
%{chromedir}/ku.manifest

%files -n iceweasel-lang-lt
%defattr(644,root,root,755)
%{chromedir}/lt.jar
%{chromedir}/lt.manifest

%files -n iceweasel-lang-pl
%defattr(644,root,root,755)
%{chromedir}/pl-PL.jar
%{chromedir}/pl-PL.manifest

%files -n iceweasel-lang-ro
%defattr(644,root,root,755)
%{chromedir}/ro.jar
%{chromedir}/ro.manifest

%files -n iceweasel-lang-ru
%defattr(644,root,root,755)
%{chromedir}/ru.jar
%{chromedir}/ru.manifest

%files -n iceweasel-lang-sk
%defattr(644,root,root,755)
%{chromedir}/sk.jar
%{chromedir}/sk.manifest

%files -n iceweasel-lang-sl
%defattr(644,root,root,755)
%{chromedir}/sl.jar
%{chromedir}/sl.manifest

%files -n iceweasel-lang-sv
%defattr(644,root,root,755)
%{chromedir}/sv-SE.jar
%{chromedir}/sv-SE.manifest
