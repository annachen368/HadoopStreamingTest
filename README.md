# Hadoop
### 1. Install Java JDK 
### 2. Set Java Path & Hadoop Path
~/.profile add the following:
```bash
export JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64
export PATH=${JAVA_HOME}/bin:${PATH}
export HADOOP_CLASSPATH=${JAVA_HOME}/lib/tools.jar
```

(Pseudo-Distributed Mode)<br>
http://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/SingleCluster.html#Pseudo-Distributed_Operation<br>
1. Format the filesystem: <br>
  `$ bin/hdfs namenode -format` <br>
2. Start NameNode daemon and DataNode daemon:<br>
  `$ sbin/start-dfs.sh`<br>

The hadoop daemon log output is written to the $HADOOP_LOG_DIR directory (defaults to$HADOOP_HOME/logs).<br>
3. Browse the web interface for the NameNode; by default it is available at:<br>

> NameNode - http://localhost:50070/<br>

### 3. Run the following command:
```bash
$ bin/hadoop com.sun.tools.javac.Main WordCount.java
$ jar cf wc.jar WordCount*.class
``` 

### 4.
```bash
$ bin/hdfs dfs -mkdir /user/
$ bin/hdfs dfs -mkdir /user/xxx/
$ bin/hdfs dfs -mkdir /user/xxx/input/

# put the local file into the hdfs input folder
$ bin/hdfs dfs -put file01 input/
$ bin/hdfs dfs -put file02 input/
$ bin/hdfs dfs -cat /user/xxx/output/part-r-00000
```
More detail: http://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html


## Installation
### Install PyExZ3:
	sudo apt-get update
	sudo apt-get install git
	sudo apt-get install g++
	sudo apt-get install make
	cd
	git clone https://github.com/QubitPi/z3.git
	python scripts/mk_make.py
	cd build
	make
	sudo make install
	cd
	git clone https://github.com/QubitPi/PyExZ3.git
	export PYTHONPATH=path_to/z3/build

### Run Python program using Hadoop Streaming API: 
	bin/hadoop jar ./share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -file python/mapper.py -mapper python/mapper.py -file python/reducer.py -reducer python/reducer.py -input /user/anna/python/input/* -output /user/anna/python/output/
