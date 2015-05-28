#!/usr/local/bin/python
# coding: utf-8
import sys

archive = {}

# Job2の出力結果を降順にソートする
for line in sys.stdin:
	if len(line.strip().split('\t')) == 3:
		fromPage, score, toPage = line.strip().split('\t')
		if fromPage not in archive:
			print '%s\t%s' % (float(score), fromPage)
			archive[fromPage] = 'appear'
		else:
			pass
