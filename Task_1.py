import sys
if len(sys.argv) !=2:
    sys.exit()
dna=sys.argv[1]
gc_content=((dna.count("G")+ dna.count("C"))/len(dna))
print("the length of the seq is ",len(dna))
print("the gc content of the seq is : ", gc_content)

for i in dna:
    if i == "G" or i == "C" or i == "A" or i == "T":
        print("your sequence is valid")
        break
    else :
        print("your seq is invalid")
a=0;
t=0;
c=0;
g=0;
for i in dna:
    if i=="A":
        a+=1
    if i=="T":
        t+=1
    if i=="C":
        c+=1
    if i=="G":
        g+=1
print("the total number of A in the seq is : ",a)
print("the total number of T in the seq is : ",t)
print("the total number of C in the seq is : ",c)
print("the total number of G in the seq is : ",g)

if(gc_content>0.4):
    print("High gc content seq")

reverse =""
for i in dna:
    reverse=i+reverse 
print("reverse of the seq is : ",reverse)

