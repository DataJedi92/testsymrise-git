from pyspark.sql import SparkSession
import pandas as pd
from pyspark.sql.functions import mean

def compute_mean_weather(input_data_weather):
    spark = SparkSession.builder.getOrCreate()
    
    data = pd.DataFrame({'Temperature': input_data_weather})
 
    # create DataFrame
    df_spark = spark.createDataFrame(data)
    
    moyenne = df_spark.select(mean(df_spark["Temperature"])).collect()[0][0]   
    
    print('mean : ', round(moyenne, 2))
    
    return round(moyenne, 2)