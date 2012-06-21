# TODO:
#   - do something with *.rdf file, there if file conflict with other lang packages
# UPDATING:
%if 0
rm -vf *.xpi
./builder -g
V=4.0
U=http://releases.mozilla.org/pub/mozilla.org/firefox/releases/$V/linux-i686/
curl -s $U | sed -ne 's,.*href="\([^"]\+\)/".*,'"$U"'xpi/\1.xpi,p'
%endif

Summary:	Language packs for Iceweasel
Summary(pl.UTF-8):	Pakiety językowe dla Iceweasela
Name:		iceweasel-languages
Version:	13.0.1
Release:	1
License:	MPL 1.1 or GPL v2+ or LGPL v2.1+
Group:		I18n
Source0:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/af.xpi
# Source0-md5:	59c80abcb0ed19b444c88115464eac26
Source1:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ak.xpi
# Source1-md5:	ac051c55dd9daaa772c4ac893af1138e
Source2:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ar.xpi
# Source2-md5:	44c06494b35472f4845435b096528cf4
Source3:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/as.xpi
# Source3-md5:	890a2b2ea4d38071468c892c0690faf6
Source4:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ast.xpi
# Source4-md5:	4c3657d3a968ced57bfc26b10f97c990
Source5:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/be.xpi
# Source5-md5:	7e030c0089f29939e55721aeea486554
Source6:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bg.xpi
# Source6-md5:	ba4a3ab7906d2a121a2579449e9413ed
Source7:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bn-BD.xpi
# Source7-md5:	d631b45c73871ef4f3698ff859fb4f91
Source8:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bn-IN.xpi
# Source8-md5:	b575b886006aa4d330052fde29ef60ff
Source9:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/br.xpi
# Source9-md5:	7d4b1f108205c24dd9e4ab8231273050
Source10:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bs.xpi
# Source10-md5:	5f93c0283b32c4ae3c6ea99fe45d855f
Source11:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ca.xpi
# Source11-md5:	6f7c166ead1ecd5955c938c58150be72
Source12:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/cs.xpi
# Source12-md5:	c6ad080d33ce0650109b05aac4289937
Source13:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/csb.xpi
# Source13-md5:	55321c24027353433c686b4cf837d137
Source14:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/cy.xpi
# Source14-md5:	dfac9a3073cb3fd1fd1af2daacc815dc
Source15:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/da.xpi
# Source15-md5:	9d56d413565f192691e0271ea0e49e40
Source16:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/de.xpi
# Source16-md5:	5ac0fab556f0d670ae28886c1371dd7c
Source17:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/el.xpi
# Source17-md5:	e0366107ae4801a9c5f7841ef833004d
Source18:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/en-GB.xpi
# Source18-md5:	4232cd58d5b8f7dfde4438090e50b50f
Source19:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/en-US.xpi
# Source19-md5:	1b6a55d8fcb7f82dd9a1d4ab0cbbe6c0
Source20:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/en-ZA.xpi
# Source20-md5:	450f6dbb8f2cc60cf5e40c9d95f7be3d
Source21:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/eo.xpi
# Source21-md5:	61ba59182c2f608225f28d976b25733b
Source22:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-AR.xpi
# Source22-md5:	6cd93da9c2bf1c9cc2887a168e04536d
Source23:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-CL.xpi
# Source23-md5:	3e3ed4d4416e4ee5aaa226a17c2f2663
Source24:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-ES.xpi
# Source24-md5:	b73e8e8cf8d6fda8d1a3b880ab48be5c
Source25:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-MX.xpi
# Source25-md5:	8f63b7436cb0c7cb433f29d1c329fadc
Source26:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/et.xpi
# Source26-md5:	648b7abbafad7a7202683474a6b4f8a4
Source27:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/eu.xpi
# Source27-md5:	fabaa3e713107df2f24b3cc261d18666
Source28:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fa.xpi
# Source28-md5:	b517b537282427122864ba4beafbf4bc
Source29:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fi.xpi
# Source29-md5:	3157514c12c06b4f783d87a6e876fc5e
Source30:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fr.xpi
# Source30-md5:	d9411175a8f3bda0c36d61511b3ce877
Source31:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fy-NL.xpi
# Source31-md5:	16e927d57f8412b6951b60986d14b447
Source32:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ga-IE.xpi
# Source32-md5:	35390661dd66ed5fa278c5fce00df710
Source33:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/gd.xpi
# Source33-md5:	fba5ae94b4f6b6e8c37767f32c230ea9
Source34:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/gl.xpi
# Source34-md5:	288d55c9bab35ec805ba66a03996844f
Source35:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/gu-IN.xpi
# Source35-md5:	981898e88bb4ffa02a22e9ce39c8d205
Source36:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/he.xpi
# Source36-md5:	d9d3db05d18d940953c2263042a0d430
Source37:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hi-IN.xpi
# Source37-md5:	2f5b312acd70f16a11b9a9c4dcc5bb67
Source38:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hr.xpi
# Source38-md5:	37d125497bf3ec3a75760be9a900c232
Source39:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hu.xpi
# Source39-md5:	08c137c94ac51c65c01a5a96e7d95d30
Source40:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hy-AM.xpi
# Source40-md5:	e5c14c495b4a1b23287ca24729baaf86
Source41:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/id.xpi
# Source41-md5:	a17905ba225cdcb201e5e193d312333a
Source42:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/is.xpi
# Source42-md5:	9b438146c585b2caad8caca47313bf9f
Source43:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/it.xpi
# Source43-md5:	6aaaef95aec14f20fe132eabd317a802
Source44:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ja.xpi
# Source44-md5:	e0a03ef9b54f8177c9bf6ed57549320e
Source45:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/kk.xpi
# Source45-md5:	c3b76f03829b6452dd4fa2c56fd6e709
Source46:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/kn.xpi
# Source46-md5:	d78b54e0406ca4ec31482df96f31bad5
Source47:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ko.xpi
# Source47-md5:	c8961404672a27c41ede5cb81dbf8c22
Source48:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ku.xpi
# Source48-md5:	81bbbfcde9a1bd04d631754607dc896b
Source49:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/lg.xpi
# Source49-md5:	cddb184a54d73814023fb8be738d9db3
Source50:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/lij.xpi
# Source50-md5:	bcdb49a764bfacefd5155ca7195ab317
Source51:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/lt.xpi
# Source51-md5:	f45261a72386548eb8501c80c6f8df3f
Source52:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/lv.xpi
# Source52-md5:	ab59a8edabe8db652fc9b7827d8c178b
Source53:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/mai.xpi
# Source53-md5:	d3bd9fc94d420b501471c295666b4988
Source54:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/mk.xpi
# Source54-md5:	94b4d3e0d53f6f1dc5a33353c30d06f2
Source55:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ml.xpi
# Source55-md5:	3e79c03ac78571a0bd77008b52fd5236
Source56:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/mr.xpi
# Source56-md5:	76466c7d70174857f1c9991aaf3d4217
Source57:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/nb-NO.xpi
# Source57-md5:	75b8a73de33ca836f8e8326ed874d0dc
Source58:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/nl.xpi
# Source58-md5:	1f11060f24b49c86c3b2617a83a49c8e
Source59:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/nn-NO.xpi
# Source59-md5:	70bd94b7f6c2ff89f50c17dd66ad5764
Source60:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/nso.xpi
# Source60-md5:	06515312df6d168e41a39efdba7b3276
Source61:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/or.xpi
# Source61-md5:	63bfeab3ccec53e9c7191ee6c63155e1
Source62:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pa-IN.xpi
# Source62-md5:	1c1a454d1eae10ae9ad077ee9373ba7f
Source63:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pl.xpi
# Source63-md5:	2b343ea2aab4e7bcebbeaf91fda6662e
Source64:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pt-BR.xpi
# Source64-md5:	50325c9e1d8a2978c83ea50b4a4c4679
Source65:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pt-PT.xpi
# Source65-md5:	83958948b2595ea88b665cf1e444290b
Source66:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/rm.xpi
# Source66-md5:	67e6c07ec5b0b189751656d369d8cfa9
Source67:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ro.xpi
# Source67-md5:	fac12081a72dfb6863a4015788bb9b8b
Source68:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ru.xpi
# Source68-md5:	ed5665f6a1c849f8f47d0747fd676e90
Source69:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/si.xpi
# Source69-md5:	3980fc8440e57bb0d9552d8c4a63706f
Source70:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sk.xpi
# Source70-md5:	6a381d173d2892d3d5811bbec1a0f35e
Source71:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sl.xpi
# Source71-md5:	1c5ea403f6305cdbba722ea33932b7ef
Source72:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/son.xpi
# Source72-md5:	ff7973c4f3775188606b7c905a4b7ffa
Source73:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sq.xpi
# Source73-md5:	43553adc3a4f09eb202520edebcf54f3
Source74:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sr.xpi
# Source74-md5:	96c705b6dc2f5deabb6235db77252e95
Source75:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sv-SE.xpi
# Source75-md5:	c7ac00fa83b56646dd5005da08f247c9
Source76:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ta.xpi
# Source76-md5:	8b660c4b8dcf8657c8bd6020867d29f1
Source77:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ta-LK.xpi
# Source77-md5:	a6b565ba115b78a0827d4d2067e42842
Source78:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/te.xpi
# Source78-md5:	77414e264921025cfba63a1e294e27e4
Source79:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/th.xpi
# Source79-md5:	81a8771f7dd065179ba7461a0460584c
Source80:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/tr.xpi
# Source80-md5:	f50667cb4fef2e79f8d6946b11fcf752
Source81:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/uk.xpi
# Source81-md5:	cdc503e1fc7fc0271f9c7a138cf35876
Source82:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/vi.xpi
# Source82-md5:	825ec0b64df9539d2cf3f43ee2f632c1
Source83:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/zh-CN.xpi
# Source83-md5:	194e482318e49fb1d6e37bf55dfbea62
Source84:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/zh-TW.xpi
# Source84-md5:	49875e1ea456a893231118a24f69f2b9
Source85:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/zu.xpi
# Source85-md5:	063a7f43128742163565b746ff9f4639
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

