@echo off
set HYPER=1

rem Full grid, identical budget for every model:
rem   hidden_dim    : 32, 64, 128
rem   learning_rate : 0.001, 0.005, 0.01
rem   dropout       : 0.3, 0.5
rem   weight_decay  : 1e-4, 5e-4
rem -> 36 combinations per model, run for gcn/gat/graphsage/gin
rem Results append to results/hyperparameter_results.xlsx

echo ===================
echo NODE CLASSIFICATION (CORA)
echo ===================

echo --- GCN ---
python main.py node gcn cora 32 0.001 0.3 1e-4 200
python main.py node gcn cora 32 0.001 0.3 5e-4 200
python main.py node gcn cora 32 0.001 0.5 1e-4 200
python main.py node gcn cora 32 0.001 0.5 5e-4 200
python main.py node gcn cora 32 0.005 0.3 1e-4 200
python main.py node gcn cora 32 0.005 0.3 5e-4 200
python main.py node gcn cora 32 0.005 0.5 1e-4 200
python main.py node gcn cora 32 0.005 0.5 5e-4 200
python main.py node gcn cora 32 0.01 0.3 1e-4 200
python main.py node gcn cora 32 0.01 0.3 5e-4 200
python main.py node gcn cora 32 0.01 0.5 1e-4 200
python main.py node gcn cora 32 0.01 0.5 5e-4 200
python main.py node gcn cora 64 0.001 0.3 1e-4 200
python main.py node gcn cora 64 0.001 0.3 5e-4 200
python main.py node gcn cora 64 0.001 0.5 1e-4 200
python main.py node gcn cora 64 0.001 0.5 5e-4 200
python main.py node gcn cora 64 0.005 0.3 1e-4 200
python main.py node gcn cora 64 0.005 0.3 5e-4 200
python main.py node gcn cora 64 0.005 0.5 1e-4 200
python main.py node gcn cora 64 0.005 0.5 5e-4 200
python main.py node gcn cora 64 0.01 0.3 1e-4 200
python main.py node gcn cora 64 0.01 0.3 5e-4 200
python main.py node gcn cora 64 0.01 0.5 1e-4 200
python main.py node gcn cora 64 0.01 0.5 5e-4 200
python main.py node gcn cora 128 0.001 0.3 1e-4 200
python main.py node gcn cora 128 0.001 0.3 5e-4 200
python main.py node gcn cora 128 0.001 0.5 1e-4 200
python main.py node gcn cora 128 0.001 0.5 5e-4 200
python main.py node gcn cora 128 0.005 0.3 1e-4 200
python main.py node gcn cora 128 0.005 0.3 5e-4 200
python main.py node gcn cora 128 0.005 0.5 1e-4 200
python main.py node gcn cora 128 0.005 0.5 5e-4 200
python main.py node gcn cora 128 0.01 0.3 1e-4 200
python main.py node gcn cora 128 0.01 0.3 5e-4 200
python main.py node gcn cora 128 0.01 0.5 1e-4 200
python main.py node gcn cora 128 0.01 0.5 5e-4 200

