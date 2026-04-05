from utils.spark_session import get_spark
from pyspark.sql import functions as F

def run(input_path):
    print("Running aggregation...")

    spark = get_spark()

    df = spark.read.parquet(input_path)

    agg_df = df.groupBy("coin").agg(
        F.avg("price").alias("avg_price")
    )

    output_path = input_path.replace("processed", "aggregated")

    agg_df.write.mode("overwrite").parquet(output_path)

    print(f"Saved aggregated data → {output_path}")
    return output_path