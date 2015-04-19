# TODO:
#   - do something with *.rdf file, there if file conflict with other lang packages
# UPDATING:
%if 0
rm -vf *.xpi
../builder -g iceweasel-languages.spec
V=33.0
U=http://releases.mozilla.org/pub/mozilla.org/firefox/releases/$V/linux-i686/
curl -s $U | sed -ne 's,.*href="\([^"]\+\)/".*,'"$U"'xpi/\1.xpi,p'
%endif

Summary:	Language packs for Iceweasel
Summary(pl.UTF-8):	Pakiety językowe dla Iceweasela
Name:		iceweasel-languages
Version:	37.0.1
Release:	1
License:	MPL v2.0
Group:		I18n
Source0:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ach.xpi
# Source0-md5:	c5cae8ab2de01c7516946ba3b8085c08
Source1:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/af.xpi
# Source1-md5:	a00179c02cfa0d3b1fae4b925609c747
Source2:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/an.xpi
# Source2-md5:	b7f65e538f8f49243d8668ebefc6454a
Source3:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/az.xpi
# Source3-md5:	a6dce288e262518b44cbcf04a50cb37f
Source4:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ar.xpi
# Source4-md5:	91dd90bf326215b304db60cac54ce8c8
Source5:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/as.xpi
# Source5-md5:	7edc8ad3aea445660a07a6ea3518959d
Source6:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ast.xpi
# Source6-md5:	29baef3584666157051b435dac6b54b4
Source7:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/be.xpi
# Source7-md5:	a223d2d1938f3252ff5492ff46631fc3
Source8:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bg.xpi
# Source8-md5:	abe1be5efd000351a8bc18752ea4ef44
Source9:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bn-BD.xpi
# Source9-md5:	e6a2b73799f8bf5de8df1afbc3ef3ab3
Source10:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bn-IN.xpi
# Source10-md5:	1f897a59bde22a13d162427e1a32f6a6
Source11:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/br.xpi
# Source11-md5:	ce2483a3d8f5476a65276164c858cb09
Source12:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bs.xpi
# Source12-md5:	ab7eef1388732fe1b77649a15e8ad0e1
Source13:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ca.xpi
# Source13-md5:	393c9e43351a9250c896b8800f14a060
Source14:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/cs.xpi
# Source14-md5:	41332baabf91035d884c4f62cc4b18b4
Source15:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/cy.xpi
# Source15-md5:	734237e67a28dcfb313f60950a9310fe
Source16:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/da.xpi
# Source16-md5:	9272838d948d98b0210cc7d7a3d6dd61
Source17:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/de.xpi
# Source17-md5:	6e8f53bc476859445fdfcac2b965b93b
Source18:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/dsb.xpi
# Source18-md5:	2438fff33c25b9797c3a5eeadaf33360
Source19:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/el.xpi
# Source19-md5:	cd2e4f61e4634f6174e86bafce8dfa06
Source20:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/en-GB.xpi
# Source20-md5:	080b6936771dc5b09e31e94db76c611c
Source21:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/en-US.xpi
# Source21-md5:	ac264d0e376c362b2181f8b98cf12c58
Source22:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/en-ZA.xpi
# Source22-md5:	f5b591d6b28083cdedd801676714992c
Source23:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/eo.xpi
# Source23-md5:	21d4e4b717490e3b9640ca5e6285bedd
Source24:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-AR.xpi
# Source24-md5:	9c6f8724ad0c19aa73e9496de31a55a7
Source25:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-CL.xpi
# Source25-md5:	b33abcdb48d5b3e4b6407b1e0cf299a9
Source26:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-ES.xpi
# Source26-md5:	43409ac61be72ef1490aaeee7046a533
Source27:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-MX.xpi
# Source27-md5:	8c43e23bdc0ecf9f83594b03780a885e
Source28:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/et.xpi
# Source28-md5:	5bc81fedcc619725684cf60351df900d
Source29:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/eu.xpi
# Source29-md5:	57beb12646a8932bb896425cc2b70ce0
Source30:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fa.xpi
# Source30-md5:	636e53937b3fa14e351975cf5a4a8f4e
Source31:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ff.xpi
# Source31-md5:	c2baeb72b04827183bc8d3c713e1bc62
Source32:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fi.xpi
# Source32-md5:	586b2cfb963eff50181cedb3b08c849f
Source33:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fr.xpi
# Source33-md5:	87df0cec9f6cdd9200d7d356078f3153
Source34:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fy-NL.xpi
# Source34-md5:	c94b2a597057c48dc18e527f5ca25382
Source35:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ga-IE.xpi
# Source35-md5:	9811aaa6179299a459c8894c6ba620ad
Source36:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/gd.xpi
# Source36-md5:	ed964ecdc7c7ba534d3b83456a47cccb
Source37:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/gl.xpi
# Source37-md5:	30bc24fe36337c096e61f7cc618be49f
Source38:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/gu-IN.xpi
# Source38-md5:	6e6b6c2dc5bc3c98d505a9b658b4d31a
Source39:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/he.xpi
# Source39-md5:	42ef9ff182f2f298dc866462b5c0a08e
Source40:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hi-IN.xpi
# Source40-md5:	e916de25470344ad3f41d00b7641f806
Source41:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hr.xpi
# Source41-md5:	59cfd3e14232c43173d27b114750bbc7
Source42:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hsb.xpi
# Source42-md5:	76e890df6d8fe9c93694cf4493bf71d6
Source43:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hu.xpi
# Source43-md5:	f7ed1075623271076f373f30cef23917
Source44:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hy-AM.xpi
# Source44-md5:	5ece6a9cd77ba66afc01583595080200
Source45:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/id.xpi
# Source45-md5:	1956faf38a034f69fdaa611d5ecbde6e
Source46:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/is.xpi
# Source46-md5:	232efb0352dd577f6f8d8243ebd5a914
Source47:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/it.xpi
# Source47-md5:	8520d45833e77eb62c0ba76a6b9f34d2
Source48:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ja.xpi
# Source48-md5:	61c37d2e34fdc5020fb3f6d19151a721
Source49:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/kk.xpi
# Source49-md5:	8afd142c6eb2c2ab5a578aad5f94d34b
Source50:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/km.xpi
# Source50-md5:	1fa326c5e6874c84a0e30a3ef30bac2f
Source51:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/kn.xpi
# Source51-md5:	25b6083f53360f7a0893b33f2184534f
Source52:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ko.xpi
# Source52-md5:	1c5429a4d54d7928a789090a04c61fe6
Source53:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/lij.xpi
# Source53-md5:	cc61d6a7775c988222ad2c4d8781a2f2
Source54:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/lt.xpi
# Source54-md5:	b9936716db0c0183c5c077848a1aada7
Source55:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/lv.xpi
# Source55-md5:	e778a42bde19ca612a03c66a2a699f74
Source56:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/mai.xpi
# Source56-md5:	ec050e1a8960c6978abf98308aa51ef4
Source57:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/mk.xpi
# Source57-md5:	9d2eaa65c0487af5fec486f9c090a467
Source58:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ml.xpi
# Source58-md5:	f28de77d52f0932c015954b2a66975c6
Source59:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/mr.xpi
# Source59-md5:	8918f14b23d9a24967ea06639e28c69c
Source60:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ms.xpi
# Source60-md5:	ed49aa6223b79b44def8421b112d827d
Source61:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/nb-NO.xpi
# Source61-md5:	29638d580b1351c6e9fa29b801c2ec02
Source62:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/nl.xpi
# Source62-md5:	23dfdc1dc9ee0961f26df910bc3335cf
Source63:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/nn-NO.xpi
# Source63-md5:	adb5c6e9adbddd118ed5be57280b675e
Source64:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/or.xpi
# Source64-md5:	c93f8764c078ea933948124a2aa687b5
Source65:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pa-IN.xpi
# Source65-md5:	c8f7641f943580c97f08876d355f1a17
Source66:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pl.xpi
# Source66-md5:	e96a576cae21c33121f32af5c539fc98
Source67:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pt-BR.xpi
# Source67-md5:	758943e9161c9def4f70ad8d8f2665c5
Source68:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pt-PT.xpi
# Source68-md5:	12a5c0ef86d5baf31eb8b76ef3f15520
Source69:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/rm.xpi
# Source69-md5:	3134330e85a5d76c55b24f0af1fc8eb4
Source70:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ro.xpi
# Source70-md5:	bb0a66509c7eac053cce2210d5746bd1
Source71:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ru.xpi
# Source71-md5:	e7cbaac4a16a83e026704fdbe55f5911
Source72:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/si.xpi
# Source72-md5:	3475ef778c7cb7fa9357a22015420211
Source73:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sk.xpi
# Source73-md5:	f09ae46d7b93bbb0b6547597c68a97bb
Source74:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sl.xpi
# Source74-md5:	9fe69b9f64e4a9eecb09b48e6d7b638f
Source75:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/son.xpi
# Source75-md5:	37a4f19ca970cd9936ce6372e6fbe68f
Source76:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sq.xpi
# Source76-md5:	3fbcb63cb5eaba808caba0586d0e3354
Source77:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sr.xpi
# Source77-md5:	35652fb2bd197ce21c7fcaba99ef82b5
Source78:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sv-SE.xpi
# Source78-md5:	162a9f79deeaaa9802c060b50d39ec20
Source79:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ta.xpi
# Source79-md5:	61e9ebfe17f683bbfb025cfac65ca006
Source80:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/te.xpi
# Source80-md5:	287420ac62c7f382a8d1f60dfa38b0cd
Source81:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/th.xpi
# Source81-md5:	bd1d8e5e43e5addebe6f096deec8a420
Source82:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/tr.xpi
# Source82-md5:	54e9e486fd86b447023ccc539bf1edbc
Source83:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/uk.xpi
# Source83-md5:	b9bc2694f6ba425f16e0968eb51893e5
Source84:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/uz.xpi
# Source84-md5:	284bcf8df85c41dc1a951e55f1ea7304
Source85:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/vi.xpi
# Source85-md5:	802a98106e61e344aaab42b1b82b0b40
Source86:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/xh.xpi
# Source86-md5:	ac6360039630b32fd052cd098898dcad
Source87:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/zh-CN.xpi
# Source87-md5:	d05717a1a392d114395c76ef9ab754b7
Source88:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/zh-TW.xpi
# Source88-md5:	6389d3de1260b0341f4a462b81fd716f
URL:		http://www.mozilla.org/
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
BuildRequires:	zip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		iceweaseldir	%{_datadir}/iceweasel

