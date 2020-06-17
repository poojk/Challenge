import csv                      #This module is used for performing operations on .csv files
import sys                      #This module is used to accept command line arguments as input

i=0                             #initializing global iterator
ordered,third_column=[],[]      #initializing emply lists for storage of temporary lists

def interchange_columns_count(lis):
    """
    Input:List with three columns in the order product,date and company
    Output: Sorted list with the column order date, product, number of occurences of a (product,year)
    Function:After interchanging the first and second columns of 
    """
    a,b=[],[]
    for k in lis:
        c=[k[0],k[1]]
        a.append(c)
    for x in (set((map(tuple,a)))):
        b.append([x,a.count(list(x))])
    return(sorted(b))

def percentage_double_quotes(fin):
    """
    Input: Final list with the columns in the order product,date, number of complaints recieved that year, minimum number of companies recieving the complaint
    Output: List where the last column contains the percentage and the product name is has quotes and is in lower case
    Function: This function first converts the first field in the list into lowercase and then checks whether it contains a ",". If yes, it adds quotes to the field. After this, percentage is calculated for the third and fourth fields and the value is appended to the last column of the list.
    """
    for i in fin:
        i[0]=i[0].lower()
        if "," in i[0]:
            str=i[0]
            i[0]= '"' + str + '"'
        d=round((i[3]/i[2])*100)
        i.append(d)
    return(fin)

def filter_year_from_date(v):
    """
    Input:Initial list with three columns in the order date, product and company
    Output: List where the date column contains only the year
    Function: This function splits the values in the cell with resoect to "-" and assigns the date part as teh value of the cell itself
    """
    for row in v:
        parts = row[0].split('-')
        data = parts[0]
        row[0]=data
    return(v)

if __name__ == '__main__':
    """
    Function: Main function with the function calls and operations with input and output files
    """
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    #using the csv attributes for reading from and writing into files
    with open(input_file,"r",encoding='UTF-8') as input:
        rdr= csv.reader( input )
        with open(output_file,"w", newline='') as output:
            wtr= csv.writer( output )
            #filtering out only the Product, Date and Company fields
            for r in rdr:
                wtr.writerow((r[0],r[1],r[7]))
    
    #All operations performed from the output file contents
    f = open(output_file,"r")
    next(f)                     #skipping the name row
    csv_f = csv.reader(f)
    v=list(csv_f)               #convering the contents of the file into a list
    
    M = list(zip(*(filter_year_from_date(v))))              #fitering out the year from the date field in the entire input
    M[0], M[1] = M[1], M[0]                                 #interchanging the first and second column to be in the format (Product,Year)
    filtered_fields=[list(t) for t in zip(*M)]              #Adding the (Product,Year) fields to the Company field

    for r in interchange_columns_count(filtered_fields):        #iterating through the list with the number of complaints recieved in a year
        r[0]=list(r[0])                                           
        r[0].append(r[1])
        ordered.append(r[0])                                    #Adding the count as another column in the main list

    for r in interchange_columns_count(set((map(tuple,filtered_fields)))):    #counting the number of companies with atleast one complaint per product
        third_column.append(r[1])                                             #adding the count to another list
    
    for r in ordered:
        r.append(third_column[i])                                           #appending the count to the last column of the main list
        i+=1
            
    with open(output_file,"w", newline='') as output:
            wtr= csv.writer( output )
            for r in percentage_double_quotes(ordered):                        #converting everything to lowercase and adding percentage and adding quotes
                wtr.writerow(r)                                                #writing the final list to the output file
