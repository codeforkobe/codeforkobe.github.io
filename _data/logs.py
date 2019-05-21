import requests
import re
import json

def line2item(line):
	m = re.match(r'\- \[([^\]]+?)]\(([^\)]+?)\)', line)
	if not m:
		return
	
	title, url = m.groups()
	if url.startswith("/"):
		url = "https://hackmd.io%s" % url
	return {"title": title, "url":url}

# thanks to https://github.com/hackmdio/codimd/issues/448
r = requests.get("https://hackmd.io/s/S1sujZKzG/download")
assert r
items = [line2item(l) for l in r.text.split("\n")]
json.dump([i for i in items if i], open("logs.json","w"), ensure_ascii=False)
