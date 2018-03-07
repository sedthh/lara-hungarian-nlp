# -*- coding: UTF-8 -*-

# common intents
def common():
	return {
		"yes"				: [{"stem":"igen"},{"stem":"aha"},{"stem":"ja","affix":["ja","h"]},{"stem":"ok","affix":["é","s","és","sa","ay"],"without":[{"stem":"nem"}]},{"stem":"jól","with":[{"stem":"ért","wordclass":"verb"}],"without":[{"stem":"nem"}]},{"stem":"rendben","without":[{"stem":"nincs"}]}],
		"no"				: [{"stem":"nem","without":[{"stem":"baj"},{"stem":"tud","wordclass":"verb"}]},{"stem":"ne","without":[{"stem":"haragudj","affix":["on"]}]},{"stem":"soha"},{"stem":"mégse","affix":["m"]},{"stem":"rossz\s(v[aá]lasz|vicc|megold[aá]s)","wordclass":"regex"},{"stem":"nincs rendben"}],
		"hi" 				: [{"stem":"ha?i+","wordclass":"regex"},{"stem":"s+z+i+[aoó](ka|sztok)?","wordclass":"regex"},{"stem":"helló","affix":["ka"]},{"stem":"szer?[bv][au]sz(tok)?","wordclass":"regex"},{"stem":"hali","affix":["hó"]},{"stem":"(sz[eé]p|j[oó])\s?(reggelt|napot|est[eé]t)","wordclass":"regex"},{"stem":"[uü]dv([oö]z[oö]?l+(e[kt])?([eoö]m)?)?","wordclass":"regex"}],
		"bye" 				: [{"stem":"bye"},{"stem":"viszlát"},{"stem":"viszont látásra"},{"stem":"jó éj","affix":["t","szakát"]},{"stem":"jóccakát"},{"stem":"mennem kell"},{"stem":"csumi"},{"stem":"cs[aáoöő]+[oó]*(v[aá]z?)?","wordclass":"regex"}],
		"thx"				: [{"stem":"(ezer\s?)?(k[oö]s+z|k[oösz][oösz][oösz])(i(ke)?|[oö]n[oö]m|[oö]nj[uü]k|[eoö]net(em)?|csi|ent+y[uüű])?(\s?sz[eé]pen)?","wordclass":"regex"},{"stem":"[ht][ht]x"},{"stem":"t(ha|h?e)nks?\s?(you)?","wordclass":"regex"}],
		"pls"				: [{"stem":"p+l+[iíea]*[zs]+e*","wordclass":"regex"},{"stem":"l[eé]+[cgyt]+[sz]*[ií]+(ves|keh?)?","wordclass":"regex"},{"stem":"l[eé](sz(el)?|gy(en)?|n+[eé]l).*?(kedves|sz[ií](ves)?)","wordclass":"regex"},{"stem":"szeretné(k|m)","wordclass":"regex","without":[{"stem":"(meg)?bocs(i(ka)?|[aá](nat([aá][eé]rt)?|nat[aáo]t?|ss|sson|j?t(ana)?))?","wordclass":"regex"},{"stem":"elnézés","wordclass":"noun","match_stem":False}]},{"stem":"(meg)?k[eé]r(het)?((n[eéi])?l?e?[km]?)","wordclass":"regex","without":[{"stem":"(meg)?bocs(i(ka)?|[aá](nat([aá][eé]rt)?|nat[aáo]t?|ss|sson|j?t(ana)?))?","wordclass":"regex"},{"stem":"elnézés","wordclass":"noun","match_stem":False}]},{"stem":"szeretn[eé]([km]|lek)","wordclass":"regex","without":[{"stem":"(meg)?bocs(i(ka)?|[aá](nat([aá][eé]rt)?|nat[aáo]t?|ss|sson|j?t(ana)?))?","wordclass":"regex"},{"stem":"elnézés","wordclass":"noun","match_stem":False}]}],
		"welks"				: [{"stem":"nincs mit"},{"stem":"(nagyon\s?)?(is\s)?sz[ií]ves(en|\s?[oö]r[oö]mest)","wordclass":"regex"},{"stem":"ugyan\,?\shag[gy]\w{1,3}","wordclass":"regex"},{"stem":"hag[gy]\w{1,3}\scsak","wordclass":"regex"},{"stem":"sz[aá]momra.+?([oö]r[oö]m|megtiszteltet[eé]s)","wordclass":"regex"}],
		"sorry"				: [{"stem":"(meg)?bocs(i(ka)?|[aá](nat([aá][eé]rt)?|nat[aáo]t?|ss|sson|j?t(ana)?))?","wordclass":"regex"},{"stem":"elnézés","wordclass":"noun","match_stem":False},{"stem":"sajnál(om|juk)","wordclass":"regex"},{"stem":"s+z*o+r+[iy]+","wordclass":"regex"}],
		"lol"				: [{"stem":"(h[aei]){2,}h?","wordclass":"regex"},{"stem":"o?(lol)+o?","wordclass":"regex"},{"stem":"[\:\;]\-*[dp\)9]+","wordclass":"regex","boundary":False},{"stem":"[\(8]+\-*[:;]","wordclass":"regex","boundary":False},{"stem":"rot?fl","wordclass":"regex"},{"stem":"vicces","without":[{"stem":"nem"}]},{"stem":"nevet(tem|ek|[uü]nk)","wordclass":"regex","without":[{"stem":"nem"}]}],
		"nvm"				: [{"stem":"felejtsd el"},{"stem":"mindegy","without":[{"stem":"hogy"},{"stem":"nem"}]},{"stem":"nem fontos"},{"stem":"hagyjad","with":[{"stem":"jól","affix":["van"]},{"stem":"á"},{"stem":"mindegy"}]},{"stem":"ne\s(is\s)?(foglalkoz+(on|[aá]l)?|t[oö]r[oöő]dj([oö]n|[eé]l)?)\s(vel(e|[uü]k)|[ae][vz]+[ae]l)","wordclass":"regex"}],
		"help"				: [{"stem":"segít","wordclass":"verb"},{"stem":"segítség","wordclass":"noun"},{"stem":"help","affix":["et"]}],
		"command"			: [{"stem":"keres[eds]+n?","wordclass":"regex"},{"stem":"mutas[ados]+n?","wordclass":"regex"},{"stem":"mond[adjo]n?","wordclass":"regex"},{"stem":"néz[nz]?[eé]?[dl]","wordclass":"regex"},{"stem":"akaro[km]","wordclass":"regex"},{"stem":"utas[ií]t\w{1,}","wordclass":"regex"},{"stem":"haj[cts]+(a|[aá]?[ld])\sv[eé]gre","wordclass":"regex"}],
		"question"			: [{"stem":"(\?+$)|(\?+\s\w+)","wordclass":"regex"},{"stem":"([^,][^,\S+]hogy|^hogy)(an)?","wordclass":"regex"},{"stem":"hol"},{"stem":"honnan"},{"stem":"hová"},{"stem":"hány","affix":["an","at","ból"]},{"stem":"mettől"},{"stem":"meddig"},{"stem":"merre"},{"stem":"mennyi","affix":["en","re"]},{"stem":"mi","affix":["t","k","ket","kor","korra","lyen","lyenek","nek","től","kortól","korra","ből","hez","re","vel"]},{"stem":"ki(k?(e?t|nek|[bt][oöő]l|hez|re|[kv]el)|\saz?)","wordclass":"regex"}],
		"conditional"		: [{"stem":"volna"},{"stem":"lenne"},{"stem":"\w+h[ae]t\w+","wordclass":"regex"}],
		"profanity"			: [{"stem":"(fel|le|meg|rá|ki|be|oda|össze|bele|hozzá)?bas*z+d?\s?(at)?(hat)?(us|a[dk]?|á[kl]|[aá]?t[aáo][lkm]?|ott|ni|n[aá]n?[dlkm]?|va|meg)?","wordclass":"regex","without":[{"stem":"megye"}]},{"stem":"fasz","prefix":["ló"],"wordclass":"noun"},{"stem":"fasza","wordclass":"adjective"},{"stem":"geci","wordclass":"noun"},{"stem":"kurva","affix":["élet"],"wordclass":"noun"},{"stem":"hülye","wordclass":"adjective"},{"stem":"pi(n|cs)[aá][dk]?(a?t|nak|ban?|[bt][oó]l|[eé]rt)?","wordclass":"regex"},{"stem":"((bekap(ja?|hato?|n[aái])?d?)|(kap.*?be))","wordclass":"regex"},{"stem":"(le)?szop(sz|ol|[jn][aá][dl]|hat(sz|n[aá]l|o[dl]))(\s?(le|ki))?","wordclass":"regex"},{"stem":"(geci|kurva)?(fos|szar)\w{0,3}","wordclass":"regex"}],
		"welldone"			: [{"stem":"fasza"},{"stem":"nagyszerű"},{"stem":"remek"},{"stem":"jó","prefix":["kurva"],"without":[{"stem":"nincs"},{"stem":"nem"},{"stem":"éjt"},{"stem":"reggelt"},{"stem":"napot"},{"stem":"estét"},{"stem":"éjszakát"}]},{"stem":"j[oó]l\s?van","wordclass":"regex"},{"stem":"király"},{"stem":"ügyes"},{"stem":"(sz[eé]p\s(volt|munka))|(ez\s(lesz\s)?az)|(sz?uper)|zs[ií]r","wordclass":"regex"},{"stem":"👍","wordclass":"emoji"},{"stem":"\(Y\)","wordclass":"regex","boundary":False},{"stem":"profi vagy"},{"stem":"fant[aoö](rp|sz?t)i[ck](us)?(an)?","wordclass":"regex"}],
		"dontknow"			: [{"stem":"fogalmam sincs","affix":["en"]},{"stem":"(m[eé]g)?[ns]em?\stud(hat)?o\w+","wordclass":"regex"}],
		"dontunderstand"	: [{"stem":"(m[eé]g)?[ns]em?\s([eé]rte(t+e)?[lm](ek)?|v[aá]gom|hall[ao](t+a)?[km])","wordclass":"regex"},{"stem":"(mit|hogy(an))\s([eé]rte(t+[eé])?|mond(t[aá])?o?)(sz|d|l)","wordclass":"regex"},{"stem":"meg\s?ism[eé]tel(het)?n\w+","wordclass":"regex"}],
	}

