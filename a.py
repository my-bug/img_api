#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib import img
import config
import json, time, re, os

"""
url = 'http://www.mzitu.com/89033/2'
name = '颜值高身材辣! 那些惊艳的美媛馆女神不同的性感你喜欢哪个?'
proxies = config.proxies
imge_urls = img.status(url, proxies)
c = re.findall('<img src="(.*)" alt=".*?" />',imge_urls , re.I)
print(c)
"""
"""
a = {}
b = [123]
a['name2'] = b
print(a)
with open('a.json', 'a') as f:
	json.dump(a, f, ensure_ascii=False)
"""
def alter(file,old_str,new_str):
	with open(file, "r", encoding="utf-8") as f1,open("%s.bak" % file, "w", encoding="utf-8") as f2:
		for line in f1:
			f2.write(re.sub(old_str,new_str,line))
		os.remove(file)
		os.rename("%s.bak" % file, file)

# alter("json/data.json", "}{", ", ")

json_file = 'json/data.json'
with open(json_file,'r') as load_f:
	load_dict = json.load(load_f)
	for i in load_dict.keys():
		print(i)