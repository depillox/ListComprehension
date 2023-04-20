#Name: Zavier DePillo
#Email: depillzj@mail.uc.edu
#Assignment Title: Assignment 06
#Course: IS 4010
#Semester/Year: Spring 2023
#Brief Description: List Comprehension with external dataset
#Citations:
#Anything else that's relevant:

from functionPackage.function import *

data = read_CSV_file(r"Warehouse_and_Retail_Sales.csv") # Question 3

maxValue = 0 # Question 4
for row in data:
    if float(row[-1]) > maxValue: maxValue = float(row[-1])
print(maxValue)

maxWarehouse = max([float(row[-1]) for row in data]) #Question 5
print(maxWarehouse)

uniqueType = set([row[5] for row in data]) # Question 6
print(len(uniqueType))

print(list(uniqueType)[0:5])

'''
uniqueType = set({data[:5] for data in data})  # Question 6

uniqueType = dict(zip(5, [1.count(data) for data in 5]))
print(set[5])'''
