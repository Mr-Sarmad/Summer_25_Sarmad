# data structures 

# list

'''
list=[]
-append()
-insert()
-remove()
-clear()
-sort()
tuple=()
dictionary={}
'''
gene_lsit=['braca1','tp53','gc5p']
gene_lsit.append('sum25')
gene_list.insert(1,'sum26')
gene_lsit.remove('sum26')
remove=gene_lsit.pop(2)
gene_lsit.sort( )
print("list of the gene id ",gene_lsit)
print("the position of sum25 is ",gene_list.index('sum25'))
print("remove gene id ",remove)

gene_tuple=('braca1','tp53','gc5p')
print("tuple of the gene id ",gene_tuple)


# tuple

gene_1=(100,200),(500,600)
for start ,end  in gene_1:
    print("the position of the gene_1 is: " ,start,'the ending id: ',end)

bases=set("ATCGGCGGATCTAGCGCGsssssss")
print("the unique bases of the gene is: ",bases)

# dictionaries
gene_dict={'braca1':1,'tp53':2,'gc5p':5}
for name , num in gene_dict:
    print("The name of the gne is",name,"and the num of this gene is",num)
