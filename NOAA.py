import matplotlib.pyplot as plt
import datetime
import pandas as pd
import numpy as np
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

from statsmodels.tsa.seasonal import MSTL
from statsmodels.tsa.seasonal import DecomposeResult
from tqdm import tqdm
import requests

def get_noaa_data(station,headers,url,start,end, debug = False):
  # start = ["2024-03-01","2023-03-01","2022-03-01"]
  # end = ["2025-03-01","2024-03-01","2023-03-01"]
  all_data = []
  data_type_list = ["TMAX", "TMIN", "PRCP", "SNOW"]
  for d in tqdm(data_type_list):
    data_type = d
    for s,e in (zip(start,end)):
      params = {
        "datasetid": "GHCND",
        "stationid": station,  # Central Park, NYC
        "startdate": s,
        "enddate": e,
        "datatypeid": data_type,
        "limit": 365*2}
      
      response = requests.get(url, headers=headers, params=params)
      if response.status_code == 200:
        if debug:
            print(response.text)
        data = response.json().get("results", [])  # Extract the 'results' key
        if data:
            # Convert to DataFrame
            df = pd.DataFrame(data)
            #print(df)  # Display DataFrame
        else:
            print("No data found for the given request.")
      else:
          print(f"Error: {response.status_code}, {response.text}")
      
      if data_type == "TMAX" or data_type == "TMIN":
        df['value'] = ( (df['value']/10) * 1.8 ) + 32
        
      else:
        df['value'] = ( (df['value']/25.4) )
        
      all_data.append(df)
      result = pd.concat(all_data, ignore_index=True).drop_duplicates()
      result = result.pivot(index=["station", "date"], columns="datatype", values=["value"]).reset_index()
      result.columns = ['_'.join(str(s).strip() for s in col if s) for col in result.columns]
      result.columns = [col.replace("value_", "") for col in result.columns]
      result["date"] = pd.to_datetime(result["date"]).dt.strftime("%Y-%m-%d")
      
  return result