%description
Language packs for Iceweasel.

%description -l pl.UTF-8
Pakiety językowe dla Iceweasela.

%package -n iceweasel-lang-ach
Summary:	Acoli resources for Iceweasel
Summary(pl.UTF-8):	Pliki językowe aczoli dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-ach

%description -n iceweasel-lang-ach
Acoli resources for Iceweasel.

%description -n iceweasel-lang-ach -l pl.UTF-8
Pliki językowe aczoli dla Iceweasela.

%package -n iceweasel-lang-af
Summary:	Afrikaans resources for Iceweasel
Summary(pl.UTF-8):	Afrykanerskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-af

%description -n iceweasel-lang-af
Afrikaans resources for Iceweasel.

%description -n iceweasel-lang-af -l pl.UTF-8
Afrykanerskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-an
Summary:	Aragonese resources for Iceweasel
Summary(pl.UTF-8):	Aragońskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-an

%description -n iceweasel-lang-an
Aragonese resources for Iceweasel.

%description -n iceweasel-lang-an -l pl.UTF-8
Aragońskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-ar
Summary:	Arabic resources for Iceweasel
Summary(pl.UTF-8):	Arabskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-ar

%description -n iceweasel-lang-ar
Arabic resources for Iceweasel.

%description -n iceweasel-lang-ar -l pl.UTF-8
Arabskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-as
Summary:	Assamese resources for Iceweasel
Summary(pl.UTF-8):	Asamskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-as

%description -n iceweasel-lang-as
Assamese resources for Iceweasel.

%description -n iceweasel-lang-as -l pl.UTF-8
Asamskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-ast
Summary:	Asturian resources for Iceweasel
Summary(pl.UTF-8):	Asturyjskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-ast

%description -n iceweasel-lang-ast
Asturian resources for Iceweasel.

%description -n iceweasel-lang-ast -l pl.UTF-8
Asturyjskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-az
Summary:	Azerbaijani resources for Iceweasel
Summary(pl.UTF-8):	Azerskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-az

