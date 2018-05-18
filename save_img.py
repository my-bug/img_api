#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import config

def save_img(url, name):
	#防盗链，修改访问来源
	headers = {
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
	'Referer': 'http://i.mzitu.com/',
	}
	ir = requests.get(url, headers = headers, proxies=config.proxies)
	sz = open(name, 'wb').write(ir.content)
	return sz