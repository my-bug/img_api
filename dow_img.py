#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
github: my-bug
blog: my-bug.github.io
"""

import config
import requests, threading, json, os, time

def save_img(url, name):
	#防盗链，修改访问来源
	headers = {
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
	'Referer': 'http://i.mzitu.com/',
	}
	a = 0
	for i in url:
		ir = requests.get(i, headers = headers) # 代理 , proxies=config.proxies)
		# 保存文件路径
		file = '{}{}/{}.jpg'.format(config.DOW, name, a)
		sz = open(file, 'wb').write(ir.content)
		a = int(a) + 1
		# 要有良心加点延迟，推荐1秒
		time.sleep(0.2)
	n = '{}  共{}张'.format(name, a)
	print(n) 

def xian_start():
	# 开始线程
	for th in threadpool:
		th.start()
	# 等待线程结束
	for th in threadpool:
		th.join()


# 创建线程池
threadpool = []
# 最大线程数
xian_max = 24

json_file = 'json/d.json'
with open(json_file,'r') as load_f:
	load_dict = json.load(load_f)
	for i in load_dict.keys():
		# 创建图片名字目录
		os.makedirs(config.DOW + i)
		# 定义线程
		th = threading.Thread(target=save_img, args=(load_dict[i]['urls'], i))
		# 将线程加入线程池
		threadpool.append(th)
		if len(threadpool) == xian_max:
			xian_start()
			# 清空线程池
			threadpool = []
	if len(threadpool) <= xian_max:
		xian_start()
		threadpool = []

"""
print(len(threadpool))	
# 开始线程
xian = 0
for th in threadpool:
	th.start()
	xian = xian + 1
	if xian == 15:
		xian = 0
		# 等待所有线程运行完毕
		for th in threadpool:
			th.join()
"""
"""	
# 等待所有线程运行完毕
for th in threadpool:
    th.join()
"""
