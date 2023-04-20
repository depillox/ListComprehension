#Name: Zavier DePillo
#Email: depillzj@mail.uc.edu
#Assignment Title: Assignment 06
#Course: IS 4010
#Semester/Year: Spring 2023
#Brief Description: List Comprehension with external dataset
#Citations:
#Anything else that's relevant:

import csv
def read_CSV_file(file_name):
    '''
    Read from a CSV file into a list
    :param file_name: The CSV file to read. It should have a header row, which will be be skipped
    :return : the list containing all the rows except the header row
    '''
    csv_data = []
    with open(file_name, newline='') as f:
        reader = csv.reader(f, delimiter=',')
        header = next(reader)
    #   csv_data.append(header)        # We don't want the header row.
        for row in reader:
            csv_data.append(row)
    #print(csv_data)
    print (type(csv_data))      # It's a list of lists!
    return csv_data