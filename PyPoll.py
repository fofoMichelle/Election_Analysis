
import csv
import os

file_to_load = os.path.join("Ressources","election_results.csv")
# Assign a variable for the file to load and the path
file_to_save = os.path.join("analysis","election_analysis.txt")
election_data = open(file_to_load,'r')
# Open the election results and read the file
with open(file_to_load) as election_data:
     print(election_data)
#Open the election results and read the file
file_to_load = 'Ressources/election_results.csv'
election_data = open(file_to_load,'r')

# Close the file.
election_data.close()
# Open the election results and the file
with open(file_to_load) as election_data:
#To do perform analysis
     print(election_data)

file_to_save = os.path.join("analysis", "election_analysis.txt")
# Print the file object.
print(election_data)
#create a filename variable to a direct or indirect path to the file.

#using the open() function with the "w" mode we will write data to the file
open(file_to_save, "w")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")

# Close the file
outfile.close()
#create a file name variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis","election_analysis.txt")
# Open file to save as a text file
with open(file_to_save, "w") as txt_file:
#write some data to the file
 txt_file.write("Arapahoe, ")
 txt_file.write("Denver, ")
 txt_file.write("Jefferson, ")
 # Write three counties to the file
 txt_file.write("Counties in the Election\n""\nArapahoe\nDenver\nJefferson")
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Ressources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:
  #Read the file object with the reader function.
 file_reader = csv.reader(election_data)
 # Read and print the header row.
 headers = next(file_reader)
print(headers)
