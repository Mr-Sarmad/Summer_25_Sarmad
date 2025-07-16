import torch
from torch.utils.data import Dataset
from math import log2

# One-hot encode full sequence
def one_hot_encode(seq, fixed_len=41):
    one_hot_map = {
        'A': [1, 0, 0, 0],
        'T': [0, 1, 0, 0],
        'G': [0, 0, 1, 0],
        'C': [0, 0, 0, 1],
        'N': [0, 0, 0, 0]  # Unknown base
    }
    seq = seq.upper()
    if len(seq) < fixed_len:
        pad = fixed_len - len(seq)
        seq = 'N' * (pad // 2) + seq + 'N' * (pad - pad // 2)
    elif len(seq) > fixed_len:
        mid = len(seq) // 2
        seq = seq[mid - fixed_len // 2: mid + fixed_len // 2 + 1]
    encoded = [one_hot_map.get(base, [0, 0, 0, 0]) for base in seq]
    return encoded  # list of one-hot vectors

# Flat one-hot sequence
def one_hot_sequence_flat(seq):
    return [bit for base_vec in one_hot_encode(seq) for bit in base_vec]

# Compute GC content
def compute_gc_content(seq):
    gc_count = sum(1 for base in seq.upper() if base in ['G', 'C'])
    return gc_count / len(seq) if len(seq) > 0 else 0.0

# Compute AT content
def compute_at_content(seq):
    at_count = sum(1 for base in seq.upper() if base in ['A', 'T'])
    return at_count / len(seq) if len(seq) > 0 else 0.0

# Compute sequence entropy
def sequence_entropy(seq):
    seq = seq.upper()
    counts = {base: seq.count(base) / len(seq) for base in "ACGT"}
    return -sum(p * log2(p) for p in counts.values() if p > 0)

# Check if transition
def is_transition(ref, alt):
    return int((ref.upper(), alt.upper()) in [('A', 'G'), ('G', 'A'), ('C', 'T'), ('T', 'C')])

# Combine all extra features
def compute_extra_features(seq, ref, alt):
    gc = compute_gc_content(seq)
    at = compute_at_content(seq)
    entropy = sequence_entropy(seq)
    transition = is_transition(ref, alt)
    return torch.tensor([gc, at, entropy, transition], dtype=torch.float32)

# Dataset Class
class SNVDataset(Dataset):
    def __init__(self, sequences, labels, refs, alts):
        self.sequences = sequences
        self.labels = labels
        self.refs = refs
        self.alts = alts

    def __len__(self):
        return len(self.sequences)

    def __getitem__(self, idx):
        seq = self.sequences[idx]
        ref = self.refs[idx]
        alt = self.alts[idx]
        label = self.labels[idx]

        one_hot = one_hot_sequence_flat(seq)
        extra_features = compute_extra_features(seq, ref, alt)

        full_features = torch.tensor(one_hot + extra_features.tolist(), dtype=torch.float32)
        label_tensor = torch.tensor(label, dtype=torch.long)

        return full_features, label_tensor
