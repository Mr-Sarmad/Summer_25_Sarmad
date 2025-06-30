from Bio import SeqIO
from Bio.Seq import Seq
seq = SeqIO.parse("seq.gb","genbank")
with open("output.fasta",'w') as w:
    for i in seq:
        i.annotations["molecule_type"] = "DNA"
        seq_id = i.id
        seq_features = i.features
        seq_sequence = i
        SeqIO.write(seq_sequence, w, "fasta")
print("Your Genbank  has been written to fasta format")