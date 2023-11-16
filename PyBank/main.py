import os
import csv

bd_path = os.path.join('Resources','budget_data.csv')
net_total = 0
bd_list = []
bd_delta = []
num_months = len(bd_list)
#delta = 0
last_change = 0
with open(bd_path) as bd_file:
    bd_reader = csv.reader(bd_file, delimiter = ',') #create reader pointer
    bd_header = next(bd_reader) #advance from header to first data containing row
    #print(f"Budget Data Header: {bd_header}") #remove before submission!!!
        
    for row in bd_reader: #read through each row in reader
        #print(row) #remove before submission!!!
        bd_list.append(row) #insert each row of data from bd_reader, excluding header
        net_total = net_total + int(row[1])
        delta = int(row[1]) - last_change
        #print(delta) #remove before submission!!!
        bd_delta.append(delta) #list of changes in Profits/Losses
        last_change = int(row[1])

str_tm = f'Total Months: {len(bd_list)}'
str_netT = f'Total: $ {net_total}'
#print(str_tm)#f'Total Months: {len(bd_list)}')
#print(str_netT)

bd_delta.pop(0) #remove first entry; no prior entry for change
#delta_sums = sum(bd_delta) / len(bd_delta)
str_avgDelta = f'Average Change: ${round(sum(bd_delta) / len(bd_delta), 2)}' ##need to format!!!
#print(str_avgDelta)

gInc = max(bd_delta)
gInc_index = bd_delta.index(gInc)
gInc_month = bd_list[bd_delta.index(gInc)+1][0] #+1 to account for popped entry in bd_delta
str_gInc = f'Greatest Increase in Profits: {bd_list[bd_delta.index(gInc)+1][0]} (${gInc})'
#print(str_gInc)

gDec = min(bd_delta)
gDec_index = bd_delta.index(gDec)
gDec_month = bd_list[bd_delta.index(gDec)+1][0] #+1 to account for popped entry in bd_delta
str_gDec = f'Greatest Increase in Profits: {bd_list[bd_delta.index(gDec)+1][0]} (${gDec})'
#print(str_gDec)

dash_str = ('-' * 28)
str_analysis = f'Financial Analysis\n{dash_str}\n{str_tm}\n{str_netT}\n{str_avgDelta}\n{str_gInc}\n{str_gDec}'
print(str_analysis)
with open('analysis/analysis.txt', 'w') as a_file:
    a_file.writelines(str_analysis) #for L = ['Financial Analysis', str_tm, str_netT, str_avgDelta, str_gInc, str_gDec]