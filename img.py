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
	re_url = re.compile(r'http://www\.[a-z]*\.com/[0-9]+')
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