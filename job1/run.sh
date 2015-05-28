#!/bin/sh

###############################################

jobname="Job1"
hadoop_in="jawiki-20150512-pagelinks.sql"
hadoop_out="config"

###############################################

currentPath=`pwd`;
mapper=$currentPath"/mapper.py"
reducer=$currentPath"/reducer.py"
combiner=$currentPath"/combiner.py"

###############################################

options="-D mapred.map.tasks=10"
options=" -D mapred.reduce.tasks=30"
options=$options" -D mapred.job.priority=NORMAL"
options=$options" -file "$combiner
options=$options" -file /home/akita/dat/line/jawiki-20150512-page.sql"
options=$options" -combiner "$combiner

###############################################

echo "remove hdfs file: \""$hadoop_out"\" ?[y/n]"
read ANS

if [ $ANS = 'y' -o $ANS = 'yes' ]; then
	hadoop fs -rmr ${hadoop_out}
	hadoop jar /home/hadoop/hadoop/contrib/streaming/hadoop-streaming-1.1.2.jar  -D mapred.job.name="${jobname}" ${options} -file ${mapper} -mapper ${mapper} -file ${reducer} -reducer ${reducer} -input ${hadoop_in} -output ${hadoop_out}
fi