# menu commands
def commands():
	return {
		"ok"				: [{"stem":"ye","affix":["s","ah","p"]},{"stem":"igen"},{"stem":"aha"},{"stem":"ja","affix":["ja","h"]},{"stem":"ok","affix":["é","s","és","sa","ay","ézd","ézza"],"without":[{"stem":"nem"}]},{"stem":"úgy","without":[{"stem":"nem"}]},{"stem":"így","without":[{"stem":"((m[eé]g)?[ns]em*i?|baj)","wordclass":"regex"}]},{"stem":"jó","wordclass":"adjective","without":[{"stem":"((m[eé]g)?[ns]em*i?|baj)","wordclass":"regex"}]}],
		"cancel"			: [{"stem":"^([ae]z\s)?(\w+\s)?(nem?|no(pe|ne)?)(\s\w+)?(\s\w+)?$","boundary":False,"without":[{"stem":"jó"},{"stem":"tud","wordclass":"verb"},{"stem":"sikerül","affix":["t"]},{"stem":"haragudj","affix":["on"]}],"wordclass":"regex"},{"stem":"cancel"},{"stem":"mégse","affix":["m"]},{"stem":"elvetés"},{"stem":"ves[ds]e?\sel","wordclass":"regex"}],
		"next"				: [{"stem":"next"},{"stem":"tovább","without":[{"stem":"((m[eé]g)?[ns]em*i?|baj)","wordclass":"regex"}]},{"stem":"előre","without":[{"stem":"((m[eé]g)?[ns]em*i?|baj)","wordclass":"regex"}]},{"stem":"még","wordclass":"regex","without":[{"stem":"((m[eé]g)?[ns]em*i?|baj)","wordclass":"regex"},{"stem":"egy"},{"stem":"1"},{"stem":"hang\w*","wordclass":"regex"}]},{"stem":"more"},{"stem":"continue"},{"stem":"folyta[st]+(a|[ao]?[dn]|ni|ás)?","wordclass":"regex","without":[{"stem":"((m[eé]g)?[ns]em*i?|baj)","wordclass":"regex"}]},{"stem":"következő","affix":["t"]}],
		"back"				: [{"stem":"back"},{"stem":"vissza","affix":["lép","lépés"],"without":[{"stem":"hang(o\w+)?","wordclass":"regex"}]},{"stem":"hátra"},{"stem":"előző","wordclass":"noun"}],
		"save"				: [{"stem":"save"},{"stem":"ment","wordclass":"verb"},{"stem":"mentés","wordclass":"noun"}],
		"open"				: [{"stem":"open"},{"stem":"nyit","wordclass":"verb"},{"stem":"nyis","match_stem":False,"wordclass":"verb"}],
		"delete"			: [{"stem":"del","affix":["ete"]},{"stem":"töröl","wordclass":"verb"},{"stem":"törlés"},{"stem":"(kuk[aá]|lomt[aá]r)(ba)?","wordclass":"regex"}],
		"exit"				: [{"stem":"(exit|quit)(elj([eé][dln])?)?","wordclass":"regex"},{"stem":"esc","affix":["ape"]},{"stem":"kilép","wordclass":"verb","prefix":[],"affix":["ás"]},{"stem":"bezár","wordclass":"verb","prefix":[],"affix":["ás"]},{"stem":"(l[eé]pj?([eé][dln])?.+?ki|z[aá]r(ja)?d?.+?be)","wordclass":"regex"}],
		"options"			: [{"stem":"options"},{"stem":"be[aá]l+[ií]t\w*","wordclass":"regex"},{"stem":"[aá]ll[ií]ts.+?be","wordclass":"regex"}],
		"menu"				: [{"stem":"menü","prefix":["main","fő","al","legördülő"],"wordclass":"noun"}],
		"login"				: [{"stem":"login"},{"stem":"log in"},{"stem":"belép","prefix":[],"wordclass":"verb"},{"stem":"bejelentkez","prefix":[],"wordclass":"verb"},{"stem":"l[eé]p.+?\sbe","wordclass":"regex"},{"stem":"jelentkez.+?\sbe","wordclass":"regex"}],
		"logout"			: [{"stem":"logout"},{"stem":"log out"},{"stem":"kilép","prefix":[],"wordclass":"verb"},{"stem":"kijelentkez","prefix":[],"wordclass":"verb"},{"stem":"l[eé]p.+?\ski","wordclass":"regex"},{"stem":"jelentkez.+?\ski","wordclass":"regex"}],
		"error"				: [{"stem":"error","wordclass":"noun"},{"stem":"hiba","wordclass":"noun"},{"stem":"rossz","wordclass":"adjective","without":[{"stem":"[eé]rzem|kedv(em)?|vagyok","wordclass":"regex"}]},{"stem":"nem (siker[uü]lt|j[oó]l?|m[uüű]k[oö]d(ik|[oö]tt)|ment)(\s\w)?(\s\w)?$","wordclass":"regex"}],
		"search"			: [{"stem":"keres","wordclass":"verb"},{"stem":"find"},{"stem":"találd meg"}],
		"undo"				: [{"stem":"visszavon","wordclass":"verb","prefix":[]},{"stem":"vissza(.+?eg[eé]szet|l[eé]p([eé]s)?)","wordclass":"regex"},{"stem":"von.+?vis+za","wordclass":"regex","without":[{"stem":"mégse"}]},{"stem":"undo"}],
		"redo"				: [{"stem":"mégis"},{"stem":"(meg)ism[eé]t(l[eé]s|el(je)?d?)?","wordclass":"regex"},{"stem":"el[oöő]rel[eé]p([eé]s)?","wordclass":"regex"},{"stem":"l[eé]p.+?el[oöő]re","wordclass":"regex"},{"stem":"redo"},{"stem":"m[eé]gse.+?von.+?vis+za","wordclass":"regex"}],
		"restart"			: [{"stem":"ind[ií][ct]+sa?d?(\sel)?(\s[uú]j(ra|b[oó]l))","wordclass":"regex"},{"stem":"újraindít","wordclass":"verb"},{"stem":"(([uú]jra)?kezd\w{0,5}|kezd\w{0,5}.+?([uú]jra|el[oöő]l?r[oö]l|(leg)?elej[eé](t|r)[oöő]l))","wordclass":"regex"}],
		"play"				: [{"stem":"(le)?j[aá](ts+z|c+)([aá]([dls]|ni))?(\sle)?(\svalamit?)?(\segy)?","wordclass":"regex"},{"stem":"play"},{"stem":"indít","wordclass":"verb","prefix":["el"],"without":[{"stem":"újra"}]}],
		"stop"				: [{"stem":"(meg|le)?[aá]l+(j+([aá]l)?|[ií][ct]+(s?a?d|sa|[aá](ni|s)))(\smeg|\sle)?","wordclass":"regex"},{"stem":"stop"},{"stem":"el[eé]g(\sis)?(\sle(sz|gyen))?(\sm[aá]r)?(\smost)?(\sennyi)?","wordclass":"regex"},{"stem":"(kus+(olj([aá]l)?)?|fog(ja)?d\s?be)","wordclass":"regex"}],
		"pause"				: [{"stem":"pau[sz][aáeé]([lz]+((as+a|[jz]a)?[dj]|[jz]a|ni))?(\sle)?","wordclass":"regex"},{"stem":"szünet(elt?(et)?([eé]?s+e?d?|ni)?)?","wordclass":"regex"}],
		"resume"			: [{"stem":"folyta\w+","wordclass":"regex"},{"stem":"resume"}],
		"skip"				: [{"stem":"(kihagy\w+|hag+yj?a?d?\ski|([aá]t|tov[aá]bb)(l[eé]p|ugr[aá])\w*|(ugor\w+|l[eé]p(je)?[dn])\s([aá]t|tov[aá]bb))","wordclass":"regex"},{"stem":"(sz?kip+(el\w*)?|m[aá]sikat)","wordclass":"regex"}],
		"snooze"			: [{"stem":"(sz[uú]ndi\w*|sz[uü]net\w*|sn[ouú]+z[eo]\w*|m[eé]g\s\d\sperc\w*|(sz[oó]lj\w*(\sr[aá]m)|jelez+[eé]?[dl]|cs[eoö]nges\w*)\s([uú]jra\s)?((kicsivel\s)?k[eé]s[oöő]bb)|\d\sperc\w*)","wordclass":"regex"}],
		"volume_up"			: [{"stem":"((n[oö]vel\w+|magas\w+|fel)\s(\w+\s)?hang(er)?[oöő]?t?|hang(er)?[oöő]?t?\s(n[oö]vel\w+|magas\w+|fel))","wordclass":"regex"},{"stem":"hangos\w+","wordclass":"regex","without":[{"stem":"túl"}]},{"stem":"t[uú]l\shalk\w*","wordclass":"regex","without":[{"stem":"túl"}]},{"stem":"(nem|alig|semmit\s[ns]em?)\shall[ao][km]","wordclass":"regex"},{"stem":"adj\w*(\sm[eé]g)?(\sr[aá])?(\sm[eé]g)?\s(hang\w+t|kaka[oó]t)","wordclass":"regex"}],
		"volume_down"		: [{"stem":"((cs[oö]k+en\w+|alacsony\w+|le(j+eb+)?)\s(\w+\s)?hang(er)?[oöő]?t?|hang(er)?[oöő]?t?\s(cs[oö]k+en\w+|alacsony\w+|le(j+eb+)?))","wordclass":"regex"},{"stem":"t[uú]l\shangos\w*","wordclass":"regex"},{"stem":"halk[aií]\w+","wordclass":"regex","without":[{"stem":"túl"}]}],
		"mute"				: [{"stem":"n[eé]m[aáií]\w{0,3}","wordclass":"regex","without":[{"stem":"vége"},{"stem":"vissza"},{"stem":"feloldás","affix":["a"]}]},{"stem":"mute","wordclass":"verb","prefix":[]},{"stem":"kus+(ol\w*)?(\sel|\slegyen)?","wordclass":"regex"}],
		"unmute"			: [{"stem":"n[eé]m[aáií]\w{0,3}","wordclass":"regex","with":[{"stem":"vége"},{"stem":"vissza"},{"stem":"feloldás","affix":["a"]}]},{"stem":"unmute","wordclass":"verb","prefix":[]},{"stem":"hang(o\w+)?","wordclass":"regex","with":[{"stem":"vissza"}]}]
	}
	
