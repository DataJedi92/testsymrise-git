# Get the database using the method we defined in pymongo_test_insert file
from mongodb_connection import get_database
import re
import json



def insert_data_into_mongodb(collection_name_input, list_data):
    dbname = get_database()
    collection_name = dbname[collection_name_input]
    collection_name.drop()
    collection_name.insert_many(list_data)

    return 0

# insert_data_into_mongodb('user_shopping_list',[item_1,item_2])

def get_data_from_mongodb(collection_name_input, field):
    dbname = get_database()
    collection_name = dbname[collection_name_input]
    date_re = re.compile(r'.*T15.*') # get temperature of the day at 1pm only
    raw_data = collection_name.find({"timestamp" : date_re},{field:1})
    
    res = [i[field] for i in raw_data]
    # print('res : ', res)
    return res

#voyons = get_data_from_mongodb('weather', 'temperature')
#print('voyons : ', voyons)
#for i in voyons:
#    print(i["temperature"])


def read_json_file(filename):
    # Opening JSON file
  f = open(filename)
  
  # returns JSON object as 
  # a dictionary
  data = json.load(f)
  

  
  # Closing file
  f.close()

  list_data = []
  for i in data['resultlist.resultlist']["resultlistEntries"][0]["resultlistEntry"]:
    #transformation to replace DOT by UNDERSCORE because dot in fieldname is ticky to request
    j=json.dumps(i)
    # print('j : ',j)
    h = json.loads(j)
    # print('h : ',type(h))
    h['resultlist_realEstate'] = h.pop('resultlist.realEstate')
    # print(' content h : ', h)
    list_data.append(h)

  

  #return data['resultlist.resultlist']["resultlistEntries"][0]["resultlistEntry"]
  return list_data
  


#locate = r'C:\Users\nnehm\symrise\testsyrime-git\testsymrise\total_cities.json'
#res = read_json_file(locate)
#print(len(res))


def get_ratio_aircon_from_mongo(collection_name_input, city):
  dbname = get_database()
  collection_name = dbname[collection_name_input]
  re_exp = re.compile(r'.*Klimaanlage.*')

  raw_data = collection_name.find()
  nb_total_document_per_city = collection_name.count_documents({"resultlist_realEstate.address.city": city})
  nb_total_document_per_city_with_aircon = collection_name.count_documents({"resultlist_realEstate.title":re_exp,"resultlist_realEstate.address.city": city})

  print("nb_total_dicument ",city," : ", nb_total_document_per_city)
  print("nb_total_dicument with AC ",city," : ", nb_total_document_per_city_with_aircon)


  return round(nb_total_document_per_city_with_aircon/nb_total_document_per_city, 2)

#get_ratio_aircon_from_mongo('real_estate', 'Berlin')