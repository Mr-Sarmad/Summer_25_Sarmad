import sys
def fasta(a):
    s=a
    try:
        with open (s, 'r') as f:
            lines = f.readlines()
            id=""
            seq={}
            for i in lines:
                line=i.strip()
                if i.startswith('>'):
                    id=i
                    seq[id]=""
                elif valid(i.strip())==True:
                    seq[id]+=i
                else:
                    print("your sequence is not valid")
        return seq
    except FileNotFoundError:
        print("CHECK YOUR FILE PATH")
def valid(seq):
    for i in seq:
        if i not in ["A", "T", "C", "G"]:
            return False
    else:
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
                f.write(f"{id}\n {seq}\n")  
    except IOError:
        print("your disk is full")
if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit()
    filepath = sys.argv[1]
    sequences = fasta(filepath)
    print(f"Total sequences are: {len(sequences)}")
    filtered = filter(sequences)
    print(f"Sequences after filtering: {len(filtered)}")
    write(filtered)