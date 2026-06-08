# GNN Model Benchmark

A benchmarking framework for comparing Graph Neural Network (GNN) models across multiple graph learning tasks.

## Implemented Models

* GCN (Graph Convolutional Network)
* GAT (Graph Attention Network)
* GraphSAGE
* GIN (Graph Isomorphism Network)

---

## Supported Tasks

### 1. Node Classification

Datasets:

* Cora
* CiteSeer
* PubMed

Metrics:

* Accuracy
* Macro F1
* Weighted F1
* Training Time
* Memory Usage
* Parameter Count

---

### 2. Link Prediction

Datasets:

* Cora
* CiteSeer
* PubMed

Metrics:

* AUC
* Average Precision
* F1
* Hits@K

Baselines:

* Common Neighbors
* Adamic Adar
* Preferential Attachment

---

### 3. Graph Classification

Datasets:

* MUTAG
* PROTEINS
* ENZYMES
* NCI1

Metrics:

* Accuracy
* Mean ± Standard Deviation
* Confusion Matrix

---

## Features Added

 Train / Test pipeline

 Validation monitoring

 Early Stopping (Patience = 20)

 Hyperparameter tuning

 Random seed reproducibility

```python
SEED = 42
```

 Dropout support

 Link prediction heuristic baselines

 Memory tracking

 Parameter counting

 Result comparison

 Automatic Excel export

---

## Hyperparameters Tested

| Parameter        | Values             |
| ---------------- | ------------------ |
| Hidden Dimension | 32, 64, 128        |
| Learning Rate    | 0.001, 0.005, 0.01 |
| Dropout          | 0.3, 0.5           |
| Weight Decay     | 1e-4, 5e-4         |
| Epochs           | 100–300            |
| Early Stopping   | Patience = 20      |

---

## Generated Result Files

### Standard Runs

results/

* node_results.xlsx
* link_results.xlsx
* graph_results.xlsx

### Hyperparameter Runs

results/

* hyperparameter_results.xlsx

---

## Batch Files

Run all benchmarks:

```bash
run_all.bat
```

Run hyperparameter search:

```bash
run_hyperparameters.bat
```

---

## Example Commands

Node:

```bash
python main.py node gcn cora
```

Link:

```bash
python main.py link gat citeseer
```

Graph:

```bash
python main.py graph gin mutag
```

---

## Best Models

| Task                 | Best Model |
| -------------------- | ---------- |
| Node Classification  | GCN        |
| Link Prediction      | GAT        |
| Graph Classification | GIN        |

---

## Tech Stack

* Python
* PyTorch
* PyTorch Geometric
* NetworkX
* NumPy
* Pandas
* Scikit-learn

---

## Author

Giresh Y