echo --- GAT ---
python main.py node gat cora 32 0.001 0.3 1e-4 200
python main.py node gat cora 32 0.001 0.3 5e-4 200
python main.py node gat cora 32 0.001 0.5 1e-4 200
python main.py node gat cora 32 0.001 0.5 5e-4 200
python main.py node gat cora 32 0.005 0.3 1e-4 200
python main.py node gat cora 32 0.005 0.3 5e-4 200
python main.py node gat cora 32 0.005 0.5 1e-4 200
python main.py node gat cora 32 0.005 0.5 5e-4 200
python main.py node gat cora 32 0.01 0.3 1e-4 200
python main.py node gat cora 32 0.01 0.3 5e-4 200
python main.py node gat cora 32 0.01 0.5 1e-4 200
python main.py node gat cora 32 0.01 0.5 5e-4 200
python main.py node gat cora 64 0.001 0.3 1e-4 200
python main.py node gat cora 64 0.001 0.3 5e-4 200
python main.py node gat cora 64 0.001 0.5 1e-4 200
python main.py node gat cora 64 0.001 0.5 5e-4 200
python main.py node gat cora 64 0.005 0.3 1e-4 200
python main.py node gat cora 64 0.005 0.3 5e-4 200
python main.py node gat cora 64 0.005 0.5 1e-4 200
python main.py node gat cora 64 0.005 0.5 5e-4 200
python main.py node gat cora 64 0.01 0.3 1e-4 200
python main.py node gat cora 64 0.01 0.3 5e-4 200
python main.py node gat cora 64 0.01 0.5 1e-4 200
python main.py node gat cora 64 0.01 0.5 5e-4 200
python main.py node gat cora 128 0.001 0.3 1e-4 200
python main.py node gat cora 128 0.001 0.3 5e-4 200
python main.py node gat cora 128 0.001 0.5 1e-4 200
python main.py node gat cora 128 0.001 0.5 5e-4 200
python main.py node gat cora 128 0.005 0.3 1e-4 200
python main.py node gat cora 128 0.005 0.3 5e-4 200
python main.py node gat cora 128 0.005 0.5 1e-4 200
python main.py node gat cora 128 0.005 0.5 5e-4 200
python main.py node gat cora 128 0.01 0.3 1e-4 200
python main.py node gat cora 128 0.01 0.3 5e-4 200
python main.py node gat cora 128 0.01 0.5 1e-4 200
python main.py node gat cora 128 0.01 0.5 5e-4 200

echo --- GRAPHSAGE ---
python main.py node graphsage cora 32 0.001 0.3 1e-4 200
python main.py node graphsage cora 32 0.001 0.3 5e-4 200
python main.py node graphsage cora 32 0.001 0.5 1e-4 200
python main.py node graphsage cora 32 0.001 0.5 5e-4 200
python main.py node graphsage cora 32 0.005 0.3 1e-4 200
python main.py node graphsage cora 32 0.005 0.3 5e-4 200
python main.py node graphsage cora 32 0.005 0.5 1e-4 200
python main.py node graphsage cora 32 0.005 0.5 5e-4 200
python main.py node graphsage cora 32 0.01 0.3 1e-4 200
python main.py node graphsage cora 32 0.01 0.3 5e-4 200
python main.py node graphsage cora 32 0.01 0.5 1e-4 200
python main.py node graphsage cora 32 0.01 0.5 5e-4 200
python main.py node graphsage cora 64 0.001 0.3 1e-4 200
python main.py node graphsage cora 64 0.001 0.3 5e-4 200
python main.py node graphsage cora 64 0.001 0.5 1e-4 200
python main.py node graphsage cora 64 0.001 0.5 5e-4 200
python main.py node graphsage cora 64 0.005 0.3 1e-4 200
python main.py node graphsage cora 64 0.005 0.3 5e-4 200
python main.py node graphsage cora 64 0.005 0.5 1e-4 200
python main.py node graphsage cora 64 0.005 0.5 5e-4 200
python main.py node graphsage cora 64 0.01 0.3 1e-4 200
python main.py node graphsage cora 64 0.01 0.3 5e-4 200
python main.py node graphsage cora 64 0.01 0.5 1e-4 200
python main.py node graphsage cora 64 0.01 0.5 5e-4 200
python main.py node graphsage cora 128 0.001 0.3 1e-4 200
python main.py node graphsage cora 128 0.001 0.3 5e-4 200
python main.py node graphsage cora 128 0.001 0.5 1e-4 200
python main.py node graphsage cora 128 0.001 0.5 5e-4 200
python main.py node graphsage cora 128 0.005 0.3 1e-4 200
python main.py node graphsage cora 128 0.005 0.3 5e-4 200
python main.py node graphsage cora 128 0.005 0.5 1e-4 200
python main.py node graphsage cora 128 0.005 0.5 5e-4 200
python main.py node graphsage cora 128 0.01 0.3 1e-4 200
python main.py node graphsage cora 128 0.01 0.3 5e-4 200
python main.py node graphsage cora 128 0.01 0.5 1e-4 200
python main.py node graphsage cora 128 0.01 0.5 5e-4 200

