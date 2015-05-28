python mapper.py < ../job1/redres > mapres
python combiner.py < mapres > comres
python reducer.py < comres > redres0

# for i in `seq 0 1`
# do
# 	c=`expr $i + 1`
# 	python mapper.py < redres${i} > mapres${i}
# 	python combiner.py < mapres${i} > comres${i}
# 	python reducer.py < comres${i} > redres${c}
# done