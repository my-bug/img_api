#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
github: my-bug
blog: my-bug.github.io
"""
import img, config, re, time

url = config.URL
#url = url + config.TYPE['最热'] 
#url = '{}{}/page/{}'.format(url, config.TYPE['最热'], page)
a = 0
b = 8
page = 1
while True:
	urls = '{}{}/page/{}'.format(url, config.TYPE['最热'], page)
	for i in img.total(url):
		# 地址
		imge_url = img.url(i)[0]
		# 名字
		name = img.name(imge_url, i)[0]
		# 时间
		times = img.times(i)[0]
		# 预览图片地址
		preview = img.preview(i)[0]
		# 获取页数
		u = img.status(imge_url)
		page = img.page(u)

		print()
		print("名称：", name)
		print("时间：", times)
		print("地址：", imge_url)
		print("预览：", preview)
		print("以下是图片地址")
		# 合成每页网
		pages = 1
		while True:
			# 每页网址
			page_url = '{}/{}'.format(imge_url, pages)
			imge_urls = img.img_url(name, img.status(page_url))
			print(imge_urls[0])

			if pages == int(page[0]):
				break
			pages = pages + 1
			time.sleep(0.5)

		a = a + 1

	time.sleep(1)
	if page == b:
		break

	page = page +1

print(str(a) + "条")