echo --- GIN ---
python main.py node gin cora 32 0.001 0.3 1e-4 200
python main.py node gin cora 32 0.001 0.3 5e-4 200
python main.py node gin cora 32 0.001 0.5 1e-4 200
python main.py node gin cora 32 0.001 0.5 5e-4 200
python main.py node gin cora 32 0.005 0.3 1e-4 200
python main.py node gin cora 32 0.005 0.3 5e-4 200
python main.py node gin cora 32 0.005 0.5 1e-4 200
python main.py node gin cora 32 0.005 0.5 5e-4 200
python main.py node gin cora 32 0.01 0.3 1e-4 200
python main.py node gin cora 32 0.01 0.3 5e-4 200
python main.py node gin cora 32 0.01 0.5 1e-4 200
python main.py node gin cora 32 0.01 0.5 5e-4 200
python main.py node gin cora 64 0.001 0.3 1e-4 200
python main.py node gin cora 64 0.001 0.3 5e-4 200
python main.py node gin cora 64 0.001 0.5 1e-4 200
python main.py node gin cora 64 0.001 0.5 5e-4 200
python main.py node gin cora 64 0.005 0.3 1e-4 200
python main.py node gin cora 64 0.005 0.3 5e-4 200
python main.py node gin cora 64 0.005 0.5 1e-4 200
python main.py node gin cora 64 0.005 0.5 5e-4 200
python main.py node gin cora 64 0.01 0.3 1e-4 200
python main.py node gin cora 64 0.01 0.3 5e-4 200
python main.py node gin cora 64 0.01 0.5 1e-4 200
python main.py node gin cora 64 0.01 0.5 5e-4 200
python main.py node gin cora 128 0.001 0.3 1e-4 200
python main.py node gin cora 128 0.001 0.3 5e-4 200
python main.py node gin cora 128 0.001 0.5 1e-4 200
python main.py node gin cora 128 0.001 0.5 5e-4 200
python main.py node gin cora 128 0.005 0.3 1e-4 200
python main.py node gin cora 128 0.005 0.3 5e-4 200
python main.py node gin cora 128 0.005 0.5 1e-4 200
python main.py node gin cora 128 0.005 0.5 5e-4 200
python main.py node gin cora 128 0.01 0.3 1e-4 200
python main.py node gin cora 128 0.01 0.3 5e-4 200
python main.py node gin cora 128 0.01 0.5 1e-4 200
python main.py node gin cora 128 0.01 0.5 5e-4 200


echo ===================
echo LINK PREDICTION (CORA)
echo ===================

