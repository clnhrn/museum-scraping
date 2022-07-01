# The Art Institute of Chicago provides an API and a data dump on their GitHub repository.
# You can download the full dataset here: https://artic-api-data.s3.amazonaws.com/artic-api-data.tar.bz2
# This code will iterate through the json files in the "artworks" folder, create a dataframe from the list,
# and save the data to a csv
import os
import json
import pandas as pd

# Download full dataset and copy the path of the artworks folder
directory_path = '.../artic-api-data/json/artworks'

artworks_list = []
print('Iterating through files in directory...')
for count, filename in enumerate(os.listdir(directory_path)):
    file_path = os.path.join(directory_path, filename)
    data = open(file_path)
    json_data = json.load(data)
    artworks_list.append(json_data)
    print('File #' + str(count) + ' written successfully')

print('Creating Dataframe...')
df = pd.DataFrame(artworks_list)
print('Exporting to CSV...')
df.to_csv('art-institute-of-chicago.csv', index=False)
print('Done!')
