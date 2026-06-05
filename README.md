# GNN Benchmark Project

Benchmarking Graph Neural Network models across different graph learning tasks.

## Models

- GCN
- GAT
- GraphSAGE
- GIN

## Tasks

### Node Classification
Datasets:
- Cora
- CiteSeer
- PubMed

### Link Prediction
Datasets:
- Cora
- CiteSeer
- PubMed

### Graph Classification
Dataset:
- MUTAG

## Project Structure

gnn-model-benchmark/

├── data/

├── models/

├── tasks/

├── results/

├── utils/

├── main.py

├── requirements.txt

└── README.md


## Run Experiments

Node Classification

```bash
python main.py node gcn cora
```

Link Prediction

```bash
python main.py link gin cora
```

Graph Classification

```bash
python main.py graph gcn mutag
```

## Output

Results are automatically saved inside:

results/

comparison.txt

auto_results.txt

## Current Status

Completed:
- Node Classification
- Link Prediction
- Graph Classification Setup


## Result

- GCN worked best for node classification because neighborhood aggregation was sufficient.

- GAT performed better in link prediction because attention helps identify important connections.

- GIN performed best in graph classification because it captures graph structure more strongly.