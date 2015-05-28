# Pagerank

・Wikipediaの各エントリのPageRankランクを計算

・それを用いて作成したサービス

## 中身詳細
- calcPageRank : wikipediaのPageRankスコアをHadoop Streamingを用いて計算
	+ job1 : 各エントリがどのエントリにリンクしているか出力
	+ job2 : PageRankスコアを計算．100回繰り返し処理
	+ job3 : job2の結果を降順ソート
	+ showTopTen : PageRankスコアが高い上位10エントリを出力

job1では"jawiki-20150512-pagelinks.sql"をHDFS上，このディレクトリに"jawiki-20150512-page.sql"が必要

job3では"jawiki-20150512-categorylinks.sql"がこのディレクトリに必要

- public
	- index.html : webページ
	+ assets : jQueryやbootstap
	+ css : cssファイル
	+ node_modules : Twitter Stream APIやnode.jsのためのディレクトリ
	+ js
		- script.js : Twitter APIによるTweetの処理やajax通信でRNNによる予測を行うファイル
