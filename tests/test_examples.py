# -*- coding: UTF-8 -*-

import pytest
import os, errno, subprocess

@pytest.mark.parametrize("entity", [
    "example_chatbot_1","example_chatbot_2","example_chatbot_3","example_chatbot_4","example_chatbot_5","example_huszt","example_news","example_readme","example_stemmer","example_tweet"
])
def test_entities(entity):
	file	= os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir, 'examples/', entity+'.py')
	if os.path.isfile(file) :
		#os.system('python '+file)
		event	= subprocess.Popen("python "+file, stdin=None, stdout=None, stderr=subprocess.PIPE).communicate()[1]
		if event:
			raise Exception(event.decode('utf-8'))
	else:
		raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), file)