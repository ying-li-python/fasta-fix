"""
Welcome! The purpose of this script is to help fix the spacing issue 
when a sequence is downloaded as a FASTA file from a public database. 

The result will give you the entire sequence in a single line and stored 
in a new fasta file. 

Please see READNE.md for detailed instructions. 
"""

# import dependencies
import os

# open and read FASTA file
fastafile = open("FlyBase_YGMHKX.fasta", 'r')

# assign variables to store header and sequence result
fasta_header = ''
fixed_sequence = ''

# create for loop to iterate every line of the file
for line in fastafile: 

	# strips line 
	line = line.strip()

	# for header that starts with the symbol >
	if line[0] == ">":

		# create a variable that stores the header information with the symbol > at the start
		fasta_header = ">" + line[1:]
	
	# for lines that do not start with the symbol > 
	else:  

		# concatenate lines and store sequence to variable 
		fixed_sequence = fixed_sequence+line 

# print results in terminal 
print(f'{fasta_header}\n{fixed_sequence}')


# write results in output file 
with open("output.fasta", "w") as output_file: 
	output_file.write(f'{fasta_header}\n{fixed_sequence}')

# close files 
fastafile.close()
output_file.close()