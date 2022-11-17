from pyspark.sql import SparkSession
from pyspark import SparkContext

sc = SparkContext(appName="Test Pyspark")
spark = SparkSession(sc)
# spark = SparkSession.builder.master("local").appName("Sparklocal").getOrCreate()
# sc = SparkSession.sparkContext
df = spark.read.csv("test.csv", header=True)
df.write.csv("output.csv") #! This is a dir!

print(df.show())

sc.stop()
