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
* Hits@10pct — candidate test edges (positives + sampled negatives) are
  ranked by predicted score; the top 10% of the ranking is taken; this
  metric is the fraction of those top-ranked edges that are true
  positive edges. Computed identically for the GNN models
  (`utils/evaluate.py`) and the heuristic baselines
  (`utils/heuristic_baselines.py`), so the two are directly comparable.

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

The same grid below is run identically for all four models (GCN, GAT,
GraphSAGE, GIN) — same hidden dims, learning rates, dropouts, and weight
decays, same number of combinations each, so models are compared fairly.
Dropout 0.5 is always compared against 0.3 rather than tuned in
isolation. See `run_hyperparameter.bat`.

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

Link (undirected, default):

```bash
python main.py link gat citeseer
```

Link (directed):

```bash
python main.py link gat citeseer 32 0.01 0.5 5e-4 200 1
```

When `directed=1`:
* `RandomLinkSplit` samples negative edges as directed (`is_undirected=False`).
* The model switches to `models/directed_link.py:DirectedLinkEncoder`,
  which wraps the chosen GNN (GCN/GAT/GraphSAGE/GIN, unchanged) and adds
  two small linear heads producing a separate source embedding and
  destination embedding per node.
* Scoring is asymmetric: edge u -> v is scored with
  `dot(src_head(z[u]), dst_head(z[v]))`, which is generally different
  from the score for v -> u. This is what actually makes the prediction
  direction-aware, since the underlying GCNConv/GATConv/SAGEConv/GINConv
  layers still just do standard message passing over `edge_index` either
  way — direction-awareness comes from the two-head wrapper and the
  asymmetric decoder on top, not from the conv layers themselves.
* The heuristic baselines also switch to `nx.DiGraph()` in this mode.

When `directed=0` (default), the original single-embedding encoder and
symmetric decoder are used unchanged, exactly as before this feature was
added.

Graph:

```bash
python main.py graph gin mutag
```

---

## Best Models



| Task  | Dataset  | Best Model | Metric            |
|-------|----------|-----------|---------------------|
| Node  | Cora     | GAT       | Accuracy = 0.7540       |
| Node  | CiteSeer | GAT       | Accuracy = 0.6200       |
| Node  | PubMed   | GAT       | Accuracy = 0.7360       |
| Link  | Cora     | GCN       | AUC = 0.9457            |
| Link  | CiteSeer | GAT       | AUC = 0.8674            |
| Link  | PubMed   | GCN       | AUC = 0.9340            |
| Graph | MUTAG    | GIN       | Accuracy_Mean = 0.8035  |
| Graph | PROTEINS | GIN       | Accuracy_Mean = 0.6892  |
| Graph | ENZYMES  | GraphSAGE       | Accuracy_Mean = 0.3200  |
| Graph | NCI1     | GraphSAGE       | Accuracy_Mean = 0.6560  |



---

## Repository Hygiene

The following are intentionally excluded from version control via
`.gitignore` and should never be pushed to GitHub:

* `__pycache__/` and `*.pyc` files
* `data/` (datasets downloaded automatically by `torch_geometric` on
  first run — large, and trivially regenerated)
* `results/*.xlsx`, `results/*.txt` (generated locally by running
  experiments; not source code)

If any of these were previously committed, remove them from the repo
history/tracking before the next push (e.g. `git rm -r --cached data
results/*.xlsx __pycache__` followed by a commit).

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