echo --- GCN ---
python main.py link gcn cora 32 0.001 0.3 1e-4 200 1
python main.py link gcn cora 32 0.001 0.3 5e-4 200 1
python main.py link gcn cora 32 0.001 0.5 1e-4 200 1
python main.py link gcn cora 32 0.001 0.5 5e-4 200 1
python main.py link gcn cora 32 0.005 0.3 1e-4 200 1
python main.py link gcn cora 32 0.005 0.3 5e-4 200 1
python main.py link gcn cora 32 0.005 0.5 1e-4 200 1
python main.py link gcn cora 32 0.005 0.5 5e-4 200 1
python main.py link gcn cora 32 0.01 0.3 1e-4 200 1
python main.py link gcn cora 32 0.01 0.3 5e-4 200 1
python main.py link gcn cora 32 0.01 0.5 1e-4 200 1
python main.py link gcn cora 32 0.01 0.5 5e-4 200 1
python main.py link gcn cora 64 0.001 0.3 1e-4 200 1
python main.py link gcn cora 64 0.001 0.3 5e-4 200 1
python main.py link gcn cora 64 0.001 0.5 1e-4 200 1
python main.py link gcn cora 64 0.001 0.5 5e-4 200 1
python main.py link gcn cora 64 0.005 0.3 1e-4 200 1
python main.py link gcn cora 64 0.005 0.3 5e-4 200 1
python main.py link gcn cora 64 0.005 0.5 1e-4 200 1
python main.py link gcn cora 64 0.005 0.5 5e-4 200 1
python main.py link gcn cora 64 0.01 0.3 1e-4 200 1
python main.py link gcn cora 64 0.01 0.3 5e-4 200 1 
python main.py link gcn cora 64 0.01 0.5 1e-4 200 1
python main.py link gcn cora 64 0.01 0.5 5e-4 200 1
python main.py link gcn cora 128 0.001 0.3 1e-4 200 1
python main.py link gcn cora 128 0.001 0.3 5e-4 200 1
python main.py link gcn cora 128 0.001 0.5 1e-4 200 1
python main.py link gcn cora 128 0.001 0.5 5e-4 200 1
python main.py link gcn cora 128 0.005 0.3 1e-4 200 1
python main.py link gcn cora 128 0.005 0.3 5e-4 200 1
python main.py link gcn cora 128 0.005 0.5 1e-4 200 1
python main.py link gcn cora 128 0.005 0.5 5e-4 200 1
python main.py link gcn cora 128 0.01 0.3 1e-4 200 1
python main.py link gcn cora 128 0.01 0.3 5e-4 200 1
python main.py link gcn cora 128 0.01 0.5 1e-4 200 1
python main.py link gcn cora 128 0.01 0.5 5e-4 200 1

echo --- GAT ---
python main.py link gat cora 32 0.001 0.3 1e-4 200 1
python main.py link gat cora 32 0.001 0.3 5e-4 200 1
python main.py link gat cora 32 0.001 0.5 1e-4 200 1
python main.py link gat cora 32 0.001 0.5 5e-4 200 1
python main.py link gat cora 32 0.005 0.3 1e-4 200 1
python main.py link gat cora 32 0.005 0.3 5e-4 200
python main.py link gat cora 32 0.005 0.5 1e-4 200
python main.py link gat cora 32 0.005 0.5 5e-4 200
python main.py link gat cora 32 0.01 0.3 1e-4 200
python main.py link gat cora 32 0.01 0.3 5e-4 200
python main.py link gat cora 32 0.01 0.5 1e-4 200
python main.py link gat cora 32 0.01 0.5 5e-4 200
python main.py link gat cora 64 0.001 0.3 1e-4 200
python main.py link gat cora 64 0.001 0.3 5e-4 200
python main.py link gat cora 64 0.001 0.5 1e-4 200
python main.py link gat cora 64 0.001 0.5 5e-4 200
python main.py link gat cora 64 0.005 0.3 1e-4 200 1
python main.py link gat cora 64 0.005 0.3 5e-4 200
python main.py link gat cora 64 0.005 0.5 1e-4 200
python main.py link gat cora 64 0.005 0.5 5e-4 200
python main.py link gat cora 64 0.01 0.3 1e-4 200 1
python main.py link gat cora 64 0.01 0.3 5e-4 200
python main.py link gat cora 64 0.01 0.5 1e-4 200 1
python main.py link gat cora 64 0.01 0.5 5e-4 200
python main.py link gat cora 128 0.001 0.3 1e-4 200
python main.py link gat cora 128 0.001 0.3 5e-4 200
python main.py link gat cora 128 0.001 0.5 1e-4 200
python main.py link gat cora 128 0.001 0.5 5e-4 200
python main.py link gat cora 128 0.005 0.3 1e-4 200
python main.py link gat cora 128 0.005 0.3 5e-4 200
python main.py link gat cora 128 0.005 0.5 1e-4 200
python main.py link gat cora 128 0.005 0.5 5e-4 200 1
python main.py link gat cora 128 0.01 0.3 1e-4 200
python main.py link gat cora 128 0.01 0.3 5e-4 200
python main.py link gat cora 128 0.01 0.5 1e-4 200
python main.py link gat cora 128 0.01 0.5 5e-4 200

