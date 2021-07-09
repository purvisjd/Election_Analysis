#import modules
import os
import csv

#set path for input and output files
election_file_load = os.path.join("Resources", "election_results.csv")
output_file = os.path.join("Analysis", "election_analysis.txt")

#initialize vote counter
total_votes = 0

#use With statements to open the read file
with open(election_file_load) as election_file:

    #read file with reader function
    file_reader = csv.reader(election_file)

    #read and print header row
    headers = next(file_reader)

    #decleare candidates list
    candidates = []
    #delcare candidates dictionary
    candidate_votes = {}


    #declare winning candidate variables
    winner = ""
    winning_count = 0
    winning_percentage = 0

    #print rows in file
    for row in file_reader:
        #count total votes
        total_votes = total_votes + 1
        
        #get candidate name
        candidate_name = row[2]

        #add unique candidate name to candidates list
        if candidate_name not in candidates:

            #add candidate name to candidate list
            candidates.append(candidate_name)

            #track candidate's vote count
            candidate_votes[candidate_name] = 0
        
        #count number of votes for candidate
        candidate_votes[candidate_name] += 1

    with open(output_file, "w") as txt_file:


        election_results = (
            f'Election Results\n'
            f'-------------------------\n'
            f'Total Votes: {total_votes:,}\n'
            f'-------------------------\n')

        print(election_results, end="")

        txt_file.write(election_results)


        for candidate_name in candidate_votes:
            final_votes = candidate_votes[candidate_name]

            #calculate percetage of vote; change numbers to floating point decimals
            vote_percentage = float(final_votes)/float(total_votes) * 100

            if (final_votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = final_votes
                winning_percentage = vote_percentage
                winner = candidate_name

            #format percentage to 1 decimal place
            #print(f'{candidate_name}: received {vote_percentage: .1f}% ({final_votes:,})\n')
            candidate_results = (f'{candidate_name}: {vote_percentage:.1f}% ({final_votes:,})\n')
            print(candidate_results)
            txt_file.write(candidate_results)

        winning_candidate_summary = (
            f'--------------------\n'
            f'Winner: {winner}\n'
            f'Winning Vote Count: {winning_count:,}\n'
            f'Winning Percentage: {winning_percentage: .1f}%\n'
        f'---------------------\n')

        txt_file.write(winning_candidate_summary)



election_file.close()
txt_file.close()

