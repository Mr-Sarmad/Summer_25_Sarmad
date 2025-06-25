# 🌿 Summer 2025 Internship: Python Scripting for Bioinformatics

**Intern:** Sarmad Nawaz  
**Lab:** Integrative Omics and Molecular Modelling Lab  
**Duration:** June–August 2025  
**Focus Areas:** Bioinformatics · Molecular Modelling · Python · Machine Learning

---

## 📚 Overview

This repository contains scripts, datasets, and notebooks developed during my **Summer 2025 Internship**, focused on applying Python to real-world biological data. Topics include scripting, sequence analysis, data visualization, and introductory machine learning in bioinformatics.

---

## 📆 Week 1: Python Scripting for Bioinformatics

### 🔧 Day 1: Programming Fundamentals & Setup
- Conda environment setup
- Git & GitHub for version control
- Python basics: input/output, variables, data types, loops, conditionals  
📁 `Week1/day1_basics.py`

### 🧩 Day 2: Modular Programming & Data Structures
- Functions, lists, tuples, sets, dictionaries
- File I/O and error handling  
📁 `Week1/day2_fasta_parser.py`

### 🧬 Day 3: Sequence Analysis with Biopython
- Read/write biological sequences using Biopython
- Reverse complement, transcription, translation  
📁 `Week1/day3_biopython_seq.py`

### 📊 Day 4: Data Analysis & Visualization
- DataFrames using Pandas and NumPy
- Visualizations with Seaborn, Matplotlib, Plotly  
📁 `Week1/day4_gene_expression_viz.ipynb`

### 🧠 Day 5: Mini Projects
- Codon Usage Analysis  
📁 `Week1/day5_codon_usage.py`
- Genomic Mutation Visualization  
📁 `Week1/day5_mutation_viz.py`

---

## 📦 Environment Setup & Installation

> This project uses **Python 3.8** and a virtual environment managed with **Conda**.  
> All packages are listed in `requirements.txt`.

### 🔧 Create and Activate Conda Environment

```bash
conda create -n bioenv python=3.8
conda activate bioenv
pip install -r requirements.txt


---

## 📂 Folder Structure

```bash
Summer_25_Sarmad/
├── Week1/
│   ├── day1_basics.py
│   ├── day2_fasta_parser.py
│   ├── day3_biopython_seq.py
│   ├── day4_gene_expression_viz.ipynb
│   ├── day5_codon_usage.py
│   └── day5_mutation_viz.py
├── datasets/
│   ├── sample.fasta
│   └── gene_expression.csv
├── README.md
└── requirements.txt

