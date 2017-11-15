# -*- coding: UTF-8 -*-

# common intents
def common():
	return {
		"_negative"		: [{"stem":"nem"},{"stem":"ne"},{"stem":"soha"},{"stem":"mégse","affix":["m"]}],
		"_positive"		: [{"stem":"igen"},{"stem":"aha"},{"stem":"ja","affix":["ja","h"]},{"stem":"ok","affix":["é","s","és","sa","ay"]}],
		"_greeting" 	: [{"stem":"hi","match_at":"start"},{"stem":"hai","match_at":"start"},{"stem":"szia","match_at":"start"},{"stem":"helló","match_at":"start","affix":["ka"]},{"stem":"szervusz","match_at":"start"},{"stem":"szerbusz","match_at":"start"},{"stem":"szevasz","match_at":"start"},{"stem":"hali","match_at":"start","affix":["hó"]},{"stem":"jó napot"},{"stem":"jó reggelt"}],
		"_leaving" 		: [{"stem":"bye","match_at":"end"},{"stem":"szia","match_at":"end"},{"stem":"viszlát"},{"stem":"viszont látásra"},{"stem":"jó éj","affix":["t","szakát"]},{"stem":"jóéjt"},{"stem":"jóccakát"},{"stem":"mennem kell"}],
		"_thanking"		: [{"stem":"kösz","affix":["i","önöm","önjük","önet","ike","csi"]},{"stem":"kössz"},{"stem":"kösszentyű"},{"stem":"thx"},{"stem":"thanks?","wordclass":"regex"}],
		"_command"		: [{"stem":"keres(s|d)","wordclass":"regex"},{"stem":"mutass(s|d)","wordclass":"regex"},{"stem":"mond(j|d)","wordclass":"regex"},{"stem":"szeretné(k|m)","wordclass":"regex"},{"stem":"akaro(k|m)","wordclass":"regex"}],
		"_question"		: [{"stem":"\?+($|\s\w+)","wordclass":"regex"},{"stem":"([^,][^,\S+]hogy|^hogy)(an)?","wordclass":"regex"},{"stem":"hol"},{"stem":"honnan"},{"stem":"hová"},{"stem":"hány","affix":["an","at","ból"]},{"stem":"mettől"},{"stem":"meddig"},{"stem":"merre"},{"stem":"mennyi","affix":["en","re"]},{"stem":"mi","affix":["t","k","ket","kor","korra","lyen","lyenek","nek","től","kortól","korra","ből","hez","re","vel"]},{"stem":"ki","affix":["t","k","ket","nek","knek","től","ktől","ből","kből","hez","re","kre","vel","kkel"]}],
		"_conditional"	: [{"stem":"volna"},{"stem":"lenne"},{"stem":"\w+h[ae]t\w+","wordclass":"regex"}],
		"_profanity"	: [{"stem":"(fel|le|meg|rá|ki|be|oda|össze|bele|hozzá)?bas*z+(at)?(hat)?(us|a[dk]?|á[kl]|[aá]?t[aáo][lkm]?|ott|ni|n[aá]n?[dlkm]?|va|meg)?","wordclass":"regex"},{"stem":"fasz","prefix":["ló"],"wordclass":"noun"},{"stem":"fasza","wordclass":"adjective"},{"stem":"geci","wordclass":"noun"},{"stem":"kurva","affix":["élet"],"wordclass":"noun"},{"stem":"hülye","wordclass":"adjective"},{"stem":"pi(n|cs)[aá][dk]?(a?t|nak|ban?|[bt][oó]l|[eé]rt)?","wordclass":"regex"},{"stem":"((bekap(ja?|hato?|n[aái])?d?)|(kap.*be))","wordclass":"regex"}]
	}
