from utils.spark_session import get_spark

def run(input_path):
    print("Running transformation...")

    spark = get_spark()

    df = spark.read.csv(input_path, header=True, inferSchema=True)

    df = df.filter(df.price > 0)

    output_path = input_path.replace("raw", "processed")

    df.write.mode("overwrite").parquet(output_path)

    print(f"Saved processed data → {output_path}")
    return output_path