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
