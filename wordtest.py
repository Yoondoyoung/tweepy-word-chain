import requests
import xmltodict
import json
import random
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)
key = os.getenv('korea_key')

def wordFinding(kword):
	result = []
	keyword = kword

	wordlen = random.randrange(2,4)
	url = 'https://stdict.korean.go.kr/api/search.do'
	
	params = {
		'key' : key,
		'q' : keyword,
		'advanced' : 'y',
		'target' : 1,
		'pos' : 1,
		'type1' : 'word',
		'method' : 'start',
		'letter_s' : wordlen
	}
	
	res = requests.get(url,params=params)
	
	cc = xmltodict.parse(res.text)
	informations = json.loads(json.dumps(cc))
	randomNumber = random.randrange(1,len(informations.get('channel').get('item')))
	word = informations.get('channel').get('item')[randomNumber].get('word')
	definition = informations.get('channel').get('item')[randomNumber].get('sense').get('definition')
	
	result.append(word.replace("-",""))
	result.append(definition)
	return result
