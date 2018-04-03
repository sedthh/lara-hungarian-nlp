# -*- coding: UTF-8 -*-

import pytest
import os, errno, subprocess

@pytest.mark.parametrize("entity", [
    "example_chatbot_1","example_chatbot_2","example_chatbot_3","example_chatbot_4","example_chatbot_5","example_chatbot_6","example_chatbot_7","example_huszt","example_news","example_wiki_intents","example_stemmer","example_tweet","example_entities"
])
def test_entities(entity):
	file	= os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir, 'examples/', entity+'.py')
	if os.path.isfile(file):
		event	= subprocess.Popen("python "+file, stdin=None, stdout=None, stderr=subprocess.PIPE).communicate()[1]
		if event:
			raise Exception(event.decode('utf-8'))
	else:
		raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), file)
	
@pytest.mark.parametrize("input_str", [
    "Teszt Elek"
])
def test_entities_input(input_str):
	file	= os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir, 'examples/example_input.py')
	if os.path.isfile(file):
		event	= subprocess.Popen("python "+file, stdin=subprocess.PIPE, stdout=None, stderr=subprocess.PIPE).communicate(input=input_str.encode())[1]
		if event:
			raise Exception(event.decode('utf-8'))
	else:
		raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), file)
	