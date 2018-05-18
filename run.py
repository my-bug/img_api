#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
github: my-bug
blog: my-bug.github.io
"""
import img, config, ip, save_img
import re, time, os

url = config.URL
#url = url + config.TYPE['最热'] 
#url = '{}{}/page/{}'.format(url, config.TYPE['最热'], page)
a = 0
b = 8
page = 1
while True:
	"""
	# 获取代理ip
	ip_list = ip.get_ip_list(config.IP_URL)
	proxies = ip.get_random_ip(ip_list)
	print(proxies)
	"""
	proxies = {
			   'https': 'http://120.52.32.46:80',
			   'https': 'http://118.123.113.4:80/',
			   'https': 'http://222.168.41.246:8090',
			  }
	# 合成网址
	#urls = '{}{}/page/{}'.format(url, config.TYPE['最热'], page)
	urls = '{}{}'.format(url, config.TYPE['最热'])
	print(urls)
	for i in img.total(url, proxies):
		print(i)
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
		page = img.page(u)

		print()
		print("名称：", name)
		print("时间：", times)
		print("地址：", imge_url)
		print("预览：", preview)
		print("以下是图片地址")
		# 创建图片文件夹
		os.makedirs(config.DOW + name)

		# 合成每页网
		pages = 1
		while True:
			# 每页网址
			page_url = '{}/{}'.format(imge_url, pages)
			imge_urls = img.img_url(name, img.status(page_url, proxies))
			#print(imge_urls[0])
			# 保存图片
			se = '{}/{}/{}.jpg'.format(config.DOW, name, pages)
			print(imge_urls[0], round(save_img.save_img(imge_urls[0], se)/1024, 2), "K")

			if pages == int(page[0]):
				break
			pages = pages + 1
			time.sleep(0.2)
		print()
		print(name, "共", pages, "张")

		a = a + 1

	time.sleep(1)
	if page == b:
		break
	print()
	print(page, "页")
	page = page +1

print(a, "条")