%description -n iceweasel-lang-az
Azerbaijani resources for Iceweasel.

%description -n iceweasel-lang-az -l pl.UTF-8
Azerskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-be
Summary:	Belarusian resources for Iceweasel
Summary(pl.UTF-8):	Białoruskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-be

%description -n iceweasel-lang-be
Belarusian resources for Iceweasel.

%description -n iceweasel-lang-be -l pl.UTF-8
Białoruskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-bg
Summary:	Bulgarian resources for Iceweasel
Summary(pl.UTF-8):	Bułgarskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-bg

%description -n iceweasel-lang-bg
Bulgarian resources for Iceweasel.

%description -n iceweasel-lang-bg -l pl.UTF-8
Bułgarskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-bn
Summary:	Bengali (Bangladesh) resources for Iceweasel
Summary(pl.UTF-8):	Bengalskie pliki językowe dla Iceweasela (wersja dla Bangladeszu)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-bn

%description -n iceweasel-lang-bn
Bengali (Bangladesh) resources for Iceweasel.

%description -n iceweasel-lang-bn -l pl.UTF-8
Bengalskie pliki językowe dla Iceweasela (wersja dla Bangladeszu).

%package -n iceweasel-lang-bn_IN
Summary:	Bengali (India) resources for Iceweasel
Summary(pl.UTF-8):	Bengalskie pliki językowe dla Iceweasela (wersja dla Indii)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-bn_IN

%description -n iceweasel-lang-bn_IN
Bengali (India) resources for Iceweasel.

%description -n iceweasel-lang-bn_IN -l pl.UTF-8
Bengalskie pliki językowe dla Iceweasela (wersja dla Indii).

%package -n iceweasel-lang-br
Summary:	Breton resources for Iceweasel
Summary(pl.UTF-8):	Bretońskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-br

%description -n iceweasel-lang-br
Breton resources for Iceweasel.

%description -n iceweasel-lang-br -l pl.UTF-8
Bretońskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-bs
Summary:	Bosnian resources for Iceweasel
Summary(pl.UTF-8):	Bośniackie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-bs

%description -n iceweasel-lang-bs
Bosnian resources for Iceweasel.

%description -n iceweasel-lang-bs -l pl.UTF-8
Bośniackie pliki językowe dla Iceweasela.

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
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-cs

%description -n iceweasel-lang-cs
Czech resources for Iceweasel.

%description -n iceweasel-lang-cs -l pl.UTF-8
Czeskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-csb
Summary:	Kashubian resources for Iceweasel
Summary(pl.UTF-8):	Kaszubskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-csb

%description -n iceweasel-lang-csb
Kashubian resources for Iceweasel.

%description -n iceweasel-lang-csb -l pl.UTF-8
Kaszubskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-cy
Summary:	Welsh resources for Iceweasel
Summary(pl.UTF-8):	Walijskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-cy

%description -n iceweasel-lang-cy
Welsh resources for Iceweasel.

%description -n iceweasel-lang-cy -l pl.UTF-8
Walijskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-da
Summary:	Danish resources for Iceweasel
Summary(pl.UTF-8):	Duńskie pliki językowe dla Iceweasela
Group:		I18n
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
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-de

%description -n iceweasel-lang-de
German resources for Iceweasel.

%description -n iceweasel-lang-de -l pl.UTF-8
Niemieckie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-dsb
Summary:	Lower Sorbian resources for Iceweasel
Summary(pl.UTF-8):	Dolnołużyckie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-dsb

%description -n iceweasel-lang-dsb
Lower Sorbian resources for Iceweasel.

%description -n iceweasel-lang-dsb -l pl.UTF-8
Dolnołużyckie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-el
Summary:	Greek resources for Iceweasel
Summary(pl.UTF-8):	Greckie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-el

%description -n iceweasel-lang-el
Greek resources for Iceweasel.

%description -n iceweasel-lang-el -l pl.UTF-8
Greckie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-en_GB
Summary:	English (British) resources for Iceweasel
Summary(pl.UTF-8):	Angielskie (brytyjskie) pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-en_GB

%description -n iceweasel-lang-en_GB
English (British) resources for Iceweasel.

%description -n iceweasel-lang-en_GB -l pl.UTF-8
Angielskie (brytyjskie) pliki językowe dla Iceweasela.

%package -n iceweasel-lang-en_US
Summary:	English (American) resources for Iceweasel
Summary(pl.UTF-8):	Angielskie (amerykańskie) pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-en_US

%description -n iceweasel-lang-en_US
English (American) resources for Iceweasel.

%description -n iceweasel-lang-en_US -l pl.UTF-8
Angielskie (amerykańskie) pliki językowe dla Iceweasela.

%package -n iceweasel-lang-en_ZA
Summary:	English (South Africa) resources for Iceweasel
Summary(pl.UTF-8):	Angielskie pliki językowe dla Iceweasela (wersja dla RPA)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-en_ZA

%description -n iceweasel-lang-en_ZA
English (South Africa) resources for Iceweasel.

%description -n iceweasel-lang-en_ZA -l pl.UTF-8
Angielskie pliki językowe dla Iceweasela (wersja dla Republiki
Południowej Afryki).

%package -n iceweasel-lang-eo
Summary:	Esperanto resources for Iceweasel
Summary(pl.UTF-8):	Pliki językowe esperanto dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-eo

%description -n iceweasel-lang-eo
Esperanto resources for Iceweasel.

%description -n iceweasel-lang-eo -l pl.UTF-8
Pliki językowe esperanto dla Iceweasela.

%package -n iceweasel-lang-es_AR
Summary:	Spanish (Andorra) resources for Iceweasel
Summary(ca.UTF-8):	Recursos espanyols (Andorra) per Iceweasel
Summary(es.UTF-8):	Recursos españoles (Andorra) para Iceweasel
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Iceweasela (wersja dla Andory)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-es_AR

%description -n iceweasel-lang-es_AR
Spanish (Spain) resources for Iceweasel.

%description -n iceweasel-lang-es_AR -l ca.UTF-8
Recursos espanyols (Andorra) per Iceweasel.

%description -n iceweasel-lang-es_AR -l es.UTF-8
Recursos españoles (Andorra) para Iceweasel.

%description -n iceweasel-lang-es_AR -l pl.UTF-8
Hiszpańskie pliki językowe dla Iceweasela (wersja dla Andory).