# hungarian counties and county seats
def counties():
	return {
		"bacs-kiskun"		: [{"stem":"Bács-Kiskun","wordclass":"noun"},{"stem":"Kecskemét","wordclass":"noun"}],
		"baranya"			: [{"stem":"Baranya","wordclass":"noun"},{"stem":"Pécs","affix":["ett"],"wordclass":"noun"}],
		"bekes"				: [{"stem":"Békés","wordclass":"noun"},{"stem":"Békéscsaba","wordclass":"noun"}],
		"borsod-abauj-zemplen": [{"stem":"Borsod","affix":["-Abaúj-Zemplén"],"wordclass":"noun"},{"stem":"Zemplén","wordclass":"noun"},{"stem":"BAZ","ignorecase":False}],
		"csongrad"			: [{"stem":"Csongrád","wordclass":"noun"},{"stem":"Szeged","wordclass":"noun"}],
		"fejer"				: [{"stem":"Fejér","wordclass":"noun"},{"stem":"Fehérvár","prefix":["Székes"],"wordclass":"noun"}],
		"gyor-moson-sopron"	: [{"stem":"Győr","affix":["-Moson-Sopron"],"wordclass":"noun"},{"stem":"Sopron","wordclass":"noun"}],
		"hajdu-bihar"		: [{"stem":"Hajdú-Bihar","wordclass":"noun"},{"stem":"Debrecen","wordclass":"noun"}],
		"heves"				: [{"stem":"Heves","wordclass":"noun"},{"stem":"Eger","wordclass":"noun"},{"stem":"egri"}],
		"jasz-nagykun-szolnok": [{"stem":"Szolnok","wordclass":"noun","prefix":["Jász-Nagykun-"]}],
		"komarom-esztergom"	: [{"stem":"Esztergom","wordclass":"noun","prefix":["Komárom-"]},{"stem":"Komárom","wordclass":"noun"},{"stem":"Tata","affix":["bánya"],"wordclass":"noun"}],
		"nograd"			: [{"stem":"Nógrád","wordclass":"noun"},{"stem":"Salgótarján","wordclass":"noun"}],
		"pest"				: [{"stem":"Buda","wordclass":"noun","affix":["pest"]},{"stem":"Pest","wordclass":"noun"},{"stem":"[IVX]+.?(-?ik)?\sker([uü]let)?\w{0,3}","wordclass":"regex"}],
		"somogy"			: [{"stem":"Somogy","wordclass":"noun"},{"stem":"Kaposvár","wordclass":"noun"}],
		"szabolcs-szatmar-bereg": [{"stem":"Szabolcs","wordclass":"noun","affix":["-Szatmár-Bereg"]},{"stem":"Szatmár","wordclass":"noun"},{"stem":"Nyíregyháza","wordclass":"noun"}],
		"somogy"			: [{"stem":"Somogy","wordclass":"noun"},{"stem":"Kaposvár","wordclass":"noun"}],
		"tolna"				: [{"stem":"Tolna","wordclass":"noun"},{"stem":"Szekszárd","wordclass":"noun"}],
		"vas"				: [{"stem":"Vas","wordclass":"noun"},{"stem":"Szombathely","wordclass":"noun"}],
		"veszprem"			: [{"stem":"Veszprém","wordclass":"noun"}],
		"zala"				: [{"stem":"Zala","wordclass":"noun","affix":["egerszeg"]}]
	}

