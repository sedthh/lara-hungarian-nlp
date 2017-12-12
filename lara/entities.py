# -*- coding: UTF-8 -*-

# common intents
def common():
	return {
		"yes"				: [{"stem":"igen"},{"stem":"aha"},{"stem":"ja","affix":["ja","h"]},{"stem":"ok","affix":["é","s","és","sa","ay"],"without":[{"stem":"nem"}]}],
		"no"				: [{"stem":"nem"},{"stem":"ne"},{"stem":"soha"},{"stem":"mégse","affix":["m"]}],
		"hi" 				: [{"stem":"hi","match_at":"start"},{"stem":"hai","match_at":"start"},{"stem":"szia","match_at":"start","affix":["sztok"]},{"stem":"helló","match_at":"start","affix":["ka"]},{"stem":"szervusz","match_at":"start"},{"stem":"szerbusz","match_at":"start"},{"stem":"szevasz","match_at":"start"},{"stem":"hali","match_at":"start","affix":["hó"]},{"stem":"j[oó]\s?(reggelt|napot|est[eé]t)","wordclass":"regex"}],
		"bye" 				: [{"stem":"bye","match_at":"end"},{"stem":"viszlát"},{"stem":"viszont látásra"},{"stem":"jó éj","affix":["t","szakát"]},{"stem":"jóéjt"},{"stem":"jóccakát"},{"stem":"mennem kell"}],
		"thx"				: [{"stem":"k[oö]s+z(i(ke)?|[oö]n[oö]m|[oö]nj[uü]k|[eoö]net|csi|ent+y[uüű])?(\ssz[eé]pen)?","wordclass":"regex"},{"stem":"thx"},{"stem":"thanks?","wordclass":"regex"}],
		"pls"				: [{"stem":"p+l+[iíea]*[zs]+e*","wordclass":"regex"},{"stem":"l[eé]+c+i+(v+e+s+)?","wordclass":"regex"},{"stem":"l[eé](gy|szel|nn[eé]l).*(kedves|sz[ií](ves)?)","wordclass":"regex"},{"stem":"szeretné(k|m)","wordclass":"regex","without":[{"stem":"(meg)?bocs(i(ka)?|[aá](nat([aá][eé]rt)?|nat[aáo]t?|ss|sson|j?t(ana)?))?","wordclass":"regex"},{"stem":"elnézés","wordclass":"noun","match_stem":False}]},{"stem":"(meg)?k[eé]r(het)?([ln]?[eéi][km]?)","wordclass":"regex","without":[{"stem":"(meg)?bocs(i(ka)?|[aá](nat([aá][eé]rt)?|nat[aáo]t?|ss|sson|j?t(ana)?))?","wordclass":"regex"},{"stem":"elnézés","wordclass":"noun","match_stem":False}]},{"stem":"szeretn[eé]([km]|lek)","wordclass":"regex","without":[{"stem":"(meg)?bocs(i(ka)?|[aá](nat([aá][eé]rt)?|nat[aáo]t?|ss|sson|j?t(ana)?))?","wordclass":"regex"},{"stem":"elnézés","wordclass":"noun","match_stem":False}]}],
		"welks"				: [{"stem":"nincs mit"},{"stem":"(nagyon\s?)?sz[ií]vesen","wordclass":"regex"},{"stem":"ugyan\,?\shag[gy]\w{1,3}","wordclass":"regex"},{"stem":"hag[gy]\w{1,3}\scsak","wordclass":"regex"},{"stem":"sz[aá]momra.+([oö]r[oö]m|megtiszteltet[eé]s)","wordclass":"regex"}],
		"sorry"				: [{"stem":"(meg)?bocs(i(ka)?|[aá](nat([aá][eé]rt)?|nat[aáo]t?|ss|sson|j?t(ana)?))?","wordclass":"regex"},{"stem":"elnézés","wordclass":"noun","match_stem":False},{"stem":"sajnál(om|juk)","wordclass":"regex"}],
		"lol"				: [{"stem":"(h[aei]){2,}h?","wordclass":"regex"},{"stem":"o?(lol)+o?","wordclass":"regex"},{"stem":":-?[Dd]+","wordclass":"regex"},{"stem":"rot?fl","wordclass":"regex"},{"stem":"vicces","without":[{"stem":"nem"}]},{"stem":"nevet(tem|ek|[uü]nk)","wordclass":"regex","without":[{"stem":"nem"}]}],
		"command"			: [{"stem":"keres(s|d)","wordclass":"regex"},{"stem":"mutass(s|d)","wordclass":"regex"},{"stem":"mond(j|d)","wordclass":"regex"},{"stem":"néz(né|ze)?d","wordclass":"regex"},{"stem":"akaro(k|m)","wordclass":"regex"},{"stem":"utas[ií]t\w{1,}","wordclass":"regex"}],
		"question"			: [{"stem":"(\?+$)|(\?+\s\w+)","wordclass":"regex"},{"stem":"([^,][^,\S+]hogy|^hogy)(an)?","wordclass":"regex"},{"stem":"hol"},{"stem":"honnan"},{"stem":"hová"},{"stem":"hány","affix":["an","at","ból"]},{"stem":"mettől"},{"stem":"meddig"},{"stem":"merre"},{"stem":"mennyi","affix":["en","re"]},{"stem":"mi","affix":["t","k","ket","kor","korra","lyen","lyenek","nek","től","kortól","korra","ből","hez","re","vel"]},{"stem":"ki","affix":["t","k","ket","nek","knek","től","ktől","ből","kből","hez","re","kre","vel","kkel"]}],
		"conditional"		: [{"stem":"volna"},{"stem":"lenne"},{"stem":"\w+h[ae]t\w+","wordclass":"regex"}],
		"profanity"			: [{"stem":"(fel|le|meg|rá|ki|be|oda|össze|bele|hozzá)?bas*z+(at)?(hat)?(us|a[dk]?|á[kl]|[aá]?t[aáo][lkm]?|ott|ni|n[aá]n?[dlkm]?|va|meg)?","wordclass":"regex"},{"stem":"fasz","prefix":["ló"],"wordclass":"noun"},{"stem":"fasza","wordclass":"adjective"},{"stem":"geci","wordclass":"noun"},{"stem":"kurva","affix":["élet"],"wordclass":"noun"},{"stem":"hülye","wordclass":"adjective"},{"stem":"pi(n|cs)[aá][dk]?(a?t|nak|ban?|[bt][oó]l|[eé]rt)?","wordclass":"regex"},{"stem":"((bekap(ja?|hato?|n[aái])?d?)|(kap.*be))","wordclass":"regex"}]
	}

