#!/usr/local/bin/python
# coding: utf-8
from operator import itemgetter
import sys
import pdb

# (fromTitle, toPageTitles)
(last_key, count) = (None, [])

for line in sys.stdin:
	(key, val) = line.strip().split("\t")

	# MapReduceにおけるkeyが変わったタイミングで last_key != key
	if last_key and last_key != key:
		# リンク元，リンク元のスコア(初期値：1.0)，リンク先のリスト
		print "%s\t1.0\t%s" % (last_key, str(count)[1:-1].decode('string-escape'))
		(last_key, count) = (key, [val])
	# 変わらなければtoPageTitlesにtoTitleをapoendしていく
	else:
		last_key = key
		count.append(val)

# 最後のkeyを出力
if last_key:
	# リンク元，リンク元のスコア(初期値：1.0)，リンク先のリスト
	print "%s\t1.0\t%s" % (last_key, str(count)[1:-1].decode('string-escape'))
