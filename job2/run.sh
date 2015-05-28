#!/bin/sh

###############################################

jobname="Job2"
hadoop_in="wiki00"
hadoop_out="wiki01"

###############################################

currentPath=`pwd`;
mapper=$currentPath"/mapper.py"
reducer=$currentPath"/reducer.py"
combiner=$currentPath"/combiner.py"

###############################################

options="-D mapred.map.tasks=40"
options=" -D mapred.reduce.tasks=40"
options=$options" -D mapred.job.priority=NORMAL"
options=$options" -file "$combiner
options=$options" -combiner "$combiner
options=$options" -file /home/akita/dat/line/toLink2.txt"

###############################################

echo "remove hdfs file: \""$hadoop_out"\" ?[y/n]"
read ANS

if [ $ANS = 'y' -o $ANS = 'yes' ]; then
	hadoop fs -rmr ${hadoop_out}
	hadoop jar /home/hadoop/hadoop/contrib/streaming/hadoop-streaming-1.1.2.jar  -D mapred.job.name="${jobname}" ${options} -file ${mapper} -mapper ${mapper} -file ${reducer} -reducer ${reducer} -input ${hadoop_in} -output ${hadoop_out}
	for i in `seq 1 99`
	do
		c=`expr $i + 1`
		hadoop_in="wiki0"${i}
		hadoop_out="wiki0"${c}
		hadoop fs -rmr ${hadoop_out}
		hadoop jar /home/hadoop/hadoop/contrib/streaming/hadoop-streaming-1.1.2.jar  -D mapred.job.name="${jobname}" ${options} -file ${mapper} -mapper ${mapper} -file ${reducer} -reducer ${reducer} -input ${hadoop_in} -output ${hadoop_out}
	done

fi
