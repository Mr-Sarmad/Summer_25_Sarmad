from extract_features import protein_features_analysis,synthetic_labels
import logging
from model import model
# configure logging 
logging.basicConfig(level=logging.INFO,filename="output.log",format='%(asctime)s-%(levelname)s-%(message)s')
def main():
    fasta_file="proteins.fasta"
    logging.info(f"Parsing and analyzing Fasta FIle :{fasta_file}")
    df=protein_features_analysis(fasta_file)
    logging.info("features extracted successfully ")
    logging.info("assigning labels")

    label_df=synthetic_labels(df)
    # m,accuracy,classification_rep,r2,error=model(label_df)



if __name__=="__main__":
    main()