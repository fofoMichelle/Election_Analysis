print("hello world")

counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1]) 
counties= ["Arapahoe", "Denver", "Jefferson"]
if"El Palso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")
if "Arapahoe" in counties and "El Paso" in counties:
    print ("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties")
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties. ")
for county in counties:
    print(county)
    county = "Arapahoe"
    county = "Denver"
    county = "Jefferson"
counties_dict = {"Arapahoe":422829,"Denver":463353,"Jefferson":432438}
for county in counties_dict:
    print(county)
for voters in counties_dict.values():
     print(voters)   

for county, voters in counties_dict.items():
    print(county,voters,)
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
{"county":"Jefferson","registered_voters": 432438},
{"county":"Denver","registered_voters" : 463353}]

for county_dict in voting_data:
    print(county_dict)
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))

message_to_candidate = ( f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")
print(message_to_candidate)
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("ressources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}
# Open the election results and read the file.
with open(file_to_load) as election_data:
  file_reader = csv.reader(election_data)
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
        # Read the header row.
headers = next(file_reader)
# Print each row in the CSV file.
for row in file_reader:
# Add to the total vote count.
  total_votes += 1
# Print the candidate name from each row.
candidate_name = row[2]
if candidate_name not in candidate_options:
# Add the candidate name to the candidate list.
  candidate_options.append(candidate_name)

# Begin tracking that candidate's vote count.
candidate_votes[candidate_name] = 0

# Add a vote to that candidate's count.
candidate_votes[candidate_name] += 1
# Determine the percentage of votes for each candidate by looping through the counts.
            
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
# 2. Retrieve vote count of a candidate.
  votes = candidate_votes[candidate_name]
# 3. Calculate the percentage of votes.
vote_percentage = float(votes) / float(total_votes) * 100
#  To do: print out each candidate's name, vote count, and percentage of
# votes to the terminal
print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
# Determine winning vote count and candidate

# Determine if the votes is greater than the winning count.
if (votes > winning_count) and (vote_percentage > winning_percentage):
# If true then set winning_count = votes and winning_percent =
# vote_percentage.
  winning_count = votes
  winning_percentage = vote_percentage
# And, set the winning_candidate equal to the candidate's name.
winning_candidate = candidate_name
   
