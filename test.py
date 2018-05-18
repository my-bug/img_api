#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re, img, requests, config, os, save_img

proxies = {'https': 'http://118.123.113.4:80/',
		    'https': 'http://222.168.41.246:8090',
		  }

url = 'http://i.meizitu.net/2018/05/17a02.jpg'
headers = {
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
	'Referer': 'http://i.mzitu.com/',
	}#防盗链，修改访问来源  

name = '头条女神米雪办公室上演护士制服魅惑大戏'
os.makedirs(config.DOW + name)
pages = 1
se = '{}/{}/{}.jpg'.format(config.DOW, name, pages)

print(url, round(save_img.save_img(url, se)/1024, 2), "K")

"""
ir = requests.get(url, headers = headers)
sz = open(se, 'wb').write(ir.content)
print(url, round(sz/1024, 2),'K')
"""
