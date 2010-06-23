# TODO:
#   - do something with *.rdf file, there if file conflict with other lang packages
#   - 54 more languages (3.5.6):
#     af ar as be bg bn-BD bn-IN cy en-GB eo es-AR es-CL es-MX et eu fa fy-NL
#     ga-IE gl gu-IN he hi-IN hr id is kk kn ko lv mk ml mn mr nb-NO nl nn-NO
#     oc or pa-IN pt-BR pt-PT rm si sq sr ta-LK ta te th tr uk vi zh-CN zh-TW
# UPDATING:
%if 0
rm -vf *.xpi
./builder -g
V=3.6.3
U=http://releases.mozilla.org/pub/mozilla.org/firefox/releases/$V/linux-i686/
curl -s $U | sed -ne 's,.*href="\([^"]\+\)/".*,'"$U"'xpi/\1.xpi,p'
%endif

Summary:	Language packs for Iceweasel
Name:		iceweasel-languages
Version:	3.6.4
Release:	1
License:	MPL 1.1 or GPL v2+ or LGPL v2.1+
Group:		I18n
Source0:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ca.xpi
# Source0-md5:	138b5c9d5f5f8e4f5a52d964bcda2f0e
Source1:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/cs.xpi
# Source1-md5:	cc6729b3e5fd1aff8f6b1e6ca8e72c62
Source2:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/da.xpi
# Source2-md5:	8d32fb5e89420a56067e72e9843aa9f5
Source3:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/de.xpi
# Source3-md5:	1a744bae95b72ce60f36514cb1e4081f
Source4:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/el.xpi
# Source4-md5:	022262ca04e272a57fff11bc3d81969f
Source5:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-ES.xpi
# Source5-md5:	f49fd44a591d21588ff9802c350a4a50
Source6:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fi.xpi
# Source6-md5:	ad2bcaebb9197ab2ce640e5cbd0f4521
Source7:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fr.xpi
# Source7-md5:	45b48f176b363be4bdbf502c56fa7cc9
Source8:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hu.xpi
# Source8-md5:	86e2e529c9cb29b310e0ef1983ab28eb
Source9:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/it.xpi
# Source9-md5:	765e60780baeb1b33100f02c30d97e08
Source10:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ja.xpi
# Source10-md5:	c06585cdce4300021673c81931c7ee91
Source11:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ka.xpi
# Source11-md5:	6d2f981b9eb863bad6c7c2f9b3bd1ab8
Source12:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ku.xpi
# Source12-md5:	581d668bb15f163b298a00d8f28490ba
Source13:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/lt.xpi
# Source13-md5:	5fc0e62d7f12487e992809039b1f6d4f
Source14:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pl.xpi
# Source14-md5:	b21629ee6ad440db4b98bb3efed15d8e
Source15:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ro.xpi
# Source15-md5:	719319e9551dcb7b6bf2c7dfb40702f5
Source16:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ru.xpi
# Source16-md5:	4b61e956bb980bbd0862b2e27ae4d5ef
Source17:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sk.xpi
# Source17-md5:	8f46443746d1c59b6c379aeae9824037
Source18:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sl.xpi
# Source18-md5:	f77a0a6d985048dd6817d26d82bebf3c
Source19:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sv-SE.xpi
# Source19-md5:	ea1f73f761b26281121d83e02bdf9893
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
