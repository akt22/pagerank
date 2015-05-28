#!/usr/local/bin/python
# coding: utf-8
import sys

data = {}
pages = {}

# 重複しているリンクを取り除くcombierクラス
# 無くても可
for line in sys.stdin:
	fromLink, toLink = line.strip().split('\t')
	if (fromLink + ',' + toLink) in data:
		pass
	else:
		data[fromLink + ',' + toLink] = 'appear'
		print line.strip()
