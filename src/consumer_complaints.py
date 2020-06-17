import csv
import functions.py

with open("./input/complaints.csv","r",encoding='UTF-8') as input:
    rdr= csv.reader( input )
    with open("report.csv","w", newline='') as output:
        wtr= csv.writer( output )
        for r in rdr:
            wtr.writerow((r[0],r[1],r[7]))
            
f = open("report.csv","r")
next(f)
csv_f = csv.reader(f)
v=list(csv_f)
    
M = list(zip(*(filter_year_from_date(v))))
M[0], M[1] = M[1], M[0]
filtered_fields=[list(t) for t in zip(*M)]

for r in interchange_columns_count(filtered_fields):
    r[0]=list(r[0])
    r[0].append(r[1])
    ordered.append(r[0])

for r in interchange_columns_count(set((map(tuple,filtered_fields)))):
    third_column.append(r[1])
    
for r in ordered:
    r.append(third_column[i])
    i+=1
            
with open("report.csv","w", newline='') as output:
        wtr= csv.writer( output )
        for r in percentage_double_quotes(ordered):
            wtr.writerow(r)