%package -n iceweasel-lang-ak
Summary:	Akan resources for Iceweasel
Summary(pl.UTF-8):	Pliki językowe akan dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-ak

%description -n iceweasel-lang-ak
Akan resources for Iceweasel.

%description -n iceweasel-lang-ak -l pl.UTF-8
Pliki językowe akan dla Iceweasela.

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

%package -n iceweasel-lang-lg
Summary:	Ganda resources for Iceweasel
Summary(pl.UTF-8):	Pliki językowe luganda dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-lg

%description -n iceweasel-lang-lg
Ganda resources for Iceweasel.

%description -n iceweasel-lang-lg -l pl.UTF-8
Pliki językowe luganda dla Iceweasela.

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

%package -n iceweasel-lang-nso
Summary:	Northern Sotho resources for Iceweasel
Summary(pl.UTF-8):	Pliki językowe sotho północnego dla Iceweasela
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-nso

%description -n iceweasel-lang-nso
Northern Sotho resources for Iceweasel.

%description -n iceweasel-lang-nso -l pl.UTF-8
Pliki językowe sotho północnego dla Iceweasela.

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

%package -n iceweasel-lang-ta_LK
Summary:	Tamil (Sri Lanka) resources for Iceweasel
Summary(pl.UTF-8):	Tamilskie pliki językowe dla Iceweasela (wersja dla Sri Lanki)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-ta_LK

