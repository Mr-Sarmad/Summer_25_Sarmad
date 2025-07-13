import sys
def  read(a):
    s={}
    try:
        with open (s, 'r') as f:
            lines = f.readlines()
            id=""
            seq=[]
            for i in lines:
                line=i.strip()
                if line.startswith('>'):
                    id=line
                    seq[id]="".join(seq)
                    if valid(seq):
                        sequences[id] = seq
                    else:
                        print("your sequence is not valid")
        return sequences
    except IOError:
        print("CHECK YOUR FILE PATH")
def valid(seq):
    for base in seq:
        if base not in ["A", "T", "C", "G"]:
            return False
    return True

def filter(a):
    filter_seq={}
    length=int(input("gave me the length of the sequence"))
    for id, seq in a.items():
        if len(seq) >= length:
            filter_seq[id] = seq
        return filter_seq
def write(a):
    try:
        with open("output.fasta", 'w') as f:
            for id,seq in a.items():
                f.write("{}\n".format(id))
                f.write("{}\n".format(seq)) 
    except IOError:
        print("your disk is full")
if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit()
    filepath = sys.argv[1]
    sequences = read(filepath)
    print("Total sequences are: {}".format(len(sequences)))
    filtered = filter(sequences)
    print("Sequences after filtering: {}".format(len(filtered)))
    write(filtered)