echo --- GRAPHSAGE ---
python main.py link graphsage cora 32 0.001 0.3 1e-4 200
python main.py link graphsage cora 32 0.001 0.3 5e-4 200
python main.py link graphsage cora 32 0.001 0.5 1e-4 200
python main.py link graphsage cora 32 0.001 0.5 5e-4 200
python main.py link graphsage cora 32 0.005 0.3 1e-4 200
python main.py link graphsage cora 32 0.005 0.3 5e-4 200
python main.py link graphsage cora 32 0.005 0.5 1e-4 200
python main.py link graphsage cora 32 0.005 0.5 5e-4 200
python main.py link graphsage cora 32 0.01 0.3 1e-4 200
python main.py link graphsage cora 32 0.01 0.3 5e-4 200
python main.py link graphsage cora 32 0.01 0.5 1e-4 200
python main.py link graphsage cora 32 0.01 0.5 5e-4 200
python main.py link graphsage cora 64 0.001 0.3 1e-4 200 1
python main.py link graphsage cora 64 0.001 0.3 5e-4 200
python main.py link graphsage cora 64 0.001 0.5 1e-4 200
python main.py link graphsage cora 64 0.001 0.5 5e-4 200
python main.py link graphsage cora 64 0.005 0.3 1e-4 200
python main.py link graphsage cora 64 0.005 0.3 5e-4 200
python main.py link graphsage cora 64 0.005 0.5 1e-4 200
python main.py link graphsage cora 64 0.005 0.5 5e-4 200
python main.py link graphsage cora 64 0.01 0.3 1e-4 200
python main.py link graphsage cora 64 0.01 0.3 5e-4 200
python main.py link graphsage cora 64 0.01 0.5 1e-4 200
python main.py link graphsage cora 64 0.01 0.5 5e-4 200
python main.py link graphsage cora 128 0.001 0.3 1e-4 200 1
python main.py link graphsage cora 128 0.001 0.3 5e-4 200
python main.py link graphsage cora 128 0.001 0.5 1e-4 200
python main.py link graphsage cora 128 0.001 0.5 5e-4 200
python main.py link graphsage cora 128 0.005 0.3 1e-4 200
python main.py link graphsage cora 128 0.005 0.3 5e-4 200
python main.py link graphsage cora 128 0.005 0.5 1e-4 200
python main.py link graphsage cora 128 0.005 0.5 5e-4 200 1
python main.py link graphsage cora 128 0.01 0.3 1e-4 200
python main.py link graphsage cora 128 0.01 0.3 5e-4 200
python main.py link graphsage cora 128 0.01 0.5 1e-4 200
python main.py link graphsage cora 128 0.01 0.5 5e-4 200

echo --- GIN ---
python main.py link gin cora 32 0.001 0.3 1e-4 200
python main.py link gin cora 32 0.001 0.3 5e-4 200
python main.py link gin cora 32 0.001 0.5 1e-4 200
python main.py link gin cora 32 0.001 0.5 5e-4 200
python main.py link gin cora 32 0.005 0.3 1e-4 200 1
python main.py link gin cora 32 0.005 0.3 5e-4 200
python main.py link gin cora 32 0.005 0.5 1e-4 200
python main.py link gin cora 32 0.005 0.5 5e-4 200
python main.py link gin cora 32 0.01 0.3 1e-4 200 1
python main.py link gin cora 32 0.01 0.3 5e-4 200
python main.py link gin cora 32 0.01 0.5 1e-4 200
python main.py link gin cora 32 0.01 0.5 5e-4 200
python main.py link gin cora 64 0.001 0.3 1e-4 200
python main.py link gin cora 64 0.001 0.3 5e-4 200
python main.py link gin cora 64 0.001 0.5 1e-4 200
python main.py link gin cora 64 0.001 0.5 5e-4 200
python main.py link gin cora 64 0.005 0.3 1e-4 200
python main.py link gin cora 64 0.005 0.3 5e-4 200
python main.py link gin cora 64 0.005 0.5 1e-4 200
python main.py link gin cora 64 0.005 0.5 5e-4 200
python main.py link gin cora 64 0.01 0.3 1e-4 200
python main.py link gin cora 64 0.01 0.3 5e-4 200
python main.py link gin cora 64 0.01 0.5 1e-4 200
python main.py link gin cora 64 0.01 0.5 5e-4 200 1
python main.py link gin cora 128 0.001 0.3 1e-4 200
python main.py link gin cora 128 0.001 0.3 5e-4 200
python main.py link gin cora 128 0.001 0.5 1e-4 200 1
python main.py link gin cora 128 0.001 0.5 5e-4 200
python main.py link gin cora 128 0.005 0.3 1e-4 200
python main.py link gin cora 128 0.005 0.3 5e-4 200
python main.py link gin cora 128 0.005 0.5 1e-4 200
python main.py link gin cora 128 0.005 0.5 5e-4 200 1
python main.py link gin cora 128 0.01 0.3 1e-4 200
python main.py link gin cora 128 0.01 0.3 5e-4 200
python main.py link gin cora 128 0.01 0.5 1e-4 200
python main.py link gin cora 128 0.01 0.5 5e-4 200 1


