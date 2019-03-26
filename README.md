# Fix improper spacing of a sequence in FASTA format 
The purpose of this folder is to remove improper tab indentation of a sequence in FASTA format to generate the sequence in a single line. 


In this case, we have downloaded the FASTA file containing <i>period</i> gene of <i>Drosophila melanogaster </i> from Flybase. 
Source: http://flybase.org/download/sequence/FBgn0003068/FBpp

To run this script: 

1) Download/clone this folder 
2) Add your FASTA file and replace file path in fasta_fix.py
3) In terminal, cd to this folder and then run the script ($ python fasta_fix.py)

##### Original FASTA file: 

<img src="https://raw.githubusercontent.com/ying-li-python/fasta-fix/master/Images/fasta_example.png"> 


##### Output as FASTA: 

<img src="https://raw.githubusercontent.com/ying-li-python/fasta-fix/master/Images/fasta_output.png">