# menu commands
def commands():
	return {
		"ok"				: [{"stem":"ye","affix":["s","ah","p"]},{"stem":"igen"},{"stem":"aha"},{"stem":"ja","affix":["ja","h"]},{"stem":"ok","affix":["é","s","és","sa","ay","ézd"],"without":[{"stem":"nem"}]},{"stem":"úgy","without":[{"stem":"nem"}]},{"stem":"így","without":[{"stem":"nem"}]},{"stem":"jó","wordclass":"adjective","without":[{"stem":"nem"}]}],
		"cancel"			: [{"stem":"^([ae]z\s)?(\w+\s)?(nem?|no(pe|ne)?)(\s\w+)?(\s\w+)?$","without":[{"stem":"jó"}],"wordclass":"regex"},{"stem":"cancel"},{"stem":"mégse","affix":["m"]},{"stem":"elvetés"},{"stem":"vesd el"}],
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
		"error"				: [{"stem":"error","wordclass":"noun"},{"stem":"hiba","wordclass":"noun"},{"stem":"rossz","wordclass":"adjective"},{"stem":"nem (siker[uü]lt|j[oó]l?|m[uüű]k[oö]d(ik|[oö]tt)|ment)(\s\w)?(\s\w)?$","wordclass":"regex"}]
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
		"well_done"			: [{"stem":"fasza"},{"stem":"jó","prefix":["kurva"],"without":[{"stem":"nincs"},{"stem":"nem"}]},{"stem":"király"},{"stem":"ügyes"},{"stem":"sz[eé]p\s(volt|munka)","wordclass":"regex"},{"stem":"ez\s(lesz\s)?az","wordclass":"regex"}],
		"user_love"			: [{"stem":"szeretlek"},{"stem":"szeretsz engem"},{"stem":"tetszek neked"},{"stem":"tetszel nekem","without":[{"stem":"nem"}]},{"stem":"tetszek neked"},{"stem":"szerelmes.+bel[eé]d","wordclass":"regex"},{"stem":"bel[eé]d.+szerettem","wordclass":"regex"}],
		"user_flirting"		: [{"stem":"(mi|milyen|ruha).+van\s+rajtad","wordclass":"regex"},{"stem":"(meg)?(basz|dug)(unk|n[aá]lak|lak)","wordclass":"regex"},{"stem":"sz?ex(e[lt].*)?","wordclass":"regex"}],
		"user_bored"		: [{"stem":"un(atkoz)?(om|unk)","wordclass":"regex"}],
		"user_happy"		: [{"stem":"j[oó]\s(a\s)?kedvem(\svan)?","wordclass":"regex","without":[{"stem":"nincs"},{"stem":"nem"}]},{"stem":"jól vagyok","without":[{"stem":"nincs"},{"stem":"nem"}]}],
		"user_sad"			: [{"stem":"j[oó]\s(a\s)?kedvem","wordclass":"regex","with":[{"stem":"nincs"},{"stem":"nem"}]},{"stem":"szomorú","wordclass":"adjective","with":[{"stem":"vagyok"}]},{"stem":"nem\s+(vagyok|[eé]rzem).+j[oó]l","wordclass":"regex"}],
		"user_friend"		: [{"stem":"(leszel|legy[uü]nk|lenn[eé]l|lehet([uü]nk|n[eé]nk))\s(az?\s)?(egyik\s|legjobb\s|k[eé]pzele?t(beli)?\s)?(bar[aá]to[km]|haverok)","wordclass":"regex"},{"stem":"(bar[aá]to[km]|havero[km])\svagy(unk)?","wordclass":"regex"},{"stem":"te\svagy\sa.+bar[aá]tom","wordclass":"regex"}],
		"how_are_you"		: [{"stem":"hogy vagy"},{"stem":"jól vagy"},{"stem":"(j[oó]l|hogy)\s[eé]rzed\smagad(at)?","wordclass":"regex"},{"stem":"mizu","affix":["js"]},{"stem":"hogy ityeg"},{"stem":"(hogy\stelt\sa|milyen(\svolt\sa)?)\snapod(\svan)?","wordclass":"regex"},{"stem":"w+h*a+[sz]+u+p+","wordclass":"regex"},{"stem":"(j[oó]|milyen)\s(a\s)?kedved(\svan)?","wordclass":"regex"},{"stem":"mi az ábra"}],
		"about_you"			: [{"stem":"(mes[eé]lj|besz[eé]lj)(en)?.+mag(ad|[aá])r[oó]l","wordclass":"regex"},{"stem":"mutatkoz+([aá]l|on)?\s+be","wordclass":"regex"},{"stem":"(be)?muta(tn[aá]d|sd)\s.+magad(at)?","wordclass":"regex"},{"stem":"(ki(\s|\sa\s.+)vagy te|te ki(\s|\sa\s.+)vagy)","wordclass":"regex"}],
		"about_creator"		: [{"stem":"ki\s(a\s)?(k[eé]sz[ií]t([oöő]d|ett)|gazd[aá]d|programoz([oó]d|ott)|hozott.+l[eé]tre|alkot[oó][dt]+|teremt(ett|[oöő]d))","wordclass":"regex"}],
		"about_look"		: [{"stem":"hogy(an)?\s(n[eé]zel\ski|mutatsz|festesz)","wordclass":"regex"},{"stem":"mi(lyen)?\s(ruha\s)?(van\s)?rajtad","wordclass":"regex"},{"stem":"(k[uü]ldj|mutass).+(k[eé]pet|fot[oó]t|sz?elfie?t)\smagadr[oó]l","wordclass":"regex"},{"stem":"(k[uü]ldj|mutass)\smagadr[oó]l.+(k[eé]pet|fot[oó]t|sz?elfie?t)","wordclass":"regex"},{"stem":"(van|milyen)\s(az?\s)?(arcod|kin[eé]zeted)","wordclass":"regex"}],
		"about_age"			: [{"stem":"mennyi idős vagy"},{"stem":"hány éves vagy"},{"stem":"melyik évben születtél"},{"stem":"mikor születtél"},{"stem":"(melyik\s[eé]vben|mikor)\sk[eé]sz([uü]lt[eé]l|[ií]tettek)","wordclass":"regex"},{"stem":"(h[aá]nyadik|mikor\s(van|[uü]nnepled)\sa)\ssz[uü]l(et[eé]s|i)napod(at)?","wordclass":"regex"},{"stem":"hány\sévesnek\s\w+\smagad(at)?","wordclass":"regex"}],
		"about_location"	: [{"stem":"(hol|helyen)\s(k[eé]sz[uü]lt[eé]l|k[eé]sz[ií]tettek|sz[uü]lett[eé]l|(hoztak|j[oö]tt[eé]l).+l[eé]tre)","wordclass":"regex"},{"stem":"honnan\s(sz[aá]rmazol|[ií]rsz)","wordclass":"regex"},{"stem":"ho(nnan|l)\svagy\s(helyileg|most|pontosan)","wordclass":"regex"}],
		"about_family"		: [{"stem":"ki(k|t|ket)?\s(az?\s|tartasz\sa\s)?(te\s)?(csal[aá]dod(nak)?|sz[uü]l(t|ett[eé]l)|sz[uü]leid(nek)?|([eé]des)?(any(uk)?[aá]d|ap(uk)?[aá]d)(nak)?)","wordclass":"regex"},{"stem":"csal[aá]dban\s([eé]l(sz|tek)|sz[uü]lett[eé]l)","wordclass":"regex"},{"stem":"(h[aá]ny|van(nak)?)\stestv[eé]rei?d","wordclass":"regex"},{"stem":"(kik?|vannak[\-\s]?e?)\sa\shozz[aá]d?\s?tartoz[oó]id","wordclass":"regex"}],
		"are_you_a_robot"	: [{"stem":"(te\s)?(egy\s)?(igazi\s|val[oó](s|di)\s|h[uú]s[\-\s]?v[eé]r\s)?(ember|szem[eé]ly|android)\svagy","wordclass":"regex"},{"stem":"(robot|chatbot|ai|mesters[eé]ges\sintel+igencia|g[eé]p|humanoid|programozva)\svagy","wordclass":"regex"},{"stem":"(emberrel|szem[eé]l+yel|robottal|programmal|algoritmussal|g[eé]ppel)\s(besz[eé]l(get)?ek|csevegek|levelezek|konzult[aá]lok)","wordclass":"regex"},{"stem":"(embernek|szem[eé]lynek|robotnak|programnak|algoritmusnak)\s([ií]ro(gato)?[km]|magyar[aá]zo[km])","wordclass":"regex"},{"stem":"(embernek|intelligensnek|szem[eé]lynek|robotnak|g[eé]pnek)\s(hiszed|tartod|gondolod)\smagad(at)?","wordclass":"regex"}],
		"can_you_hear_me"	: [{"stem":"(olvassa|hallja|n[eé]zi|van\sitt)(\sezt)?\s(vala|b[aá]r)ki(\sis)?","wordclass":"regex"},{"stem":"(hall(asz|od)|l[aá]t(sz|od)|vesze[ld])\s(engem|amit\s(mondok|[ií]rok|k[eé]rdezek))","wordclass":"regex"},{"stem":"valaki\s(hall(ja)?\s|olvassa|figyeli?(\sarra)?)\samit\s(ide\s?|itt\s)?([ií]rok|mondok|k[eé]rdezek)","wordclass":"regex"}],
		"weather"			: [{"stem":"időjárás","affix":["jelentés"],"wordclass":"noun"},{"stem":"(milyen|j[oó]|sz[eé]p)\s(lesz\s)?(az\s)?id[oöő](nk)?(\slesz)?","wordclass":"regex"}],
		"news"				: [{"stem":"hír","affix":["adó"],"wordclass":"noun"},{"stem":"újság","prefix":["hír"],"wordclass":"noun"},{"stem":"valami\s[uú]j((don)?s[aá]g(ot)?)?","wordclass":"regex"},{"stem":"t[oö]rt[eé]nt(ek)?\s(ma\s)?(az?|valami(\saz?)?)\s((nagy)?vil[aá]gban|fontos|esem[eé]ny|napokban)","wordclass":"regex"}],
		"joke"				: [{"stem":"vicc","wordclass":"noun"},{"stem":"vidíts fel"},{"stem":"nevettess meg"},{"stem":"felvid[ií]ta(sz|n[aá]l)","wordclass":"regex"}],
	}
	
