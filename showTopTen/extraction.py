# coding: utf-8
import re
import sys
import pdb

# categorylinkToTitle.pyで出力された
# そのカテゴリに含まれるエントリ
zonmeiDic = {}
# ページランクスコアが高い上位10エントリのタイトルのリスト
topTenTitleList = []
# ページランクスコアが高い上位10エントリのスコアのリスト
topTenScoreList = []

# 表示したいカテゴリ
category = 'zonmei'


# ページランクスコアが上位10エントリか確認
# スコアが高ければ一番低いものを削除して
# 現在のタイトルをappend
def checkAdd(title, score):
	if len(topTenScoreList) < 10:
		topTenScoreList.append(float(score))
		topTenTitleList.append(title)
		return
	if min(topTenScoreList) < float(score):
		i = topTenScoreList.index(min(topTenScoreList))
		del topTenScoreList[i]
		del topTenTitleList[i]
		topTenScoreList.append(float(score))
		topTenTitleList.append(title)


# そのカテゴリに含まれるエントリを辞書に格納
# 辞書の方が xx in dic が高速のため
f = open(category + '.txt')
for line in f.readlines():
	zonmeiDic[line.strip()] = 'appear'

# 全ページランクを標準入力から読み込む
for line in sys.stdin:
	score, title = line.strip().split('\t')
	if title in zonmeiDic:
		checkAdd(title, score)

# 最終結果を出力
for i in range(len(topTenScoreList)):
	print str(topTenScoreList[i]) + '\t' + topTenTitleList[i][:-3]
	# print topTenTitleList[i][:-3]
