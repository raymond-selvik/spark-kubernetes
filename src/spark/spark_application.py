import configparser
from pyspark import conf

from pyspark.sql import SparkSession
from pyspark.conf import SparkConf

class SparkApplication:
    def __init__(self, name, config_file):
        conf = self._readSparkConfig(config_file)


        self.spark = SparkSession.builder.appName(name).config(conf=conf).getOrCreate()

    def _readSparkConfig(self, config_file):
        config = configparser.ConfigParser()
        try:
            with open(config_file) as f:
                config.read_file(f)
        except IOError:
            print("Could not read config.")

        spark_conf = SparkConf().setAll(config.items("spark"))
        return spark_conf

    def stop(self):
        self.spark.stop()
        

        


        