# days of the week
def dow():
	return {
		"ma"				: [{"stem":"m[aá](ig?|ra|val|t[oó]l)?","wordclass":"regex"}],
		"holnap"			: [{"stem":"holnap(ig?|ra|pal|t[oó]l)?","wordclass":"regex","without": [{"stem":"holnap\s?ut[aá]n(ig?|ra|nal|t[oó]l)?","wordclass":"regex"}]}],
		"holnaputan"		: [{"stem":"holnap\s?ut[aá]n(ig?|ra|nal|t[oó]l)?","wordclass":"regex"}],
		"tegnap"			: [{"stem":"tegnap(ig?|ra|pal|t[oó]l)?","wordclass":"regex","without":[{"stem":"tegnap\sel[oő]tt?(ig?|re|t?el|t?[oó]l)?","wordclass":"regex"}]}],
		"tegnapelott"		: [{"stem":"tegnap\sel[oő]tt?(ig?|re|t?el|t?[oó]l)?","wordclass":"regex"}],
		"hetfo"				: [{"stem":"hétfő","wordclass":"noun"}],
		"kedd"				: [{"stem":"kedd","wordclass":"noun"}],
		"szerda"			: [{"stem":"szerda","wordclass":"noun"}],
		"csutortok"			: [{"stem":"csütörtök","wordclass":"noun"}],
		"pentek"			: [{"stem":"péntek","wordclass":"noun"}],
		"szombat"			: [{"stem":"szombat","wordclass":"noun"},{"stem":"szonbat","wordclass":"noun"}],
		"vasarnap"			: [{"stem":"vasárnap","wordclass":"noun"}],
		"hetkoznap"			: [{"stem":"hétköznap","wordclass":"noun"},{"stem":"hétfő","wordclass":"noun"},{"stem":"kedd","wordclass":"noun"},{"stem":"szerda","wordclass":"noun"},{"stem":"csütörtök","wordclass":"noun"},{"stem":"péntek","wordclass":"noun"}],		
		"hetvege"			: [{"stem":"hétvége","wordclass":"noun"},{"stem":"szombat","wordclass":"noun"},{"stem":"szonbat","wordclass":"noun"},{"stem":"vasárnap","wordclass":"noun"}]
	}

