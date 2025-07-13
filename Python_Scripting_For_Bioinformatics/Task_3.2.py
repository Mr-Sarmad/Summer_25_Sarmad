import sys
def gc_content_count(seq):
    len_seq = len(seq)
    gc_content = (seq.count('G') + seq.count('C')) / len_seq
    return gc_content
def is_valid(seq):
    validation = all(base in 'ATGC' for base in seq)
    if validation == True:
        return True
    else:
        return False
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("for using this script: sequences.fasta <fasta sequence>")
        sys.exit(1)
fasta_file = sys.argv[1]
sequences = {}
with open(fasta_file, "r") as f:
    lines = f.readlines()
    current_id = ""
    for line in lines:
        line = line.strip() 
        if line.startswith('>'):
            current_id = line
            sequences[current_id] = "" 
        else:
            sequences[current_id] += line
print("The fasta file is divided as:\n", sequences)

unique = set()
for id,dna in sequences.items():
    unique.update(dna)
    print("Unique base is: ", unique )
with open("results1.csv" , 'w') as f:
    k.write('ID,Length,GC Content,Validation\n')
    for seq_id, dna_seq in sequences.items():
        length = len(dna_seq)
        gc_content = gc_content_count(dna_seq)
        validity = is_valid(dna_seq)
        f.write("{},{},{},{}\n".format(seq_id, length, gc_content, validity)) 
print("Analysis written to csv file with name: results.csv ")