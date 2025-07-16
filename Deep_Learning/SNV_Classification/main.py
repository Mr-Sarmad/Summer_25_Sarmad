import torch
import pandas as pd
from evaluate_model import evaluate_predictions, plot_conf_matrix, save_model,plot_roc_curve
from Training import train_model
from Data_extraction import extract_variants, process_snv_file

def main():
    # === Paths ===
    vcf_path = "D:/PROGRAMING/Summer/Deep_Learning/SNV_Classification/clinvar_20250706.vcf"
    fasta_path = "D:/PROGRAMING/Summer/Deep_Learning/SNV_Classification/Homo_sapiens.GRCh37.dna.chromosome.1.fa"
    intermediate_csv = "snv.csv"
    final_csv = "snv_dataset.csv"
    extract_variants(vcf_path, limit_each=6500, save_path=intermediate_csv)
    process_snv_file(intermediate_csv, fasta_path, final_csv)
    df = pd.read_csv(final_csv)
    model, test_loader, device = train_model(df)
    model.eval()
    all_preds = []
    all_labels = []
    with torch.no_grad():
        for seq_tensor, labels in test_loader:
            seq_tensor = seq_tensor.view(seq_tensor.size(0), -1).to(device)
            labels = labels.to(device)
            outputs = model(seq_tensor)
            probs = torch.softmax(outputs, dim=1)[:, 1]
            preds = torch.argmax(outputs, dim=1)
            all_preds.extend(preds.cpu().numpy())
            all_labels.extend(labels.cpu().numpy())
    evaluate_predictions(all_labels, all_preds)
    plot_conf_matrix(all_labels, all_preds)
    save_model(model)
if __name__ == "__main__":
    main()
