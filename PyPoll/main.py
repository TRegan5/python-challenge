import os
import csv


elect_path = os.path.join('Resources','election_data.csv')
#num_records = 0
with open(elect_path) as elect_file:
    elect_reader = csv.reader(elect_file, delimiter = ',') #create reader pointer

    elect_header = next(elect_reader) #advance from header to first data containng row
    print(f"Election Data Header: {elect_header}")
    #election_d = {}
    #print(election_d)
    for row in elect_reader: #read through each row in reader
        election_d = {row[0] : [row[1], row[2]]}
        
print((election_d))