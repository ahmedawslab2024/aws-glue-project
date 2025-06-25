import sys
from awsglue.context import GlueContext
from pyspark.context import SparkContext

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Load silver layer
df_trans = spark.read.parquet("s3://your-bucket/silver/transactions_cleaned/")
df_tiers = spark.read.csv("s3://your-bucket/raw/tiers.csv", header=True)

# Join and write as Iceberg
df_joined = df_trans.join(df_tiers, "tiers_id", "left")
df_joined.write.format("iceberg").mode("overwrite").save("s3://your-bucket/gold/transactions_iceberg/")