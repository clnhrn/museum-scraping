import pandas as pd
# set path to csv
path = "PATH-TO-CSV"
# iterate through the data, set chunksize to 50000 rows, then save to csv
for i, chunk in enumerate(pd.read_csv(path, chunksize=50000, dtype='string')):
    chunk.to_csv('NAME-OF-MUSEUM-{}.csv'.format(i), index=False)
