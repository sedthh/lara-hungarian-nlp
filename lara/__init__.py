# -*- coding: UTF-8 -*-

# Lara - Lingusitic Aim Recognizer API

__all__				= 'nlp','parser','tippmix','entities','magic'
__version__ 		= '0.4.2'
__version_info__	= tuple(int(num) for num in __version__.split('.'))

import sys
import lara.nlp
import lara.parser
import lara.tippmix
import lara.entities
import lara.magic
