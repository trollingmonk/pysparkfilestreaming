# Pysparkfilestreaming
Spark Streaming example with Pyspark


sentence_gen.py is being used to generate the contenet into the 10 (con be configured) random_logxxx.log files in to the destination folder.

Execution command :
python sentence_gen.py

textfile_streaming.py is spark streaming expaple using python to process the streaming the data in every 20 seconds that is avaialble in destination folder.

Execution command :
spark-submit --master local[2] --deploy-mode client --driver-memory 1g --executor-memory 1g textfile_streaming.py
