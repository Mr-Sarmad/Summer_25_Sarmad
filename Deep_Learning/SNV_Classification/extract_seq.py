import pandas as pd
from Bio import SeqIO

def load_reference_genome(fasta_path):
    print("Loading reference genome...")
    return SeqIO.to_dict(SeqIO.parse(fasta_path, "fasta"))

def extract_sequence(chrom, pos, ref, alt, genome_dict, window=20, replace=True):
    """
    Extract ±window bp around the SNV. Replace center ref with alt if `replace=True`.
    """
    if chrom not in genome_dict and chrom.startswith("chr") and chrom[3:] in genome_dict:
        chrom = chrom[3:]
    elif not chrom.startswith("chr") and "chr" + chrom in genome_dict:
        chrom = "chr" + chrom

    seq_record = genome_dict.get(chrom)
    if not seq_record:
        return None

    pos = int(pos)
    start = max(0, pos - window - 1)
    end = pos + window

    seq = seq_record.seq[start:end].upper()

    if len(seq) != 2 * window + 1:
        return None

    if replace:
        center_index = window
        seq = seq[:center_index] + alt + seq[center_index+1:]

    return str(seq)

def process_snv_file(snv_csv, fasta_path, output_csv, window=20):
    snv_df = pd.read_csv(snv_csv)
    genome_dict = load_reference_genome(fasta_path)

    sequences = []
    for i, row in snv_df.iterrows():
        chrom = str(row['Chrom'])
        pos = int(row['Pos'])
        ref = str(row['Ref'])
        alt = str(row['Alt'])
        seq = extract_sequence(chrom, pos, ref, alt, genome_dict, window)
        sequences.append(seq if seq else "N" * (2 * window + 1))

        if i % 1000 == 0:
            print(f"Processed {i}/{len(snv_df)} variants")

    snv_df['Sequence'] = sequences
    snv_df = snv_df[snv_df['Sequence'].str.count('N') < 5]  # Remove bad sequences
    snv_df.to_csv(output_csv, index=False)
    print(f"\nSaved extracted sequences to: {output_csv}")

# === Run ===
snv_csv_path = "D:/PROGRAMING/Summer/Deep_Learning/SNV_Classification/snv_20000_each.csv"
fasta_path = "D:/PROGRAMING/Summer/Deep_Learning/SNV_Classification/Homo_sapiens.GRCh37.dna.chromosome.1.fa"
output_csv = "snv_with_sequences.csv"

process_snv_file(snv_csv_path, fasta_path, output_csv)
