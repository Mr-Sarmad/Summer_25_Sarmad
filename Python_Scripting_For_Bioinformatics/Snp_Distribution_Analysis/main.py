import pandas as pd
from scipy.stats import pearsonr
import seaborn as sns
import matplotlib.pyplot as plt
import sys 

def parse_gff(a):
    try:
        e=[]
        with open(a,'r',encoding='utf-8') as r: # opening gff in reading 
            for line in r:
                if line.startswith("#"):  # skipping the line that start with hashtags
                    continue
                l= line.strip().split('\t')   # removing extra spaces and adding tab or spaces
                if len(l) < 9: # gff file have mainly 9 parts so is checking that 
                    continue
                feature_type = l[2].lower()  # getting third column as feature which means type such cds and make it lower case 
                if feature_type != 'cds':   # checking if it is cds then we get exons ( coding sequences)
                    continue
                attributes = l[8]
                chrom = l[0].lower()   # getting the chromosomes in index 0 and position in the gff file 
                start = int(l[3])     # getting the start position of the gene in index 3
                end = int(l[4])       # getting the end position of the   gene  in index 4
                score = l[5]           # getting the score  in index 5 
                gene_id = None
                for key in ['gene_id', 'gene', 'Parent', 'ID']:   # check if one of this key is present in the gff file 
                    if f"{key}=" in attributes:   # if one  of the key is matched with the our attributes 
                        gene_id = attributes.split(f"{key}=")[1].split(";")[0]   #split the attribute from their id and add in the gene_id
                        gene_id = gene_id.split('_')[0].upper().strip() # getting just id 
                        break
                e.append({'chrom': chrom,'start': start,'end': end,'score': score,'gene_id': gene_id}) # this will add the exons information which we requires
        return e
    except FileNotFoundError:
        print("Your GFF file not found")

def parse_vcf(a):
    try:
        s=[]
        with open(a, 'r',encoding='utf-8')as r:  # opening vcf in reading  format
            for line in r:
                if line.startswith("#"):  # skipping the line that start with hashtags
                    continue
                l= line.strip().split('\t')   # removing extra spaces and adding tab or spaces
                if len(l) < 2: # this file contain only two main column chromosome and position
                    continue
                s.append({'chrom':l[0],'pos':int(l[1])})  # append with chromosome and their position
            return s
    except FileExistsError:
        print(" Your VCF file is not found")

def map_snps_to_exons(snps, exons):
    try:
        map=[]
        for exon in exons:  #Loop through every exon (CDS)
            for snp in snps: #Loop through every snp
                snp_chrom = snp['chrom'].lower() # chromosomes in the snp is lowered and save in the snp_chrom
                if snp_chrom == 'chrm':
                    snp_chrom = 'chrmt' # converting the chrm in snp into the chrmt gff format for mapping
                if snp_chrom == exon['chrom']:   # check if the chromosomes are  same in snp and exons
                    if exon['start'] <= snp['pos'] <= exon['end']: # check if the snp lines in between the exons 
                        map.append({'gene_id': exon['gene_id'],'snp_pos': snp['pos'],'chrom': exon['chrom'],'exon_start': exon['start'],'exon_end': exon['end']})# appending the mapped exon
        return map
    except ModuleNotFoundError:
        print("Your File not having any mapping format ")
def calculate_snp_density(a):
    try:
        d= {}
        for snp in a:
            gene = snp['gene_id']
            exon_len = snp['exon_end'] - snp['exon_start'] + 1  # calculate the exon where snp position fall
            if gene not in d:
                d[gene] = {'snp_count': 0, 'exon_length': 0} # saving the one gene in the dictionary of the results
            d[gene]['snp_count'] += 1
            d[gene]['exon_length'] += exon_len   # if we have multiple genes
        f= []
        for gene, values in d.items(): # iteration for gene and values in dictionary
            snp_count = values['snp_count']  # saving counts of snp in the snp_count 
            exon_len = values['exon_length']  # saving the exon length in exon_len
            density = (snp_count / exon_len) * 1000   # getting the density per kb
            f.append({'gene_id': gene,'snp_count': snp_count,'exon_length': exon_len,'snp_density_per_kb': round(density, 4)}) # append the final results
        return f
    except MemoryError:
        print(" You have limited memory and the data is large ")
def expression(file_path):
    try:
        df = pd.read_csv(file_path, sep='\t', encoding='utf-8') # reading the expression file and saving it in the df
        e= []
        for col in df.columns: # iteration of all the columns in the df 
            column=col.strip().lower() # removing extra space and lower all the data 
            e.append(column) # now appending the column 
        df.columns = e
        if 'gene_id' not in df.columns and 'gene' in df.columns:
            df.rename(columns={'gene': 'gene_id'}, inplace=True)  # converting the column name gene into gene_id as in the vcf file 
            df['gene_id'] = df['gene_id'].str.split('.').str[0].str.strip().str.upper()  # getting the required gene name for merging
        return df
    except FileExistsError:
        print("your expression file is not found ")
def merge(density, df):
    try:
        density_df= pd.DataFrame(density)  # Converts list of dicts into a df
        merged = pd.merge(density_df, df, on='gene_id', how='inner')  # Inner join on gene_id
        return merged
    except ModuleNotFoundError:
        print("your file is not having proper data ")
def plot_corelation_visuals_from_merged(m,output_file):
    try:
        sns.set_style("whitegrid")           # set the background as wwhite
        plt.figure(figsize=(8, 6))     # setting the  size of the plot
        sns.scatterplot(data=m, x='mean_expression', y='snp_density_per_kb')
        plt.title(" SNP Density vs Gene Expression", fontsize=14) # setting the title 
        plt.xlabel("Gene Expression (mean)", fontsize=12)  # setting the name of x_label and fontsize
        plt.ylabel("SNP Density per kb", fontsize=12) # setting the name of x_label and fontsize
        plt.xticks(rotation=45, ha='right')  # setting the values rotation on x 
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.tight_layout() 
        plt.savefig(output_file, dpi=300)
        plt.close()
    except ModuleNotFoundError :
        print("the modules used are not found")

if __name__=='__main__':
    if len(sys.argv)!=4:
        print("adding more files ")
        sys.exit(1)
gff=sys.argv[1]
snp=sys.argv[2]
exp=sys.argv[3]
exon=parse_gff(gff)
snp=parse_vcf(snp)
express=expression(exp)
mapped=map_snps_to_exons(snp,exon)
density=calculate_snp_density(mapped)
merg=merge(density,express)
plot_corelation_visuals_from_merged(merg,"D:/PROGRAMING/Python Scripting For Bioinformatics/Snp Distribution Analysis/SNP_Density_vs_Expression.png")
corr, pval = pearsonr(merg['snp_density_per_kb'], merg['mean_expression'])  # applying stats 
print(f"Pearson correlation: r = {corr:.4f}")# displaying corelation value .
print(f"p-value = {pval:.4e}") # displaying p-value





