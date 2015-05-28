#!/usr/local/bin/python
# coding: utf-8
import sys
import pdb

damping = 0.85

# どのページがどのリンクに結びついているかの辞書
# key:リンク元，value:リンク先のリスト
linkDic = {}

# last_key:リンク元，score:リンク元のスコア
(last_key, score) = (None, 0.0)

# どのページがどのリンクに結びついているかのファイルを読み込む（Job1）の出力結果
f = open('toLink2.txt', 'r')
for l in f.readlines():
	fromPage, _, toPage = l.strip().split('\t')
	linkDic[fromPage] = toPage

# 入力はSTDIN
for line in sys.stdin:
	toLink, _, pageScore = line.strip().split('\t')
	# reducerへの入力のkeyが変わったタイミング
	if last_key and last_key != toLink:
		if last_key in linkDic:
			# リンク元，スコア，リンク先のリスト
			print '%s\t%s\t%s' % (last_key, str(damping * score + (1 - damping)), linkDic[last_key])
		else:
			# リンク元，スコア，NoLink（リンク先なし）
			print '%s\t%s\t%s' % (last_key, str(damping * score + (1 - damping)), 'NoLink')
		# 初期化
		(last_key, score) = (toLink, float(pageScore))
	else:
		last_key = toLink
		# reducerへの入力のkeyが同じ間スコアをたす
		score += float(pageScore)

# 最後のkeyを出力
if last_key:
	if last_key in linkDic:
		print '%s\t%s\t%s' % (last_key, str(damping * score + (1 - damping)), linkDic[last_key])
	else:
		print '%s\t%s\t%s' % (last_key, str(damping * score + (1 - damping)), 'NoLink')
