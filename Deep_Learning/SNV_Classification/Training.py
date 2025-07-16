import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt

from feature_extraction import SNVDataset, one_hot_sequence_flat
from model import simpleANN


# === Plotting Loss Curve ===
def plot_loss(train_losses, val_losses, fname="loss_curve.png"):
    plt.figure(figsize=(8, 5))
    plt.plot(train_losses, label="Training Loss", marker='o')
    plt.plot(val_losses, label="Validation Loss", marker='s')
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.title("Training vs Validation Loss")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(fname)
    plt.close()


# === Main Training Function ===
def train_model(df, batch_size=64, epochs=20, lr=0.001, patience=5):
    # Extract input columns
    sequences = df["Sequence"].tolist()
    labels = df["Label"].tolist()
    refs = df["Ref"].tolist()
    alts = df["Alt"].tolist()

    # === Data Splitting ===
    X_temp, X_test, y_temp, y_test, r_temp, r_test, a_temp, a_test = train_test_split(
        sequences, labels, refs, alts, test_size=0.15, stratify=labels, random_state=42
    )
    X_train, X_val, y_train, y_val, r_train, r_val, a_train, a_val = train_test_split(
        X_temp, y_temp, r_temp, a_temp, test_size=0.176, stratify=y_temp, random_state=42
    )

    # === Dataset and DataLoaders ===
    train_ds = SNVDataset(X_train, y_train, r_train, a_train)
    val_ds = SNVDataset(X_val, y_val, r_val, a_val)
    test_ds = SNVDataset(X_test, y_test, r_test, a_test)

    train_loader = DataLoader(train_ds, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_ds, batch_size=batch_size)
    test_loader = DataLoader(test_ds, batch_size=batch_size)

    # === Model Setup ===
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    input_dim = len(one_hot_sequence_flat(sequences[0])) + 4  # One-hot + GC + AT + Entropy + Transition

    model = simpleANN(input_dim=input_dim).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)

    # === Training Loop ===
    best_val_loss = float('inf')
    best_model_state = None
    patience_counter = 0
    train_losses = []
    val_losses = []

    print("\n Training started...\n")

    for epoch in range(1, epochs + 1):
        model.train()
        total_train_loss = 0.0

        for seq_tensor, labels in train_loader:
            seq_tensor = seq_tensor.view(seq_tensor.size(0), -1)
            input_tensor = seq_tensor.to(device)
            labels = labels.to(device)

            optimizer.zero_grad()
            outputs = model(input_tensor)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            total_train_loss += loss.item()

        avg_train_loss = total_train_loss / len(train_loader)

        # === Validation Phase ===
        model.eval()
        val_loss = 0.0
        with torch.no_grad():
            for seq_tensor, labels in val_loader:
                seq_tensor = seq_tensor.view(seq_tensor.size(0), -1)
                input_tensor = seq_tensor.to(device)
                labels = labels.to(device)
                outputs = model(input_tensor)
                loss = criterion(outputs, labels)
                val_loss += loss.item()

        avg_val_loss = val_loss / len(val_loader)
        train_losses.append(avg_train_loss)
        val_losses.append(avg_val_loss)

        print(f"Epoch {epoch}: Train Loss = {avg_train_loss:.4f}, Val Loss = {avg_val_loss:.4f}")

        # === Early Stopping ===
        if avg_val_loss < best_val_loss:
            best_val_loss = avg_val_loss
            best_model_state = model.state_dict()
            patience_counter = 0
        else:
            patience_counter += 1
            if patience_counter >= patience:
                print(" Early stopping triggered!")
                break

    # === Load Best Model ===
    if best_model_state:
        model.load_state_dict(best_model_state)

    # === Plot Loss Curve ===
    plot_loss(train_losses, val_losses)

    print("\n Training complete.\n")
    return model, test_loader, device
