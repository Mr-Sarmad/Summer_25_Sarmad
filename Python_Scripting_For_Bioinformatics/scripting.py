import sys 
# my_list = sys.argv[1]
# print("my list is: ", my_list) 


if len(sys.argv)!=3:
    sys.exit()
dna=sys.argv[1]
rna=sys.argv[2]
print("the dna seq is ", dna)
print("the dna seq is ", len(dna))
print("the rna seq is ", rna)
print("the rna seq is ", len(rna))
