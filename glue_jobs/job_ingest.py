import sys
from awsglue.context import GlueContext
from pyspark.context import SparkContext

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Read CSV from S3
df = spark.read.csv("s3://your-bucket/raw/transactions.csv", header=True)

# Clean data (example)
df_clean = df.dropna()

# Save to silver layer as parquet
df_clean.write.mode("overwrite").parquet("s3://your-bucket/silver/transactions_cleaned/")