%package -n iceweasel-lang-es_CL
Summary:	Spanish (Chile) resources for Iceweasel
Summary(ca.UTF-8):	Recursos espanyols (Xile) per Iceweasel
Summary(es.UTF-8):	Recursos españoles (Chile) para Iceweasel
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Iceweasela (wersja dla Chile)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-es_CL

%description -n iceweasel-lang-es_CL
Spanish (Chile) resources for Iceweasel.

%description -n iceweasel-lang-es_CL -l ca.UTF-8
Recursos espanyols (Xile) per Iceweasel.

%description -n iceweasel-lang-es_CL -l es.UTF-8
Recursos españoles (Chile) para Iceweasel.

%description -n iceweasel-lang-es_CL -l pl.UTF-8
Hiszpańskie pliki językowe dla Iceweasela (wersja dla Chile).

%package -n iceweasel-lang-es
Summary:	Spanish (Spain) resources for Iceweasel
Summary(ca.UTF-8):	Recursos espanyols (Espanya) per Iceweasel
Summary(es.UTF-8):	Recursos españoles (España) para Iceweasel
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Iceweasela (wersja dla Hiszpanii)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-es

%description -n iceweasel-lang-es
Spanish (Spain) resources for Iceweasel.

%description -n iceweasel-lang-es -l ca.UTF-8
Recursos espanyols (Espanya) per Iceweasel.

%description -n iceweasel-lang-es -l es.UTF-8
Recursos españoles (España) para Iceweasel.

%description -n iceweasel-lang-es -l pl.UTF-8
Hiszpańskie pliki językowe dla Iceweasela (wersja dla Hiszpanii).

%package -n iceweasel-lang-es_MX
Summary:	Spanish (Mexico) resources for Iceweasel
Summary(ca.UTF-8):	Recursos espanyols (Mèxic) per Iceweasel
Summary(es.UTF-8):	Recursos españoles (México) para Iceweasel
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Iceweasela (wersja dla Meksyku)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-es_MX

%description -n iceweasel-lang-es_MX
Spanish (Mexico) resources for Iceweasel.

%description -n iceweasel-lang-es_MX -l ca.UTF-8
Recursos espanyols (Mèxic) per Iceweasel.

%description -n iceweasel-lang-es_MX -l es.UTF-8
Recursos españoles (México) para Iceweasel.

%description -n iceweasel-lang-es_MX -l pl.UTF-8
Hiszpańskie pliki językowe dla Iceweasela (wersja dla Meksyku).

%package -n iceweasel-lang-et
Summary:	Estonian resources for Iceweasel
Summary(pl.UTF-8):	Estońskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-et

%description -n iceweasel-lang-et
Estonian resources for Iceweasel.

%description -n iceweasel-lang-et -l pl.UTF-8
Estońskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-eu
Summary:	Basque resources for Iceweasel
Summary(pl.UTF-8):	Baskijskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-eu

%description -n iceweasel-lang-eu
Basque resources for Iceweasel.

%description -n iceweasel-lang-eu -l pl.UTF-8
Baskijskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-fa
Summary:	Persian resources for Iceweasel
Summary(pl.UTF-8):	Perskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-fa

%description -n iceweasel-lang-fa
Persian resources for Iceweasel.

%description -n iceweasel-lang-fa -l pl.UTF-8
Perskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-ff
Summary:	Fulah resources for Iceweasel
Summary(pl.UTF-8):	Pliki językowe fulani dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-ff

%description -n iceweasel-lang-ff
Fulah resources for Iceweasel.

%description -n iceweasel-lang-ff -l pl.UTF-8
Pliki językowe fulani dla Iceweasela.

%package -n iceweasel-lang-fi
Summary:	Finnish resources for Iceweasel
Summary(pl.UTF-8):	Fińskie pliki językowe dla Iceweasela
Group:		I18n
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
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-fr

%description -n iceweasel-lang-fr
French resources for Iceweasel.

%description -n iceweasel-lang-fr -l pl.UTF-8
Francuskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-fy
Summary:	Frisian resources for Iceweasel
Summary(pl.UTF-8):	Fryzyjskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-fy

%description -n iceweasel-lang-fy
Frisian resources for Iceweasel.

%description -n iceweasel-lang-fy -l pl.UTF-8
Fryzyjskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-ga
Summary:	Irish resources for Iceweasel
Summary(pl.UTF-8):	Irlandzkie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-ga

%description -n iceweasel-lang-ga
Irish resources for Iceweasel.

%description -n iceweasel-lang-ga -l pl.UTF-8
Irlandzkie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-gd
Summary:	Gaelic resources for Iceweasel
Summary(pl.UTF-8):	Szkockie (gaelickie) pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-gd

%description -n iceweasel-lang-gd
Gaelic resources for Iceweasel.

%description -n iceweasel-lang-gd -l pl.UTF-8
Szkockie (gaelickie) pliki językowe dla Iceweasela.

%package -n iceweasel-lang-gl
Summary:	Galician resources for Iceweasel
Summary(pl.UTF-8):	Galicyjskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-gl

%description -n iceweasel-lang-gl
Galician resources for Iceweasel.

%description -n iceweasel-lang-gl -l pl.UTF-8
Galicyjskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-gu
Summary:	Gujarati resources for Iceweasel
Summary(pl.UTF-8):	Pliki językowe gudźarati dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-gu

%description -n iceweasel-lang-gu
Gujarati resources for Iceweasel.

%description -n iceweasel-lang-gu -l pl.UTF-8
Pliki językowe gudźarati dla Iceweasela.

%package -n iceweasel-lang-he
Summary:	Hebrew resources for Iceweasel
Summary(pl.UTF-8):	Hebrajskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-he

%description -n iceweasel-lang-he
Hebrew resources for Iceweasel.

%description -n iceweasel-lang-he -l pl.UTF-8
Hebrajskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-hi
Summary:	Hindi resources for Iceweasel
Summary(pl.UTF-8):	Pliki językowe hindi dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-hi

%description -n iceweasel-lang-hi
Hindi resources for Iceweasel.

%description -n iceweasel-lang-hi -l pl.UTF-8
Pliki językowe hindi dla Iceweasela.

%package -n iceweasel-lang-hr
Summary:	Croatian resources for Iceweasel
Summary(pl.UTF-8):	Chorwackie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-hr

