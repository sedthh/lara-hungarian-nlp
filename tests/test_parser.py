# -*- coding: UTF-8 -*-

import pytest
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from lara import nlp, parser

@pytest.mark.parametrize("intents,text,match", [
	(	
		[
			{
				"alma"			: [{"stem":"alma","wordclass":"noun"}],
				"szed"			: [{"stem":"szed","wordclass":"verb"}]
			},
			{
				"piros"			: [{"stem":"piros","wordclass":"adjective"}]
			},
			{
				"zold"			: [{"stem":"zöld","wordclass":"adjective"}]
			}
		],
		[
			"Már a zöld almákat is szedjem le, vagy cask a pirosakat?",
			"Már a zöld almákat is szedjem le, vagy cask a pirosakat?",
			"Már a zöld almákat is szedjem le, vagy cask a pirosakat?",
			"Már a zöld almákat is szedjem le, vagy cask a pirosakat?"
		],
		[
			{'alma': 1, 'szed': 2},
			{'alma': 1, 'szed': 2, 'piros': 2},
			{'alma': 1, 'szed': 2, 'piros': 2, 'zold': 2},
			{'alma': 1, 'szed': 2, 'piros': 2, 'zold': 2}
		]
	),
])
def test_parser_intents_add(intents,text,match):
	test	= []
	test.append(parser.Intents(intents[0]))
	test.append(test[0]+parser.Intents(intents[1]))
	test.append(test[1]+intents[2])
	test.append(parser.Intents(str(test[2]),True))
	for i in range(len(text)):
		result	= test[i].match(text[i])
		assert match[i] == result
		
@pytest.mark.parametrize("intent,text,match", [
    (	
		{
			"alma"			: [{"stem":"alma","wordclass":"noun"}],
			"szed"			: [{"stem":"szed","wordclass":"verb"}],
			"piros"			: [{"stem":"piros","wordclass":"adjective"}]
		},
		[
			"Mikor szedjük le a pirosabb almákat?"
		],
		[
			{'alma': 1, 'szed': 2, 'piros': 2}
		]
	),
	(
		{
			"to_do"			: [{"stem":"csinál","wordclass":"verb"}],
		},
		[
			"Ő mit csinál a szobában?",
			"Mit fogok még csinálni?",
			"Mikor csináltad meg a szekrényt?",
			"Megcsináltatták a berendezést.",
			"Teljesen kicsinálva érzem magamat ettől a melegtől.",
			"Csinálhatott volna mást is.",
			"Visszacsinalnad az ekezeteket a billentyuzetemen, kerlek?"
		],
		[
			{'to_do': 2},
			{'to_do': 2},
			{'to_do': 2},
			{'to_do': 2},
			{'to_do': 2},
			{'to_do': 2},
			{'to_do': 1}
		]
	),
	(
		{
			"palyaudvar"	: [{"stem":"pályaudvar","wordclass":"noun","prefix":["busz"]}],
			"auto"			: [{"stem":"autó","wordclass":"noun","affix":["busz"]}],
			"szinten_jo"	: [{"stem":"pálya","wordclass":"noun","prefix":["busz"],"affix":["udvar"]}]
		},
		[
			"Lassan beérünk az autóval a pályaudvarra.",
			"Lassan beérünk az autóbusszal a buszpályaudvarra."
		],
		[
			{'palyaudvar': 2, 'auto': 2, 'szinten_jo': 2},
			{'palyaudvar': 2, 'auto': 1, 'szinten_jo': 2}
		]
	),
	(
		{
			"enni"		: [{"stem":"esz","wordclass":"verb","match_stem":False},{"stem":"en","wordclass":"verb","match_stem":False}]
		},
		[
			"Tőmorfémák: esz, en.",
			"Eszel valamit?",
			"Azt nem lehet megenni."
		],
		[
			{},
			{'enni': 2},
			{'enni': 2}
		]	
	),
	(
		{
			"jo_ido"	: [{"stem":"jó","wordclass":"adjective","inc":[{"stem":"idő","wordclass":"noun","affix":["járás"]},{"stem":"meleg","wordclass":"adjective"}]}]
		},
		[
			"Jó.",
			"Meleg van.",
			"Milyen az időjárás?",
			"Jó meleg van.",
			"Jó az idő.",
			"Jó meleg az idő.",
			"Jó meleg az időjárás."
		],
		[
			{},
			{},
			{},
			{'jo_ido': 2},
			{'jo_ido': 2},
			{'jo_ido': 4},
			{'jo_ido': 4}
		]
	),
	(
		{
			"jobb_ido"	: [{"stem":"jó","wordclass":"adjective",
							"inc":[{"stem":"idő","wordclass":"noun","affix":["járás"]},{"stem":"meleg","wordclass":"adjective"}],
							"exc":[{"stem":"este","wordclass":"noun"}]}]
		},
		[
			"Jó.",
			"Jó meleg az időjárás.",
			"Jó estét!",
			"Jó meleg esténk van!"
		],
		[
			{},
			{'jobb_ido': 4},
			{},
			{}
		]
	),
	(
		{
			"megszerel"	: [{"stem":"szerel","wordclass":"verb"}],
			"hibasan"		: [{"stem":"alma","wordclass":"noun"}],
		},
		[
			"Gyönyörű dolog a szerelem",
			"Ezt is elfogadja találatként: Almainüdböz"
		],
		[
			{'megszerel': 2},
			{'hibasan': 2}
		]
	),
	(
		{
			"float"		: [{"stem":"a","score":.75},{"stem":"b","score":.6,"typo_score":1}],
		},
		[
			"a b c"
		],
		[
			{'float': 3.1},
		]
	),
])
def test_parser_intents_match(intent,text,match):
	test	= parser.Intents(intent)
	for i in range(len(text)):
		result	= test.match(text[i])
		assert match[i] == result