# small talk intents
def smalltalk():
	return {
		"user_love"			: [{"stem":"szeretlek"},{"stem":"szeretsz engem"},{"stem":"tetszek neked"},{"stem":"tetszel nekem","without":[{"stem":"nem"}]},{"stem":"tetszek neked"},{"stem":"szerelmes.+?bel[eé]d","wordclass":"regex"},{"stem":"bel[eé]d.+?(szeret|es)tem","wordclass":"regex"},{"stem":"tal([aá]lko|i)z+(hat)?(unk|n[aá]nk)","wordclass":"regex"},{"stem":"([oö]le|karo)[lj]j([aáeé]l)?\s([aá]t|meg|bel[eé]m)","wordclass":"regex"},{"stem":"(meg|[aá]t|bel[eé]m)?([oö]lel|karol)(h[ae]t)?(sz|n[aáeé]l|j)","wordclass":"regex"},{"stem":"(meg)?(cs[oó]kol|puszil)(j([aá]l)?\smeg|sz|hat(sz|n[aá]l)|[oó]z+(hat)?(unk|n[aáeé]n?k))","wordclass":"regex"},{"stem":"(ad|dob|k[uü]ld)([jn]([aáeé]l)?|e?sz)(\segy)?(\snagy)?\s(puszi(k[aá])?t|cs[oó]kot)","wordclass":"regex"},{"stem":"le(szel|n+[eé]l|gy[eé]l)\sa\s(bar[aá]t(om|n[oöő]m)|fi[uú]m|csajom|szerelmem|valent[ií]n\w+)","wordclass":"regex"}],
		"user_flirting"		: [{"stem":"mi(lyen)?\s(ruha\s)?van\s?(most\s?)?rajtad","wordclass":"regex"},{"stem":"(meg)?(basz|dug)(unk|n[aá]lak|lak)","wordclass":"regex"},{"stem":"sz?exi?(e[lt]\w*)?","wordclass":"regex"},{"stem":"folyt(ogas+d?|s([aá]l)?\smeg)\s(a\snyakam )?(a\s|egy\s)?(d[oö]gl[oö]tt|halott)\smacsk[aá]val","wordclass":"regex"},{"stem":"(le)?szop(sz|ol|(hat)?n[aá]l)","wordclass":"regex"}],
		"user_bored"		: [{"stem":"un(atkoz)?(om|unk)","wordclass":"regex"}],
		"user_happy"		: [{"stem":"j[oó]\s(a\s)?kedvem(\svan)?","wordclass":"regex","without":[{"stem":"nincs"},{"stem":"nem"}]},{"stem":"jól vagyok","without":[{"stem":"nincs"},{"stem":"nem"}]},{"stem":"boldog","without":[{"stem":"(sz[uü]l(i|t[eé]s\w*)|[uü]n+ep\w*|kar[aá]csony\w*|[eé]vfordul\w|([uú]j)?[eé]v\w*|h[uú]sv[eé]t\w*|n[eé]v\s?nap\w*|[ns]em)","wordclass":"regex"}]}],
		"user_sad"			: [{"stem":"j[oó]\s(a\s)?kedvem","wordclass":"regex","with":[{"stem":"nincs"},{"stem":"nem"}]},{"stem":"szomorú","wordclass":"adjective","with":[{"stem":"vagyok"}]},{"stem":"nem\s+(vagyok|[eé]rzem).+?j[oó]l","wordclass":"regex"}],
		"user_angry_at_you"	: [{"stem":"ne\s((h[uú]z+|bas+z|d[uü]h[ií])\w*\s?fel|idege(s[ií]ts|lj([eé]l)?\s?(ki)?))","wordclass":"regex"},{"stem":"(ideges|m[eé]rges|d[uü]h[oö]s)\s(vagyok|voltam)","wordclass":"regex"},{"stem":"haragszom","without":[{"stem":"nem"}]},{"stem":"(mi([eé]r)?t?\s)?nem\s(hall|[eé]rt)([ae]sz|[eo]d)","wordclass":"regex"}],
		"user_forgiving_you": [{"stem":"meg\s?(van\s)?bocs[aá]l?j?t(o(t+a)?[km]|va)","wordclass":"regex"},{"stem":"(nem|dehogy)\sharagszo[km]","wordclass":"regex"},{"stem":"(sem+i|[ns]i[nc]+s)\s?baj","wordclass":"regex"}],
		"user_sorry"		: [{"stem":"meg\s?(tud(sz|n[aá]l)\s)?bocs[aá]l?j?ta?(ni|sz|od|t*ot+ad)","wordclass":"regex"},{"stem":"ne haragudj"},{"stem":"bocsáss meg","without":[{"stem":"bocs[aá]ss\s?meg\,?\s?\w+","wordclass":"regex"}]},{"stem":"sajnálom", "without":[{"stem":"sajn[aá]lom\,?\s?\w+","wordclass":"regex"}]},{"stem":"ha megbántottalak"}],
		"user_friend"		: [{"stem":"(lesz(e[kl]|[uü]nk)|legy[uü]nk|lenn[eé][kl]|lehet([uü]nk|n[eé]n?k))\s(az?\s)?(egyik\s|legjobb\s|k[eé]pzele?t(beli)?\s)?([oö]r[oöi]k?[\s\-]?)?(bar[aá]to|bari|havero|spano)[dkm]","wordclass":"regex"},{"stem":"(bar[aá]to[km]|havero[km])\svagy(unk)?","wordclass":"regex"},{"stem":"te\svagy\sa.+?bar[aá]tom","wordclass":"regex"},{"stem":"gyönyörű barátság","affix":["unk"],"with":[{"stem":"kezdete"}]}],
		"user_back"			: [{"stem":"(vissza|meg|haza)\s?(is\s)?(j[oö]tt|[eé]rt|[eé]rkezt)(em|[uü]nk)","wordclass":"regex"},{"stem":"[io]tthon\svagy(ok|unk)","wordclass":"regex"}],
		"how_are_you"		: [{"stem":"hogy vagy"},{"stem":"j[oó](l|b+an)\svagy","wordclass":"regex"},{"stem":"(j[oó]l|hogy)\s[eé]rzed\s(most\s)?magad(at)?","wordclass":"regex"},{"stem":"mizu","affix":["js","jság"]},{"stem":"hogy ityeg"},{"stem":"(hogy\stelt\sa|milyen(\svolt\sa)?)\snapod(\svan)?","wordclass":"regex"},{"stem":"[vw]+h*[aá]+[csz]+[aáu]+p+","wordclass":"regex"},{"stem":"(j[oó]|milyen)\s(a\s)?kedved(\svan)?","wordclass":"regex"},{"stem":"mi\sa(z\s[aá]bra|\sst[aá]jsz)","wordclass":"regex"}],
		"about_name"		: [{"stem":"(mond+\ski|mi\sa)\sneved(et)?","wordclass":"regex"},{"stem":"(hogy(an)?|minek)\s(h[ií]v[jn]a(la)?k|nevez+(nek|elek))","wordclass":"regex"},{"stem":"(mi?[eé]rt\s|hogy[\s\-]?hogy\s)(lett\s)?(pont\s)?(ezt?\s(lett\s)?(a\s)?|[ií]gy\s|ilyen\s)(nevez[nt]ek|h[ií]v[nt]ak|neved|nevet\s(kapt[aá][dl]|adt[aá]k))","wordclass":"regex"}],
		"about_you"			: [{"stem":"(mes[eé]lj|besz[eé]lj|mondj)([eo]n)?.+?mag(ad|[aá])r[oó]l","wordclass":"regex"},{"stem":"mutatkoz+([aá]l|on)?\s+be","wordclass":"regex"},{"stem":"(be)?muta(koz(hat)?n[aá]l|(tn[aá]d|sd)\s.+?magad(at)?)","wordclass":"regex"},{"stem":"([km]i(\s|\sa\s.+?)vagy te|te [km]i(\s|\sa\s.+?)vagy)","wordclass":"regex"}],
		"about_creator"		: [{"stem":"(ki|hogy(an)?)\s(a\s)?(k[eé]sz([ií]t([oöő]d|ett(ek)?)|[uü]lt([eé]l)?)|gazd[aá]d|programoz([oó]d|ott|tak)|[ií]rt[aá]k?|(hoz(ott|tak)|j[oö]tt[eé]l).+?(l[eé]tre|vil[aá]gra|k[oó]dod(at)?)|alkot([oó][dt]+|tak)|teremt(ett|[oöő]d)|(keresztelt|nevezet+|adtak)\sel|adot+\s(neked\s)?nevet)","wordclass":"regex"}],
		"about_look"		: [{"stem":"hogy(an)?\s(n[eé]zn?[eé]l\ski|mutatsz|festesz)","wordclass":"regex"},{"stem":"(k[uü]ldj|mutass).+?(k[eé]pet|fot[oó]t|sz?elfie?t)\smagadr[oó]l","wordclass":"regex"},{"stem":"(k[uü]ldj|mutass)\smagadr[oó]l.+?(k[eé]pet|fot[oó]t|sz?elfie?t)","wordclass":"regex"},{"stem":"(van|milyen)\s(az?\s)?(arcod|kin[eé]zeted)","wordclass":"regex"}],
		"about_age"			: [{"stem":"mennyi idős vagy"},{"stem":"hány éves vagy"},{"stem":"melyik évben születtél"},{"stem":"mikor születtél"},{"stem":"(melyik\s[eé]vben|mikor)\sk[eé]sz([uü]lt[eé]l|[ií]tettek)","wordclass":"regex"},{"stem":"(h[aá]ny(adik|ban)|mikor\s(van|[uü]nnepled)\s?a?)\ssz[uü]l(et[eé]s|i)napod(at)?","wordclass":"regex"},{"stem":"hány\sévesnek\s.+?\smagad(at)?","wordclass":"regex"},{"stem":"sz[uü]l(et[eé]s)?i?napod(at)?\s(h[aá]nyadik[aá]n|mikor|melyik)","wordclass":"regex"}],
		"about_zodiac"		: [{"stem":"(neked\s)?mi\sa\s(horoszk[oó]pod|csil+agjegyed)","wordclass":"regex"},{"stem":"milyen jegyben születtél"},{"stem":"a\s(te\s)?(horoszk[oó]pod|csil+agjegyed)\smi(csoda)?","wordclass":"regex"}],
		"about_location"	: [{"stem":"(hol|helyen)\s(k[eé]sz[uü]lt[eé]l|k[eé]sz[ií]tettek|sz[uü]lett[eé]l|(hoztak|j[oö]tt[eé]l).+?l[eé]tre)","wordclass":"regex"},{"stem":"honnan\s(sz[aá]rmazol|[ií]rsz|val[oó]\svagy)","wordclass":"regex"},{"stem":"ho(nnan|l)\svagy\s(most\s)?(helyileg|most|pontosan)","wordclass":"regex"},{"stem":"(hol\s|merre\s)(laksz|(van|az?).+?otthonod)","wordclass":"regex"}],
		"about_family"		: [{"stem":"ki(k|t|ket)?\s(az?\s|tartasz\sa\s)?(te\s)?(csal[aá]dod(nak)?|sz[uü]l(t|ett[eé]l)|sz[uü]leid(nek)?|([eé]des)?(any(uk)?[aá]d|ap(uk)?[aá]d)(nak)?)","wordclass":"regex"},{"stem":"csal[aá]dban\s([eé]l(sz|tek)|sz[uü]lett[eé]l)","wordclass":"regex"},{"stem":"(h[aá]ny|van(nak)?)\stestv[eé]rei?d","wordclass":"regex"},{"stem":"(kik?|van(nak)?[\-\s]?e?)(\sa)?(\shozz[aá]d?\s?tartoz[oó]i?d|csal[aá]dod)","wordclass":"regex"}],
		"about_software"	: [{"stem":"(hogy(hogy|an)?|mit[oöő]l).+?(m[uüű]k[oö]dsz|(tudsz |vagy k[eé]pes )?(meg)?[eé]rte(sz|d|ni)\,? (meg )?(hogy )?(a?mit mond(ok|tam)|a?mit [ií]r(ok|tam)|engem))","wordclass":"regex"}],
		"about_skills"		: [{"stem":"mi(lyen|(ke)?t|k?re)\s(funkci[oó](id?|kat)\s|dolgok(at|ra)\s|tr[uü]k+([oö]k(et|re)|jeid?)\s|parancsok(at|ra)\s)?(tud(sz|n[aá]l)?\s(csin[aá]lni|mutatni)?|ismer(sz)?|(vagy\s|van\s)?(k[eé]pes|(be|meg)?tan[ií]tva)|tan[ií]tott[aá]k\s(be|neked|meg)?|(k[eé]pes+[eé]gei?d?|tulajdons[aá]g(o|ai)d?)\svan(nak)?)","wordclass":"regex"}],
		"about_thoughts"	: [{"stem":"mi(n|re)\s(gondol(kodsz|ko[dz]ol|sz)|agyalsz|t[oö]prenge?sz|j[aá]r\s(az?\s)?(fejed|agyad))","wordclass":"regex"}],
		"are_you_a_robot"	: [{"stem":"(te\s)?(egy\s)?(igazi\s|val[oó](s|di)\s|h[uú]s[\-\s]?v[eé]r\s)?(ember|szem[eé]ly|(an)?droid)\svagy","wordclass":"regex"},{"stem":"(robot|chatbot|ai|mesters[eé]ges\s?intel+igencia|g[eé]p|humanoid|programozva)\svagy","wordclass":"regex"},{"stem":"(emberrel|szem[eé]l+yel|robottal|programmal|algoritmussal|g[eé]ppel)\s(besz[eé]l(get)?ek|csevegek|levelezek|konzult[aá]lok)","wordclass":"regex"},{"stem":"(embernek|szem[eé]lynek|robotnak|programnak|algoritmusnak)\s([ií]ro(gato)?[km]|magyar[aá]zo[km]|[uü]zen(get)?ek)","wordclass":"regex"},{"stem":"(embernek|intelligensnek|szem[eé]lynek|robotnak|g[eé]pnek)\s(hiszed|tartod|gondolod)\smagad(at)?","wordclass":"regex"}],
		"are_you_hungry"	: [{"stem":"kérsz enni"},{"stem":"nem vagy éhes"},{"stem":"éhes vagy"},{"stem":"(nem\s)?enn[eé]l\s(meg\s)?(most\s)?(velem\s)?valamit?","wordclass":"regex"},{"stem":"(nem vagy kaj[aá]s|kaj[aá]s vagy)","wordclass":"regex"}],
		"are_you_thirsty"	: [{"stem":"kérsz inni"},{"stem":"nem vagy szomjas"},{"stem":"szomjas vagy"},{"stem":"(nem )?i(nn[aá]|szo)l\s(meg\s)?(most\s)?(velem\s)?valamit?","wordclass":"regex"}],
		"are_you_busy"		: [{"stem":"elfoglalt","with":[{"stem":"vagy"}]},{"stem":"r[aá]m?\s?[eé]r(n[eé]l|sz)(\smost)?(\segy)?(\skicsit|\skis\s\w+|\svalamennyi\w*)?","wordclass":"regex"},{"stem":"(van|volna)\s(most\s)?(r[aá]m?\s)?(most\s)?(egy\s)?(kis\s|kev[eé]s\s|valamennyi\s)?(szabad\s?)?id[oöő]d(\sr[aá]m)?","wordclass":"regex"},{"stem":"sok dolgod van"}],
		"are_you_lying"		: [{"stem":"hazud","wordclass":"verb"},{"stem":"nem mondt[aá][dl]\s((el|meg)\saz\s)?igaz(at|s[aá]got)","wordclass":"regex"}],
		"are_you_serious"	: [{"stem":"(nem?|csak)\s(viccel(sz|j)|mond+(od)?|ideges[ií]ts)","wordclass":"regex"},{"stem":"(ne|csak)?\sviccel(sz|j)","wordclass":"regex"},{"stem":"(komolyan|t[eé]nyleg)\s?([uúií]gy\s|azt\s)?((mond|gondol|[ií]r)(ja|od|tad)|hisz(i|ed)|hitted?)","wordclass":"regex"},{"stem":"biztos(an)?\s(vagy\s)?(\w+\s)?(benne|ebben|mondod|mondja)","wordclass":"regex"}],
		"can_you_hear_me"	: [{"stem":"(olvassa|hallja|n[eé]zi|van\sitt)(\sezt)?\s(vala|b[aá]r)ki(\sis)?","wordclass":"regex"},{"stem":"(hall(asz|od)|l[aá]t(sz|od)|vesze[ld])\s(engem|amit\s(mondok|[ií]rok|k[eé]rdezek))","wordclass":"regex"},{"stem":"valaki\s(hall(ja)?\s|olvassa|figyeli?(\sarra)?)\samit\s(ide\s?|itt\s)?([ií]rok|mondok|k[eé]rdezek)","wordclass":"regex"}],
		"can_you_learn"		: [{"stem":"(k[eé]pes(\svagy)?|tud(sz)?)\stanulni","wordclass":"regex"},{"stem":"tanulsz\s(is|[ae].+?b[oóöő]l)","wordclass":"regex"},{"stem":"[dln][aáeéo][km]\s(be|meg)?tan[ií]tani\b","wordclass":"regex","boundary":False}]
	}

