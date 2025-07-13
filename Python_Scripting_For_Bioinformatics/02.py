dna = input("write your seq :")
print("the seq is : " , dna)

# operators
'''
arthimetic operators
+  -  *  /  %  **  //  ~  <
>
=  ==  !=  >
logical operators 
and
or
not

'''

dna=5
rna=5
add=dna+rna
print("addition is ",add)

seq_1="ATCGCGATAGC"
seq_2="ATCGATGCATGGATCG "
seq_3="T"
print("the seq are ",seq_1==seq_2)
print("the seq are ",seq_1!=seq_2)
print("the seq are ",seq_1<seq_2)
print("the seq are ",seq_1<seq_2)



#logical operators 
print("logical operator" , seq_1 and seq_3 == seq_2)
print("logical operator" , seq_1 or seq_3 == seq_2)

# condtions 
# if , elif , else
dna_Seq= " ATGCTAGTCAGTCAGTACGATCAGAAAGAAT"
threshold=10
gc_content=dna.count("G")+ dna.count("C")
if gc_content == threshold:
    print(" its equal to threshold")
else gc_content != threshold:
    print(" its not equal to threshold")

# elif
dna_Seq= " ATGCTAGTCAGTCAGTACGATCAGAA"
threshold=10
gc_content=dna_Seq.count("G")+ dna_Seq.count("C")
if gc_content == threshold:
    print(" its  eqaul tp threshold")
elif gc_content > threshold:
    print(" its greater than threshold")
elif gc_content < threshold:
    print(" its less than threshold")
else :
    print(gc_content)


# loops
for i in range (10):
    print(i)
complement=""
for i in dna_Seq:
    complement=i +dna_Seq
print(complement)

import sys
