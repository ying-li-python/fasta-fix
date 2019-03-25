"""
Welcome! The purpose of this script is to help fix the spacing issue 
when a sequence is downloaded as a FASTA file from a public database. 

The result will give you the entire sequence in a single line and stored 
in an output.txt file. 

Example: $ python fasta_fix.py
"""

# import dependencies
import os

# open .txt or .fasta file
fastafile = open("FlyBase_YGMHKX.fasta", 'r')

# create empty list to store gene name (starts at >) and sequence result
fasta_name = ''
fixed_sequence = ''

# creatae for loop to iterate every line of the file
for line in fastafile: 

	# strips line 
	line = line.strip()

	# for header that includes gene information starting with >
	if line[0] == ">":

		# add header to the list 
		fasta_name = ">" + line[1:].strip()
	
	# for lines except header
	else:  
		# concatenate lines 
		fixed_sequence = fixed_sequence+line 

# print results in terminal 
print(f'{fasta_name}\n{fixed_sequence}')


# write results in output file 
with open("fastaOutput.txt", "w") as output_file: 
	output_file.write(f'{fasta_name}\n{fixed_sequence}')

# close files 
fastafile.close()
output_file.close()