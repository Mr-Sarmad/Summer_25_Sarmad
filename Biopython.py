from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Restriction import EcoRI
# seq =Seq("AGCGATGCAGTCGTGACTTAGCCA")

# seq=SeqIO.parse('sequence.fasta','fasta')
# for i in seq:
#     seq_id=i.id
#     seq_sequence=i.seq
#     print("the id of the file is ",seq_id)
#     print("the sequence of the file is ",seq_sequence)
# seq_complement=seq.complement()
# R_complement=seq.reverse_complement()
# rna=seq.transcribe()
# dna_prot=seq.translate()
# cout_a=seq.count('A')
# lower_case=seq.lower()
# region=seq.find("TCG")
# seq_codon=seq.startswith('TAG')
# print("the complement of the sequence is ",seq_complement)
# print("The reverse complement of the sequence is ",R_complement)
# print(" The transcription of the sequence is ",rna)
# print("The translation of the sequence is ",dna_prot)
# print("The count of A in the sequence is ",cout_a)
# print("The lower case of the sequence is ",lower_case)
# print("Does our sequence is start with stop codon ",seq_codon)
# print("The region is: ",region)
# convert a fasta file into Fasta
# seq=SeqIO.parse('sequence.fasta','fasta')
# for i in seq:
#     seq_id=i.id
#     print(seq_id)
# for i in seq:
#     seq.annotations["molecule_type"]="PROTEIN"

# with open('new_file','w') as w:
#     SeqIO.write(seq,w,'genbank')
#     print("file is saved")
seq=SeqIO.parse('bacteria.fa','fasta')
for i in seq:
    seq_id=i.id
    sequence=i.seq
    cut_site=EcoRI.search(sequence)
    print("the cut site os the EcoRI are these : ",cut_site)




