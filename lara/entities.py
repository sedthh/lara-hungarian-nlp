# -*- coding: UTF-8 -*-

# common intents
def common():
	return {
		"yes"				: [{"stem":"igen"},{"stem":"aha"},{"stem":"ja","affix":["ja","h"]},{"stem":"ok","affix":["é","s","és","sa","ay"],"without":[{"stem":"nem"}]}],
		"no"				: [{"stem":"nem"},{"stem":"ne"},{"stem":"soha"},{"stem":"mégse","affix":["m"]}],
		"hi" 				: [{"stem":"hi","match_at":"start"},{"stem":"hai","match_at":"start"},{"stem":"szia","match_at":"start","affix":["sztok"]},{"stem":"helló","match_at":"start","affix":["ka"]},{"stem":"szervusz","match_at":"start"},{"stem":"szerbusz","match_at":"start"},{"stem":"szevasz","match_at":"start"},{"stem":"hali","match_at":"start","affix":["hó"]},{"stem":"j[oó]\s?(reggelt|napot|est[eé]t)","wordclass":"regex"}],
		"bye" 				: [{"stem":"bye","match_at":"end"},{"stem":"viszlát"},{"stem":"viszont látásra"},{"stem":"jó éj","affix":["t","szakát"]},{"stem":"jóéjt"},{"stem":"jóccakát"},{"stem":"mennem kell"}],
		"thx"				: [{"stem":"kösz","affix":["i","önöm","önjük","önet","ike","csi"]},{"stem":"kössz"},{"stem":"kösszentyű"},{"stem":"thx"},{"stem":"thanks?","wordclass":"regex"}],
		"pls"				: [{"stem":"p+l+[iíea]*[zs]+e*","wordclass":"regex"},{"stem":"l[eé]+c+i+(v+e+s+)?","wordclass":"regex"},{"stem":"l[eé](gy|szel|nn[eé]l).*(kedves|sz[ií](ves)?)","wordclass":"regex"},{"stem":"szeretné(k|m)","wordclass":"regex","without":[{"stem":"(meg)?bocs(i(ka)?|[aá](nat([aá][eé]rt)?|nat[aáo]t?|ss|sson|j?t(ana)?))?","wordclass":"regex"},{"stem":"elnézés","wordclass":"noun","match_stem":False}]},{"stem":"(meg)?k[eé]r(het)?([ln]?[eéi][km]?)","wordclass":"regex","without":[{"stem":"(meg)?bocs(i(ka)?|[aá](nat([aá][eé]rt)?|nat[aáo]t?|ss|sson|j?t(ana)?))?","wordclass":"regex"},{"stem":"elnézés","wordclass":"noun","match_stem":False}]},{"stem":"szeretn[eé]([km]|lek)","wordclass":"regex","without":[{"stem":"(meg)?bocs(i(ka)?|[aá](nat([aá][eé]rt)?|nat[aáo]t?|ss|sson|j?t(ana)?))?","wordclass":"regex"},{"stem":"elnézés","wordclass":"noun","match_stem":False}]}],
		"welks"				: [{"stem":"nincs mit"},{"stem":"(nagyon\s?)?sz[ií]vesen","wordclass":"regex"},{"stem":"ugyan\,?\shag[gy]\w{1,3}","wordclass":"regex"},{"stem":"hag[gy]\w{1,3}\scsak","wordclass":"regex"},{"stem":"sz[aá]momra.+([oö]r[oö]m|megtiszteltet[eé]s)","wordclass":"regex"}],
		"sorry"				: [{"stem":"(meg)?bocs(i(ka)?|[aá](nat([aá][eé]rt)?|nat[aáo]t?|ss|sson|j?t(ana)?))?","wordclass":"regex"},{"stem":"elnézés","wordclass":"noun","match_stem":False},{"stem":"sajnál(om|juk)","wordclass":"regex"}],
		"lol"				: [{"stem":"(h[aei]){2,}h?","wordclass":"regex"},{"stem":"o?(lol)+o?","wordclass":"regex"},{"stem":":-?[Dd]+","wordclass":"regex"},{"stem":"rot?fl","wordclass":"regex"},{"stem":"vicces","without":[{"stem":"nem"}]},{"stem":"nevet(tem|ek|[uü]nk)","wordclass":"regex","without":[{"stem":"nem"}]}],
		"command"			: [{"stem":"keres(s|d)","wordclass":"regex"},{"stem":"mutass(s|d)","wordclass":"regex"},{"stem":"mond(j|d)","wordclass":"regex"},{"stem":"néz(né|ze)?d","wordclass":"regex"},{"stem":"akaro(k|m)","wordclass":"regex"},{"stem":"utas[ií]t\w{1,}","wordclass":"regex"}],
		"question"			: [{"stem":"\?+($|\s\w+)","wordclass":"regex"},{"stem":"([^,][^,\S+]hogy|^hogy)(an)?","wordclass":"regex"},{"stem":"hol"},{"stem":"honnan"},{"stem":"hová"},{"stem":"hány","affix":["an","at","ból"]},{"stem":"mettől"},{"stem":"meddig"},{"stem":"merre"},{"stem":"mennyi","affix":["en","re"]},{"stem":"mi","affix":["t","k","ket","kor","korra","lyen","lyenek","nek","től","kortól","korra","ből","hez","re","vel"]},{"stem":"ki","affix":["t","k","ket","nek","knek","től","ktől","ből","kből","hez","re","kre","vel","kkel"]}],
		"conditional"		: [{"stem":"volna"},{"stem":"lenne"},{"stem":"\w+h[ae]t\w+","wordclass":"regex"}],
		"profanity"			: [{"stem":"(fel|le|meg|rá|ki|be|oda|össze|bele|hozzá)?bas*z+(at)?(hat)?(us|a[dk]?|á[kl]|[aá]?t[aáo][lkm]?|ott|ni|n[aá]n?[dlkm]?|va|meg)?","wordclass":"regex"},{"stem":"fasz","prefix":["ló"],"wordclass":"noun"},{"stem":"fasza","wordclass":"adjective"},{"stem":"geci","wordclass":"noun"},{"stem":"kurva","affix":["élet"],"wordclass":"noun"},{"stem":"hülye","wordclass":"adjective"},{"stem":"pi(n|cs)[aá][dk]?(a?t|nak|ban?|[bt][oó]l|[eé]rt)?","wordclass":"regex"},{"stem":"((bekap(ja?|hato?|n[aái])?d?)|(kap.*be))","wordclass":"regex"}]
	}

