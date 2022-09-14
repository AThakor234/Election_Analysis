# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_options = []
county_votes ={}



# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
winning_county = ""
votes_count = 0
votes_percent = 0
Largest_County_Turnout = 0



# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]


        # If the candidate does not match any existing candidate add it to the candidate list
        if candidate_name not in candidate_options:

        # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

        # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the  county does not match any existing county in the county list.
        if county_name not in county_options:
        # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)

        # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0
        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

# 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
            # Retrieve vote count and percentage.
            # 6b: Retrieve the county vote count.
            votes1 = county_votes[county_name]
            # 6c: Calculate the percentage of votes for the county.
            vote1_percentage = float(votes1) / float(total_votes) * 100

            # 6d: Print the county results to the terminal.
            county_result = (f"{county_name}: {vote1_percentage:.1f}% ({votes1:,})\n")
            print(county_result, end="")
            txt_file.write(county_result)
    max_county_turnout = max(county_votes, key=county_votes.get)
    county_max_result =(
                f"--------------------------\n"
                f"Largest County Turnout: {max_county_turnout:}\n"
                f"--------------------------\n"
            ) 
    txt_file.write(county_max_result)


            # 6e: Save the county votes to a text file.
            #txt_file.write(county_result)

        #for candidate_name in candidate_votes:
            # Retrieve vote count and percentage.
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print each candidate, their voter count, and percentage to the
        # terminal.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidates' results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)
