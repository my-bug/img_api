#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

class Save_json():
	"""docstring for save_json"""
	def __init__(self, save_file, times, img_url, preview, urls):
		self.save_file = save_file
		self.times = times
		self.img_url = img_url
		self.preview = preview
		self.urls = urls


	def img_key(self):
		image = {}
		image['times'] = self.times
		image['img_url'] = self.img_url
		image['preview'] = self.preview
		image['urls'] = self.urls
		#total[self.name] = image
		return image


	def save_image(self, total):
		with open(self.save_file, 'w') as f:
			json.dump(total, f, ensure_ascii=False)
			return True