%description -n iceweasel-lang-hr
Croatian resources for Iceweasel.

%description -n iceweasel-lang-hr -l pl.UTF-8
Chorwackie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-hsb
Summary:	Upper Sorbian resources for Iceweasel
Summary(pl.UTF-8):	Górnołużyckie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-hsb

%description -n iceweasel-lang-hsb
Upper Sorbian resources for Iceweasel.

%description -n iceweasel-lang-hsb -l pl.UTF-8
Górnołużyckie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-hu
Summary:	Hungarian resources for Iceweasel
Summary(hu.UTF-8):	Magyar nyelv Iceweasel-hez
Summary(pl.UTF-8):	Węgierskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-hu

%description -n iceweasel-lang-hu
Hungarian resources for Iceweasel.

%description -n iceweasel-lang-hu -l hu.UTF-8
Magyar nyelv Iceweasel-hez.

%description -n iceweasel-lang-hu -l pl.UTF-8
Węgierskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-hy
Summary:	Armenian resources for Iceweasel
Summary(pl.UTF-8):	Ormiańskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-hy

%description -n iceweasel-lang-hy
Armenian resources for Iceweasel.

%description -n iceweasel-lang-hy -l pl.UTF-8
Ormiańskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-id
Summary:	Indonesian resources for Iceweasel
Summary(pl.UTF-8):	Indonezyjskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-id

%description -n iceweasel-lang-id
Indonesian resources for Iceweasel.

%description -n iceweasel-lang-id -l pl.UTF-8
Indonezyjskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-is
Summary:	Icelandic resources for Iceweasel
Summary(pl.UTF-8):	Islandzkie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-is

%description -n iceweasel-lang-is
Icelandic resources for Iceweasel.

%description -n iceweasel-lang-is -l pl.UTF-8
Islandzkie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-it
Summary:	Italian resources for Iceweasel
Summary(pl.UTF-8):	Włoskie pliki językowe dla Iceweasela
Group:		I18n
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
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-ja

%description -n iceweasel-lang-ja
Japanese resources for Iceweasel.

%description -n iceweasel-lang-ja -l pl.UTF-8
Japońskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-kk
Summary:	Kazakh resources for Iceweasel
Summary(pl.UTF-8):	Kazachskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-kk

%description -n iceweasel-lang-kk
Kazakh resources for Iceweasel.

%description -n iceweasel-lang-kk -l pl.UTF-8
Kazachskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-km
Summary:	Khmer resources for Iceweasel
Summary(pl.UTF-8):	Khmerskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-km

%description -n iceweasel-lang-km
Khmer resources for Iceweasel.

%description -n iceweasel-lang-km -l pl.UTF-8
Khmerskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-kn
Summary:	Kannada resources for Iceweasel
Summary(pl.UTF-8):	Pliki językowe kannada dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-kn

%description -n iceweasel-lang-kn
Kannada resources for Iceweasel.

%description -n iceweasel-lang-kn -l pl.UTF-8
Pliki językowe kannada dla Iceweasela.

%package -n iceweasel-lang-ko
Summary:	Korean resources for Iceweasel
Summary(pl.UTF-8):	Koreańskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-ko

%description -n iceweasel-lang-ko
Korean resources for Iceweasel.

%description -n iceweasel-lang-ko -l pl.UTF-8
Koreańskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-ku
Summary:	Kurdish resources for Iceweasel
Summary(pl.UTF-8):	Kurdyjskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-ku

%description -n iceweasel-lang-ku
Kurdish resources for Iceweasel.

%description -n iceweasel-lang-ku -l pl.UTF-8
Kurdyjskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-lij
Summary:	Ligurian resources for Iceweasel
Summary(pl.UTF-8):	Liguryjskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-lij

%description -n iceweasel-lang-lij
Ligurian resources for Iceweasel.

%description -n iceweasel-lang-lij -l pl.UTF-8
Liguryjskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-lt
Summary:	Lithuanian resources for Iceweasel
Summary(pl.UTF-8):	Litewskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-lt

%description -n iceweasel-lang-lt
Lithuanian resources for Iceweasel.

%description -n iceweasel-lang-lt -l pl.UTF-8
Litewskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-lv
Summary:	Latvian resources for Iceweasel
Summary(pl.UTF-8):	Łotewskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-lv

%description -n iceweasel-lang-lv
Latvian resources for Iceweasel.

%description -n iceweasel-lang-lv -l pl.UTF-8
Łotewskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-mai
Summary:	Maithili resources for Iceweasel
Summary(pl.UTF-8):	Pliki językowe maithili dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-mai

%description -n iceweasel-lang-mai
Maithili resources for Iceweasel.

%description -n iceweasel-lang-mai -l pl.UTF-8
Pliki językowe maithili dla Iceweasela.

%package -n iceweasel-lang-mk
Summary:	Macedonian resources for Iceweasel
Summary(pl.UTF-8):	Macedońskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-mk

%description -n iceweasel-lang-mk
Macedonian resources for Iceweasel.

%description -n iceweasel-lang-mk -l pl.UTF-8
Macedońskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-ml
Summary:	Malayalam resources for Iceweasel
Summary(pl.UTF-8):	Pliki językowe malajalam dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-ml

%description -n iceweasel-lang-ml
Malayalam resources for Iceweasel.

%description -n iceweasel-lang-ml -l pl.UTF-8
Pliki językowe malajalam dla Iceweasela.

%package -n iceweasel-lang-mr
Summary:	Marathi resources for Iceweasel
Summary(pl.UTF-8):	Pliki językowe marathi dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-mr

%description -n iceweasel-lang-mr
Marathi resources for Iceweasel.

%description -n iceweasel-lang-mr -l pl.UTF-8
Pliki językowe marathi dla Iceweasela.

%package -n iceweasel-lang-ms
Summary:	Malay resources for Iceweasel
Summary(pl.UTF-8):	Malajskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-ms

%description -n iceweasel-lang-ms
Malay resources for Iceweasel.

%description -n iceweasel-lang-ms -l pl.UTF-8
Malajskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-nb
Summary:	Norwegian Bokmaal resources for Iceweasel
Summary(pl.UTF-8):	Norweskie (bokmaal) pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-nb

%description -n iceweasel-lang-nb
Norwegian Bokmaal resources for Iceweasel.