@pytest.mark.parametrize("intent,text,match", [
	(
		{
			"change"	: [{"stem":"szép","wordclass":"adjective"}],
			"typo"		: [{"stem":"görbe","wordclass":"adjective"}],
			"fail"			: [{"stem":"kék","wordclass":"adjective"}]
		},
		[
			"Szebb sárga bögre göbre bögre."
		],
		[
			['change','typo']
		]
	),
	(
		{
			"capital"		: [{"stem":"NAGY","wordclass":"adjective","ignorecase":False}],
			"lower"		: [{"stem":"kicsi","wordclass":"adjective","ignorecase":False}],
			"any"			: [{"stem":"VáLtAkOzÓ","wordclass":"adjective","ignorecase":True}],
			"acr"			: [{"stem":"KFT","ignorecase":False}]
		},
		[
			"legesLEGNAGYobb kicsiNEK vÁlTaKoZó szöveg kft"
		],
		[
			['capital','lower','any']
		]
	),
	(
		{
			"szoto"		: [{"stem":"töv","wordclass":"noun","match_stem":False,"prefix":["szó"]}],
			"ragoz"		: [{"stem":"ragozatlan","wordclass":"adjective","match_stem":False}],
			"talal"		: [{"stem":"talál","wordclass":"verb","match_stem":False}],
			"talan"		: [{"stem":"TALÁN","wordclass":"verb","match_stem":False,"ignorecase":False}]
		},
		[
			"SZÓTÖVEK SZÓTÖVEK SZÓTÖVEK",
			"Szótövet RAGOZATLANUL nem talál meg. TALÁN így?",
			"Ebben semmi sincs"
		],
		[
			['szoto'],
			['szoto','ragoz'],
			[]
		]
	)
])
def test_parser_intents_match_set(intent,text,match):
	test	= parser.Intents(intent)
	for i in range(len(text)):
		result	= test.match_set(text[i])
		assert set(match[i]) == result

@pytest.mark.parametrize("intent,text,best", [
	(	
		{
			"kave"			: [{"stem":"kávé","wordclass":"noun","affix":["gép"]}],
			"takarit"			: [{"stem":"takarít","wordclass":"verb"}],
			"sehol"			: [{"stem":"sehol"}]
		},
		[
			"Valakinek ki kellene takarítani a kávégépet. Tegnap is én takarítottam ki.",
			"Kávé kávét kávénk kávém. Takarít.",
			"Kávé kávét kávénk kávém. Takarít."
		],
		[
			{'takarit': 4},
			{'kave': 8, 'takarit': 2},
			{'kave': 8, 'takarit': 2}
		]
	),
])
def test_parser_intents_match_best(intent,text,best):
	test	= parser.Intents(intent)
	for i in range(len(text)):
		result	= test.match_best(text[i],i+1)
		assert best[i] == result

@pytest.mark.parametrize("intent,text,best", [
	(	
		{
			"kave"			: [{"stem":"kávé","wordclass":"noun","affix":["gép"]}],
			"takarit"			: [{"stem":"takarít","wordclass":"verb"}],
			"sehol"			: [{"stem":"sehol"}]
		},
		[
			"Valakinek ki kellene takarítani a a tudod mit. Tegnap is én takarítottam ki.",
			"Kávé kávét kávénk kávém. Takarít.",
		],
		[
			{'kave': 0, 'takarit': 4, 'sehol': 0},
			{'kave': 8, 'takarit': 2, 'sehol': 0},
		]
	),
])
def test_parser_intents_match_zeros(intent,text,best):
	test	= parser.Intents(intent)
	for i in range(len(text)):
		result	= test.match(text[i],True)
		assert best[i] == result
		
