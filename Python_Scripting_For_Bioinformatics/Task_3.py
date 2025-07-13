import sys

def gc(seq):
    content = seq.count('G') + seq.count('C')
    length = len(seq)
    percentage = (content / length) * 100 if length > 0 else 0
    print("GC content is:", int(percentage))
    return int(percentage)

def valid(seq):
    for i in seq:
        if i not in ["A", "T", "C", "G"]:
            return False
    else:
        return True

def unique(a):
    unique_seq=set(a)
    print("unique sequence are : ",unique_seq)


def fasta(file_path):
    sequences = {}
    with open(file_path, "r") as f:
        current_id = ""
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                current_id = line[1:].split()[0]
                sequences[current_id] = ""
            else:
                line = line.replace(" ", "") 
                sequences[current_id] += line
    return sequences

def csv(a):
    with open("results.csv", "w") as f:
        f.write("ID,Length,GC_Content,Is_Valid\n")
        for seq_id, seq in a.items():
            length = len(seq)
            gc_content = gc(seq)
            validity = valid(seq)
            f.write("{},{},{},{}\n".format(seq_id, length, gc_content, validity))
    print("Results saved to 'results.csv'")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit()

    fasta_file = sys.argv[1]
    sequences = fasta(fasta_file)

    unique(sequences)
    csv(sequences)
