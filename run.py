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
		imge = img.url(i)[0]
		print(img.name(imge, i)[0])
		print(img.times(i)[0])
		print(imge)
		print(img.preview(i)[0])
		a = a + 1

	time.sleep(1)
	if page == b:
		break

	page = page +1

print(str(a) + "条")