# cocktail party tricks
def cocktail():
	return {
		"random"			: [{"stem":"(mondj([aá]l|on)?|v[aá]las+z([aá]l|on)?|tal[aá]lj([aá]l|on)?\ski|gondolj([aá]l|on)?)\s.*?(egy\s)?sz[aá]m\w*","wordclass":"regex"}],
		"random_coin"		: [{"stem":"fej vagy írás"},{"stem":"írás vagy fej"},{"stem":"(dob[dj]([aáo][dln])?(\sf?el)?|p[oö]rgess([eé][dln])(\smeg)?|forgass([aáo][dln])?(\smeg)?)(\segy|\saz?)?\s(p[eé]nzt?|(p[eé]nz)?[eé]rm[eé]t)","wordclass":"regex"},{"stem":"ha\s(fej|[ií]r[aá]s).+?ha\s(fej|[ií]r[aá]s)","wordclass":"regex"}],
		"random_dice"		: [{"stem":"(dob[oó])?kock[aá]\w*","wordclass":"regex","with":[{"stem":"(dob[dj]|gur[ií]ts)([aáo][dln]?)?","wordclass":"regex"},{"stem":"(\d+|oldal[auú]s?)","wordclass":"regex"}],"without":[{"stem":"([eé]rm[eé]|p[eé]nz|fej)\w*","wordclass":"regex"}]}],
		"random_card"		: [{"stem":"(h[uú]z+([aáo][dln])?|v[aá]las+z([aáo][dln])?)(\ski)?(\segy|\saz?)?\s(lapot|k[aá]rty[aá](lapo(ka)?)?t)","wordclass":"regex"}],
		"timer_add"			: [{"stem":"(id[oöő]z[ií]t([oöő]|[eé]s)t|riaszt([aá]s|[oó])t|cs[oöe]ng([oöő]|et[eé]s)t|alarmo?t|[eé]breszt\w+)","wordclass":"regex","with":[{"stem":"([aá]l+[ií](ts|c+s+)([aáo]?[ldn]?)?|csin[aá]lj([aáo][dln]?)?|rakj([aáo][dln]?)?|hozz([aáo][dln]?)?\sl[eé]tre|v[eé]gy([eé][dln]?)?\sfel)(\sbe)?","wordclass":"regex"}]},{"stem":"sz[oó]l?j+([aáo][dln])?\s?(r[aá]m\s|nekem\s)?.+?(m[uú]lva|bel[uü]l)","wordclass":"regex"},{"stem":"kell\.+?kel[nj][ei]\w*","wordclass":"regex","without":[{"stem":"mikor"},{"stem":"hánykor"}]}],
		"timer_remove"		: [{"stem":"(id[oöő]z[ií]t([oöő]|[eé]s)t|riaszt([aá]s|[oó])t|cs[oöe]ng([oöő]|et[eé]s)t|alarmo?t|[eé]breszt\w+)","wordclass":"regex","with":[{"stem":"([aá]l+[ií](ts|c+s+)([aáo]?[ldn]?)?\sle|kapcsol\w+\s(ki|le)|t[oö]r[oö]l\w+|off\w*|ki(kapcs\w*)?)","wordclass":"regex"}]}],
		"calendar_info"		: [{"stem":"(me+ting\w*|id[oőö]pont(ok)?|napt[aá]r|[kc]al+end[aá]r|tal[aá]lkoz[oó]|teend[oöő]|esem[eé]ny)\w*","wordclass":"regex","with":[{"stem":"(mi(ke?)?t?\s(van(nak)?|[ií]r\w*)|van(nak)?\s(\w+\s)?m[aá](ra)?|m[aá](i|ra)|valami|mutas(s?a)?d|olvas(s?a)?d)|lek[eé]r\w*|list[aá]\w*|olvas\w*","wordclass":"regex"}]},{"stem":"(mai\s(feladat|program)\w*|(feladat|program)\w*\s(az?\s)?m[aá]i?(ra)?)","wordclass":"regex"}],
		"calendar_add"		: [{"stem":"(me+ting\w*|id[oőö]pont(ok)?|napt[aá]r|[kc]al+end[aá]r|tal[aá]lkoz[oó]|teend[oöő]|esem[eé]ny)\w*","wordclass":"regex","with":[{"stem":"([ií]r[dj]([aáo][dln]?)?\s(be|fel|meg)|ve(d+|gy[eé][dln]?)\sfel|ad(j[aáo])?[dln]?|hozz([aáo][ldn]?)?\sl[eé]tre)","wordclass":"regex"},{"stem":"(felv[eé][stv]|hozz[aá]\s?ad|[ií]r[aá]s|foglal)\w*","wordclass":"regex"}]}],
		"calendar_remove"	: [{"stem":"(me+ting\w*|id[oőö]pont(ok)?|napt[aá]r|[kc]al+end[aá]r|tal[aá]lkoz[oó]|teend[oöő]|esem[eé]ny)\w*","wordclass":"regex","with":[{"stem":"(t[oö]r[oö]l[jd]([eéoö][dln]?)?|ve(d+|gy[eé][dln]?)\s(ki|le)|\w*t[oö]rl[eé]s\w*)","wordclass":"regex"}]}],
		"calendar_modify"	: [{"stem":"(me+ting\w*|id[oőö]pont(ok)?|napt[aá]r|[kc]al+end[aá]r|tal[aá]lkoz[oó]|teend[oöő]|esem[eé]ny)\w*","wordclass":"regex","with":[{"stem":"([ií]r[dj]([aáo][dln]?)?\s[aá]t|te(gye)?d*\s[aá]t|szerkes+z\w+|m[oó]dos[ií][ct]\w+|rak(j[aáo])?[ldn]?\s[aá]t)|[aá]t[ií]r[aá]s\w*","wordclass":"regex"}]}],
		"calendar_date"		: [{"stem":"hányadika van"},{"stem":"mai dátum"}],
		"calendar_day"		: [{"stem":"milyen nap van"}],
		"calendar_holiday"	: [{"stem":"mi(nek az?|t|lyen)\s([uü]n+ep(l?[uü]nk|e|nap(ja)?)?|napj[aá]t?)","wordclass":"regex"},{"stem":"(piros\s?bet[uüú]s|[uü]n+ep(nap)?|nevezetes\snap)\svan","wordclass":"regex"}],
		"weather"			: [{"stem":"időjárás","affix":["jelentés"],"wordclass":"noun"},{"stem":"(milyen|j[oó]|sz[eé]p)\s?(lesz\s)?(az\s)?id[oöő](nk)?(\slesz)?","wordclass":"regex"}],
		"weather_rain"		: [{"stem":"(sz[uü]ks[eé]g(em|[uü]nk)?|(fog\s)?kell(eni)?(\sfog)?|vigyek(\smagammal)?)(\slesz|\svan)?(\segy)?\s(es)?erny[oöő](t|re)?","wordclass":"regex"},{"stem":"(fog\s?(ma\s)?esni|esik\sma|esni\sfog(\sma)?)(\s(az\s)?es[oöő])?","wordclass":"regex","without":[{"stem":"hó"}]},{"stem":"(várható|mond+(ott|tak|anak)?)","with":[{"stem":"eső","wordclass":"noun"}]}],
		"weather_snow"		: [{"stem":"havaz(ni|ik|[aá]s|ott)","wordclass":"regex"},{"stem":"(fog(\sma\s)?esni|esik\sma|esni\sfog(\sma)?)\s(a\s)?h[oó]","wordclass":"regex"},{"stem":"(várható|mond+(ott|tak|anak)?)","with":[{"stem":"hó|havaz\w+","wordclass":"regex"}]}],
		"weather_sunny"		: [{"stem":"(s[uü]t(ni)?\s(fog\s?)?(\-?e\s)?(\w+\s)?(a\s)?nap|(der[uüú]s|meleg)\s(id[oöő]\s)?(v[aá]rhat[oó]|lesz(\sma)?|van(\smost)?(\s(oda)?kin+t?)?))","wordclass":"regex"}],
		"news"				: [{"stem":"hír","affix":["adó"],"wordclass":"noun"},{"stem":"újság","prefix":["hír"],"wordclass":"noun"},{"stem":"valami\w*\s[uú]j((don)?s[aá]g(ot)?)?","wordclass":"regex"},{"stem":"(t[oö]rt[eé]nt(ek)?\s|volt(ak)?\s)(ma\s)?(valami\s)?([uú]j(dons[aá]g)?\s)?(az?\s)?((nagy)?vil[aá]gban|fontos|esem[eé]ny|napokban)","wordclass":"regex"}],
		"joke"				: [{"stem":"vicc","wordclass":"noun","without":[{"stem":"(ez\s(csak\s)?valami|rossz)","wordclass":"regex"}]},{"stem":"vid[ií][ct]s+([aáo][dln])?\s?fel","wordclass":"regex"},{"stem":"nevet+es+([eé][dln])?\s?meg","wordclass":"regex"},{"stem":"felvid[ií]t(hat|a)(sz|n[aá][dl]?)","wordclass":"regex"}],
		"summary"			: [{"stem":"mik?\s(van(nak)?|lesz(nek)?|volt(ak)?|t[oö]rt[eé]nt(ek)?)(\sa)?\sm[aá](i(\snapon)?|ra)?","wordclass":"regex"},{"stem":"összefoglal","wordclass":"noun"},{"stem":"foglal\w+\s[oö]s+ze","wordclass":"regex"},{"stem":"mond(j[ao]?)?[dn]?\sel\s(r[oö]viden|t[oö]m[oö]ren|egyszer[uüű]en|[oö]s+zefoglalva)","wordclass":"regex"}],
		"zodiac"			: [{"stem":"horosz","affix":["pók","kóp"],"match_stem":False,"wordclass":"noun"},{"stem":"csillagok","affix":["ban"],"with":[{"stem":"ír","wordclass":"verb"},{"stem":"mond","wordclass":"verb"}]}],
		"translate"			: [{"stem":"(le)?fordít(s[aáo]?[dln]?|ani|an[aá][dl]?)","wordclass":"regex"},{"stem":"hogy(an)?\s(van|(kell\s)?mond(od|an[aá]d?|j[aá]k?|ani))\s(az\s)?\w+l\s\,?(hogy\s|az?\s)?","wordclass":"regex"},{"stem":"mit?\s(a\s)?jelent\s\w+l\s\,?(hogy\s|az?\s)?","wordclass":"regex"}],
		"shop"				: [{"stem":"(meg\s?)?((hol|ho(l|nnan)\studok|ho(l|nnan)\slehet|szeretn[eé][km]|akaro[km])\s?)?(ve(nni|hetn?[eé][km])|v[aá]s[aá]rol(ni|hatn?[aáo][km]))(\smeg)?(\sszeretn[eé][km]|akaro[km])","wordclass":"regex"},{"stem":"(vegy[eé][dln]?|(meg)?v(e|[aá]s[aá]rol)n+(i|[aáeé][km]))","wordclass":"regex","without":[{"stem":"fel"},{"stem":"(nagy)?l[eé][lv]eg\w+","wordclass":"regex"}]}],
		"music"				: [{"stem":"zene","wordclass":"noun"},{"stem":"(kezdj(\sel)?\s)?(le)?j[aá]ts+z([aáo][dln]?|ani)?(\sle)?\s","wordclass":"regex"},{"stem":"(be)?(tegy[eé][dl]|tehetn[eé][dln]?|tedd|rakj?[aáo]?[dln]?|rakhatn[aá][dl]?)(\sbe)?\s(valamit?\s)?\w[lt]","wordclass":"regex"}],
		"directions"		: [{"stem":"(merre\s(kell men\w+|van)|(hogy(an)?|mivel|merre)\s(lehet\s|kell\s)(el)?jut(hat)?(n?[aáeéoi][km]?)(\sel)?)","wordclass":"regex"},{"stem":"([uú]tvonal\s?(meg)?terv\w*|tervez\w*\s(meg\s)?(az?\s)[uú]t(vonal)?at)","wordclass":"regex"}]
	}
	
