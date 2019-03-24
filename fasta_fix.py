"""
Welcome! The purpose of this script is to help fix the spacing issue 
when copying and pasting a protein or cDNA sequence from a public database. 

The result will give you the entire sequence in a single line and stored 
in an output.txt file. 

"""

# import dependencies
import os

# open sequence from .txt or .fasta file
# for example, the cDNA of the period gene from Drosophila melanogaster
sequence = open("FlyBase_YGMHKX.fasta", 'r')

# create empty list to store gene name (starts at >) and sequence result
gene_name = []
fixed_sequence = ''

# creatae for loop to iterate every line of the file
for line in sequence: 

	# strips line 
	line = line.strip()

	# for header that includes gene information starting with >
	if line[0] == ">":

		# add header to the list 
		gene_name.append(line[1:].strip())
	
	# for lines except header
	else:  

		# concatenate lines 
		fixed_sequence = fixed_sequence+line 

# print results in terminal 
print(f'{gene_name}\n{fixed_sequence}')


# write results in output file 
with open("output.txt", "w") as output_file: 
	output_file.write(f'{gene_name}\n{fixed_sequence}')