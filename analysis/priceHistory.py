from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql import Window
import pyspark.sql.functions as func
spark = SparkSession.builder.master("local[1]").getOrCreate()
customSchema = StructType([
  StructField("date", DateType(), True),
  StructField("Owners", StringType(), True),
  StructField("event", StringType(), True),
  StructField("link", StringType(), True),
  StructField("color", StringType(), True),
  StructField("Price", DoubleType(), True),
  StructField("val3", StringType(), True),
])

df = spark.read.load('Downloads/example/374320.csv', format="csv", header="true", sep=',', schema=customSchema)
df.printSchema()
df.show()
w = Window.orderBy("date")
df.withColumn("rn",row_number().over(w)).\
withColumn("PriceChangeTo",lead(col("Price"),1).over(w)).\
withColumn("discount", func.round((col("PriceChangeTo")/ col("Price"))*100, 2)).\
where(col("Price") != col("PriceChangeTo")).\
drop("rn","event","link","color", "val3").\
toPandas().to_csv("Downloads/example/res/374320.csv", header = True, index = False)