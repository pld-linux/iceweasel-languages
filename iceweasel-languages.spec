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
Version:	44.0
Release:	1
License:	MPL v2.0
Group:		I18n
Source0:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ach.xpi
# Source0-md5:	ad4bfc30ad73313cd440a79abe580a05
Source1:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/af.xpi
# Source1-md5:	1bdb81383a7429734e0b90277d43b1f4
Source2:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/an.xpi
# Source2-md5:	51fa9d3b2ca74cf1af97d55a2e28bbb9
Source3:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/az.xpi
# Source3-md5:	0b2410b71f5427aad93a54035b3a6a58
Source4:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ar.xpi
# Source4-md5:	257396e1545cc8926c450bdba839a2ab
Source5:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/as.xpi
# Source5-md5:	d070560bbaf20da20a9c2a3cc5a74d62
Source6:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ast.xpi
# Source6-md5:	6fa00f798f684b8c84b391bb531aa33b
Source7:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/be.xpi
# Source7-md5:	555b62a11e24b8df71e17cad7f523f1a
Source8:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bg.xpi
# Source8-md5:	b1a07bb058302cee3f86ecfba35638f5
Source9:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bn-BD.xpi
# Source9-md5:	6c9b74297cd63862ef19e17efdc92189
Source10:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bn-IN.xpi
# Source10-md5:	39fe34bf21752999592f77b5fcc10dda
Source11:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/br.xpi
# Source11-md5:	7d16a43078b385990fc2255473306058
Source12:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bs.xpi
# Source12-md5:	7d512b7009c013106d4bd1f4fd317ced
Source13:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ca.xpi
# Source13-md5:	8762374312244f00af9e109c1de2b93b
Source14:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/cs.xpi
# Source14-md5:	ddaa560b6d0607f1eef69cc58db99d3b
Source15:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/cy.xpi
# Source15-md5:	788a0693108bebc0b5e393e02c6a5c24
Source16:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/da.xpi
# Source16-md5:	8392330b2f14479cf71c4ea0a2864b4c
Source17:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/de.xpi
# Source17-md5:	0654073f7626e84a07c9f53a41854ad5
Source18:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/dsb.xpi
# Source18-md5:	a35a58618a26037e696fd9930a5901e4
Source19:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/el.xpi
# Source19-md5:	fa97ad18d9824a8ba6ea6a2471c1ce03
Source20:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/en-GB.xpi
# Source20-md5:	2bf3aa0f59697b487e9543a7b9a92c22
Source21:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/en-US.xpi
# Source21-md5:	9aa06cd22eb48160adbbcad236b9ed76
Source22:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/en-ZA.xpi
# Source22-md5:	e2cd6953daa743fcd17c3c4d6c21c21f
Source23:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/eo.xpi
# Source23-md5:	12c0c2374e3fb263525b9e2278e46fb2
Source24:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-AR.xpi
# Source24-md5:	72d1e05ba10bbecd42e98baa087017f7
Source25:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-CL.xpi
# Source25-md5:	ce593eab5d0dc8154544e3ee7e1a8a29
Source26:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-ES.xpi
# Source26-md5:	a7e03197f7fc44ad760d64a477936841
Source27:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-MX.xpi
# Source27-md5:	4b5fc52f41dd7d25686254b20eef8146
Source28:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/et.xpi
# Source28-md5:	f9fc8a10a9bae22378231eca00e0f73d
Source29:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/eu.xpi
# Source29-md5:	a7ac21fbc3ab23f3fbc33b48a21cf5be
Source30:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fa.xpi
# Source30-md5:	268f45c4517d6619c74cf9cfba8d3ce9
Source31:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ff.xpi
# Source31-md5:	01b6e230b4dbdf4f927b899b6cf2d6cf
Source32:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fi.xpi
# Source32-md5:	a797699679f553210e5e64614172c36f
Source33:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fr.xpi
# Source33-md5:	9f30c0591aeb92a83bb5b825d1758435
Source34:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fy-NL.xpi
# Source34-md5:	c88a57354b17558787e8eb9d3843151c
Source35:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ga-IE.xpi
# Source35-md5:	b2081b08285cb0cdc6cf96e291599b23
Source36:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/gd.xpi
# Source36-md5:	379eb1dea120bb0692160fdb52b8854c
Source37:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/gl.xpi
# Source37-md5:	92b48d64bca09a398a3f6b9fba958ce8
Source38:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/gu-IN.xpi
# Source38-md5:	10c7b1f56a950a083151073a3fa42578
Source39:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/he.xpi
# Source39-md5:	7e5d566d88bb1f21dffecc92e785de2f
Source40:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hi-IN.xpi
# Source40-md5:	474ef84d993059b30e04903622495977
Source41:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hr.xpi
# Source41-md5:	fc962f1e23240b910b459a2e48990f89
Source42:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hsb.xpi
# Source42-md5:	e9a5f78a990f1a4520d42b86f173ea5d
Source43:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hu.xpi
# Source43-md5:	ea5af5ae3ae7fe6bb086add3c7cbcf89
Source44:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hy-AM.xpi
# Source44-md5:	267061b29099911ce95a4028315252bc
Source45:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/id.xpi
# Source45-md5:	2dd4255264246f671b23d8ba0585189f
Source46:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/is.xpi
# Source46-md5:	52db1effd30219ef631031b133883449
Source47:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/it.xpi
# Source47-md5:	357e6a7fa931fe640eaa3e54fbebea52
Source48:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ja.xpi
# Source48-md5:	cf7c8a5a0870042b74214f7a5b3e9860
Source49:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/kk.xpi
# Source49-md5:	6e6c61efa4bff26a4e0ed717eea5971d
Source50:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/km.xpi
# Source50-md5:	e976f33ca440a29a61db141ef581fbb1
Source51:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/kn.xpi
# Source51-md5:	724f8589ebac08803baa728f0cd18cd3
Source52:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ko.xpi
# Source52-md5:	147ff5802147d9e25321707a72780184
Source53:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/lij.xpi
# Source53-md5:	9b3a1411956d6d8fb5a26a12f8531bdf
Source54:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/lt.xpi
# Source54-md5:	d4becd651e993729742bea42c4897ad7
Source55:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/lv.xpi
# Source55-md5:	e9b9fde40816d4819f847a5a50d40baa
Source56:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/mai.xpi
# Source56-md5:	4c797b54cc5b3bd41372241b3fe72978
Source57:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/mk.xpi
# Source57-md5:	62ff636d4571cfc3228f17b30542530b
Source58:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ml.xpi
# Source58-md5:	35e78bd6541112a573cb2d955b4acc4a
Source59:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/mr.xpi
# Source59-md5:	8269ab9a10249731f828fea1ca239efc
Source60:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ms.xpi
# Source60-md5:	3b425e1376f57294aef05269b8ed1e1e
Source61:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/nb-NO.xpi
# Source61-md5:	6917b3da4a9005b70cdc8bb0f4fa730b
Source62:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/nl.xpi
# Source62-md5:	937248d9e3305cfc7838fd7e5599f9a6
Source63:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/nn-NO.xpi
# Source63-md5:	9edbf6ddbcde80567240d367aa5fedf8
Source64:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/or.xpi
# Source64-md5:	31e03d903a97a95252849e69be98a544
Source65:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pa-IN.xpi
# Source65-md5:	ac1319ac3742a9a8e9aa3df339d78669
Source66:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pl.xpi
# Source66-md5:	f18e916a391c31737b523ad501210c86
Source67:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pt-BR.xpi
# Source67-md5:	b000b3761359da8c01151363c6ff03ab
Source68:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pt-PT.xpi
# Source68-md5:	ddc931b2ff4b293608984cd7fe040616
Source69:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/rm.xpi
# Source69-md5:	0bf357f1dfa52ae8fa229646f82ed013
Source70:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ro.xpi
# Source70-md5:	e2d2d7afbdbefbbf05bfc677afa8ba5a
Source71:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ru.xpi
# Source71-md5:	fd7baad5f7d39686a2c00d8e25bd41a1
Source72:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/si.xpi
# Source72-md5:	49887cc84ab304770b2bc639e13a36c8
Source73:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sk.xpi
# Source73-md5:	7bb54d35509e8a8147ccf9b408211e55
Source74:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sl.xpi
# Source74-md5:	23cf3a56839c5c044d3a5b08def3422b
Source75:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/son.xpi
# Source75-md5:	917d039633d643cad1ff9c31b1c5774f
Source76:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sq.xpi
# Source76-md5:	2b60380926852cc3ee1a35f1b6f780be
Source77:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sr.xpi
# Source77-md5:	dd47536a19f2b1efe251d91b43c0bd29
Source78:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sv-SE.xpi
# Source78-md5:	903cdfa1e8035b20b4d9d6678172b910
Source79:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ta.xpi
# Source79-md5:	29632ae3da3576f1e62a99909ee70449
Source80:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/te.xpi
# Source80-md5:	f9553854207719751014488de18257eb
Source81:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/th.xpi
# Source81-md5:	3f2ab64219785d4cf25a9336e37a13a1
Source82:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/tr.xpi
# Source82-md5:	e309d50d27302ba8466cc524a6b931fd
Source83:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/uk.xpi
# Source83-md5:	f0fe6f7ae1b66fbb1e5f9e6d20aa46d0
Source84:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/uz.xpi
# Source84-md5:	3fe79dca86d99eb35f4476f41ed02dcb
Source85:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/vi.xpi
# Source85-md5:	be52d869c085fb3655b0180d18161421
Source86:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/xh.xpi
# Source86-md5:	ce9e74e468fcba5f46958abdaabe2817
Source87:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/zh-CN.xpi
# Source87-md5:	ba58836fbf5368aaf9544d145f726204
Source88:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/zh-TW.xpi
# Source88-md5:	39a06a91ed38ab22e464358256820917
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
%setup -qcT %(seq -f '-a %g' 0 88 | xargs)

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