@pytest.mark.parametrize("intents,text,cleaned", [
	(
		[
			{
				"thanks"	: [{"stem":"köszön","wordclass":"verb"}]
			},
			{
				"thanks"	: [{"stem":"köszön","wordclass":"verb","exc":[{"stem":"szép","wordclass":"adjective"}]}]
			},
			{
				"thanks"	: [{"stem":"köszön","wordclass":"verb","inc":[{"stem":"nagy","wordclass":"adjective"}]}]
			},
			{
				"thanks"	: [{"stem":"köszön","wordclass":"verb","inc":[{"stem":"kicsi","wordclass":"adjective"}]}]
			},
			{
				"thanks"	: [{"stem":"köszön","wordclass":"verb","inc":[{"stem":"nagy","wordclass":"adjective"}],"exc":[{"stem":"szép","wordclass":"adjective"}]}]
			}
		],
		[
			"Nagyon szépen köszönöm a teszteket!",
			"Nagyon szépen köszönöm a teszteket!",
			"Nagyon szépen köszönöm a teszteket!",
			"Nagyon szépen köszönöm a teszteket!",
			"Nagyon szépen köszönöm a teszteket!"
		],
		[
			"Nagyon szépen a teszteket!",
			"Nagyon szépen köszönöm a teszteket!",
			"Nagyon szépen a teszteket!",
			"Nagyon szépen köszönöm a teszteket!",
			"Nagyon szépen köszönöm a teszteket!"
		]
	)
])
def test_parser_intents_clean(intents,text,cleaned):
	for i in range(len(intents)):
		test	= parser.Intents(intents[i])
		result	= nlp.trim(test.clean(text[i]))
		assert cleaned[i] == result
		
@pytest.mark.parametrize("info", [
	(
		{
			"text"		: "teszt szöveg"			
		}
	),
	(
		{
			"text"		: "teszt szöveg https://www.youtube.com/watch?v=dQw4w9WgXcQ",
			"urls"			: ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
			"smileys"	: ["=d"]
		}
	),
	(
		{
			"text"		: "@mention",
			"mentions"	: ["@mention"],
		}
	),
	(
		{
			"text"		: "@mention D:",
			"mentions"	: ["@mention"],
			"smileys"	: ["D:"],
		}
	),
	(
		{
			"text"		: ":DDDDdddd :(((8888 :3 http://",
			"smileys"	: [":DDDDdddd",":(((8888",":3"]
		}
	),
	(
		{
			"text"		: "$ßŁł 🍹-😃🍔 :) ß¤é$× asddasd",
			"emojis"		: ["🍹","😃","🍔"],
			"smileys"	: [":)"]
		}
	),
	(
		{
			"text"		: "john.doe@gmail.com email",
			"emails"		: ["john.doe@gmail.com"]
		}
	),
	(
		{
			"text"		: "notmention@gmail.com email @mention",
			"emails"		: ["notmention@gmail.com"],
			"mentions"	: ["@mention"]
		}
	)
])
def test_parser_extract(info):
	test	= parser.Extract(info['text'])
	check	= ['mentions','urls','smileys','emojis','emails']
	for item in info:
		if item!='text' and item not in check:
			raise ValueError('Possible typo in test case:',item)
	for item in check:
		result	= eval('test.'+item+'()')
		if item in info:
			assert set(info[item]) == set(result)
		else:
			assert not result

@pytest.mark.parametrize("info", [
	(
		{
			"in"		: "tízenkétmillióhatvanezerhetvenegy és hárommillió száz huszonkettő vagy még nullamilliárd de akkor már kettő kettő tizenkettő :) harmincnégy és nyolcvan illetve kilencvenezer az állás pedig egy-egy és végül egy kettő három",
			"out"		: "12060071 és 3000122 vagy még 0 de akkor már 2212 :) 34 és 80 illetve 90000 az állás pedig 1-1 és végül 1 2 3"
		}
	),
	(
		{
			"in"		: "harmincnégy lol első a második harmadik :D negyed végén ötödikén mit más csinálsz tízenkétmillióhatvanezerhetvenegy és hárommillió száz huszonkettő vagy még nullamilliárd de akkor már kettő kettő tizenkettő :) harmincnégy és nyolcvan illetve kilencvenezer az állás pedig egy-egy és végül egy kettő három",
			"out"		: "34 lol 1 a 2 3 :D negyed végén 5 mit más csinálsz 12060071 és 3000122 vagy még 0 de akkor már 2212 :) 34 és 80 illetve 90000 az állás pedig 1-1 és végül 1 2 3"
		}
	),
	(
		{
			"in"		: "egymillió és százezer és tízezer és tízmilliótíz és százezerszáz",
			"out"		: "1000000 és 100000 és 10000 és 10000010 és 100100"
		}
	)
])
def test_parser_extract_convert_numbers(info):
	test	= parser.Extract(info['in'])
	assert test.ntext==info['out']
			
