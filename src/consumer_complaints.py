#This module is used for performing operations on .csv files
import csv

#This module is used to accept command line arguments as input
import sys                 

#initializing global iterator and emply lists for storage of temporary lists
i,ordered,third_column=0,[],[]                             

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
    #mapping the items in the list to a tuple and iterating through a set    
    for x in (set((map(tuple,a)))):                 
        b.append([x,a.count(list(x))])
    #sorting the output list so that the products are displayed in alphabetical order and the years are sorted as well
    return(sorted(b))                               

def percentage_double_quotes(fin):
    """
    Input: Final list with the columns in the order product,date, number of complaints recieved that year, minimum number of companies recieving the complaint
    Output: List where the last column contains the percentage and the product name is has quotes and is in lower case
    Function: This function first converts the first field in the list into lowercase and then checks whether it contains a ",". If yes, it adds quotes to the field. After this, percentage is calculated for the third and fourth fields and the value is appended to the last column of the list.
    """
    for i in fin:
        #converting the product names in the first column into lower case
        i[0]=i[0].lower()               
        if "," in i[0]:
            i[0]=str(i[0])
            #i[0]= '"' + str + '"'
        #adding quotes to the product names that contain "'"in them    
        d=round((i[3]/i[2])*100)
        i.append(d)
    return(fin)

def filter_year_from_date(v):
    """
    Input:Initial list with three columns in the order date, product and company
    Output: List where the date column contains only the year
    Function: This function splits the values in the cell and filters out the year part,immaterial of what format the date is of
    """
    for row in v:
        """
        If the date is of the format mm/dd/yyyy, yyyy/mm/dd, yyyy-mm-dd, mm-dd-yyyy or any of the combinations with "/" or "-" in it, the year part is filtered out accordingly.
        """
        if "/" in row[0]:
            parts=row[0].split('/')
            for a in parts:
                if len(str(a)) == 4:
                    row[0]=a
        elif "-" in row[0]:
            parts=row[0].split('-')
            for a in parts:
                if len(str(a)) == 4:
                    row[0]=a
        else:
            #error handled in case the date is not in proper format
            print("Date not in proper format")
    return (v)

def capture_columns(file):
    with open(file,"r",encoding='UTF-8') as input:
        rdr= csv.reader(input)
        i=list(rdr)
        k=list(i[0])
        global date_index,product_index,company_index
        for i in k:
            if i.lower() == "date received":
                date_index = k.index(i)
            elif i.lower() == "product":
                product_index = k.index(i)
            elif i.lower() == "company":
                company_index = k.index(i)
    return(date_index,product_index,company_index)

if __name__ == '__main__':
    """
    Function: Main function with the function calls and operations with input and output files
    """
    #accepting the second and third arguements of the command line as the input and output file respectively
    input_file = sys.argv[1]                    
    output_file = sys.argv[2]                   
    #using the csv attributes for reading from and writing into files
    #opening the input file in the UTF-8 format
    date,product,company=capture_columns(input_file)
    with open(input_file,"r",encoding='UTF-8') as input:            
        rdr= csv.reader(input)    
        with open(output_file","w", newline='') as output:
            wtr= csv.writer( output )
           #filtering out only the Product, Date and Company fields
            for r in rdr:
                #print(r[0])
                wtr.writerow((r[date],r[product],r[company]))
    
    #All operations performed from the output file contents
    f = open(output_file,"r")
    #skipping the row with column labels
    next(f)                     
    csv_f = csv.reader(f)
    #converting the contents of the file into a list
    v=list(csv_f)
    
    #fitering out the year from the date field in the entire input,interchanging the first and second column to be in the format (Product,Year) and adding the company field
    M = list(zip(*(filter_year_from_date(v))))              
    #M[0], M[1] = M[1], M[0]                                 
    filtered_fields=[list(t) for t in zip(*M)]              
    
    #iterating through the list with the number of complaints recieved in a year
    for r in interchange_columns_count(filtered_fields):        
        r[0]=list(r[0])                                           
        r[0].append(r[1])
        ordered.append(r[0])                                    

    #counting the number of companies with atleast one complaint per product and adding the count to another new list    
    for r in interchange_columns_count(set((map(tuple,filtered_fields)))):    
        third_column.append(r[1])
        
    #appending the count to the last column of the main list
    for r in ordered:
        r.append(third_column[i])                                           
        i+=1
        
    #converting everything to lowercase and adding percentage,adding quotes to the product and writing the final list to the output file        
    with open(output_file,"w", newline='') as output:
            wtr= csv.writer( output )
            for r in percentage_double_quotes(ordered):                        
                wtr.writerow(r)                                                
