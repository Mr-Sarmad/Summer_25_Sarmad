import sys
def parse(file):
    with open(file,'r') as f:
        lines=f.readlines()
        # fasta.strip()
        header=lines[0].strip()
        print(header)
        seq=''
        for i in lines[1:]:
            seq+=i.strip()
        print(seq)


if __name__=='__main__':
    if len(sys.argv)!=2:
        sys.exit("invalid argument")
    
    sequence=sys.argv[1]
    parse(sequence)

# parcing the gff file
# def gff(file):
#     with open(file,'r')as g:
#         for i in g:
#             lines=i.strip()
#             lines=lines.split('\t')

#             id=lines[0]
#             type=lines[2]
#             starting_coord=lines[3]
#             ending_coord=lines[4]
#             score=lines[5]
#             with open('output.csv','w' )as w:
#                 w.write("the id this",id,"the type is ",type,"the starting is ",starting_coord,"the ending is ",ending_coord,"the score is ",score)   
    
# if __name__=='__main__':
#     if len(sys.argv)!=2:
#         sys.exit("invalid ")
    
#     file=sys.argv[1]
#     gff(file)