import sys

# GC content (no upper)
def gc(seq):
    content = seq.count('G') + seq.count('C')
    length = len(seq)
    percentage = (content / length) * 100 if length > 0 else 0
    print("GC content is:", int(percentage))
    return int(percentage)

# Validate DNA sequence (no upper)
def valid(seq):
    for base in seq:
        if base not in ['A', 'T', 'C', 'G']:
            return False
    return True

# ✅ Your original unique() function
def unique(a):
    unique_seq = set(a)
    print("Unique nucleotides are:", unique_seq)

# FASTA reader
def fasta(file_path):
    sequences = {}
    with open(file_path, "r") as f:
        current_id = ""
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                current_id = line[1:].split()[0]  # Only take ID like NC_000017.11
                sequences[current_id] = ""
            else:
                line = line.replace(" ", "")  # Remove any spaces from the sequence
                sequences[current_id] += line
    print("FASTA file parsed successfully.")
    return sequences

# Save to CSV
def save_to_csv(sequences):
    with open("results.csv", "w") as f:
        f.write("ID,Length,GC_Content,Is_Valid\n")
        for seq_id, seq in sequences.items():
            length = len(seq)
            gc_content = gc(seq)
            validity = valid(seq)
            f.write("{},{},{},{}\n".format(seq_id, length, gc_content, validity))
    print("Results saved to 'results.csv'")

# Main
if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit("Invalid arguments. Usage: python script.py <fasta_file>")

    fasta_file = sys.argv[1]
    sequences = fasta(fasta_file)

    for seq_id, seq in sequences.items():
        print(f"\nSequence ID: {seq_id}")
        unique(seq)  # Use your own function

    save_to_csv(sequences)
