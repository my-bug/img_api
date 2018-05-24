#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

class Save_json():
	"""docstring for save_json"""
	def __init__(self, save_file, name, times, img_url, preview, urls):
		self.save_file = save_file
		self.name = name
		self.times = times
		self.img_url = img_url
		self.preview = preview
		self.urls = urls


	def img_key(self):
		image = {}
		total = {}
		image['times'] = self.times
		image['img_url'] = self.img_url
		image['preview'] = self.preview
		image['urls'] = self.urls
		total[self.name] = image
		return total


	def save_image(self):
		with open(self.save_file,'r') as load_f: 
			load_dict = json.load(load_f)
		d1 = {}
		d1.update(self.img_key())
		d1.update(load_dict)
		with open(self.save_file, 'w') as f:
			json.dump(d1, f, ensure_ascii=False)
		return True