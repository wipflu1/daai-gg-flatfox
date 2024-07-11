import pandas as pd
import requests

df = pd.read_csv("flatfox.csv")
df =df[['pk','latitude','longitude']]


lat = ""
lon = ""
apiKey = "AIzaSyAVcOjnwFLQdi_LNZD5QD7wv6PPSRk3mPI"
results=[]

for index, row in df.iterrows():
    lat = str(row['latitude'])
    lon = str(row['longitude'])
    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?latlng=' + lat + ',' + lon + '&key=' + apiKey )
    json = response.json()
    #print(json)
    try:
        print(json["results"][0]["formatted_address"])
        results.append(json["results"][0]["formatted_address"])
    except:
        print("BAD_DATA")
        results.append("BAD_DATA")
df['streetAddress'] = results


df.to_csv("pkAddress.csv", index=False)