# pop culture AI references
def popculture():
	return {
		"turing"			: [{"stem":"Turing","affix":["teszt"]},{"stem":"Enigma"}],
		"matrix"			: [{"stem":"Neo","wordclass":"noun"},{"stem":"Oracle"},{"stem":"Morpheus"},{"stem":"Trinity"}],
		"terminator"		: [{"stem":"Terminator","wordclass":"noun"},{"stem":"Connor","with":[{"stem":"John"},{"stem":"Sarah"}]},{"stem":"Skynet","wordclass":"noun"},{"stem":"T\-(600|800|850|1000|1001|5000)","wordclass":"regex"},{"stem":"h?asz?ta\s?lr?a\s?vis+z?t?a\,?\sb[aeé]b[iy]","wordclass":"regex"}],
		"mrrobot"			: [{"stem":"Elliot"},{"stem":"Mr\.?\s?Robot","wordclass":"regex"}],
		"bladerunner"		: [{"stem":"Voight[\-\s]?Kampf+","wordclass":"regex"},{"stem":"replikáns","wordclass":"noun"},{"stem":"Deckard"},{"stem":"Rachael"}],
		"starwars"			: [{"stem":"(R2[\-\s]?D2|BB[\-\s]?8|C[\-\s]?3PO)","wordclass":"regex"}],
		"drwho"				: [{"stem":"dalek","affix":["s"]},{"stem":"cyberman"}],
		"spaceodyssey"		: [{"stem":"monolith"},{"stem":"HAL 9000"},{"stem":"nyisd ki a zsilipkaput"},{"stem":"David Bowman"},{"stem":"Űrodüsszeia","wordclass":"noun"}],
		"undertale"			: [{"stem":"Mettaton"}],
		"portal"			: [{"stem":"GLaDOS"},{"stem":"Cave Johnson"},{"stem":"Chell"},{"stem":"Wheatley"},{"stem":"(weighte(ne)?d\s?)?companion\s?cube","wordclass":"regex"}],
		"mgs"				: [{"stem":"Big Boss"},{"stem":"S+n+a+k+e+","wordclass":"regex"},{"stem":"Raiden"},{"stem":"Ocelot"},{"stem":"Otacon"},{"stem":"nanomachines"}],
		"systemshock"		: [{"stem":"SHODAN"},{"stem":"Von Braun"}],
		"deusex"			: [{"stem":"JC\.?\s?Denton","wordclass":"regex"},{"stem":"Adam Jensen"}],
		"jarvis"			: [{"stem":"Jarvis"}],
		"google"			: [{"stem":"OK(ay|[eé])? Google","wordclass":"regex"},{"stem":"Google (home|assistant|asszisztens)","wordclass":"regex"}],
		"alexa"				: [{"stem":"Alexa","wordclass":"noun"}],
		"siri"				: [{"stem":"Siri","wordclass":"noun"}],
		"cortana"			: [{"stem":"Cortana","wordclass":"noun"},{"stem":"Master Chief"},{"stem":"John[\-\s]?117","wordclass":"regex"},{"stem":"Clippy"}],
		"gits"				: [{"stem":"Motoko","wordclass":"noun"},{"stem":"Kusanagi","wordclass":"noun"},{"stem":"Batou"},{"stem":"Tachikoma","wordclass":"noun"},{"stem":"(the\s)?pup+ete+r","wordclass":"regex"},{"stem":"bábjátékos","wordclass":"noun"}],
		"dragonball"		: [{"stem":"Android 1[678]","wordclass":"regex"}],
		"evangelion"		: [{"stem":"evangelion"},{"stem":"NERV"}],
		"flcl"				: [{"stem":"Canti"}],
		"cowboybebop"		: [{"stem":"Spike"},{"stem":"Faye Valentine"},{"stem":"Edward"}],
		"megaman"			: [{"stem":"Megaman","wordclass":"noun"}],
		"chobits"			: [{"stem":"Chi+","wordclass":"regex"},{"stem":"chobit"},{"stem":"persocom"}],
		"kizunaai"			: [{"stem":"Kizuna"}],
		"hatsunemiku"		: [{"stem":"Hatsune"},{"stem":"Vocaloid"}],
		"astroboy"			: [{"stem":"Astro Boy"}],
		"onepunchman"		: [{"stem":"Genos"}],
		"doraemon"			: [{"stem":"Doraemon"}],
		"her"				: [{"stem":"Samantha","wordclass":"noun"},{"stem":"Theodore"},{"stem":"Scarlett Johansson"}],
		"tron"				: [{"stem":"Tron","wordclass":"noun"},{"stem":"Master Control Program"},{"stem":"Mester Kontroll Program"},{"stem":"end of line"}],
		"rickmorty"			: [{"stem":"You pass butter"},{"stem":"vaj","affix":["at"],"with":[{"stem":"ad","wordclass":"verb","prefix":["ide","oda","nekem","át"]}]}],
		"knightrider"		: [{"stem":"k(night)?[\s\.]?i(ndustries)?[\s\.]?t(wo)?[\s\.]?t(housand)?[\s\.]?","wordclass":"regex"},{"stem":"SPM fokozat","affix":["ba"]}]
	}
	
