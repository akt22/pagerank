# Pagerank

・Wikipediaの各エントリのPageRankランクを計算\n
・それを用いて作成したサービス

## 中身詳細
- calcPageRank : wikipediaのPageRankスコアをHadoop Streamingを用いて計算
	+ job1 : "jawiki-20150512-pagelinks.sql"がHDFS上にありこのディレクトリに"jawiki-20150512-page.sql"が存在するとき，各エントリがどのエントリにリンクしているか出力
	+ job2 : PageRankスコアを計算．100回繰り返し処理．
	+ job3 : job2の結果を降順ソート
	+ showTopTen : PageRankスコアが高い上位10エントリを出力．"jawiki-20150512-categorylinks.sql"が必要


- public
	- index.html : webページ
	+ assets : jQueryやbootstap
	+ css : cssファイル
	+ node_modules : Twitter Stream APIやnode.jsのためのディレクトリ
	+ js
		- script.js : Twitter APIによるTweetの処理やajax通信でRNNによる予測を行うファイル
