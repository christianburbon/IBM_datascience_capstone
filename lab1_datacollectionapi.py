# Requests enable HTTP requests to get data frop API
import requests
import pandas as pd
import numpy as np
# Datetime library for date representation
import datetime

#%% 
# print all columns of a dataframe
pd.set_option('display.max_columns',None)
# prinat all of the data in a feature
pd.set_option('display.max_colwidth',None)

# %% Define Booster Name
# Takes the dataset and uses the rocket column to call the API and append the data to the list
def getBoosterVersion(data):
    for x in data['rocket']:
        if x:
            response = requests.get("https://api.spacexdata.com/v4/rockets/"+str(x))
            BoosterVersion.append(response['name'])
# %% Define Launch Site - Long and Lat
# Takes the dataset and uses the launchpad column to call the API and append the data to the list
def getLaunchSite(data):
    for x in data['launchpad']:
        if x:
            response = requests.get("https://api.spacexdata.com/v4/launchpads/"+str(x)).json()
            Longitude.append(response['longitude'])
            Latitude.append(response['latitude'])
            LaunchSite.append(response['name'])
#%% from "cores" table, identify outcome and features
# Takes the dataset and uses the cores column to call the API and append the data to the lists
def getCoreData(data):
    for core in data['cores']:
        if core['core'] != None:
            response = requests.get("https://api.spacexdata.com/v4/cores/"+core['core']).json()
            Block.append(response['block'])
            ReusedCount.append(response['reuse_count'])
            Serial.append(response['serial'])
        else:
            Block.append(None)
            ReusedCount.append(None)
            Serial.append(None)
        Outcome.append(str(core['landing_success'])+' '+str(core['landing_type']))
        Flights.append(core['flight'])
        GridFins.append(core['gridfins'])
        Reused.append(core['reused'])
        Legs.append(core['legs'])
        LandingPad.append(core['landpad'])
#%% Request rocket launch data from SpaceX API
spacex_url = "https://api.spacexdata.com/v4/launches/past"
response = requests.get(spacex_url)
#%% Check Contect of the response
print(response.content)
#%% Task 1: Request and parse the SpaceX launch data using the GET request
#json consistency
static_json_url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/API_call_spacex_api.json'
print(response.status_code)
df = response.json().json_normalize()
# %%