%description -n iceweasel-lang-nb -l pl.UTF-8
Norweskie (bokmaal) pliki językowe dla Iceweasela.

%package -n iceweasel-lang-nl
Summary:	Dutch resources for Iceweasel
Summary(pl.UTF-8):	Holenderskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-nl

%description -n iceweasel-lang-nl
Dutch resources for Iceweasel.

%description -n iceweasel-lang-nl -l pl.UTF-8
Holenderskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-nn
Summary:	Norwegian Nynorsk resources for Iceweasel
Summary(pl.UTF-8):	Norweskie (nynorsk) pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-nn

%description -n iceweasel-lang-nn
Norwegian Nynorsk resources for Iceweasel.

%description -n iceweasel-lang-nn -l pl.UTF-8
Norweskie (nynorsk) pliki językowe dla Iceweasela.

%package -n iceweasel-lang-or
Summary:	Oriya resources for Iceweasel
Summary(pl.UTF-8):	Pliki językowe orija dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-or

%description -n iceweasel-lang-or
Oriya resources for Iceweasel.

%description -n iceweasel-lang-or -l pl.UTF-8
Pliki językowe orija dla Iceweasela.

%package -n iceweasel-lang-pa
Summary:	Panjabi resources for Iceweasel
Summary(pl.UTF-8):	Pendżabskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-pa

%description -n iceweasel-lang-pa
Panjabi resources for Iceweasel.

%description -n iceweasel-lang-pa -l pl.UTF-8
Pendżabskie pliki językowe dla Iceweasela.

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

%package -n iceweasel-lang-pt_BR
Summary:	Portuguese (Brazil) resources for Iceweasel
Summary(pl.UTF-8):	Portugalskie (brazylijskie) pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-pt_BR

%description -n iceweasel-lang-pt_BR
Portuguese (Brazil) resources for Iceweasel.

%description -n iceweasel-lang-pt_BR -l pl.UTF-8
Portugalskie (brazylijskie) pliki językowe dla Iceweasela.

%package -n iceweasel-lang-pt
Summary:	Portuguese (Portugal) resources for Iceweasel
Summary(pl.UTF-8):	Portugalskie pliki językowe dla Iceweasela (wersja dla Portugalii)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-pt

%description -n iceweasel-lang-pt
Portuguese (Portugal) resources for Iceweasel.

%description -n iceweasel-lang-pt -l pl.UTF-8
Portugalskie pliki językowe dla Iceweasela (wersja dla Portugalii).

%package -n iceweasel-lang-rm
Summary:	Romansh resources for Iceweasel
Summary(pl.UTF-8):	Retoromańskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-rm

%description -n iceweasel-lang-rm
Romansh resources for Iceweasel.

%description -n iceweasel-lang-rm -l pl.UTF-8
Retoromańskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-ro
Summary:	Romanian resources for Iceweasel
Summary(pl.UTF-8):	Rumuńskie pliki językowe dla Iceweasela
Group:		I18n
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
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-ru

%description -n iceweasel-lang-ru
Russian resources for Iceweasel.

%description -n iceweasel-lang-ru -l pl.UTF-8
Rosyjskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-si
Summary:	Sinhala resources for Iceweasel
Summary(pl.UTF-8):	Syngaleskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-si

%description -n iceweasel-lang-si
Sinhala resources for Iceweasel.

%description -n iceweasel-lang-si -l pl.UTF-8
Syngaleskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-sk
Summary:	Slovak resources for Iceweasel
Summary(pl.UTF-8):	Słowackie pliki językowe dla Iceweasela
Group:		I18n
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
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-sl

%description -n iceweasel-lang-sl
Slovene resources for Iceweasel.

%description -n iceweasel-lang-sl -l pl.UTF-8
Słoweńskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-son
Summary:	Songhai resources for Iceweasel
Summary(pl.UTF-8):	Songhajskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-son

%description -n iceweasel-lang-son
Songhai resources for Iceweasel.

%description -n iceweasel-lang-son -l pl.UTF-8
Songhajskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-sq
Summary:	Albanian resources for Iceweasel
Summary(pl.UTF-8):	Albańskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-sq

%description -n iceweasel-lang-sq
Albanian resources for Iceweasel.

%description -n iceweasel-lang-sq -l pl.UTF-8
Albańskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-sr
Summary:	Serbian resources for Iceweasel
Summary(pl.UTF-8):	Serbskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-sr

%description -n iceweasel-lang-sr
Serbian resources for Iceweasel.

%description -n iceweasel-lang-sr -l pl.UTF-8
Serbskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-sv
Summary:	Swedish resources for Iceweasel
Summary(pl.UTF-8):	Szwedzkie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-sv

%description -n iceweasel-lang-sv
Swedish resources for Iceweasel.

%description -n iceweasel-lang-sv -l pl.UTF-8
Szwedzkie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-ta
Summary:	Tamil (India) resources for Iceweasel
Summary(pl.UTF-8):	Tamilskie pliki językowe dla Iceweasela (wersja dla Indii)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-ta

%description -n iceweasel-lang-ta
Tamil (India) resources for Iceweasel.

%description -n iceweasel-lang-ta -l pl.UTF-8
Tamilskie pliki językowe dla Iceweasela (wersja dla Indii).

%package -n iceweasel-lang-te
Summary:	Telugu resources for Iceweasel
Summary(pl.UTF-8):	Pliki językowe telugu dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-te

%description -n iceweasel-lang-te
Telugu resources for Iceweasel.

%description -n iceweasel-lang-te -l pl.UTF-8
Pliki językowe telugu dla Iceweasela.

%package -n iceweasel-lang-th
Summary:	Thai resources for Iceweasel
Summary(pl.UTF-8):	Tajskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-th

%description -n iceweasel-lang-th
Thai resources for Iceweasel.

%description -n iceweasel-lang-th -l pl.UTF-8
Tajskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-tr
Summary:	Turkish resources for Iceweasel
Summary(pl.UTF-8):	Tureckie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-tr

%description -n iceweasel-lang-tr
Turkish resources for Iceweasel.

%description -n iceweasel-lang-tr -l pl.UTF-8
Tureckie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-uk
Summary:	Ukrainian resources for Iceweasel
Summary(pl.UTF-8):	Ukraińskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-uk