echo ===================
echo GRAPH CLASSIFICATION (MUTAG)
echo ===================

echo --- GCN ---
python main.py graph gcn mutag 32 0.001 0.3 1e-4 100
python main.py graph gcn mutag 32 0.001 0.3 5e-4 100
python main.py graph gcn mutag 32 0.001 0.5 1e-4 100
python main.py graph gcn mutag 32 0.001 0.5 5e-4 100
python main.py graph gcn mutag 32 0.005 0.3 1e-4 100
python main.py graph gcn mutag 32 0.005 0.3 5e-4 100
python main.py graph gcn mutag 32 0.005 0.5 1e-4 100
python main.py graph gcn mutag 32 0.005 0.5 5e-4 100
python main.py graph gcn mutag 32 0.01 0.3 1e-4 100
python main.py graph gcn mutag 32 0.01 0.3 5e-4 100
python main.py graph gcn mutag 32 0.01 0.5 1e-4 100
python main.py graph gcn mutag 32 0.01 0.5 5e-4 100
python main.py graph gcn mutag 64 0.001 0.3 1e-4 100
python main.py graph gcn mutag 64 0.001 0.3 5e-4 100
python main.py graph gcn mutag 64 0.001 0.5 1e-4 100
python main.py graph gcn mutag 64 0.001 0.5 5e-4 100
python main.py graph gcn mutag 64 0.005 0.3 1e-4 100
python main.py graph gcn mutag 64 0.005 0.3 5e-4 100
python main.py graph gcn mutag 64 0.005 0.5 1e-4 100
python main.py graph gcn mutag 64 0.005 0.5 5e-4 100
python main.py graph gcn mutag 64 0.01 0.3 1e-4 100
python main.py graph gcn mutag 64 0.01 0.3 5e-4 100
python main.py graph gcn mutag 64 0.01 0.5 1e-4 100
python main.py graph gcn mutag 64 0.01 0.5 5e-4 100
python main.py graph gcn mutag 128 0.001 0.3 1e-4 100
python main.py graph gcn mutag 128 0.001 0.3 5e-4 100
python main.py graph gcn mutag 128 0.001 0.5 1e-4 100
python main.py graph gcn mutag 128 0.001 0.5 5e-4 100
python main.py graph gcn mutag 128 0.005 0.3 1e-4 100
python main.py graph gcn mutag 128 0.005 0.3 5e-4 100
python main.py graph gcn mutag 128 0.005 0.5 1e-4 100
python main.py graph gcn mutag 128 0.005 0.5 5e-4 100
python main.py graph gcn mutag 128 0.01 0.3 1e-4 100
python main.py graph gcn mutag 128 0.01 0.3 5e-4 100
python main.py graph gcn mutag 128 0.01 0.5 1e-4 100
python main.py graph gcn mutag 128 0.01 0.5 5e-4 100

