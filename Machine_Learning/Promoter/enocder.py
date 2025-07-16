import pandas as pd
import csv

def one_hot_encode_promoter(input_file="final_dataset.csv", output_file="tata_onehot_encoded.csv", tata_length=20):
    one_hot = {
        'A': ['1', '0', '0', '0'],
        'C': ['0', '1', '0', '0'],
        'G': ['0', '0', '1', '0'],
        'T': ['0', '0', '0', '1'],
        'N': ['0', '0', '0', '0']
    }
    df = pd.read_csv(input_file)
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        header = ['gene_id'] + [f'pos{i+1}_{base}' for i in range(tata_length) for base in 'ACGT']
        writer.writerow(header)
        for row in df.iterrows():
            seq = str(row['promoter_sequence']).upper()[-tata_length:].ljust(tata_length, 'N')
            row_data = [row['gene_id']]
            for base in seq:
                row_data.extend(one_hot.get(base, one_hot['N']))
            writer.writerow(row_data)
    return pd.read_csv(output_file)
