from spark.spark_application import SparkApplication


def main():
    app = SparkApplication("test", 'config.ini')


if __name__ == "__main__":
    main()