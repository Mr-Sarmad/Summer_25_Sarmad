import pandas as pd
from collections import Counter
from itertools import product
import math

def calculate_gc_content(sequence):
    if not sequence:
        return 0.0
    sequence = sequence.upper()
    gc_count = sequence.count('G') + sequence.count('C')
    return round((gc_count / len(sequence)) * 100, 2)

def calculate_at_content(sequence):
    if not sequence:
        return 0.0
    sequence = sequence.upper()
    at_count = sequence.count('A') + sequence.count('T')
    return round((at_count / len(sequence)) * 100, 2)

def calculate_entropy(sequence):
    if not sequence:
        return 0.0
    sequence = sequence.upper()
    length = len(sequence)
    freq = [sequence.count(base) / length for base in "ACGT"]
    entropy = -sum(p * math.log2(p) for p in freq if p > 0)
    return round(entropy, 4)

def get_kmer_frequencies(sequence, k=3):
    if not sequence or len(sequence) < k:
        return {f"{kmer}": 0 for kmer in [''.join(p) for p in product('ACGT', repeat=k)]}
    kmers = [sequence[i:i+k] for i in range(len(sequence) - k + 1)]
    total_kmers = len(kmers)
    counts = Counter(kmers)
    return {f"{kmer}": round(counts.get(kmer, 0) / total_kmers, 4) for kmer in [''.join(p) for p in product('ACGT', repeat=k)]}

def extract_features(input_file):
    df = pd.read_csv(input_file)
    df.rename(columns={"gene": "gene_id", "sequence": "promoter_sequence"}, inplace=True)
    df["GC_content"] = df["promoter_sequence"].apply(calculate_gc_content)
    df["AT_content"] = df["promoter_sequence"].apply(calculate_at_content)
    df["entropy"] = df["promoter_sequence"].apply(calculate_entropy)
    kmer_df = df["promoter_sequence"].apply(get_kmer_frequencies).apply(pd.Series)
    final_df = pd.concat([df, kmer_df], axis=1)
    final_df.to_csv("final_dataset.csv", index=False)
    return final_df