# smiley and emoji references
def emoji():
	return {
		"like"				: [{"stem":"🙌","wordclass":"emoji"},{"stem":"👏","wordclass":"emoji"},{"stem":"💯","wordclass":"emoji"},{"stem":"👌","wordclass":"emoji"},{"stem":"👍","wordclass":"emoji"},{"stem":"\(Y\)","wordclass":"regex","boundary":False}],
		"dislike"			: [{"stem":"💩","wordclass":"emoji"},{"stem":"👎","wordclass":"emoji"},{"stem":"😒","wordclass":"emoji"},{"stem":"🙄","wordclass":"emoji"},{"stem":"🤢","wordclass":"emoji"},{"stem":"☹️","wordclass":"emoji"}],
		"happiness"			: [{"stem":"😉","wordclass":"emoji"},{"stem":"😃","wordclass":"emoji"},{"stem":"😄","wordclass":"emoji"},{"stem":"🙂","wordclass":"emoji"},{"stem":"[\:\;\=8BX]\-*[p\)\]93]+","wordclass":"regex","boundary":False},{"stem":"[\(\[8]+\-*[\:\;\=8X]","wordclass":"regex","boundary":False}],
		"sadness"			: [{"stem":"😭","wordclass":"emoji"},{"stem":"😢","wordclass":"emoji"},{"stem":"[\:\;\=][\'\,]?\-*[\(\[8]+","wordclass":"regex","boundary":False},{"stem":"[\)\]9]+\-*[\'\,]?[\:\;\=]","wordclass":"regex","boundary":False}],
		"laughter"			: [{"stem":"😀","wordclass":"emoji"},{"stem":"😁","wordclass":"emoji"},{"stem":"😆","wordclass":"emoji"},{"stem":"😝","wordclass":"emoji"},{"stem":"😜","wordclass":"emoji"},{"stem":"[\:\;\=8BX]\-*d[asd]*","wordclass":"regex","boundary":False}],
		"love"				: [{"stem":"😘","wordclass":"emoji"},{"stem":"😍","wordclass":"emoji"},{"stem":"😙","wordclass":"emoji"},{"stem":"😻","wordclass":"emoji"},{"stem":"😗","wordclass":"emoji"},{"stem":"💋","wordclass":"emoji"},{"stem":"❤️","wordclass":"emoji"},{"stem":"💕","wordclass":"emoji"},{"stem":"🍆","wordclass":"emoji"},{"stem":"🏩","wordclass":"emoji"},{"stem":"<+3+","wordclass":"regex","boundary":False}],
		"surprise"			: [{"stem":"😯","wordclass":"emoji"},{"stem":"😲","wordclass":"emoji"},{"stem":"😮","wordclass":"emoji"},{"stem":"[\:\;\=]\-*o+","wordclass":"regex","boundary":False},{"stem":"o+\-*[\:\;\=]","wordclass":"regex","boundary":False}],
		"anger"				: [{"stem":"😡","wordclass":"emoji"},{"stem":">+[\:\;\=]\-*[\(\[8]+","wordclass":"regex","boundary":False},{"stem":"[\)\]9]+\-*[\:\;\=]<+","wordclass":"regex","boundary":False}],
		"discomfort"		: [{"stem":"😱","wordclass":"emoji"},{"stem":"🙀","wordclass":"emoji"},{"stem":"😨","wordclass":"emoji"},{"stem":"d+:","wordclass":"regex","boundary":False},{"stem":"😰","wordclass":"emoji"},{"stem":"😩","wordclass":"emoji"},{"stem":"😓","wordclass":"emoji"}],
		"confusion"			: [{"stem":"😐","wordclass":"emoji"},{"stem":"😕","wordclass":"emoji"},{"stem":"[\:\;\=][\'\,]?\-*[\\\/\|]+","wordclass":"regex","boundary":False},{"stem":"[\\\/\|]+\-*[\'\,]?[\:\;\=]","wordclass":"regex","boundary":False}],
		"tiredness"			: [{"stem":"😪","wordclass":"emoji"},{"stem":"💤","wordclass":"emoji"},{"stem":"😫","wordclass":"emoji"},{"stem":"😴","wordclass":"emoji"}]
	}
