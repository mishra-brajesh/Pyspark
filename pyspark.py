
from pyspark.sql import SparkSession
import spark.implicits._#Useful for toDF method

  


 
spark= SparkSession.builder().master("local[1]").appName("SparkByExamples.com").getOrCreate();
"""
Note:
1. Use local[x] when running in Standalone mode.Ideally, x value should be the number of CPU cores you have.
2. When using cluster mode it can be yarn or mesos.
"""
spark.version #Spark version
spark.sparkContext.setLogLevel("ERROR")#Change log level to debug, info, warn, fatal and error



##############################CREATION OF RDD######################################

rdd=spark.sparkContext.parallelize([1,2,3,5],10)#Here 10 is the number of partition we want to do 

1. Read all text files from a directory to single RDD #spark.sparkContext.textFile("C:/tmp/files/*")
2. Read text files base on wildcard character #spark.sparkContext.textFile("C:/tmp/files/text*.txt")
3. Read multiple text files into a RDD #spark.sparkContext.textFile("C:/tmp/files/text01.txt,C:/tmp/files/text02.txt")
4. Read files and directory together #spark.sparkContext.textFile("C:/tmp/files/text01.txt,C:/tmp/files/text02.txt,C:/tmp/files/*")

rdd = spark.sparkContext.textFile("C:/tmp/files/*")
rdd.foreach(f=>{println(f)})

#RDD from a dataframe
val myRdd2 = spark.range(20).toDF().rdd


# Creates empty RDD with no partition    
rdd = spark.sparkContext.emptyRDD 

##############################CREATION OF DATAFRAME#################################
from pyspark.sql.types import StructType,StructField, StringType, IntegerType

data2 = [("James","","Smith","36636","M",3000),
    ("Michael","Rose","","40288","M",4000),
    ("Robert","","Williams","42114","M",4000),
    ("Maria","Anne","Jones","39192","F",4000),
    ("Jen","Mary","Brown","","F",-1)
  ]

schema = StructType([ \
    StructField("firstname",StringType(),True), \
    StructField("middlename",StringType(),True), \
    StructField("lastname",StringType(),True), \
    StructField("id", StringType(), True), \
    StructField("gender", StringType(), True), \
    StructField("salary", IntegerType(), True) \
  ])

df = spark.createDataFrame(data=data2,schema=schema)
df.printSchema()
df.show()#It will show top 20 rows from the dataframe or we can pass the number of rows in parenthesis.

df = spark.read.csv("/tmp/resources/zipcodes.csv")#creation of dataframe from external source