%description -n iceweasel-lang-uk
Ukrainian resources for Iceweasel.

%description -n iceweasel-lang-uk -l pl.UTF-8
Ukraińskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-uz
Summary:	Uzbek resources for Iceweasel
Summary(pl.UTF-8):	Uzbeckie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-uz

%description -n iceweasel-lang-uz
Uzbek resources for Iceweasel.

%description -n iceweasel-lang-uz -l pl.UTF-8
Uzbeckie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-vi
Summary:	Vietmanese resources for Iceweasel
Summary(pl.UTF-8):	Wietnamskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-vi

%description -n iceweasel-lang-vi
Vietmanese resources for Iceweasel.

%description -n iceweasel-lang-vi -l pl.UTF-8
Wietnamskie pliki językowe dla Iceweasela.

%package -n iceweasel-lang-xh
Summary:	Xhosa resources for Iceweasel
Summary(pl.UTF-8):	Pliki językowe xhosa dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-xh

%description -n iceweasel-lang-xh
Xhosa resources for Iceweasel.

%description -n iceweasel-lang-xh -l pl.UTF-8
Pliki językowe xhosa dla Iceweasela.

%package -n iceweasel-lang-zh_CN
Summary:	Simplified Chinese resources for Iceweasel
Summary(pl.UTF-8):	Chińskie (uproszczone) pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-zh_CN

%description -n iceweasel-lang-zh_CN
Simplified Chinese resources for Iceweasel.

%description -n iceweasel-lang-zh_CN -l pl.UTF-8
Chińskie uproszczone pliki językowe dla Iceweasela.

%package -n iceweasel-lang-zh_TW
Summary:	Traditional Chinese resources for Iceweasel
Summary(pl.UTF-8):	Chińskie tradycyjne pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-zh_TW

%description -n iceweasel-lang-zh_TW
Traditional Chinese resources for Iceweasel.

%description -n iceweasel-lang-zh_TW -l pl.UTF-8
Chińskie tradycyjne pliki językowe dla Iceweasela.

%package -n iceweasel-lang-zu
Summary:	Zulu resources for Iceweasel
Summary(pl.UTF-8):	Zuluskie pliki językowe dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-zu

%description -n iceweasel-lang-zu
Zulu resources for Iceweasel.

%description -n iceweasel-lang-zu -l pl.UTF-8
Zuluskie pliki językowe dla Iceweasela.

