import os
import csv

budget_data= os.path.join("budget_data.csv")

# Print to terminal and write to file

def print_and_write(text, file=None):
	formatted_text=text+ "\n"  # Add newline character for consistent formatting
	print(formatted_text, end="") # Use end="" to prevent a new line after
	if file:
		file.write(formatted_text)  #write formatted text to file

#Open text file for writing

output_file_path="output.txt"
with open(output_file_path, 'w') as output_file:

	# Print to terminal and write to file

	print_and_write("Financial Analysis", output_file)
	print_and_write("------------------------------------------", output_file)

	#Functions to count Months as unique elements
	def count_unique_elements(budget_data, column_index):

		unique_elements=set()

		with open(budget_data, newline="") as csvfile:

			header_row= next(csvfile) #skip header row

			csvreader=csv.reader(csvfile)
		
			#skip header row
			next (csvfile)
		
			for row in csvreader:
				for item in row:

					csvreader=csv.reader(csvfile, delimiter=",")

					if len(row)> column_index:
						unique_elements.add(row[column_index])

		return len(unique_elements), header_row

	#Count total number of months
	column_index=0
	total_months, header_row=count_unique_elements(budget_data, column_index)
	print_and_write(f"Total Months: {total_months}", output_file)

	#Function to sum profits column in range
	def sum_column_in_range(budget_data, column_index, start_row, end_row):

		total=0

		with open(budget_data, newline="") as csvfile:

			csvreader=csv.reader(csvfile)
			next (csvfile)  #skip header row

			for i, row in enumerate(csvreader):
				if start_row <=i <= end_row:
					if len(row)> column_index:  #check if the column exists in this row
						try:
							total+=int(row[column_index]) 
						except ValueError:
							pass   #ignore non-numeric values	
		return total

	#Sum total profits	
	column_index=1
	start_row=0
	end_row=87
	total=sum_column_in_range(budget_data, column_index, start_row, end_row)

	print_and_write(f"Total: ${total}", output_file)

	#Function to calulate average change in profit 

	def average_change_in_column (budget_data, column_index):
		changes=[]
		with open(budget_data, newline="") as csvfile:
			csvreader=csv.reader(csvfile)
			next(csvreader)#skip headerrow
			previous_value=None
			for row in csvreader:
				if len(row)>column_index:
					try:
						current_value=float(row[column_index])
						if previous_value is not None:
							change=current_value-previous_value
							changes.append(change)
						previous_value=current_value
					except ValueError:
						pass # Ignore non-numeric values
			if changes:
				average_change=sum(changes)/len(changes)
				return average_change
		
			#If no changes found, return 0	
			else:
				return 0 
	#Calculate average change			
	column_index=1
	average_change=average_change_in_column(budget_data, column_index)
	print_and_write(f"Average change: ${round(average_change,2)}",output_file)

	#Function to find the greatest increase and decrease in profits

	def find_greatest_increase_decrease_with_dates(budget_data,column_index, column_index_date):
		greatest_increase=float('-inf')  #Initialize with negative infinity
		greatest_increase_date=None   #Initialize with date as none
		greatest_decrease_date=None
		greatest_decrease=float('inf')  #Initialize with negative infinity

		with open(budget_data, newline="") as csvfile:
			csvreader=csv.reader(csvfile)
			
			next(csvreader)#skip header row
			previous_value=None

			for row in csvreader:
					if len(row)>column_index and len(row)>column_index_date:
							try:
								current_value=float(row[column_index])
								current_date=row[column_index_date]
								if previous_value is not None:
									change=current_value-previous_value
									if change>greatest_increase:
										greatest_increase=change
										greatest_increase_date=current_date
									if change<greatest_decrease:
										greatest_decrease=change
										greatest_decrease_date=current_date
								previous_value=current_value
							except ValueError: 
								pass #Ignore non-numeric values

			return greatest_increase, greatest_increase_date, greatest_decrease, greatest_decrease_date

	#Find greatest increase and greatest decrease with the related months		
	column_index=1
	column_index_date=0
	(greatest_increase, greatest_increase_date, greatest_decrease, greatest_decrease_date)=find_greatest_increase_decrease_with_dates(budget_data,column_index, column_index_date)

	print_and_write(f"Greatest increase in Profits: {greatest_increase_date} (${round(greatest_increase)})", output_file)
	print_and_write(f"Greatest decrease in Profits: {greatest_decrease_date} (${round(greatest_decrease)})",output_file)


#Output saved to output.txt



