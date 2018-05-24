#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib import img
import config, save_json
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

#alter("json/data.json", "}{", ", ")

name = "美女筱慧身姿妙曼优美挺拔 魔鬼身材真惹眼3"
times = "2018-02-13"
img_url = "http://www.mzitu.com/120370"
preview = "http://i.meizitu.net/thumbs/2018/02/120370_13b16_236.jpg"
urls = [
            "http://i.meizitu.net/2018/02/13b01.jpg",
            "http://i.meizitu.net/2018/02/13b02.jpg",
            "http://i.meizitu.net/2018/02/13b03.jpg",
            "http://i.meizitu.net/2018/02/13b04.jpg",
            "http://i.meizitu.net/2018/02/13b05.jpg",
            "http://i.meizitu.net/2018/02/13b06.jpg",
            "http://i.meizitu.net/2018/02/13b07.jpg",
            "http://i.meizitu.net/2018/02/13b08.jpg",
            "http://i.meizitu.net/2018/02/13b09.jpg",
            "http://i.meizitu.net/2018/02/13b10.jpg",
            "http://i.meizitu.net/2018/02/13b11.jpg",
            "http://i.meizitu.net/2018/02/13b12.jpg",
            "http://i.meizitu.net/2018/02/13b13.jpg",
            "http://i.meizitu.net/2018/02/13b14.jpg",
            "http://i.meizitu.net/2018/02/13b15.jpg",
            "http://i.meizitu.net/2018/02/13b16.jpg",
            "http://i.meizitu.net/2018/02/13b17.jpg",
            "http://i.meizitu.net/2018/02/13b18.jpg",
            "http://i.meizitu.net/2018/02/13b19.jpg",
            "http://i.meizitu.net/2018/02/13b20.jpg",
            "http://i.meizitu.net/2018/02/13b21.jpg",
            "http://i.meizitu.net/2018/02/13b22.jpg",
            "http://i.meizitu.net/2018/02/13b23.jpg",
            "http://i.meizitu.net/2018/02/13b24.jpg",
            "http://i.meizitu.net/2018/02/13b25.jpg",
            "http://i.meizitu.net/2018/02/13b26.jpg",
            "http://i.meizitu.net/2018/02/13b27.jpg",
            "http://i.meizitu.net/2018/02/13b28.jpg",
            "http://i.meizitu.net/2018/02/13b29.jpg",
            "http://i.meizitu.net/2018/02/13b30.jpg",
            "http://i.meizitu.net/2018/02/13b31.jpg",
            "http://i.meizitu.net/2018/02/13b32.jpg",
            "http://i.meizitu.net/2018/02/13b33.jpg",
            "http://i.meizitu.net/2018/02/13b34.jpg",
            "http://i.meizitu.net/2018/02/13b35.jpg",
            "http://i.meizitu.net/2018/02/13b36.jpg",
            "http://i.meizitu.net/2018/02/13b37.jpg",
            "http://i.meizitu.net/2018/02/13b38.jpg",
            "http://i.meizitu.net/2018/02/13b39.jpg"
        ]

# b = save_json.Save_json(config.SAVE_FILE, name, times, img_url, preview, urls)
# print(b.save_image())
"""
image = {}
total = {}
image['times'] = times
image['img_url'] = img_url
image['preview'] = preview
image['urls'] = urls
total[name] = image
#print(total)
"""
m = []
json_file = 'json/data.json'
with open(json_file,'r') as load_f: 
	load_dict = json.load(load_f)
#	for i in load_dict.keys():
#		for n in load_dict[i]['urls']:
#			m.append(n)

print(len(load_dict.keys()))


"""
d1 = {}
d1.update(total)
d1.update(load_dict)
print(d1.keys())
"""