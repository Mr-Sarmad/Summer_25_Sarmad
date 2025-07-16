import pandas as pd
from Bio import SeqIO
def parse_info(info_str):
    info_dict = {}
    for item in info_str.split(';'):
        if '=' in item:
            key, value = item.split('=', 1)
            info_dict[key] = value
    return info_dict
def extract_variants(vcf_path, limit_each=6500, save_path="snv.csv"):
    variants = []
    pathogenic = []
    benign = []
    with open(vcf_path, 'r') as f:
        for line in f:
            if line.startswith("#"):
                continue
            cols = line.strip().split('\t')
            chrom, pos, var_id, ref, alt, qual, filt, info = cols[:8]
            info_dict = parse_info(info)
            clnsig = info_dict.get('CLNSIG', '').lower()
            if 'pathogenic' in clnsig and 'benign' not in clnsig:
                label = 1
            elif 'benign' in clnsig and 'pathogenic' not in clnsig:
                label = 0
            else:
                continue  # Skip ambiguous/conflicting labels
            gene = info_dict.get('GENEINFO', '').split(':')[0]
            variant_type = info_dict.get('MC', 'NA').split('|')[0]
            variant = {
                'Chrom': chrom,
                'Pos': pos,
                'Ref': ref,
                'Alt': alt,
                'Gene': gene,
                'Variant_Type': variant_type,
                'Label': label
            }
            if label == 1 and len(pathogenic) < limit_each:
                pathogenic.append(variant)
            elif label == 0 and len(benign) < limit_each:
                benign.append(variant)
            if len(pathogenic) >= limit_each and len(benign) >= limit_each:
                break
    df = pd.DataFrame(pathogenic + benign)
    df.to_csv(save_path, index=False)
    print(f" Saved {len(df)} variants to {save_path}")
    return save_path
def load_reference_genome(fasta_path):
    print(" Loading reference genome...")
    return SeqIO.to_dict(SeqIO.parse(fasta_path, "fasta"))
def extract_sequence(chrom, pos, ref, alt, genome_dict, window=20, replace=True):
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
        seq = seq[:center_index] + alt + seq[center_index + 1:]
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
            print(f" Processed {i}/{len(snv_df)} variants")
    snv_df['Sequence'] = sequences
    snv_df = snv_df[snv_df['Sequence'].str.count('N') < 5]
    snv_df.to_csv(output_csv, index=False)
    print(f" Saved extracted sequences to {output_csv}")
    return output_csv
