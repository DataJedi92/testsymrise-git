from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField, DecimalType, IntegerType
from pyspark.sql.functions import mean
import pandas as pd
pd.DataFrame.iteritems = pd.DataFrame.items


import graph_function as gf
import requeteApiBrightSky as rab

import transformation_functions as tf
import pymongo_functions as pf




if __name__ == '__main__':
    STUDIED_CITIES = [{"city": "Berlin", "latitude":52.52, "longitude":13.4},
                     {"city": "Koln", "latitude":50.9375, "longitude":6.9603},{"city": "Munchen", "latitude":48.1351, "longitude":11.5820}]
    

    LOCATE_JSON_FILE_REAL_ESTATE = r'C:\Users\nnehm\symrise\testsyrime-git\testsymrise\total_cities.json'

    # get reat estate data
    real_estate_data = pf.read_json_file(LOCATE_JSON_FILE_REAL_ESTATE)
    
    # push real estate data into mongodb atlas
    pf.insert_data_into_mongodb('real_estate',real_estate_data)
    
    
    spark = SparkSession.builder.getOrCreate()
    
    schema = StructType([
        StructField('city', IntegerType(), True),
        StructField('ratio_AC', DecimalType(), True),
        StructField('temperature', DecimalType(), True)
        ])
    
    df = spark.createDataFrame([], schema)

    cpt = 0
    for city in STUDIED_CITIES:
        cpt = cpt + 1
    
        
        res_weather_city = rab.get_data_from_brightsky(city["latitude"],city["longitude"])
        # print(res_weather_city)
        pf.insert_data_into_mongodb('weather',res_weather_city)
        res = pf.get_data_from_mongodb('weather', 'temperature')
        # print(res)
        
        
        ratio = pf.get_ratio_aircon_from_mongo('real_estate',city["city"])
        moyenne = tf.compute_mean_weather(res)
        # row.show()
        new_row = spark.createDataFrame([(cpt, ratio, moyenne)])
        df = df.union(new_row)
        df.show()

    gf.correlation_heatmap(df)

    

    
    

        

    