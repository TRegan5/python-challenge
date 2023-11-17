import os
import csv

voter_info = []
votes = []
cand_set = []

elect_path = os.path.join('Resources','election_data.csv')
#num_records = 0
with open(elect_path) as file:
    elect_reader = csv.reader(file, delimiter = ',') #create reader pointer
    elect_header = next(elect_reader) #advance from header to first data containng row

    for row in elect_reader: #read through each row in reader
        voter_info.append({row[0],row[1]}) #collect voter_id and county; not needed for later analysis, but could be zipped
        votes.append(row[2]) #list of all votes recorded
        if row[2] not in cand_set: #record each unique vote cast / candidate receiving votes
            cand_set.append(row[2])
        
total_votes = len(votes)
results = [{'name' : cand_set[0], 'pervotes' : round(votes.count(cand_set[0]) / total_votes * 100, 3), 'popvotes' : votes.count(cand_set[0])},
           {'name' : cand_set[1], 'pervotes' : round(votes.count(cand_set[1]) / total_votes * 100, 3), 'popvotes' : votes.count(cand_set[1])},
           {'name' : cand_set[2], 'pervotes' : round(votes.count(cand_set[2]) / total_votes * 100, 3), 'popvotes' : votes.count(cand_set[2])}
           ]
dash_str = ('-' * 25)
results_str = 'Election Results\n'+dash_str+'\nTotal Votes: '+str(total_votes)+'\n'+dash_str+'\n'\
                +results[0]['name']+': '+str(results[0]['pervotes'])+'% ('+str(results[0]['popvotes'])+')\n'\
                +results[1]['name']+': '+str(results[1]['pervotes'])+'% ('+str(results[1]['popvotes'])+')\n'\
                +results[2]['name']+': '+str(results[2]['pervotes'])+'% ('+str(results[2]['popvotes'])+')\n'\
                +dash_str+'\nWinner: '+max(results, key=lambda x:x['popvotes'])["name"]+'\n'+dash_str
print(results_str)
with open('analysis/analysis.txt', 'w') as a_file:
    a_file.writelines(results_str)