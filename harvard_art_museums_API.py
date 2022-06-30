import pandas as pd
import requests
import json

API_key = "YOUR-API-KEY"
page = 1
# For this particular API, a request will return a default of 10 records/page, set size to maximum (100 records/page)
url = "https://api.harvardartmuseums.org/object?apikey={}&size={}&page={}".format(API_key, 100, page)
# Create an empty list for the artworks
records_list = []
# Set up a count variable to keep track of the number of items being added to the list
count = 0

# Run the program until it reaches the last page of artworks
while page < 2401:
    print("Page: " + str(page))
    response = requests.request("GET", url)
    if response is not None:
        page += 1
        data = json.loads(response.text)
        for i in data['records']:
            count += 1
            print("Row "+str(count) + ': Success')
            records_list.append(i)

# Create a dataframe from the list of artworks and export to CSV
df = pd.DataFrame(records_list, dtype='string')
df.to_csv('harvard-art-museums.csv', index=False)
