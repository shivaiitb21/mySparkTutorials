import findspark
findspark.init()
findspark.find() 

#Import pyspark
from pyspark.sql import SparkSession

df = spark.read.csv("E:\Shivanand\Learnings\Spark\gdp_up.csv",header=True, inferSchema=True)
df.printSchema()
df.describe().toPandas()
