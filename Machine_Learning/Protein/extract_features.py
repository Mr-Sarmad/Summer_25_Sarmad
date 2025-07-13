import pandas as pd
import numpy as np
from  Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import sys

def protein_features_analysis(fasta_file):
    try :
        all_features=[]
        for record in SeqIO.parse(fasta_file,"fasta"):
            sequence=str(record.seq).replace("-","").replace("*","")
            protein=ProteinAnalysis(str(sequence))
            features={
                "id":record.id,
                "molecular_weight": protein.molecular_weight(),
                "isoelectric_point":protein.isoelectric_point(),
                "aromaticity":protein.aromaticity(),
                "instability_index":protein.instability_index(),
                "gravy":protein.gravy()
            }
            all_features.append(features)
        df=pd.DataFrame([all_features])
        print("all Feautres are : ",df )
        return df 
    except FileExistsError:
        print("your file doesn't exist")
        sys.exit(1)
def synthetic_labels(df):
    try:
        label=['cytoplasm','nucleotide','mitochondria']
        df['labels']=np.random.choice(label,size=len(df))
        return df 
    except ModuleNotFoundError:
        print("no dataset found ")
