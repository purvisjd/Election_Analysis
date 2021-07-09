#import modules
import os
import csv

#set path for input and output files
election_file_load = os.path.join("Resources", "election_results.csv")
output_file = os.path.join("Analysis", "election_analysis.txt")

#use With statements to open the read file
with open(election_file_load) as election_file:

    #read file with reader function
    file_reader = csv.reader(election_file)

    #read and print header row
    headers = next(file_reader)
    print(headers)





#1)  Total number of votes cast
#2)  Complete list of candidates who received votes
#3)  The percentage of votes each candidate won
#4)  The total number of votes each candidate won
#5)  The winner of the election based on popular vote

#close data file