# menu commands
def commands():
	return {
		"ok"				: [{"stem":"ye","affix":["s","ah","p"]},{"stem":"igen"},{"stem":"aha"},{"stem":"ja","affix":["ja","h"]},{"stem":"ok","affix":["é","s","és","sa","ay","ézd"],"without":[{"stem":"nem"}]},{"stem":"úgy","without":[{"stem":"nem"}]},{"stem":"így","without":[{"stem":"nem"}]},{"stem":"jó","wordclass":"adjective","without":[{"stem":"nem"}]}],
		"cancel"			: [{"stem":"no","affix":["ne","pe"]},{"stem":"cancel"},{"stem":"ne","affix":["m"]},{"stem":"mégse","affix":["m"]},{"stem":"elvetés"},{"stem":"ál","affix":["lít"],"wordclass":"verb"}],
		"next"				: [{"stem":"next"},{"stem":"tovább"},{"stem":"előre"},{"stem":"még","wordclass":"regex"},{"stem":"more"},{"stem":"continue"},{"stem":"folytat","wordclass":"verb"},{"stem":"folyta[st]+([ao]?d|ni|ás)?","wordclass":"regex"}],
		"back"				: [{"stem":"back"},{"stem":"vissza","affix":["lép","lépés"]},{"stem":"hátra"}],
		"save"				: [{"stem":"save"},{"stem":"ment","wordclass":"verb"},{"stem":"mentés","wordclass":"noun"}],
		"open"				: [{"stem":"open"},{"stem":"nyit","wordclass":"verb"},{"stem":"nyis","match_stem":False,"wordclass":"verb"}],
		"delete"			: [{"stem":"del","affix":["ete"]},{"stem":"töröl","wordclass":"verb"},{"stem":"törlés"}],
		"exit"				: [{"stem":"exit"},{"stem":"quit"},{"stem":"esc","affix":["ape"]},{"stem":"kilép","wordclass":"verb"},{"stem":"l[eé]pj?([eé][dln])?.+ki","wordclass":"regex"}],
		"options"			: [{"stem":"options"},{"stem":"beállít","wordclass":"verb"},{"stem":"[aá]ll[ií]ts.+be","wordclass":"regex"}],
		"menu"				: [{"stem":"menü","prefix":["main","fő","al","legördülő"],"wordclass":"noun"}],
		"login"				: [{"stem":"login"},{"stem":"log in"},{"stem":"belép","prefix":[],"wordclass":"verb"},{"stem":"bejelentkez","prefix":[],"wordclass":"verb"},{"stem":"l[eé]p.+be","wordclass":"regex"},{"stem":"jelentkez.+be","wordclass":"regex"}],
		"logout"			: [{"stem":"logout"},{"stem":"log out"},{"stem":"kilép","prefix":[],"wordclass":"verb"},{"stem":"kijelentkez","prefix":[],"wordclass":"verb"},{"stem":"l[eé]p.+ki","wordclass":"regex"},{"stem":"jelentkez.+ki","wordclass":"regex"}],
		"error"				: [{"stem":"error","wordclass":"noun"},{"stem":"hiba","wordclass":"noun"},{"stem":"rossz","wordclass":"adjective"},{"stem":"nem (siker[uü]lt|j[oó]l?|m[uüű]k[oö]d(ik|[oö]tt)|ment)","wordclass":"regex"}]
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
		"szabolcs-szatmar-bereg": [{"stem":"Szabolcs","wordclass":"noun","affix":["-Szatmár-Bereg"]},{"stem":"Szatmár","wordclass":"noun"},{"stem":"Nyíregyháza","wordclass":"noun"}],"somogy"			: [{"stem":"Somogy","wordclass":"noun"},{"stem":"Kaposvár","wordclass":"noun"}],
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
		"well_done"			: [{"stem":"fasza"},{"stem":"jó","prefix":["kurva"]},{"stem":"király"},{"stem":"ügyes"},{"stem":"sz[eé]p\s(volt|munka)","wordclass":"regex"},{"stem":"ez\s(lesz\s)?az","wordclass":"regex"}],
		"user_love"			: [{"stem":"szeretlek"},{"stem":"szeretsz engem"},{"stem":"tetszek neked"},{"stem":"tetszel nekem","without":[{"stem":"nem"}]},{"stem":"tetszek neked"},{"stem":"szerelmes.+bel[eé]d","wordclass":"regex"},{"stem":"bel[eé]d.+szerettem","wordclass":"regex"}],
		"user_flirting"		: [{"stem":"(mi|milyen|ruha).+van\s+rajtad","wordclass":"regex"},{"stem":"(meg)?(basz|dug)(unk|n[aá]lak)","wordclass":"regex"},{"stem":"sz?ex(e[lt].*)?","wordclass":"regex"}],
		"user_bored"		: [{"stem":"un(atkoz)?(om|unk)","wordclass":"regex"}],
		"user_happy"		: [{"stem":"j[oó](\sa\s)?kedvem(\svan)?","wordclass":"regex","without":[{"stem":"nincs"},{"stem":"nem"}]},{"stem":"jól vagyok","without":[{"stem":"nincs"},{"stem":"nem"}]}],
		"user_sad"			: [{"stem":"j[oó](\sa\s)?kedvem(\svan)?","wordclass":"regex","with":[{"stem":"nincs"},{"stem":"nem"}]},{"stem":"szomorú","wordclass":"adjective","with":[{"stem":"vagyok"}]},{"stem":"nem\s+(vagyok|[eé]rzem).+j[oó]l","wordclass":"regex"}]
	}