import os
import csv

election_data= os.path.join("election_data.csv")

# Print to terminal and write to file

def print_and_write(text, file=None):
	formatted_text=text+ "\n"  # Add newline character for consistent formatting
	print(formatted_text, end="") # Use end="" to prevent a new line after
	if file:
		file.write(formatted_text)  #write formatted text to file

#Open text file for writing

output_file_path="election_output.txt"
with open(output_file_path, 'w') as output_file:

	# Print to terminal and write to file

	print_and_write("Election Results", output_file)
	print_and_write("------------------------------------------", output_file)

	#Functions to count total votes as unique elements through ballot numbers
	def count_unique_elements(election_data, column_index):

		unique_elements=set()

		with open(election_data, newline="") as csvfile:
			csvreader=csv.reader(csvfile)
			
			header_row= next(csvfile) #skip header row
			
			#skip header row
			next (csvfile)
		
			for row in csvreader:
				for item in row:

					csvreader=csv.reader(csvfile, delimiter=",")

					if len(row)> column_index:
						unique_elements.add(row[column_index])

		return len(unique_elements), header_row

	#Count total number of votes cast
	column_index=0
	total_votes, header_row=count_unique_elements(election_data, column_index)
	print_and_write(f"Total Votes: {total_votes}", output_file)
	print_and_write("------------------------------------------")


	#Functions to print unique cadidates by names
	def get_unique_candidates_names(election_data, column_index):

		unique_candidates=set()

		with open(election_data, newline="") as csvfile:
			csvreader=csv.reader(csvfile)
		
			#skip header row
			next (csvfile)
		
			for row in csvreader:
				if len(row)> column_index:
					unique_candidates.add(row[column_index])

		return list(unique_candidates)

	#Count total number of votes cast
	column_index=2
	unique_candidates_names=get_unique_candidates_names(election_data, column_index)

	#Print unique cadidate names
	winner=None
	max_votes=0
	for candidate_name in unique_candidates_names:
		votes=0
		with open(election_data, newline="") as csvfile:
			csvreader=csv.reader(csvfile)
			next(csvfile)  #Skip header row
			for row in csvreader:
				if len(row)>2 and row[2] ==candidate_name:
					votes+=1
		percentage=(votes/total_votes)*100
		print_and_write(f"{candidate_name}:   {percentage:.3f}% ({votes})", output_file)
		if votes>max_votes:
			max_votes=votes
			winner= candidate_name

	print_and_write("------------------------------------------")
	print_and_write(f"Winner: {winner}", output_file)
	print (header_row)


#Output saved to output.txt



