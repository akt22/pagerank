# Pagerank

・Wikipediaの各エントリのPageRankランクを計算

・それを用いて作成したサービス([ネタにこまたったー](http://www.ai.cs.kobe-u.ac.jp/~akita/netter/))


## 中身詳細
- calcPageRank : wikipediaのPageRankスコアをHadoop Streamingを用いて計算
	+ job1 : 各エントリがどのエントリにリンクしているか出力
	+ job2 : PageRankスコアを計算．100回繰り返し処理
	+ job3 : job2の結果を降順ソート
	+ showTopTen : PageRankスコアが高い上位10エントリを出力

job1では"jawiki-20150512-pagelinks.sql"をHDFS上，このディレクトリに"jawiki-20150512-page.sql"が必要

job3では"jawiki-20150512-categorylinks.sql"がこのディレクトリに必要


- service
	+ netter : ウェブページ
	+ wiki : ページランクの出力結果を返す
