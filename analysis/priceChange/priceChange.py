from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql import Window
import pyspark.sql.functions as func
def file(filename):
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

  df = spark.read.load('../data/owners_price/sales_discounts/*.csv'+filename, format="csv", header="true", sep=',', schema=customSchema)
  #df.printSchema()
  #df.show()
  w = Window.orderBy("date")
  df.withColumn("rn",row_number().over(w)).\
  withColumn("PriceChangeTo",lead(col("Price"),1).over(w)).\
  withColumn("discount", func.round((col("PriceChangeTo")/ col("Price"))*100, 2)).\
  where(col("Price") != col("PriceChangeTo")).\
  drop("rn","event","link","color", "val3").\
  toPandas().to_csv("priceChange/res"+filename, header = True, index = False)

 my_file = open("../data/priceList/list.txt", "r")
  
# reading the file
data = my_file.read()
  
list = data.split("\n")
for i in list:
    file(i) 