echo --- GAT ---
python main.py graph gat mutag 32 0.001 0.3 1e-4 100
python main.py graph gat mutag 32 0.001 0.3 5e-4 100
python main.py graph gat mutag 32 0.001 0.5 1e-4 100
python main.py graph gat mutag 32 0.001 0.5 5e-4 100
python main.py graph gat mutag 32 0.005 0.3 1e-4 100
python main.py graph gat mutag 32 0.005 0.3 5e-4 100
python main.py graph gat mutag 32 0.005 0.5 1e-4 100
python main.py graph gat mutag 32 0.005 0.5 5e-4 100
python main.py graph gat mutag 32 0.01 0.3 1e-4 100
python main.py graph gat mutag 32 0.01 0.3 5e-4 100
python main.py graph gat mutag 32 0.01 0.5 1e-4 100
python main.py graph gat mutag 32 0.01 0.5 5e-4 100
python main.py graph gat mutag 64 0.001 0.3 1e-4 100
python main.py graph gat mutag 64 0.001 0.3 5e-4 100
python main.py graph gat mutag 64 0.001 0.5 1e-4 100
python main.py graph gat mutag 64 0.001 0.5 5e-4 100
python main.py graph gat mutag 64 0.005 0.3 1e-4 100
python main.py graph gat mutag 64 0.005 0.3 5e-4 100
python main.py graph gat mutag 64 0.005 0.5 1e-4 100
python main.py graph gat mutag 64 0.005 0.5 5e-4 100
python main.py graph gat mutag 64 0.01 0.3 1e-4 100
python main.py graph gat mutag 64 0.01 0.3 5e-4 100
python main.py graph gat mutag 64 0.01 0.5 1e-4 100
python main.py graph gat mutag 64 0.01 0.5 5e-4 100
python main.py graph gat mutag 128 0.001 0.3 1e-4 100
python main.py graph gat mutag 128 0.001 0.3 5e-4 100
python main.py graph gat mutag 128 0.001 0.5 1e-4 100
python main.py graph gat mutag 128 0.001 0.5 5e-4 100
python main.py graph gat mutag 128 0.005 0.3 1e-4 100
python main.py graph gat mutag 128 0.005 0.3 5e-4 100
python main.py graph gat mutag 128 0.005 0.5 1e-4 100
python main.py graph gat mutag 128 0.005 0.5 5e-4 100
python main.py graph gat mutag 128 0.01 0.3 1e-4 100
python main.py graph gat mutag 128 0.01 0.3 5e-4 100
python main.py graph gat mutag 128 0.01 0.5 1e-4 100
python main.py graph gat mutag 128 0.01 0.5 5e-4 100

echo --- GRAPHSAGE ---
python main.py graph graphsage mutag 32 0.001 0.3 1e-4 100
python main.py graph graphsage mutag 32 0.001 0.3 5e-4 100
python main.py graph graphsage mutag 32 0.001 0.5 1e-4 100
python main.py graph graphsage mutag 32 0.001 0.5 5e-4 100
python main.py graph graphsage mutag 32 0.005 0.3 1e-4 100
python main.py graph graphsage mutag 32 0.005 0.3 5e-4 100
python main.py graph graphsage mutag 32 0.005 0.5 1e-4 100
python main.py graph graphsage mutag 32 0.005 0.5 5e-4 100
python main.py graph graphsage mutag 32 0.01 0.3 1e-4 100
python main.py graph graphsage mutag 32 0.01 0.3 5e-4 100
python main.py graph graphsage mutag 32 0.01 0.5 1e-4 100
python main.py graph graphsage mutag 32 0.01 0.5 5e-4 100
python main.py graph graphsage mutag 64 0.001 0.3 1e-4 100
python main.py graph graphsage mutag 64 0.001 0.3 5e-4 100
python main.py graph graphsage mutag 64 0.001 0.5 1e-4 100
python main.py graph graphsage mutag 64 0.001 0.5 5e-4 100
python main.py graph graphsage mutag 64 0.005 0.3 1e-4 100
python main.py graph graphsage mutag 64 0.005 0.3 5e-4 100
python main.py graph graphsage mutag 64 0.005 0.5 1e-4 100
python main.py graph graphsage mutag 64 0.005 0.5 5e-4 100
python main.py graph graphsage mutag 64 0.01 0.3 1e-4 100
python main.py graph graphsage mutag 64 0.01 0.3 5e-4 100
python main.py graph graphsage mutag 64 0.01 0.5 1e-4 100
python main.py graph graphsage mutag 64 0.01 0.5 5e-4 100
python main.py graph graphsage mutag 128 0.001 0.3 1e-4 100
python main.py graph graphsage mutag 128 0.001 0.3 5e-4 100
python main.py graph graphsage mutag 128 0.001 0.5 1e-4 100
python main.py graph graphsage mutag 128 0.001 0.5 5e-4 100
python main.py graph graphsage mutag 128 0.005 0.3 1e-4 100
python main.py graph graphsage mutag 128 0.005 0.3 5e-4 100
python main.py graph graphsage mutag 128 0.005 0.5 1e-4 100
python main.py graph graphsage mutag 128 0.005 0.5 5e-4 100
python main.py graph graphsage mutag 128 0.01 0.3 1e-4 100
python main.py graph graphsage mutag 128 0.01 0.3 5e-4 100
python main.py graph graphsage mutag 128 0.01 0.5 1e-4 100
python main.py graph graphsage mutag 128 0.01 0.5 5e-4 100

