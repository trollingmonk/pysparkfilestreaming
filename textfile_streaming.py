import sys
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

def main():
 sc = SparkContext(appName='PysparkStreaming')
 ssc = StreamingContext(sc,20)
 lines = ssc.textFileStream('C:\\Users\\rpawar2\\Spark3\\datafolder\\')
 counts = lines.flatMap(lambda line: line.split(" ")).map(lambda x: (x, 1)).reduceByKey(lambda a, b: a + b)
 counts.pprint()
 ssc.start()
 ssc.awaitTermination()

if __name__ == "__main__":
 main()