# Fix spacing in FASTA 
FASTA is the standard format for biologists to store a sequence of a gene. However, some FASTA files have improper spacing when downloaded from a public database such as [Pubmed](https://www.ncbi.nlm.nih.gov/pubmed/). The purpose of this folder is to remove improper tab indentation of a sequence in FASTA format to generate the sequence in a single line. 


In this case, we have downloaded the FASTA file containing the <i>[period](http://flybase.org/download/sequence/FBgn0003068/FBpp)</i> gene of <i>Drosophila melanogaster </i> from Flybase. 

## Getting started

You will need to download/clone this folder, and in command line, route to this folder using the cd command. 
```
git clone https://github.com/ying-li-python/fasta-fix.git
cd fasta-fix 
```
### Original FASTA file 

Your FASTA file should have indentation. See example.  

Example FASTA: 

<img src="https://raw.githubusercontent.com/ying-li-python/fasta-fix/master/Images/fasta_example.png"> 

## Setting up
Add a FASTA file in the fasta-fix folder for you to fix. In this case, the file is [FlyBase_YGMHKX.fasta](https://github.com/ying-li-python/fasta-fix/blob/master/FlyBase_YGMHKX.fasta).

Using a text or code editor, open fasta_fix.py. 

Replace the FASTA file path to your own. 

```
fastafile = open("FlyBase_YGMHKX.fasta", 'r')
```

## Running the script 
Now that you provided the setup, you can run the the script in command line. Make sure your directory is still in fasta-fix folder.

```
python fasta_fix.py 
```

Your script will generate a new FASTA file named output.fasta in the same folder. And you're done! 

##### Output: 

<img src="https://raw.githubusercontent.com/ying-li-python/fasta-fix/master/Images/output.png">


## Authors: 
Ying Li 


