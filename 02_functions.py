import sys

def func(a,b):
    seq1=a
    seq2=b
    c=seq1+seq2
    return c

if __name__=="__main__":
    if len(sys.argv) !=3:
        sys.exit("usage: python file_name arg_1,arg_2")
    sequence_1=sys.argv[1]
    sequence_2=sys.argv[2]
    print(func(sequence_1,sequence_2))