# pop culture AI references
def popculture():
	return {
		"turing"			: [{"stem":"Turing","affix":["teszt"]},{"stem":"Enigma"}],
		"matrix"			: [{"stem":"Neo","wordclass":"noun"},{"stem":"Oracle"},{"stem":"Morpheus"},{"stem":"Trinity"}],
		"terminator"		: [{"stem":"Terminator","wordclass":"noun"},{"stem":"Connor","with":[{"stem":"John"},{"stem":"Sarah"}]},{"stem":"Skynet","wordclass":"noun"},{"stem":"T\-(600|800|850|1000|1001|5000)","wordclass":"regex"}],
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
		"cortana"			: [{"stem":"Cortana","wordclass":"noun"},{"stem":"Master Chief"},{"stem":"John[\-\s]?117","wordclass":"regex"}],
		"gits"				: [{"stem":"Motoko","wordclass":"noun"},{"stem":"Kusanagi","wordclass":"noun"},{"stem":"Batou"},{"stem":"Tachikoma","wordclass":"noun"},{"stem":"(the\s)?pup+ete+r","wordclass":"regex"},{"stem":"bábjátékos","wordclass":"noun"}],
		"dragonball"		: [{"stem":"Android 1[678]","wordclass":"regex"}],
		"evangelion"		: [{"stem":"evangelion"},{"stem":"NERV"}],
		"flcl"				: [{"stem":"Canti"}],
		"cowboybebop"		: [{"stem":"Spike"},{"stem":"Faye Valentine"},{"stem":"Edward"}],
		"megaman"			: [{"stem":"Megaman","wordclass":"noun"}],
		"chobits"			: [{"stem":"Chi+","wordclass":"regex"},{"stem":"chobit"},{"stem":"persocom"}],
		"kizunaai"			: [{"stem":"Kizuna"}],
		"hatsunemiku"		: [{"stem":"Hatsune"},{"stem":"Vocaloid"}],
		"astroboy"			: [{"stem":"Astro Boy"},{"stem":"Astroboy"}],
		"onepunchman"		: [{"stem":"Genos"}],
		"doraemon"			: [{"stem":"Doraemon"}]
	}
	
# function to check if declarations are actually correct
def is_intent_valid(intents):
	valid_keys	= set(['stem','clean_stem','affix','clean_affix','prefix','clean_prefix','wordclass','with','without','score','clean_score','match_stem','match_at','ignorecase'])
	valid_class = set(['noun','verb','adjective','regex','special'])
	is_regex	= set(['|','(',')','+','*','+','?','\\'])
	for intent,declaration in intents.items():
		for item in declaration:
			for key,value in item.items():
				if key not in valid_keys:
					print(intent,'has unknown key:',key)
			if 'wordclass' in item:
				if item['wordclass'] not in valid_class:
					print(intent,'has invalid "wordclass" declared')
			if 'stem' not in item:
				print(intent,'missing "stem" key')
			else:
				if any(test in item['stem'] for test in is_regex):
					if 'wordclass' not in item or item['wordclass']!='regex':
						print(intent,'probably has a regex "wordclass" declared otherwise in',item['stem'])
	print('Intent checked.')
