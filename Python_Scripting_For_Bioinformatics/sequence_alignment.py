from Bio import pairwise2
from Bio.Seq import Seq
import sys

def align_seq(seq_1, seq_2, match=2, mismatch=-2, gap_open=-2, gap_extend=-2):
    alignment = pairwise2.align.globalms(seq_1, seq_2, match, mismatch, gap_open, gap_extend)
    best_alignment = alignment[0]

    print("The alignment score is:", best_alignment.score)
    print("The alignment sequence 1 is:", best_alignment.seqA)
    print("The alignment sequence 2 is:", best_alignment.seqB)
    print("The start of the alignment is:", best_alignment.start)
    print("The end of the alignment is:", best_alignment.end)
    return best_alignment

def similarity(alignment):
    seq1 = alignment.seqA
    seq2 = alignment.seqB
    start = alignment.start
    end = alignment.end
    aligned1 = seq1[start:end]
    aligned2 = seq2[start:end]
    matches = 0

    for i in range(len(aligned1)):
        if aligned1[i] == aligned2[i] and aligned1[i] != '-':
            matches += 1 

    length = end - start
    similarity = (matches / length) * 100 if length > 0 else 0
    print("The similarity of the alignment is:", similarity, "%")
    return similarity

def gap_frequency(alignment):
    seq1 = alignment.seqA 
    seq2 = alignment.seqB

    gapsA = seq1.count('-')
    gapsB = seq2.count('-')

    frequency_sequence1 = gapsA / len(seq1) if len(seq1) > 0 else 0
    frequency_sequence2 = gapsB / len(seq2) if len(seq2) > 0 else 0

    print("Gap frequency in sequence 1:", frequency_sequence1)
    print("Gap frequency in sequence 2:", frequency_sequence2)
    return frequency_sequence1, frequency_sequence2

def conserved_region(alignment, threshold=20):
    aligned1 = alignment.seqA
    aligned2 = alignment.seqB

    conserve_reg = []
    match = ""

    for i in range(len(aligned1)):
        if aligned1[i] == aligned2[i] and aligned1[i] != '-':
            match += aligned1[i]
        else:
            if len(match) >= threshold:
                conserve_reg.append(match)
            match = ""

    # Check at the end after the loop
    if len(match) >= threshold:
        conserve_reg.append(match)

    print("Conserved regions (length ≥", threshold, "):")
    if conserve_reg:
        print(" | ".join(conserve_reg))
    else:
        print("No conserved region found above threshold.")

    return conserve_reg




if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit("Usage: python your_script.py <sequence1> <sequence2>")

    sequence1 = sys.argv[1]
    sequence2 = sys.argv[2]
alignment_results = align_seq(sequence1, sequence2)
similarity(alignment_results)
gap_frequency(alignment_results)
conserved_region(alignment_results)