%description -n iceweasel-lang-ta_LK
Tamil (Sri Lanka) resources for Iceweasel.

%description -n iceweasel-lang-ta_LK -l pl.UTF-8
Tamilskie pliki językowe dla Iceweasela (wersja dla Sri Lanki).

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
	unzip -q $lang.xpi install.rdf chrome/$lang/locale/branding/brand.{dtd,properties} chrome/$lang/locale/browser/appstrings.properties
	sed -i -e 's/Mozilla Firefox/Iceweasel/g; s/Firefox/Iceweasel/g;' chrome/$lang/locale/branding/brand.{dtd,properties}
	sed -i -e 's/Firefox/Iceweasel/g;' chrome/$lang/locale/browser/appstrings.properties
	zip -q0 $lang.xpi chrome/$lang/locale/branding/brand.{dtd,properties} chrome/$lang/locale/browser/appstrings.properties
	if ! grep -q "<em:minVersion>%{version}</em:minVersion>" install.rdf; then
		echo "$lang.xpi most likely doesn't work with iceweasel %{version}!" >&2
		exit 1
	fi
	%{__rm} -rf chrome install.rdf
	cd ..
}
%define __unzip unpack
%setup -qcT %(seq -f '-a %g' 0 85 | xargs)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{iceweaseldir}/extensions
for a in */*.xpi; do
	basename=$(basename $a .xpi)
	cp -p $a $RPM_BUILD_ROOT%{iceweaseldir}/extensions/langpack-$basename@firefox.mozilla.org.xpi
done

%clean
rm -rf $RPM_BUILD_ROOT

%files -n iceweasel-lang-af
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-af@firefox.mozilla.org.xpi

%files -n iceweasel-lang-ak
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-ak@firefox.mozilla.org.xpi

%files -n iceweasel-lang-ar
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-ar@firefox.mozilla.org.xpi

%files -n iceweasel-lang-as
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-as@firefox.mozilla.org.xpi

%files -n iceweasel-lang-ast
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-ast@firefox.mozilla.org.xpi

%files -n iceweasel-lang-be
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-be@firefox.mozilla.org.xpi

%files -n iceweasel-lang-bg
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-bg@firefox.mozilla.org.xpi

%files -n iceweasel-lang-bn
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-bn-BD@firefox.mozilla.org.xpi

%files -n iceweasel-lang-bn_IN
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-bn-IN@firefox.mozilla.org.xpi

%files -n iceweasel-lang-br
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-br@firefox.mozilla.org.xpi

%files -n iceweasel-lang-bs
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-bs@firefox.mozilla.org.xpi

%files -n iceweasel-lang-ca
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-ca@firefox.mozilla.org.xpi

%files -n iceweasel-lang-cs
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-cs@firefox.mozilla.org.xpi

%files -n iceweasel-lang-csb
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-csb@firefox.mozilla.org.xpi

%files -n iceweasel-lang-cy
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-cy@firefox.mozilla.org.xpi

%files -n iceweasel-lang-da
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-da@firefox.mozilla.org.xpi

%files -n iceweasel-lang-de
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-de@firefox.mozilla.org.xpi

%files -n iceweasel-lang-el
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-el@firefox.mozilla.org.xpi

%files -n iceweasel-lang-en_GB
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-en-GB@firefox.mozilla.org.xpi

%files -n iceweasel-lang-en_US
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-en-US@firefox.mozilla.org.xpi

%files -n iceweasel-lang-en_ZA
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-en-ZA@firefox.mozilla.org.xpi

%files -n iceweasel-lang-eo
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-eo@firefox.mozilla.org.xpi

%files -n iceweasel-lang-es_AR
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-es-AR@firefox.mozilla.org.xpi

%files -n iceweasel-lang-es_CL
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-es-CL@firefox.mozilla.org.xpi

%files -n iceweasel-lang-es
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-es-ES@firefox.mozilla.org.xpi

%files -n iceweasel-lang-es_MX
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-es-MX@firefox.mozilla.org.xpi

%files -n iceweasel-lang-et
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-et@firefox.mozilla.org.xpi

%files -n iceweasel-lang-eu
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-eu@firefox.mozilla.org.xpi

%files -n iceweasel-lang-fa
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-fa@firefox.mozilla.org.xpi

%files -n iceweasel-lang-fi
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-fi@firefox.mozilla.org.xpi

%files -n iceweasel-lang-fr
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-fr@firefox.mozilla.org.xpi

%files -n iceweasel-lang-fy
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-fy-NL@firefox.mozilla.org.xpi

%files -n iceweasel-lang-ga
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-ga-IE@firefox.mozilla.org.xpi

%files -n iceweasel-lang-gd
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-gd@firefox.mozilla.org.xpi

%files -n iceweasel-lang-gl
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-gl@firefox.mozilla.org.xpi

%files -n iceweasel-lang-gu
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-gu-IN@firefox.mozilla.org.xpi

%files -n iceweasel-lang-he
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-he@firefox.mozilla.org.xpi

%files -n iceweasel-lang-hi
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-hi-IN@firefox.mozilla.org.xpi

%files -n iceweasel-lang-hr
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-hr@firefox.mozilla.org.xpi

%files -n iceweasel-lang-hu
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-hu@firefox.mozilla.org.xpi

%files -n iceweasel-lang-hy
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-hy-AM@firefox.mozilla.org.xpi

%files -n iceweasel-lang-id
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-id@firefox.mozilla.org.xpi

%files -n iceweasel-lang-is
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-is@firefox.mozilla.org.xpi

%files -n iceweasel-lang-it
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-it@firefox.mozilla.org.xpi

%files -n iceweasel-lang-ja
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-ja@firefox.mozilla.org.xpi

%files -n iceweasel-lang-kk
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-kk@firefox.mozilla.org.xpi

%files -n iceweasel-lang-kn
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-kn@firefox.mozilla.org.xpi

%files -n iceweasel-lang-ko
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-ko@firefox.mozilla.org.xpi

%files -n iceweasel-lang-ku
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-ku@firefox.mozilla.org.xpi

%files -n iceweasel-lang-lg
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-lg@firefox.mozilla.org.xpi

%files -n iceweasel-lang-lij
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-lij@firefox.mozilla.org.xpi

%files -n iceweasel-lang-lt
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-lt@firefox.mozilla.org.xpi

%files -n iceweasel-lang-lv
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-lv@firefox.mozilla.org.xpi

%files -n iceweasel-lang-mai
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-mai@firefox.mozilla.org.xpi

%files -n iceweasel-lang-mk
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-mk@firefox.mozilla.org.xpi

%files -n iceweasel-lang-ml
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-ml@firefox.mozilla.org.xpi

%files -n iceweasel-lang-mr
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-mr@firefox.mozilla.org.xpi

%files -n iceweasel-lang-nb
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-nb-NO@firefox.mozilla.org.xpi

%files -n iceweasel-lang-nl
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-nl@firefox.mozilla.org.xpi

%files -n iceweasel-lang-nn
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-nn-NO@firefox.mozilla.org.xpi

%files -n iceweasel-lang-nso
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-nso@firefox.mozilla.org.xpi

%files -n iceweasel-lang-or
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-or@firefox.mozilla.org.xpi

%files -n iceweasel-lang-pa
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-pa-IN@firefox.mozilla.org.xpi

%files -n iceweasel-lang-pl
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-pl@firefox.mozilla.org.xpi

%files -n iceweasel-lang-pt_BR
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-pt-BR@firefox.mozilla.org.xpi

%files -n iceweasel-lang-pt
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-pt-PT@firefox.mozilla.org.xpi

%files -n iceweasel-lang-rm
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-rm@firefox.mozilla.org.xpi

%files -n iceweasel-lang-ro
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-ro@firefox.mozilla.org.xpi

%files -n iceweasel-lang-ru
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-ru@firefox.mozilla.org.xpi

%files -n iceweasel-lang-si
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-si@firefox.mozilla.org.xpi

%files -n iceweasel-lang-sk
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-sk@firefox.mozilla.org.xpi

%files -n iceweasel-lang-sl
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-sl@firefox.mozilla.org.xpi

%files -n iceweasel-lang-son
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-son@firefox.mozilla.org.xpi

%files -n iceweasel-lang-sq
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-sq@firefox.mozilla.org.xpi

%files -n iceweasel-lang-sr
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-sr@firefox.mozilla.org.xpi

%files -n iceweasel-lang-sv
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-sv-SE@firefox.mozilla.org.xpi

%files -n iceweasel-lang-ta
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-ta@firefox.mozilla.org.xpi

%files -n iceweasel-lang-ta_LK
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-ta-LK@firefox.mozilla.org.xpi

%files -n iceweasel-lang-te
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-te@firefox.mozilla.org.xpi

%files -n iceweasel-lang-th
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-th@firefox.mozilla.org.xpi

%files -n iceweasel-lang-tr
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-tr@firefox.mozilla.org.xpi

%files -n iceweasel-lang-uk
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-uk@firefox.mozilla.org.xpi

%files -n iceweasel-lang-vi
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-vi@firefox.mozilla.org.xpi

%files -n iceweasel-lang-zh_CN
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-zh-CN@firefox.mozilla.org.xpi

%files -n iceweasel-lang-zh_TW
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-zh-TW@firefox.mozilla.org.xpi

%files -n iceweasel-lang-zu
%defattr(644,root,root,755)
%{iceweaseldir}/extensions/langpack-zu@firefox.mozilla.org.xpi
