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
Version:	37.0.2
Release:	1
License:	MPL v2.0
Group:		I18n
Source0:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ach.xpi
# Source0-md5:	0e7586ffb36d7a2b106b7cb4dd91e0a2
Source1:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/af.xpi
# Source1-md5:	b04ce63911bc8feab2fb6bb00668aec9
Source2:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/an.xpi
# Source2-md5:	d0bffa74c157c899b87abe33d6c7c809
Source3:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/az.xpi
# Source3-md5:	ba7000fa775133dbf734223343bcefa5
Source4:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ar.xpi
# Source4-md5:	1111cf370263a2dee96d52938ce93d2c
Source5:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/as.xpi
# Source5-md5:	f4914a52783f5c091641c9f245cfdf51
Source6:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ast.xpi
# Source6-md5:	ae299df51cb0719aba9c79f8122bdc4a
Source7:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/be.xpi
# Source7-md5:	84e2772041cc8b49f7876e54d8cbc9dd
Source8:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bg.xpi
# Source8-md5:	1b1988c2f1bb62144c5bdb338bb6c929
Source9:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bn-BD.xpi
# Source9-md5:	adbdc8cf9df3f83cf3b431c4c51fc574
Source10:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bn-IN.xpi
# Source10-md5:	6078480ac3f39ce8bd64433baccd8b90
Source11:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/br.xpi
# Source11-md5:	e4cf1506a3d4bcd766a1df1f2f2d38a9
Source12:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bs.xpi
# Source12-md5:	26dcecd9d2dbd28680d9ee01d4781ec7
Source13:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ca.xpi
# Source13-md5:	916b6923ea9e5d6fe113d43c8d2288b0
Source14:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/cs.xpi
# Source14-md5:	8a655e0d3cf3cc1e54a42002623de1cb
Source15:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/cy.xpi
# Source15-md5:	87bd63cc9dd5af7b898dcbfe5e2de957
Source16:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/da.xpi
# Source16-md5:	7fb185c14369f350fee9588312076ab7
Source17:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/de.xpi
# Source17-md5:	067f52aea446ac42ba7c1ba0458c1829
Source18:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/dsb.xpi
# Source18-md5:	91a67c0f5d6c8855ea0543c7fc66e7dc
Source19:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/el.xpi
# Source19-md5:	d4c1a9b2cc125c8c25b823fece19a3d7
Source20:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/en-GB.xpi
# Source20-md5:	7a66dd6fb6bf86d699e071c57fcf070a
Source21:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/en-US.xpi
# Source21-md5:	73ec7efd654425c65fbf99e5c2ed5f3f
Source22:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/en-ZA.xpi
# Source22-md5:	36c51377854b13b93ae1dcc9c0453ee7
Source23:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/eo.xpi
# Source23-md5:	ba7eaf4f0fc47fc55ba0c73db92c4d0d
Source24:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-AR.xpi
# Source24-md5:	04977820cedf6ec3b5cceefb00a349a9
Source25:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-CL.xpi
# Source25-md5:	f8832d8f4c6b7ab14f378a1b066e6ee8
Source26:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-ES.xpi
# Source26-md5:	d704eecfb09f7b71a6fceb5c4b336fa3
Source27:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-MX.xpi
# Source27-md5:	0cfcac2fdbf74b484b0a04b8bd2eb131
Source28:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/et.xpi
# Source28-md5:	2c578a7a485c15b036fee59731218dc8
Source29:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/eu.xpi
# Source29-md5:	f90d31cbd32b987713a6c740ea10e942
Source30:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fa.xpi
# Source30-md5:	9ae7ae89a12c7e5839bf9e1c80fe676a
Source31:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ff.xpi
# Source31-md5:	e710285fd8b243557afc6cc63a541bc4
Source32:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fi.xpi
# Source32-md5:	59637788e1c2f8bf9847c0148967a1fa
Source33:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fr.xpi
# Source33-md5:	e5cb6ab6be1ef256dc698f2b8319691d
Source34:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fy-NL.xpi
# Source34-md5:	2810b85dbae2eb36d2996a75eeb54fd4
Source35:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ga-IE.xpi
# Source35-md5:	5d24dac81f408f1682c5485f451f33b8
Source36:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/gd.xpi
# Source36-md5:	df3730adb7835a61e71726725c7cc712
Source37:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/gl.xpi
# Source37-md5:	82a7bd027c129f73b396aff219a7cd46
Source38:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/gu-IN.xpi
# Source38-md5:	bdced696b2e1d1e6a83f119eb9af3c2c
Source39:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/he.xpi
# Source39-md5:	9d2a335c3a7d59e212d90e39a5ec96f1
Source40:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hi-IN.xpi
# Source40-md5:	4195d0f35078534318a5de97a3716c22
Source41:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hr.xpi
# Source41-md5:	20e3fc355e07cb04b5b59e28400636b4
Source42:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hsb.xpi
# Source42-md5:	c5b2fed146db979e449df89ee0908cd4
Source43:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hu.xpi
# Source43-md5:	6266422c2d69cc84033d540fe52a9192
Source44:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hy-AM.xpi
# Source44-md5:	f4c00551a5c1ee4a8c71fc12b0bc680b
Source45:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/id.xpi
# Source45-md5:	46b057d26990894bfa94cdb9a20ebc82
Source46:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/is.xpi
# Source46-md5:	b3f9bea2fa39fbc56e5972b281c78ca4
Source47:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/it.xpi
# Source47-md5:	34002e4b7736f91b463ba753645f286c
Source48:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ja.xpi
# Source48-md5:	133a54a10521d39aed2803bc18c1603b
Source49:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/kk.xpi
# Source49-md5:	09a1f2fdc1cbafe56e21944fb4fcb908
Source50:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/km.xpi
# Source50-md5:	2ef7b6d810c9714dcd6192fdb84d0644
Source51:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/kn.xpi
# Source51-md5:	13a18d41075350c31583b13f07874417
Source52:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ko.xpi
# Source52-md5:	0b7cd6fa7436a73a29d239a995a55b78
Source53:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/lij.xpi
# Source53-md5:	6d7bf009d4595e310976e03c13ba4562
Source54:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/lt.xpi
# Source54-md5:	b30dd18714509f43230c7988da5c8bc3
Source55:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/lv.xpi
# Source55-md5:	819215bee1a14d9c72c9a5fae948de92
Source56:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/mai.xpi
# Source56-md5:	f1996827cc45ac53a12e7757f89b7c65
Source57:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/mk.xpi
# Source57-md5:	a393c506876f0ef0642fc66e883c5d46
Source58:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ml.xpi
# Source58-md5:	170d93c88738f1fed690d9cd3b99f9f7
Source59:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/mr.xpi
# Source59-md5:	c96a91446ce6c2a80008785d66343e0c
Source60:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ms.xpi
# Source60-md5:	040c5a58d14ccaa1980fd67bcb9d3d8e
Source61:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/nb-NO.xpi
# Source61-md5:	2c1d15ca024bcc77ff97457e6b273337
Source62:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/nl.xpi
# Source62-md5:	8c987131a903981427e1d9b27a432091
Source63:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/nn-NO.xpi
# Source63-md5:	23bf859b5515ad8f04948d9e8e3ee431
Source64:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/or.xpi
# Source64-md5:	99e6b8c619d4744c24302c6f84f7254f
Source65:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pa-IN.xpi
# Source65-md5:	4692f97b0b1b3dfc80bee1299533c1bd
Source66:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pl.xpi
# Source66-md5:	26cb54f76823da9308f5222ca2d89109
Source67:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pt-BR.xpi
# Source67-md5:	f09ac6ab10119980bf461fc037321743
Source68:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pt-PT.xpi
# Source68-md5:	d78df68dadc9c26c1dba3c093e42e9a4
Source69:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/rm.xpi
# Source69-md5:	a194d3e110b35acc07692e528b5ef56e
Source70:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ro.xpi
# Source70-md5:	c75161e8c31d0090744176e088a3de46
Source71:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ru.xpi
# Source71-md5:	2595a1b0d44e3f43a0aa3a5c3170c288
Source72:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/si.xpi
# Source72-md5:	039e32d2a03751bdb733d4144908b352
Source73:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sk.xpi
# Source73-md5:	b87e693e184abd16b328e86372250502
Source74:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sl.xpi
# Source74-md5:	e43fd5c7f3779541b33aa4525c565ec1
Source75:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/son.xpi
# Source75-md5:	fef81024bbbead76bb9f80fd387e8d89
Source76:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sq.xpi
# Source76-md5:	0d6612f8aabc4054c480329071a97b50
Source77:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sr.xpi
# Source77-md5:	2b63058a9012b8921aab4af863ec15be
Source78:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sv-SE.xpi
# Source78-md5:	df8f34295bc1e9f8973bcc058bd0395b
Source79:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ta.xpi
# Source79-md5:	4c538d560cfae51b3dcc50572e4d9b72
Source80:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/te.xpi
# Source80-md5:	fee2e8f163dd46f7cd0e707664511483
Source81:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/th.xpi
# Source81-md5:	924a7e577eaca0ab00067bd7b0da8c44
Source82:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/tr.xpi
# Source82-md5:	7d08dacf83c27c9d4b22834279692e45
Source83:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/uk.xpi
# Source83-md5:	c8510bfb4cbd07435aa55124ce2c93ed
Source84:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/uz.xpi
# Source84-md5:	d1306fccceb6573a1f4e6bec44872ce8
Source85:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/vi.xpi
# Source85-md5:	1538962183649263133a84790baa2def
Source86:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/xh.xpi
# Source86-md5:	ef0c3b7f321f2edad619eb0bb474854f
Source87:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/zh-CN.xpi
# Source87-md5:	6ca1361ae382d89a8901da91eaf52da0
Source88:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/zh-TW.xpi
# Source88-md5:	f9ba03b830064cc95badb94c11bbc89f
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
