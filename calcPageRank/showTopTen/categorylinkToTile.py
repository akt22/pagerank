# coding: utf-8
import re
import pdb

patternCategory = r"\((\S+?),'(\S*?)','((\S|\s)*?)','((\S|\s)*?)','(\S*?)','(\S*?)','(\S*?)'\)"

# 放映中のテレビ番組を抽出する際に使用
appearFlag = {}

category = 'zonmei'


# 'jawiki-20150512-categorylinks.sql'からカテゴリ：存命人物に含まれるエントリを抽出
def judgeZonmei(linkList):
	for link in linkList:
		if link.group(2) == '存命人物':
			if len(str(link.group(3)).split('\\n')) == 2:
				print (str(link.group(3)).split('\\n')[1] + '||0')
			else:
				print (str(link.group(3)).strip() + '||0')


# テレビ番組に関するエントリ
def judgeTV(linkList):
	for link in linkList:
		if 'テレビ番組_(日本)' in link.group(2) or '継続中の作品' in link.group(2):
			flag = [0, 0]
			if 'テレビ番組_(日本)' in link.group(2):
				flag[0] = 1
			if '継続中の作品' in link.group(2):
				flag[1] = 1
			if link.group(3) in appearFlag:
				appearFlag[link.group(3)][0] += flag[0]
				appearFlag[link.group(3)][1] += flag[1]
			else:
				appearFlag[link.group(3)] = flag
			if appearFlag[link.group(3)][0] > 0 and appearFlag[link.group(3)][1] > 0:
				if len(str(link.group(3)).split('\\n')) == 2:
					print (str(link.group(3)).split('\\n')[1] + '||0')
				else:
					print (str(link.group(3)).strip() + '||0')


# アニメに関するエントリ
def judgeAnime(linkList):
	for link in linkList:
		match = re.match(u'アニメ作品_[あ-ん]', link.group(2).decode("utf-8"))
		if match is not None:
			if len(str(link.group(3)).split('\\n')) == 2:
				print (str(link.group(3)).split('\\n')[1] + '||0')
			else:
				print (str(link.group(3)).strip() + '||0')


# 音楽（歌手）に関するエントリ
def judgeMusic(linkList):
	for link in linkList:
		if 'の歌手' in link.group(2):
			if len(str(link.group(3)).split('\\n')) == 2:
				print (str(link.group(3)).split('\\n')[1] + '||0')
			else:
				print (str(link.group(3)).strip() + '||0')


# ゲームに関するエントリ
def judgeGame(linkList):
	for link in linkList:
		if '用ソフト' in link.group(2):
			if len(str(link.group(3)).split('\\n')) == 2:
				print (str(link.group(3)).split('\\n')[1] + '||0')
			else:
				print (str(link.group(3)).strip() + '||0')


# 漫画に関するエントリ
def judgeManga(linkList):
	for link in linkList:
		if '漫画作品' in link.group(2):
			if len(str(link.group(3)).split('\\n')) == 2:
				print (str(link.group(3)).split('\\n')[1] + '||0')
			else:
				print (str(link.group(3)).strip() + '||0')

f = open('jawiki-20150512-categorylinks.sql', 'r')
for line in f.readlines():
	if line[0:6] == 'INSERT':
		linkList = re.finditer(patternCategory, line.strip())
		if category == 'zonmei':
			judgeZonmei(linkList)
		if category == 'anime':
			judgeAnime(linkList)
		if category == 'music':
			judgeMusic(linkList)
		if category == 'game':
			judgeGame(linkList)
		if category == 'manga':
			judgeManga(linkList)
