import pandas as pd
from feature_extract import extract_features
from enocder import one_hot_encode_promoter
from model import model

def main():
    print("Extracting base features.")
    feature_df = extract_features("promoter_activity_dataset.csv")
    print("One-hot encoding TATA region.")
    one_hot_df = one_hot_encode_promoter("final_dataset.csv", "tata_onehot_encoded.csv")
    merged_df = pd.merge(feature_df, one_hot_df, on="gene_id")
    merged_df.to_csv("merged_features.csv", index=False)
    model("merged_features.csv")
if __name__ == "__main__":
    main()
