# -*- coding: UTF-8 -*-

from lara import parser
import pytest

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
	)
])
def test_parser_match(intent,text,match):
	test	= parser.Intents(intent)
	for i in range(len(text)):
		result	= test.match(text[i])
		assert match[i] == result