%prep
unpack() {
    local args="$1" file="$2"
	local lang=$(basename $file .xpi)
	install -d $lang

	# rebrand locale for Iceweasel
	cd $lang
	cp -p $file .
	unzip -q $lang.xpi install.rdf browser/chrome/$lang/locale/branding/brand.{dtd,properties} browser/chrome/$lang/locale/browser/appstrings.properties
	sed -i -e 's/Mozilla Firefox/Iceweasel/g; s/Firefox/Iceweasel/g;' browser/chrome/$lang/locale/branding/brand.{dtd,properties}
	sed -i -e 's/Firefox/Iceweasel/g;' browser/chrome/$lang/locale/browser/appstrings.properties
	zip -q0 $lang.xpi browser/chrome/$lang/locale/branding/brand.{dtd,properties} browser/chrome/$lang/locale/browser/appstrings.properties
	if ! grep -q "<em:minVersion>%{version}</em:minVersion>" install.rdf; then
		echo "$lang.xpi most likely doesn't work with iceweasel %{version}!" >&2
		exit 1
	fi
	%{__rm} -rf chrome install.rdf
	cd ..
}
%define __unzip unpack
%setup -qcT %(seq -f '-a %g' 0 87 | xargs)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{iceweaseldir}/browser/extensions
for a in */*.xpi; do
	basename=$(basename $a .xpi)
	cp -p $a $RPM_BUILD_ROOT%{iceweaseldir}/browser/extensions/langpack-$basename@firefox.mozilla.org.xpi
done

%clean
rm -rf $RPM_BUILD_ROOT

%files -n iceweasel-lang-ach
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-ach@firefox.mozilla.org.xpi

%files -n iceweasel-lang-af
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-af@firefox.mozilla.org.xpi

%files -n iceweasel-lang-an
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-an@firefox.mozilla.org.xpi

%files -n iceweasel-lang-ar
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-ar@firefox.mozilla.org.xpi

%files -n iceweasel-lang-as
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-as@firefox.mozilla.org.xpi

%files -n iceweasel-lang-ast
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-ast@firefox.mozilla.org.xpi

%files -n iceweasel-lang-az
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-az@firefox.mozilla.org.xpi

%files -n iceweasel-lang-be
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-be@firefox.mozilla.org.xpi

%files -n iceweasel-lang-bg
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-bg@firefox.mozilla.org.xpi

%files -n iceweasel-lang-bn
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-bn-BD@firefox.mozilla.org.xpi

%files -n iceweasel-lang-bn_IN
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-bn-IN@firefox.mozilla.org.xpi

%files -n iceweasel-lang-br
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-br@firefox.mozilla.org.xpi

%files -n iceweasel-lang-bs
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-bs@firefox.mozilla.org.xpi

%files -n iceweasel-lang-ca
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-ca@firefox.mozilla.org.xpi

%files -n iceweasel-lang-cs
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-cs@firefox.mozilla.org.xpi

#%files -n iceweasel-lang-csb
#%defattr(644,root,root,755)
#%{iceweaseldir}/browser/extensions/langpack-csb@firefox.mozilla.org.xpi

%files -n iceweasel-lang-cy
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-cy@firefox.mozilla.org.xpi

%files -n iceweasel-lang-da
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-da@firefox.mozilla.org.xpi

%files -n iceweasel-lang-de
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-de@firefox.mozilla.org.xpi

%files -n iceweasel-lang-dsb
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-dsb@firefox.mozilla.org.xpi

%files -n iceweasel-lang-el
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-el@firefox.mozilla.org.xpi

%files -n iceweasel-lang-en_GB
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-en-GB@firefox.mozilla.org.xpi

%files -n iceweasel-lang-en_US
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-en-US@firefox.mozilla.org.xpi

%files -n iceweasel-lang-en_ZA
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-en-ZA@firefox.mozilla.org.xpi

%files -n iceweasel-lang-eo
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-eo@firefox.mozilla.org.xpi

%files -n iceweasel-lang-es_AR
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-es-AR@firefox.mozilla.org.xpi

%files -n iceweasel-lang-es_CL
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-es-CL@firefox.mozilla.org.xpi

%files -n iceweasel-lang-es
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-es-ES@firefox.mozilla.org.xpi

%files -n iceweasel-lang-es_MX
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-es-MX@firefox.mozilla.org.xpi

%files -n iceweasel-lang-et
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-et@firefox.mozilla.org.xpi

%files -n iceweasel-lang-eu
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-eu@firefox.mozilla.org.xpi

%files -n iceweasel-lang-fa
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-fa@firefox.mozilla.org.xpi

%files -n iceweasel-lang-ff
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-ff@firefox.mozilla.org.xpi

%files -n iceweasel-lang-fi
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-fi@firefox.mozilla.org.xpi

%files -n iceweasel-lang-fr
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-fr@firefox.mozilla.org.xpi

%files -n iceweasel-lang-fy
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-fy-NL@firefox.mozilla.org.xpi

%files -n iceweasel-lang-ga
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-ga-IE@firefox.mozilla.org.xpi

%files -n iceweasel-lang-gd
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-gd@firefox.mozilla.org.xpi

%files -n iceweasel-lang-gl
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-gl@firefox.mozilla.org.xpi

%files -n iceweasel-lang-gu
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-gu-IN@firefox.mozilla.org.xpi

%files -n iceweasel-lang-he
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-he@firefox.mozilla.org.xpi

%files -n iceweasel-lang-hi
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-hi-IN@firefox.mozilla.org.xpi

%files -n iceweasel-lang-hr
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-hr@firefox.mozilla.org.xpi

%files -n iceweasel-lang-hsb
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-hsb@firefox.mozilla.org.xpi

%files -n iceweasel-lang-hu
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-hu@firefox.mozilla.org.xpi

%files -n iceweasel-lang-hy
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-hy-AM@firefox.mozilla.org.xpi

%files -n iceweasel-lang-id
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-id@firefox.mozilla.org.xpi

%files -n iceweasel-lang-is
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-is@firefox.mozilla.org.xpi

%files -n iceweasel-lang-it
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-it@firefox.mozilla.org.xpi

%files -n iceweasel-lang-ja
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-ja@firefox.mozilla.org.xpi

%files -n iceweasel-lang-kk
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-kk@firefox.mozilla.org.xpi

%files -n iceweasel-lang-km
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-km@firefox.mozilla.org.xpi

%files -n iceweasel-lang-kn
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-kn@firefox.mozilla.org.xpi

%files -n iceweasel-lang-ko
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-ko@firefox.mozilla.org.xpi

#%files -n iceweasel-lang-ku
#%defattr(644,root,root,755)
#%{iceweaseldir}/browser/extensions/langpack-ku@firefox.mozilla.org.xpi

%files -n iceweasel-lang-lij
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-lij@firefox.mozilla.org.xpi

%files -n iceweasel-lang-lt
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-lt@firefox.mozilla.org.xpi

%files -n iceweasel-lang-lv
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-lv@firefox.mozilla.org.xpi

%files -n iceweasel-lang-mai
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-mai@firefox.mozilla.org.xpi

%files -n iceweasel-lang-mk
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-mk@firefox.mozilla.org.xpi

%files -n iceweasel-lang-ml
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-ml@firefox.mozilla.org.xpi

%files -n iceweasel-lang-mr
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-mr@firefox.mozilla.org.xpi

%files -n iceweasel-lang-ms
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-ms@firefox.mozilla.org.xpi

%files -n iceweasel-lang-nb
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-nb-NO@firefox.mozilla.org.xpi

%files -n iceweasel-lang-nl
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-nl@firefox.mozilla.org.xpi

%files -n iceweasel-lang-nn
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-nn-NO@firefox.mozilla.org.xpi

%files -n iceweasel-lang-or
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-or@firefox.mozilla.org.xpi

%files -n iceweasel-lang-pa
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-pa-IN@firefox.mozilla.org.xpi

%files -n iceweasel-lang-pl
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-pl@firefox.mozilla.org.xpi

%files -n iceweasel-lang-pt_BR
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-pt-BR@firefox.mozilla.org.xpi

%files -n iceweasel-lang-pt
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-pt-PT@firefox.mozilla.org.xpi

%files -n iceweasel-lang-rm
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-rm@firefox.mozilla.org.xpi

%files -n iceweasel-lang-ro
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-ro@firefox.mozilla.org.xpi

%files -n iceweasel-lang-ru
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-ru@firefox.mozilla.org.xpi

%files -n iceweasel-lang-si
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-si@firefox.mozilla.org.xpi

%files -n iceweasel-lang-sk
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-sk@firefox.mozilla.org.xpi

%files -n iceweasel-lang-sl
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-sl@firefox.mozilla.org.xpi

%files -n iceweasel-lang-son
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-son@firefox.mozilla.org.xpi

%files -n iceweasel-lang-sq
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-sq@firefox.mozilla.org.xpi

%files -n iceweasel-lang-sr
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-sr@firefox.mozilla.org.xpi

%files -n iceweasel-lang-sv
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-sv-SE@firefox.mozilla.org.xpi

%files -n iceweasel-lang-ta
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-ta@firefox.mozilla.org.xpi

%files -n iceweasel-lang-te
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-te@firefox.mozilla.org.xpi

%files -n iceweasel-lang-th
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-th@firefox.mozilla.org.xpi

%files -n iceweasel-lang-tr
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-tr@firefox.mozilla.org.xpi

%files -n iceweasel-lang-uk
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-uk@firefox.mozilla.org.xpi

%files -n iceweasel-lang-uz
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-uz@firefox.mozilla.org.xpi

%files -n iceweasel-lang-vi
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-vi@firefox.mozilla.org.xpi

%files -n iceweasel-lang-xh
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-xh@firefox.mozilla.org.xpi

%files -n iceweasel-lang-zh_CN
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-zh-CN@firefox.mozilla.org.xpi

%files -n iceweasel-lang-zh_TW
%defattr(644,root,root,755)
%{iceweaseldir}/browser/extensions/langpack-zh-TW@firefox.mozilla.org.xpi

#%files -n iceweasel-lang-zu
#%defattr(644,root,root,755)
#%{iceweaseldir}/browser/extensions/langpack-zu@firefox.mozilla.org.xpi
