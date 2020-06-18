## Heading
This repository contains solved [consumer complaints coding challenge](https://github.com/InsightDataScience/consumer_complaints)

## Overview
The `consumer_complaints.py` script reads the input file, filters out the required colums of date, product and company. These three fields are written to the output file in the start after which the necessary operations are performed on them. There are mainly 5 tasks that are being performed here:
* The year is filtered out from the date field
* The (product,year) pairs are counted forming the third column - total number of complaints recieved for that particular year and product.
* The unique (product,year,company) sets are counted forming the fourth column which is the number of complaints that went to atleast one     company for a particular product and year.
* The percentage is calculated between the prevous two columns forming the fifth column - highest percentage (rounded to the nearest whole   number) of total complaints filed against one company for that product and year
* One another specification is that the products which contain "," in it are displayed with "" whereas the others are not.

## Instructions
The 'run.sh' file in the home directory can be used for execution. Also, execution can be triggered by executing the following command in the terminal

```

python3.7 ./src/consumer_complaints.py ./input/complaints.csv ./output/report.csv

```
The above command takes input and output file paths as arguments. The output file is pushed into the following path when the program consumer_complaints.py is executed.
