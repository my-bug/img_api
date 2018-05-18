# -*- coding: utf-8 -*-

import requests, re

def status(url):
	header = {
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:59.0) Gecko/20100101 Firefox/59.0'
	}
	status = requests.get(url, header)
	if status.status_code == 200:
		web_enco = re.findall('charset=(.*)"', status.text, re.I)
		status.encoding = web_enco[0]
		return status.text
	return False

def total(url):
	if status(url):
		total = re.compile('<li>.*</span></li>')
		total = total.findall(status(url))
		return total
	else:
		return False

def url(character):
	re_url = re.compile(r'https*://www\.[a-z]*\.com/[0-9]+')
	url = re_url.findall(character)
	if len(url):
		return url
	return False

def name(url, character):
	r = '<span><a href="{}" target="_blank">(.*)</a></span>'.format(url)
	name = re.findall(r, character, re.I)
	if len(name):
		return name
	return False

def times(character):
	times = re.findall('<span class="time">(.*)</span><span', character, re.I)
	if len(times):
		return times
	return False

def preview(character):
	preview = re.findall("data-original='(.*)' /></a>", character, re.I)
	if len(preview):
		return preview
	return False

def img_url(name, character):
	img_text = '<img src="(.*)" alt="{}" />'.format(name)
	img_url = re.findall(img_text, character, re.I)
	if len(img_url):
		return img_url
	return False

def page(character):
	k = re.compile(r"…</span><a href='https*://www\.[a-z]*\.com/[0-9]*/[0-9]{2}'><span>[0-9]{2,3}</span></a>")
	pag = k.findall(character)
	page = re.findall('<span>(.*)</span>', pag[0], re.I)
	if len(page):
		return page
	return False
