import requests
import json
from mongodb_connection import get_database
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
from dateutil.relativedelta import relativedelta



def get_data_from_brightsky(latitude, longitude):
    

    one_yr_ago = datetime.now() - relativedelta(days=700)
    query = f"https://api.brightsky.dev/weather?date={one_yr_ago}&last_date={datetime.now()}&lat={latitude}&lon={longitude}"
    # print('query : ', query)
    
    r = requests.get(query)

    if(r.status_code == 200):

        response = r.text
        json_object = json.loads(response)
        # print(json_object["weather"])
        # print(r.text)

        return json_object["weather"]
    else:
        print('trouble when you request brightsky, error : ', r.status_code)
        exit()
    

#get_data_from_brightsky(52.52,13.4)





