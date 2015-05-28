#!/usr/local/bin/python
# coding: utf-8
import sys
import re

# 'jawiki-20150512-page.sql'用の正規表現
patternPage =  r"\((\S+?),(\S+?),'(\S+?)','(\S*?)',(\S+?),(\S+?),(\S+?),('(\S+?)'|(\S+?)),'(\S+?)',('(\S+?)'|(\S+?)),(\S+?),(\S+?),('(\S+?)'|(\S+?))\)"
# 'jawiki-20150512-pagelinks.sql'用の正規表現
patternPageLink = r"\((\S+?),(\S+?),'(\S+?)',(\S+?)\)"


# ページ情報のファイルから(id -> page_title)に変換する辞書を返す
# key: page_id (str),  value: page_title (str)
def getid2title(filename):
	id2title = {}
	f = open(filename, 'r')
	for line in f.readlines():
		if line[0:6] == 'INSERT':
			pageList = re.finditer(patternPage, line.strip())
			for page in pageList:
				id2title[page.group(1)] = page.group(3)
	return id2title

# idからタイトルに変換する辞書
id2title = getid2title('jawiki-20150512-page.sql')

# 'jawiki-20150512-pagelinks.sql'を1行づつ読み込む
for line in sys.stdin:
	# 正規表現により要素を獲得
	linkList = re.finditer(patternPageLink, line.strip())
	for link in linkList:
		if str(link.group(1)) in id2title:
			# fromTitle||from_namespace\ttoTitle||to_namespaceで出力
			# namespaceを考慮しなければ重複するタイトルあり
			# Job2においてシングルクオートをreplaceするので「B'z」などを「B"z」に変換
			print "%s||%s\t%s||%s" % (id2title[str(link.group(1))].replace("'", '"'), str(link.group(4)), str(link.group(3)).replace("'", '"'), str(link.group(2)))
		# 「削除依頼」などのページのため無視
		else:
			pass