echo --- GIN ---
python main.py graph gin mutag 32 0.001 0.3 1e-4 100
python main.py graph gin mutag 32 0.001 0.3 5e-4 100
python main.py graph gin mutag 32 0.001 0.5 1e-4 100
python main.py graph gin mutag 32 0.001 0.5 5e-4 100
python main.py graph gin mutag 32 0.005 0.3 1e-4 100
python main.py graph gin mutag 32 0.005 0.3 5e-4 100
python main.py graph gin mutag 32 0.005 0.5 1e-4 100
python main.py graph gin mutag 32 0.005 0.5 5e-4 100
python main.py graph gin mutag 32 0.01 0.3 1e-4 100
python main.py graph gin mutag 32 0.01 0.3 5e-4 100
python main.py graph gin mutag 32 0.01 0.5 1e-4 100
python main.py graph gin mutag 32 0.01 0.5 5e-4 100
python main.py graph gin mutag 64 0.001 0.3 1e-4 100
python main.py graph gin mutag 64 0.001 0.3 5e-4 100
python main.py graph gin mutag 64 0.001 0.5 1e-4 100
python main.py graph gin mutag 64 0.001 0.5 5e-4 100
python main.py graph gin mutag 64 0.005 0.3 1e-4 100
python main.py graph gin mutag 64 0.005 0.3 5e-4 100
python main.py graph gin mutag 64 0.005 0.5 1e-4 100
python main.py graph gin mutag 64 0.005 0.5 5e-4 100
python main.py graph gin mutag 64 0.01 0.3 1e-4 100
python main.py graph gin mutag 64 0.01 0.3 5e-4 100
python main.py graph gin mutag 64 0.01 0.5 1e-4 100
python main.py graph gin mutag 64 0.01 0.5 5e-4 100
python main.py graph gin mutag 128 0.001 0.3 1e-4 100
python main.py graph gin mutag 128 0.001 0.3 5e-4 100
python main.py graph gin mutag 128 0.001 0.5 1e-4 100
python main.py graph gin mutag 128 0.001 0.5 5e-4 100
python main.py graph gin mutag 128 0.005 0.3 1e-4 100
python main.py graph gin mutag 128 0.005 0.3 5e-4 100
python main.py graph gin mutag 128 0.005 0.5 1e-4 100
python main.py graph gin mutag 128 0.005 0.5 5e-4 100
python main.py graph gin mutag 128 0.01 0.3 1e-4 100
python main.py graph gin mutag 128 0.01 0.3 5e-4 100
python main.py graph gin mutag 128 0.01 0.5 1e-4 100
python main.py graph gin mutag 128 0.01 0.5 5e-4 100


echo COMPLETE

set HYPER=
pause
