import os
import time
import sys
import pandas as pd
from pyspark.sql.functions import col

from spark.spark_application import SparkApplication

from pyspark.sql import SparkSession


def main():
    sys.path.append("src/config/")

    print(sys.path)
    app = SparkApplication("kubernetes-demo", './config/config.ini')
    print(app.spark.version)
    print("Spark Session created")
    input("...Press a button to continue")



    ###CREATE, SHOW AND COUNT DATAFRAME
    df_person = app.spark.createDataFrame(
        [(1, "Alice", 33),
        (2, "Bob", 44),
        (3, "John", 36),
        (4, "Smith", 75)],
        ["id", "name", "age"]
    )

    df_address = app.spark.createDataFrame([
        ("Oxford Street 1", "London", 1),
        ("Oxford Street 2", "London", 2),
        ("Broadway 4", "Mew York", 3),
        ("Brooklyn Lane 6", "New York", 4)
    ],
    ["address", "city", "personId"],
    )

    print(df_person.count())
    print(df_address.count())

    input("...Press a button to continue")


    df_person.select("*").where(df_person['age']< 40).show()
    input("...Press a button to continue")
    

    df_person_by_address = df_person.join(df_address, df_person['id'] == df_address['personId'], "inner")
    df_person_by_address.show()


    input("Press a button to continue")

    df_person_by_address_cleaned = df_person_by_address.drop('personId')
    df_person_by_address_cleaned.show()

    input("Press a button to end program.")
    app.stop()
    


if __name__ == "__main__":
    main()
