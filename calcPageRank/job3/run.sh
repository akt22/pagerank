#!/bin/sh

###############################################

jobname="Job3"
hadoop_in="wiki0100"
hadoop_out="output"

###############################################

currentPath=`pwd`;
mapper=$currentPath"/mapper.py"

###############################################

options="-D mapred.map.tasks=1"
options=$options" -D mapred.job.priority=NORMAL"
options=$options" -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator"
# keyを降順にソートするオプション
options=$options" -D mapred.text.key.comparator.options=-k1nr"


###############################################

echo "remove hdfs file: \""$hadoop_out"\" ?[y/n]"
read ANS

if [ $ANS = 'y' -o $ANS = 'yes' ]; then
	hadoop fs -rmr ${hadoop_out}
	hadoop jar /home/hadoop/hadoop/contrib/streaming/hadoop-streaming-1.1.2.jar  -D mapred.job.name="${jobname}" ${options} -file ${mapper} -mapper ${mapper} -input ${hadoop_in} -output ${hadoop_out}
fi

 hadoop fs -cat output/part-\* > ../showTopTen/output.txt
