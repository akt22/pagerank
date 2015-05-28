#!/usr/local/bin/python
# coding: utf-8
import sys

# 入力されたエントリが被らないようにチェックする辞書
archive = {}

# 入力はSTDIN
for line in sys.stdin:
	if len(line.strip().split('\t')) == 3:
		# リンク元，リンク元のスコア，リンク先('A', 'B', 'C', ...)
		fromPage, score, toPage = line.strip().split('\t')
		if fromPage not in archive:
			toPageList = []
			# リンク先をspilit
			toPageList = toPage.strip().split("', '")
			# リンク先一つ一つを抽出
			for to in toPageList:
				lenToPage = len(toPageList)
				# リンク先（シングルクオート削除），リンク元，（リンク元のスコア）/（リンク元のリンク数）
				print '%s\t%s\t%s' % (to.replace("'", '').strip(), fromPage, (float(score) / float(lenToPage)))
			archive[fromPage] = 'appear'
			print '%s\t%s\t%s' % (fromPage, fromPage, score)
	else:
		pass