@pytest.mark.parametrize("info", [
	(
		{
			"text"		: "120 a 5 100 forint 420 dollár 34.56 yen 300 300 és 20. 3 és 2.3.4 1",
			"function"	: "digits",
			"result"		: ['120', '5100', '420', '3456', '300300', '20', '3', '2341']
		}
	),
	(
		{
			"text"		: "120 a 5 100 forint 420 dollár 34.56 yen 300 300 és 20. 3 és 2.3.4 1",
			"function"	: "digits",
			"args"		: [3],
			"result"		: ['120', '420']
		}
	),
	(
		{
			"text"		: "1-2-0 és 420 meg 3.6.0",
			"function"	: "digits",
			"args"		: [3,False],
			"result"		: ['1-2-0', '420', '3.6.0']
		}
	),
	(
		{
			"text"		: "120 a 5 100 forint 420 dollár 34.56 yen 78,90 yen 300 300 és 20. 3 és 2.3.4 1 de -2 jó e és a -2.0",
			"function"	: "numbers",
			"result"		: [120.0, 5100.0, 420.0, 34.56, 78.90, 300300.0, 20.0, 3.0, 2.0, 3.4, 1.0, -2.0, -2.0]
		}
	),
	(
		{
			"text"		: "120 a 5 100 forint 420 dollár 34.56 yen 300 300 és 20. 3 és 2.3.4 1 de -2 jó e és a -2.0",
			"function"	: "numbers",
			"args"		: [False,False],
			"result"		: [120, 5100, 420, 300300, 20, 3, 1, -2]
		}
	),
	(
		{
			"text"		: "100 a 90% 1100% 123,45% 0.5 % és 0,4% valamint .7 %",
			"function"	: "percentages",
			"result"		: [0.90,11.0,1.2345,0.005,0.004,0.007]
		}
	),
	(
		{
			"text"		: "100 a 90% 1100% 123,45% 0.5 % és 0,4% valamint .7 %",
			"function"	: "percentages",
			"args"		: [False],
			"result"		: ["90%","1100%","123,45%","0.5 %","0,4%",".7 %"]
		}
	),
	(
		{
			"text"		: "#hashtag #YOLO",
			"function"	: "hashtags",
			"result"		: ["#hashtag","#yolo"]
		}
	),
	(
		{
			"text"		: "#hashtag #YOLO",
			"function"	: "hashtags",
			"args"		: [False],
			"result"		: ["#hashtag","#YOLO"]
		}
	),
	(
		{
			"text"		: "Hívj fel! A számom (06 30) 123/45 67!",
			"function"	: "phone_numbers",
			"result"		: ['+36 30 1234567']
		}
	),
	(
		{
			"text"		: "Hívj fel! A számom (0630) 123/45 67!",
			"function"	: "phone_numbers",
			"args"		: [False],
			"result"		: ['(0630) 123/45 67']
		}
	),
	(
		{
			"text"		: "5 000 YEN vagy 5 000€ vagy 5000 fontot 5000£",
			"function"	: "currencies",
			"result"		: ["5000.0 JPY","5000.0 EUR","5000.0 GBP","5000.0 GBP"],
		}
	),
	(
		{
			"text"		: "$5 000 vagy 5 000$ vagy 5000 dollár 5000.-",
			"function"	: "currencies",
			"args"		: [False],
			"result"		: ["$5 000","5 000$","5000 dollár","5000.-"],
		}
	),
	(
		{
			"text"		: "adj nekem $99,99-et meg 19 dollárt és 99 centet!",
			"function"	: "currencies",
			"result"		: ["99.99 USD", "19.99 USD"]
		}
	),
	(
		{
			"text"		: "adj nekem $99,99-et meg 19 dollárt és 99 centet!",
			"function"	: "currencies",
			"args"		: [False],
			"result"		: ["$99,99", "19 dollárt és 99 centet"]
		}
	),
	(
		{
			"text"		: "csak 1 000 000 van ide írva",
			"function"	: "currencies",
			"result"		: ["1000000.0 HUF"],
		}
	),
	(
		{	
			"text"		: "találkozzunk háromnegyed 3 előtt 4 perccel, holnap!",
			"function"	: "times",
			"args"		: [False,False,0],
			"result"		: ["háromnegyed 3 előtt 4 perccel, holnap"]
		}
	),
	(
		{	
			"text"		: "3 óra 4 perc",
			"function"	: "times",
			"args"		: [True,False,0],
			"result"		: ["03:04"]
		}
	),
	(
		{	
			"text"		: "három óra négy perc",
			"function"	: "times",
			"args"		: [True,True,10],
			"result"		: ["15:04"]
		}
	),
	(
		{	
			"text"		: "találkozzunk 10 perccel 9 előtt vagy 20 perccel 20 előtt vagy akár nekem 10 perccel 20 után is jó",
			"function"	: "times",
			"args"		: [True,False,10],
			"result"		: ["20:50","19:40","20:10"]
		}
	),
	(
		{	
			"text"		: "10:30 simán, de reggel 9-től este 10-ig és holnap 4-kor vagy holnap délután 4-kor illetve 8-kor és holnap 8-kor",
			"function"	: "times",
			"args"		: [True,False,10],
			"result"		: ["10:30","09:00","22:00","16:00","16:00","20:00","20:00"]
		}
	),
	(
		{	
			"text"		: "fél 3 után 2 perccel vagy háromnegyed 2 körül vagy fél 5 előtt vagy 5 előtt 2 perccel vagy fél 5 előtt 2 perccel vagy 2 perccel fél 5 előtt vagy fél 5 után vagy fél 5 után 2 perccel vagy 2 perccel fél 5 után",
			"function"	: "times",
			"args"		: [True,False,10],
			"result"		: ["14:32","13:45","16:30","16:58","16:28","16:28","16:30","16:32","16:32"]
		}
	),
	(
		{
			"text"		: "18/01/09 vagy 18-01-09 vagy 2018. 01. 09. vagy 2018. 01. 09-én vagy 2018 VII 20. és így 2018 január 20-án",
			"function"	: "dates",
			"args"		: [False],
			"result"		: ["18/01/09","18-01-09","2018. 01. 09","2018. 01. 09","2018 VII 20","2018 január 20"]
		}
	),
	(
		{
			"text"		: "18/01/09 vagy 18-01-09 vagy 2019. 01. 09. vagy 2018. 01. 09-én vagy 2018 VII 20. és így 2018 január 20-án",
			"function"	: "dates",
			"args"		: [True],
			"result"		: ["2018-01-09","2018-01-09","2019-01-09","2018-01-09","2018-07-20","2018-01-20"]
		}
	),
	(
		{
			"text"		: "3 óra múlva vagy 12 percen belül de akár 2 és fél évvel előbb is megtörténhet, hogy 5 órával vissza kell állítani, az órát, mert jöttömre kelet felől 1,5 hét múlva számítsatok",
			"function"	: "durations",
			"args"		: [True],
			"result"		: [10800.0, 720.0, -78840000.0, -18000.0, 907200.0]
		}
	),
	(
		{
			"text"		: "3 óra és 4 perc múlva valamint majd egyszer egy héttel rá",
			"function"	: "durations",
			"args"		: [False],
			"result"		: ['3 óra és 4 perc múlva', '1 7 rá']
		}
	),
	(
		{
			"text"		: "3 óra és 4 perc múlva valamint majd egyszer 1 héttel rá",
			"function"	: "durations",
			"args"		: [True],
			"result"		: [11040.0, 604800.0]
		}
	),
	(
		{
			"text"		: "vagyis jövő kedden is tegnapelőtt vagyis múlt hét vasárnap azaz hétfőn",
			"function"	: "relative_dates",
			"args"		: [True,'2018-04-01'],
			"result"		: ['2018-04-03', '2018-03-30', '2018-03-25', '2018-03-26']
		}
	),
	(
		{
			"text"		: "vagyis jövő kedden is tegnapelőtt vagyis múlt hét vasárnap azaz hétfőn",
			"function"	: "relative_dates",
			"args"		: [False,'2018-04-01'],
			"result"		: ['jövő kedd', 'tegnapelőtt', 'múlt hét vasárnap', 'hétfő']
		}
	),
])
def test_parser_extract_parameter(info):
	test	= parser.Extract(info['text'])
	if 'args' not in info or not info['args']:
		result	= eval('test.'+info['function']+'()')
	else:
		result	= eval('test.'+info['function']+'('+str(info['args']).strip('[]')+')')
	assert info['result'] == result
	