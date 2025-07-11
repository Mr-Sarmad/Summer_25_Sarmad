# 🌿 Summer 2025 Internship: Python Scripting for Bioinformatics

# 🌿 Summer 2025 Internship: Python Scripting & Machine Learning in Bioinformatics

**Intern:** Sarmad Nawaz  
**Lab:** Integrative Omics and Molecular Modelling Lab  
**Duration:** June–August 2025  
**Focus Areas:** Bioinformatics · Molecular Modelling · Python · Machine Learning

---

## 📚 Overview

This repository contains scripts, datasets, and notebooks developed during my **Summer 2025 Internship**, focused on applying **Python programming and machine learning** to biological datasets. Topics covered include:

- Core Python scripting for bioinformatics
- Sequence analysis using Biopython
- Gene expression data visualization
- Machine learning and dimensionality reduction
- Explainable AI (XAI) using SHAP

---

## 📆 Weekly Progress

### 📆 Week 1: Python Scripting Fundamentals

- 📁 `day1_basics.py` — Python installation, Conda setup, Git/GitHub, I/O, variables, data types  
- 📁 `day2_data_structures.py` — Lists, dictionaries, loops, functions, conditionals  
- 📁 `day3_fasta_parser.py` — File handling, FASTA parser, error handling  
- 📁 `day4_modular_code.py` — Code modularization, reusable scripts, testing  
- 📁 `day5_mini_projects.py` — GC content calculator, nucleotide counter, length stats

---

### 📆 Week 2: Biopython & Data Visualization

- 📁 `day1_seq_handling.py` — Transcription, translation, reverse complement, motifs (Biopython)  
- 📁 `day3_gene_expression_viz.ipynb` — Pandas for data analysis; Seaborn, Matplotlib, Plotly for plotting  
- 📁 `day5_codon_usage.py` — Codon frequency analysis  
- 📁 `day5_mutation_viz.py` — Genomic mutation visualization with bar/heatmap plots

---

### 📆 Week 3: Machine Learning in Bioinformatics

- 📁 `supervised_learning.ipynb` — Classification using Logistic Regression, SVM, Random Forest  
- 📁 `unsupervised_pca_tsne.ipynb` — K-Means clustering, PCA, t-SNE for dimensionality reduction  
- 📁 `model_eval_shap.ipynb` — Model evaluation (accuracy, ROC), SHAP for interpretability

---

## 📦 Environment Setup

> Python 3.8 environment managed with **Conda**

### 🔧 Create and Activate Conda Environment

```bash
conda create -n bioenv python=3.8
conda activate bioenv
pip install -r requirements.txt
```

## 📂 Folder Structure

```bash
Summer_25_Sarmad/
├── Week1/
│   ├── day1_basics.py
│   ├── day2_data_structures.py
│   ├── day3_fasta_parser.py
│   ├── day4_modular_code.py
│   └── day5_mini_projects.py
├── Week2/
│   ├── day1_seq_handling.py
│   ├── day3_gene_expression_viz.ipynb
│   ├── day5_codon_usage.py
│   └── day5_mutation_viz.py
├── Week3/
│   ├── supervised_learning.ipynb
│   ├── unsupervised_pca_tsne.ipynb
│   └── model_eval_shap.ipynb
├── datasets/
│   ├── sample.fasta
│   ├── gene_expression.csv
│   └── ml_dataset.csv
├── requirements.txt
└── README.md




