#!/usr/local/bin/python
# coding: utf-8
import sys

# key:リンク先，value：スコア
(last_key, score) = (None, 0.0)

# 入力はSTDIN
for line in sys.stdin:
	if len(line.strip().split('\t')) == 3:
		# リンク先(key)，リンク元，リンク元のスコア
		toLink, fromLink, pageScore = line.strip().split('\t')
		# combinerへの入力のkeyが変わったタイミング
		if last_key and last_key != toLink:
			# リンク先，リンク元，リンク先のスコア
			print '%s\t%s\t%s' % (last_key, fromLink, str(score))
			# 初期化
			(last_key, score) = (toLink, float(pageScore))
		else:
			last_key = toLink
			# combinerに同じkeyが入力され続けている限り，スコアをたす
			score += float(pageScore)

# 最後のkeyを出力
if last_key:
	print '%s\t%s\t%s' % (last_key, fromLink, str(score))
