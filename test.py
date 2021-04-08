import requests
import xmltodict
import json
import key

url = 'https://stdict.korean.go.kr/api/search.do'

key = key.api_key
keyword = '면'

params = {
	'key' : key,
	'q' : keyword,
	'advanced' : 'y',
	'target' : 1,
	'pos' : 1,
	'type1' : 'word',
	'method' : 'start',
	'letter_s' : 2
}

res = requests.get(url,params=params)

cc = xmltodict.parse(res.text)
dd = json.loads(json.dumps(cc))

word = dd.get('channel').get('item')[1].get('word')
definition = dd.get('channel').get('item')[1].get('sense').get('definition')

print(word)
print(definition)

def wordReturn(val,s,e):
	if s in val:
		tmp = val.split(s)
		val = []
		for i in range(0,len(tmp)):
			if e in tmp[i]:
				val.append(tmp[i][:tmp[i].find(e)])
	else:
		val = []
	return val

words = wordReturn(res.text,'<word>','</word>')
definitions = wordReturn(res.text,'<definition>','</definition>')

print(words)
print(definitions)