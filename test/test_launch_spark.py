
# importing module 
import pyspark 
  
# importing sparksession from pyspark.sql module 
from pyspark.sql import SparkSession 
  
# creating sparksession and giving an app name 
spark = SparkSession.builder.appName('sparkdf').getOrCreate() 
  
# list  of employee data with 5 row values 
data =[["1","sravan","company 1"], 
       ["2","ojaswi","company 2"], 
       ["3","bobby","company 3"], 
       ["4","rohith","company 2"], 
       ["5","gnanesh","company 1"]] 
  
# specify column names 
columns=['Employee ID','Employee NAME', 
         'Company Name'] 
  
# creating a dataframe from the lists of data 
dataframe = spark.createDataFrame(data,columns) 
  
# display dataframe 
dataframe.show()
# display dataframe using collect() 
print("First row :",dataframe.collect()[0][1]) 
  
