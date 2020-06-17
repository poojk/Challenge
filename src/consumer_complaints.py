import csv
import sys

i=0
ordered,third_column=[],[]

def interchange_columns_count(lis):
    a,b=[],[]
    for k in lis:
        c=[k[0],k[1]]
        a.append(c)
    for x in (set((map(tuple,a)))):
        b.append([x,a.count(list(x))])
    return(sorted(b))

def percentage_double_quotes(fin):   
    for i in fin:
        if "," in i[0]:
            str=i[0]
            i[0]= "\"" + str + "\""
        d=round((i[3]/i[2])*100)
        i.append(d)
    return(fin)

def filter_year_from_date(v):
    for row in v:
        parts = row[0].split('/')
        data = parts[2]
        row[0]=data
    return(v)

if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    with open(input_file,"r",encoding='UTF-8') as input:
        rdr= csv.reader( input )
        with open(output_file,"w", newline='') as output:
            wtr= csv.writer( output )
            for r in rdr:
                wtr.writerow((r[0],r[1],r[7]))
            
    f = open(output_file,"r")
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
            
    with open(output_file,"w", newline='') as output:
            wtr= csv.writer( output )
            for r in percentage_double_quotes(ordered):
                wtr.writerow(r)
