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
			"jo_ido"	: [{"stem":"jó","wordclass":"adjective","with":[{"stem":"idő","wordclass":"noun","affix":["járás"]},{"stem":"meleg","wordclass":"adjective"}]}]
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
							"with":[{"stem":"idő","wordclass":"noun","affix":["járás"]},{"stem":"meleg","wordclass":"adjective"}],
							"without":[{"stem":"este","wordclass":"noun"}]}]
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
			"hibasan"	: [{"stem":"alma","wordclass":"noun"}],
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
			"float"	: [{"stem":"a","score":.75},{"stem":"b","score":.6,"typo_score":1}],
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
			"fail"		: [{"stem":"kék","wordclass":"adjective"}]
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
			"capital"	: [{"stem":"NAGY","wordclass":"adjective","ignorecase":False}],
			"lower"		: [{"stem":"kicsi","wordclass":"adjective","ignorecase":False}],
			"any"		: [{"stem":"VáLtAkOzÓ","wordclass":"adjective","ignorecase":True}],
			"acr"		: [{"stem":"KFT","ignorecase":False}]
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
			"takarit"		: [{"stem":"takarít","wordclass":"verb"}],
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
		
@pytest.mark.parametrize("intents,text,cleaned", [
	(
		[
			{
				"thanks"	: [{"stem":"köszön","wordclass":"verb"}]
			},
			{
				"thanks"	: [{"stem":"köszön","wordclass":"verb","without":[{"stem":"szép","wordclass":"adjective"}]}]
			},
			{
				"thanks"	: [{"stem":"köszön","wordclass":"verb","with":[{"stem":"nagy","wordclass":"adjective"}]}]
			},
			{
				"thanks"	: [{"stem":"köszön","wordclass":"verb","with":[{"stem":"kicsi","wordclass":"adjective"}]}]
			},
			{
				"thanks"	: [{"stem":"köszön","wordclass":"verb","with":[{"stem":"nagy","wordclass":"adjective"}],"without":[{"stem":"szép","wordclass":"adjective"}]}]
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
			"text"	: "teszt szöveg"			
		}
	),
	(
		{
			"text"	: "teszt szöveg https://www.youtube.com/watch?v=dQw4w9WgXcQ",
			"urls"	: ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"]
		}
	)
])
def test_parser_extract(info):
	test	= parser.Extract(info['text'])
	check	= ['hashtags','mentions','urls','smileys','dates','currencies','emojis']
	for item in check:
		result	= eval('test.'+item+'()')
		if item in info:
			assert set(info[item]) == set(result)
		else:
			assert not result