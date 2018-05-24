#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
github: my-bug
blog: my-bug.github.io
"""
from lib import img
import config, save_json, save_img
import re, time, os, threading

def start(urls):
	# 获取代理ip
	#ip_list = ip.get_ip_list(config.IP_URL)
	#proxies = ip.get_random_ip(ip_list)
	print()
	proxies = config.proxies
	print("代理IP:", proxies['https'])
	for i in img.total(urls, proxies):
		total = {}
		# 地址
		imge_url = img.url(i)[0]
		# 名字
		name = img.name(imge_url, i)[0]
		# 时间
		times = img.times(i)[0]
		# 预览图片地址
		preview = img.preview(i)[0]
		# 获取页数
		u = img.status(imge_url, proxies)
		paged = img.page(u)
		print()
		print("名称：", name)
		print("时间：", times)
		print("地址：", imge_url)
		print("预览：", preview)
		print("以下是图片地址")
		# 如果有页数，那么获取每页图片
		if paged:
			# 图片每页地址
			inde_pages = 1
			# 创建一个列表存放图片url
			save_url = []
			# 输出所有地址
			for img_url in range(1, int(paged[0]) + 1):
				# 每页网址
				page_url = '{}/{}'.format(imge_url, img_url)
				# 获取图片链接
				imge_urls = img.img_url(img.status(page_url, proxies))
				if imge_urls:
					if len(imge_urls):
						# 把链接储存到列表
						save_url.append(imge_urls[0])	
						print(imge_urls[0])
					else:
						imge_urls = ['False']
						save_url.append(imge_urls[0])
				else:
					imge_urls = ['False']
					save_url.append(imge_urls[0])
				time.sleep(0.2)
		else: 
			save_url = img.img_url(img.status(imge_url, proxies))
			for n in save_url:
				print(n)

			paged = [len(save_url)]
			time.sleep(0.2)
		print(name, "共", paged[0], "张")

		# 锁线程
		lock.acquire()
		save_image = save_json.Save_json(config.SAVE_FILE, name, times, imge_url, preview, save_url)
		print("保存状态：", save_image.save_image())
		# 解锁线程
		lock.release()


# 获取url
url = config.URL
# 创建一个计数器，储存条数
#article = 0
# 爬取页数
pages = 40
# 开始页数
#page = 1
# 储存json数据的字典
#total = {}
# 合成网址
#urls = '{}{}/page/{}'.format(url, config.TYPE['最热'], page)
#start(urls)

# 创建线程池
threadpool = []
# 创建锁
lock = threading.Lock()
# 最大线程数
xian_max = 24
for m in range(1, pages + 1):
	# 首页
	urls = '{}page/{}'.format(url, m)
	th = threading.Thread(target=start, args=(urls,))
	# 将线程加入线程池
	threadpool.append(th)

for th in threadpool:
	th.setDaemon(True)
	th.start()
for n in threadpool:
	th.join()
	#print(total)
#print("保存状态", save_image.save_image(total))
