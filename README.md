# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has tasked me with following specific tasks to complete the election audit of a recent local
congressional election.

1)  Calculate the total number of votes cast.
2)  Compile a list of each county represented and the total number of votes for each county.
3)  Calculate the percentage of the vote represented by each county.
4)  Determine the county with the largest number of votes.
5)  Get a complete list of candidates who received votes.
6)  Calculate the total number of votes each candidate received.
7)  Calculate the percentage of votes each candidate won.
8)  Determine the winner of the election based on popular vote.

## Resources
-- Data:  election_results.csv
-- Software:  Vistual Studio Code 1.58.0, Python 3.7

## Election-Audit Results:
###  Total Vote Count
*  The total votes were calculated by getting a basic count of all votes represented in the dataset.  
       The dataset was looped through, incrementally, increasing the total by one for each vote represented
       using the following code segment:
      
       `total_votes = total_votes + 1`
       


*  Based on this calculation, there were a total of 369,711 votes cast in this congressional election
###  Breakdown of votes by county:
*  A list of the unique counties represented in this dataset was isolated and then the individual total of votes
   for each county was determined using the following code:
   
   `county_name = row[1]`
   
   ...
   
   `if county_name not in county_votes:
        county_list.append(county_name)`
        
   ...
   
   `county_votes[county_name] += 1`
   
   
   
   The percentage of the total vote was then calculated with the following code:
   
   `county_percentage = float(county_total_vote)/float(total_votes)*100`


*  The following results were determined based on these calculations:
    *  Jefferson County:
        *  Received 38,855 votes; 10.5%
    *  Denver County:
        *  Received 306,055 votes; 82.8%
        *  Denver County represents the largest number of votes cast in the precinct
    *  Arapahoe County:
        *  Received 24,801 votes; 6.7%

###  Breakdown of votes by candidate:
A list of the unique candidates receiving votes was extracted from the dataset.  The total votes received
by each candidate was then tallied and their percentage of the total vote was calculated using the following
code:

`candidate_name = row[2]`

...

`if candidate_name not in candidate_options:`

    `candidate_options.append(candidate_name)`

    `candidate_votes[candidate_name] += 1`
...
`vote_percentage = float(votes)/float(total_votes) * 100`


*  Breakdown of votes by candidate:
    *  Charles Casper Stockham
        *  Received 85, 213 votes; 23.0%
    *  Diana DeGette
        *  Received 272,892 votes; 73.8%
    *  Raymon Anthony Doane
        *  Received 11,606 votes; 3.1%
 
 *  Based on the results of this audit, the winner of the popular vote was:
    *  Diana DeGette
    *  272,892 votes received
    *  73.8%
    

## Summary
This audit code successfully managed to take the raw data provided in 
[Election_Results](https://github.com/purvisjd/Election_Analysis/blob/main/Resources/election_results.csv) and extract the total number of votes cast in the precinct, the counties in which votes were cast, and the candidates receiving the votes and then calculate the number of votes per county and per candidate as well as calculate the overall percentage of votes in each category and the overall winner for the precinct.  Minimal modifications would need to be made to make the code more usable to a wider dataset.  If the general structure of the CSV file were changed, modifications to the code applying the candidate names to tables (i.e. candidate_name = row[x]) can be easily made to have the proper "column" of information searched to find the needed data.  If code were applied to a larger scale election (multiple precincts or national elections) then the only adjustments that would be needed would be to modify where within the CSV dataset the code looks for given values.  The formumlas calculating total votes, percentage of votes, etc. are already dynamic and would be adaptable to different datasets without modifications to the existing code being needed.  

