@echo off
set HYPER=1

echo ===================
echo NODE CLASSIFICATION
echo ===================

echo =================== CORA ===================
echo --- GCN ---
python main.py node gcn cora 32 0.001 0.3 1e-4 200
python main.py node gcn cora 32 0.001 0.3 5e-4 200
python main.py node gcn cora 32 0.005 0.3 1e-4 200
python main.py node gcn cora 32 0.005 0.3 5e-4 200
python main.py node gcn cora 32 0.01 0.3 1e-4 200
python main.py node gcn cora 32 0.01 0.3 5e-4 200
python main.py node gcn cora 64 0.001 0.3 1e-4 200
python main.py node gcn cora 64 0.001 0.3 5e-4 200
python main.py node gcn cora 64 0.005 0.3 1e-4 200
python main.py node gcn cora 64 0.005 0.3 5e-4 200
python main.py node gcn cora 64 0.01 0.3 1e-4 200
python main.py node gcn cora 64 0.01 0.3 5e-4 200
python main.py node gcn cora 128 0.001 0.5 1e-4 200
python main.py node gcn cora 128 0.001 0.5 5e-4 200
python main.py node gcn cora 128 0.005 0.5 1e-4 200
python main.py node gcn cora 128 0.005 0.5 5e-4 200
python main.py node gcn cora 128 0.01 0.5 1e-4 200
python main.py node gcn cora 128 0.01 0.5 5e-4 200

echo --- GAT ---
python main.py node gat cora 32 0.001 0.3 1e-4 200
python main.py node gat cora 32 0.001 0.3 5e-4 200
python main.py node gat cora 32 0.005 0.3 1e-4 200
python main.py node gat cora 32 0.005 0.3 5e-4 200
python main.py node gat cora 32 0.01 0.3 1e-4 200
python main.py node gat cora 32 0.01 0.3 5e-4 200
python main.py node gat cora 64 0.001 0.3 1e-4 200
python main.py node gat cora 64 0.001 0.3 5e-4 200
python main.py node gat cora 64 0.005 0.3 1e-4 200
python main.py node gat cora 64 0.005 0.3 5e-4 200
python main.py node gat cora 64 0.01 0.3 1e-4 200
python main.py node gat cora 64 0.01 0.3 5e-4 200
python main.py node gat cora 128 0.001 0.5 1e-4 200
python main.py node gat cora 128 0.001 0.5 5e-4 200
python main.py node gat cora 128 0.005 0.5 1e-4 200
python main.py node gat cora 128 0.005 0.5 5e-4 200
python main.py node gat cora 128 0.01 0.5 1e-4 200
python main.py node gat cora 128 0.01 0.5 5e-4 200

echo --- GRAPHSAGE ---
python main.py node graphsage cora 32 0.001 0.3 1e-4 200
python main.py node graphsage cora 32 0.001 0.3 5e-4 200
python main.py node graphsage cora 32 0.005 0.3 1e-4 200
python main.py node graphsage cora 32 0.005 0.3 5e-4 200
python main.py node graphsage cora 32 0.01 0.3 1e-4 200
python main.py node graphsage cora 32 0.01 0.3 5e-4 200
python main.py node graphsage cora 64 0.001 0.3 1e-4 200
python main.py node graphsage cora 64 0.001 0.3 5e-4 200
python main.py node graphsage cora 64 0.005 0.3 1e-4 200
python main.py node graphsage cora 64 0.005 0.3 5e-4 200
python main.py node graphsage cora 64 0.01 0.3 1e-4 200
python main.py node graphsage cora 64 0.01 0.3 5e-4 200
python main.py node graphsage cora 128 0.001 0.5 1e-4 200
python main.py node graphsage cora 128 0.001 0.5 5e-4 200
python main.py node graphsage cora 128 0.005 0.5 1e-4 200
python main.py node graphsage cora 128 0.005 0.5 5e-4 200
python main.py node graphsage cora 128 0.01 0.5 1e-4 200
python main.py node graphsage cora 128 0.01 0.5 5e-4 200

echo --- GIN ---
python main.py node gin cora 32 0.001 0.3 1e-4 200
python main.py node gin cora 32 0.001 0.3 5e-4 200
python main.py node gin cora 32 0.005 0.3 1e-4 200
python main.py node gin cora 32 0.005 0.3 5e-4 200
python main.py node gin cora 32 0.01 0.3 1e-4 200
python main.py node gin cora 32 0.01 0.3 5e-4 200
python main.py node gin cora 64 0.001 0.3 1e-4 200
python main.py node gin cora 64 0.001 0.3 5e-4 200
python main.py node gin cora 64 0.005 0.3 1e-4 200
python main.py node gin cora 64 0.005 0.3 5e-4 200
python main.py node gin cora 64 0.01 0.3 1e-4 200
python main.py node gin cora 64 0.01 0.3 5e-4 200
python main.py node gin cora 128 0.001 0.5 1e-4 200
python main.py node gin cora 128 0.001 0.5 5e-4 200
python main.py node gin cora 128 0.005 0.5 1e-4 200
python main.py node gin cora 128 0.005 0.5 5e-4 200
python main.py node gin cora 128 0.01 0.5 1e-4 200
python main.py node gin cora 128 0.01 0.5 5e-4 200

echo =================== CITESEER ===================
echo --- GCN ---
python main.py node gcn citeseer 32 0.001 0.3 1e-4 200
python main.py node gcn citeseer 32 0.001 0.3 5e-4 200
python main.py node gcn citeseer 32 0.005 0.3 1e-4 200
python main.py node gcn citeseer 32 0.005 0.3 5e-4 200
python main.py node gcn citeseer 32 0.01 0.3 1e-4 200
python main.py node gcn citeseer 32 0.01 0.3 5e-4 200
python main.py node gcn citeseer 64 0.001 0.3 1e-4 200
python main.py node gcn citeseer 64 0.001 0.3 5e-4 200
python main.py node gcn citeseer 64 0.005 0.3 1e-4 200
python main.py node gcn citeseer 64 0.005 0.3 5e-4 200
python main.py node gcn citeseer 64 0.01 0.3 1e-4 200
python main.py node gcn citeseer 64 0.01 0.3 5e-4 200
python main.py node gcn citeseer 128 0.001 0.5 1e-4 200
python main.py node gcn citeseer 128 0.001 0.5 5e-4 200
python main.py node gcn citeseer 128 0.005 0.5 1e-4 200
python main.py node gcn citeseer 128 0.005 0.5 5e-4 200
python main.py node gcn citeseer 128 0.01 0.5 1e-4 200
python main.py node gcn citeseer 128 0.01 0.5 5e-4 200

echo --- GAT ---
python main.py node gat citeseer 32 0.001 0.3 1e-4 200
python main.py node gat citeseer 32 0.001 0.3 5e-4 200
python main.py node gat citeseer 32 0.005 0.3 1e-4 200
python main.py node gat citeseer 32 0.005 0.3 5e-4 200
python main.py node gat citeseer 32 0.01 0.3 1e-4 200
python main.py node gat citeseer 32 0.01 0.3 5e-4 200
python main.py node gat citeseer 64 0.001 0.3 1e-4 200
python main.py node gat citeseer 64 0.001 0.3 5e-4 200
python main.py node gat citeseer 64 0.005 0.3 1e-4 200
python main.py node gat citeseer 64 0.005 0.3 5e-4 200
python main.py node gat citeseer 64 0.01 0.3 1e-4 200
python main.py node gat citeseer 64 0.01 0.3 5e-4 200
python main.py node gat citeseer 128 0.001 0.5 1e-4 200
python main.py node gat citeseer 128 0.001 0.5 5e-4 200
python main.py node gat citeseer 128 0.005 0.5 1e-4 200
python main.py node gat citeseer 128 0.005 0.5 5e-4 200
python main.py node gat citeseer 128 0.01 0.5 1e-4 200
python main.py node gat citeseer 128 0.01 0.5 5e-4 200

echo --- GRAPHSAGE ---
python main.py node graphsage citeseer 32 0.001 0.3 1e-4 200
python main.py node graphsage citeseer 32 0.001 0.3 5e-4 200
python main.py node graphsage citeseer 32 0.005 0.3 1e-4 200
python main.py node graphsage citeseer 32 0.005 0.3 5e-4 200
python main.py node graphsage citeseer 32 0.01 0.3 1e-4 200
python main.py node graphsage citeseer 32 0.01 0.3 5e-4 200
python main.py node graphsage citeseer 64 0.001 0.3 1e-4 200
python main.py node graphsage citeseer 64 0.001 0.3 5e-4 200
python main.py node graphsage citeseer 64 0.005 0.3 1e-4 200
python main.py node graphsage citeseer 64 0.005 0.3 5e-4 200
python main.py node graphsage citeseer 64 0.01 0.3 1e-4 200
python main.py node graphsage citeseer 64 0.01 0.3 5e-4 200
python main.py node graphsage citeseer 128 0.001 0.5 1e-4 200
python main.py node graphsage citeseer 128 0.001 0.5 5e-4 200
python main.py node graphsage citeseer 128 0.005 0.5 1e-4 200
python main.py node graphsage citeseer 128 0.005 0.5 5e-4 200
python main.py node graphsage citeseer 128 0.01 0.5 1e-4 200
python main.py node graphsage citeseer 128 0.01 0.5 5e-4 200

echo --- GIN ---
python main.py node gin citeseer 32 0.001 0.3 1e-4 200
python main.py node gin citeseer 32 0.001 0.3 5e-4 200
python main.py node gin citeseer 32 0.005 0.3 1e-4 200
python main.py node gin citeseer 32 0.005 0.3 5e-4 200
python main.py node gin citeseer 32 0.01 0.3 1e-4 200
python main.py node gin citeseer 32 0.01 0.3 5e-4 200
python main.py node gin citeseer 64 0.001 0.3 1e-4 200
python main.py node gin citeseer 64 0.001 0.3 5e-4 200
python main.py node gin citeseer 64 0.005 0.3 1e-4 200
python main.py node gin citeseer 64 0.005 0.3 5e-4 200
python main.py node gin citeseer 64 0.01 0.3 1e-4 200
python main.py node gin citeseer 64 0.01 0.3 5e-4 200
python main.py node gin citeseer 128 0.001 0.5 1e-4 200
python main.py node gin citeseer 128 0.001 0.5 5e-4 200
python main.py node gin citeseer 128 0.005 0.5 1e-4 200
python main.py node gin citeseer 128 0.005 0.5 5e-4 200
python main.py node gin citeseer 128 0.01 0.5 1e-4 200
python main.py node gin citeseer 128 0.01 0.5 5e-4 200

echo =================== PUBMED ===================
echo --- GCN ---
python main.py node gcn pubmed 32 0.001 0.3 1e-4 200
python main.py node gcn pubmed 32 0.001 0.3 5e-4 200
python main.py node gcn pubmed 32 0.005 0.3 1e-4 200
python main.py node gcn pubmed 32 0.005 0.3 5e-4 200
python main.py node gcn pubmed 32 0.01 0.3 1e-4 200
python main.py node gcn pubmed 32 0.01 0.3 5e-4 200
python main.py node gcn pubmed 64 0.001 0.3 1e-4 200
python main.py node gcn pubmed 64 0.001 0.3 5e-4 200
python main.py node gcn pubmed 64 0.005 0.3 1e-4 200
python main.py node gcn pubmed 64 0.005 0.3 5e-4 200
python main.py node gcn pubmed 64 0.01 0.3 1e-4 200
python main.py node gcn pubmed 64 0.01 0.3 5e-4 200
python main.py node gcn pubmed 128 0.001 0.5 1e-4 200
python main.py node gcn pubmed 128 0.001 0.5 5e-4 200
python main.py node gcn pubmed 128 0.005 0.5 1e-4 200
python main.py node gcn pubmed 128 0.005 0.5 5e-4 200
python main.py node gcn pubmed 128 0.01 0.5 1e-4 200
python main.py node gcn pubmed 128 0.01 0.5 5e-4 200

echo --- GAT ---
python main.py node gat pubmed 32 0.001 0.3 1e-4 200
python main.py node gat pubmed 32 0.001 0.3 5e-4 200
python main.py node gat pubmed 32 0.005 0.3 1e-4 200
python main.py node gat pubmed 32 0.005 0.3 5e-4 200
python main.py node gat pubmed 32 0.01 0.3 1e-4 200
python main.py node gat pubmed 32 0.01 0.3 5e-4 200
python main.py node gat pubmed 64 0.001 0.3 1e-4 200
python main.py node gat pubmed 64 0.001 0.3 5e-4 200
python main.py node gat pubmed 64 0.005 0.3 1e-4 200
python main.py node gat pubmed 64 0.005 0.3 5e-4 200
python main.py node gat pubmed 64 0.01 0.3 1e-4 200
python main.py node gat pubmed 64 0.01 0.3 5e-4 200
python main.py node gat pubmed 128 0.001 0.5 1e-4 200
python main.py node gat pubmed 128 0.001 0.5 5e-4 200
python main.py node gat pubmed 128 0.005 0.5 1e-4 200
python main.py node gat pubmed 128 0.005 0.5 5e-4 200
python main.py node gat pubmed 128 0.01 0.5 1e-4 200
python main.py node gat pubmed 128 0.01 0.5 5e-4 200

echo --- GRAPHSAGE ---
python main.py node graphsage pubmed 32 0.001 0.3 1e-4 200
python main.py node graphsage pubmed 32 0.001 0.3 5e-4 200
python main.py node graphsage pubmed 32 0.005 0.3 1e-4 200
python main.py node graphsage pubmed 32 0.005 0.3 5e-4 200
python main.py node graphsage pubmed 32 0.01 0.3 1e-4 200
python main.py node graphsage pubmed 32 0.01 0.3 5e-4 200
python main.py node graphsage pubmed 64 0.001 0.3 1e-4 200
python main.py node graphsage pubmed 64 0.001 0.3 5e-4 200
python main.py node graphsage pubmed 64 0.005 0.3 1e-4 200
python main.py node graphsage pubmed 64 0.005 0.3 5e-4 200
python main.py node graphsage pubmed 64 0.01 0.3 1e-4 200
python main.py node graphsage pubmed 64 0.01 0.3 5e-4 200
python main.py node graphsage pubmed 128 0.001 0.5 1e-4 200
python main.py node graphsage pubmed 128 0.001 0.5 5e-4 200
python main.py node graphsage pubmed 128 0.005 0.5 1e-4 200
python main.py node graphsage pubmed 128 0.005 0.5 5e-4 200
python main.py node graphsage pubmed 128 0.01 0.5 1e-4 200
python main.py node graphsage pubmed 128 0.01 0.5 5e-4 200

echo --- GIN ---
python main.py node gin pubmed 32 0.001 0.3 1e-4 200
python main.py node gin pubmed 32 0.001 0.3 5e-4 200
python main.py node gin pubmed 32 0.005 0.3 1e-4 200
python main.py node gin pubmed 32 0.005 0.3 5e-4 200
python main.py node gin pubmed 32 0.01 0.3 1e-4 200
python main.py node gin pubmed 32 0.01 0.3 5e-4 200
python main.py node gin pubmed 64 0.001 0.3 1e-4 200
python main.py node gin pubmed 64 0.001 0.3 5e-4 200
python main.py node gin pubmed 64 0.005 0.3 1e-4 200
python main.py node gin pubmed 64 0.005 0.3 5e-4 200
python main.py node gin pubmed 64 0.01 0.3 1e-4 200
python main.py node gin pubmed 64 0.01 0.3 5e-4 200
python main.py node gin pubmed 128 0.001 0.5 1e-4 200
python main.py node gin pubmed 128 0.001 0.5 5e-4 200
python main.py node gin pubmed 128 0.005 0.5 1e-4 200
python main.py node gin pubmed 128 0.005 0.5 5e-4 200
python main.py node gin pubmed 128 0.01 0.5 1e-4 200
python main.py node gin pubmed 128 0.01 0.5 5e-4 200

echo ===================
echo LINK PREDICTION
echo ===================

echo =================== CORA ===================
echo --- GCN ---
python main.py link gcn cora 32 0.001 0.3 1e-4 200 1
python main.py link gcn cora 32 0.001 0.3 5e-4 200 1
python main.py link gcn cora 32 0.005 0.3 1e-4 200 1
python main.py link gcn cora 32 0.005 0.3 5e-4 200 1
python main.py link gcn cora 32 0.01 0.3 1e-4 200 1
python main.py link gcn cora 32 0.01 0.3 5e-4 200 1
python main.py link gcn cora 64 0.001 0.3 1e-4 200 1
python main.py link gcn cora 64 0.001 0.3 5e-4 200 1
python main.py link gcn cora 64 0.005 0.3 1e-4 200 1
python main.py link gcn cora 64 0.005 0.3 5e-4 200 1
python main.py link gcn cora 64 0.01 0.3 1e-4 200 1
python main.py link gcn cora 64 0.01 0.3 5e-4 200 1
python main.py link gcn cora 128 0.001 0.5 1e-4 200 1
python main.py link gcn cora 128 0.001 0.5 5e-4 200 1
python main.py link gcn cora 128 0.005 0.5 1e-4 200 1
python main.py link gcn cora 128 0.005 0.5 5e-4 200 1
python main.py link gcn cora 128 0.01 0.5 1e-4 200 1
python main.py link gcn cora 128 0.01 0.5 5e-4 200 1

echo --- GAT ---
python main.py link gat cora 32 0.001 0.3 1e-4 200 1
python main.py link gat cora 32 0.001 0.3 5e-4 200 1
python main.py link gat cora 32 0.005 0.3 1e-4 200 1
python main.py link gat cora 32 0.005 0.3 5e-4 200 1
python main.py link gat cora 32 0.01 0.3 1e-4 200 1
python main.py link gat cora 32 0.01 0.3 5e-4 200 1
python main.py link gat cora 64 0.001 0.3 1e-4 200 1
python main.py link gat cora 64 0.001 0.3 5e-4 200 1
python main.py link gat cora 64 0.005 0.3 1e-4 200 1
python main.py link gat cora 64 0.005 0.3 5e-4 200 1
python main.py link gat cora 64 0.01 0.3 1e-4 200 1
python main.py link gat cora 64 0.01 0.3 5e-4 200 1
python main.py link gat cora 128 0.001 0.5 1e-4 200 1
python main.py link gat cora 128 0.001 0.5 5e-4 200 1
python main.py link gat cora 128 0.005 0.5 1e-4 200 1
python main.py link gat cora 128 0.005 0.5 5e-4 200 1
python main.py link gat cora 128 0.01 0.5 1e-4 200 1
python main.py link gat cora 128 0.01 0.5 5e-4 200 1

echo --- GRAPHSAGE ---
python main.py link graphsage cora 32 0.001 0.3 1e-4 200 1
python main.py link graphsage cora 32 0.001 0.3 5e-4 200 1
python main.py link graphsage cora 32 0.005 0.3 1e-4 200 1
python main.py link graphsage cora 32 0.005 0.3 5e-4 200 1
python main.py link graphsage cora 32 0.01 0.3 1e-4 200 1
python main.py link graphsage cora 32 0.01 0.3 5e-4 200 1
python main.py link graphsage cora 64 0.001 0.3 1e-4 200 1
python main.py link graphsage cora 64 0.001 0.3 5e-4 200 1
python main.py link graphsage cora 64 0.005 0.3 1e-4 200 1
python main.py link graphsage cora 64 0.005 0.3 5e-4 200 1
python main.py link graphsage cora 64 0.01 0.3 1e-4 200 1
python main.py link graphsage cora 64 0.01 0.3 5e-4 200 1
python main.py link graphsage cora 128 0.001 0.5 1e-4 200 1
python main.py link graphsage cora 128 0.001 0.5 5e-4 200 1
python main.py link graphsage cora 128 0.005 0.5 1e-4 200 1
python main.py link graphsage cora 128 0.005 0.5 5e-4 200 1
python main.py link graphsage cora 128 0.01 0.5 1e-4 200 1
python main.py link graphsage cora 128 0.01 0.5 5e-4 200 1

echo --- GIN ---
python main.py link gin cora 32 0.001 0.3 1e-4 200 1
python main.py link gin cora 32 0.001 0.3 5e-4 200 1
python main.py link gin cora 32 0.005 0.3 1e-4 200 1
python main.py link gin cora 32 0.005 0.3 5e-4 200 1
python main.py link gin cora 32 0.01 0.3 1e-4 200 1
python main.py link gin cora 32 0.01 0.3 5e-4 200 1
python main.py link gin cora 64 0.001 0.3 1e-4 200 1
python main.py link gin cora 64 0.001 0.3 5e-4 200 1
python main.py link gin cora 64 0.005 0.3 1e-4 200 1
python main.py link gin cora 64 0.005 0.3 5e-4 200 1
python main.py link gin cora 64 0.01 0.3 1e-4 200 1
python main.py link gin cora 64 0.01 0.3 5e-4 200 1
python main.py link gin cora 128 0.001 0.5 1e-4 200 1
python main.py link gin cora 128 0.001 0.5 5e-4 200 1
python main.py link gin cora 128 0.005 0.5 1e-4 200 1
python main.py link gin cora 128 0.005 0.5 5e-4 200 1
python main.py link gin cora 128 0.01 0.5 1e-4 200 1
python main.py link gin cora 128 0.01 0.5 5e-4 200 1

echo =================== CITESEER ===================
echo --- GCN ---
python main.py link gcn citeseer 32 0.001 0.3 1e-4 200 1
python main.py link gcn citeseer 32 0.001 0.3 5e-4 200 1
python main.py link gcn citeseer 32 0.005 0.3 1e-4 200 1
python main.py link gcn citeseer 32 0.005 0.3 5e-4 200 1
python main.py link gcn citeseer 32 0.01 0.3 1e-4 200 1
python main.py link gcn citeseer 32 0.01 0.3 5e-4 200 1
python main.py link gcn citeseer 64 0.001 0.3 1e-4 200 1
python main.py link gcn citeseer 64 0.001 0.3 5e-4 200 1
python main.py link gcn citeseer 64 0.005 0.3 1e-4 200 1
python main.py link gcn citeseer 64 0.005 0.3 5e-4 200 1
python main.py link gcn citeseer 64 0.01 0.3 1e-4 200 1
python main.py link gcn citeseer 64 0.01 0.3 5e-4 200 1
python main.py link gcn citeseer 128 0.001 0.5 1e-4 200 1
python main.py link gcn citeseer 128 0.001 0.5 5e-4 200 1
python main.py link gcn citeseer 128 0.005 0.5 1e-4 200 1
python main.py link gcn citeseer 128 0.005 0.5 5e-4 200 1
python main.py link gcn citeseer 128 0.01 0.5 1e-4 200 1
python main.py link gcn citeseer 128 0.01 0.5 5e-4 200 1

echo --- GAT ---
python main.py link gat citeseer 32 0.001 0.3 1e-4 200 1
python main.py link gat citeseer 32 0.001 0.3 5e-4 200 1
python main.py link gat citeseer 32 0.005 0.3 1e-4 200 1
python main.py link gat citeseer 32 0.005 0.3 5e-4 200 1
python main.py link gat citeseer 32 0.01 0.3 1e-4 200 1
python main.py link gat citeseer 32 0.01 0.3 5e-4 200 1
python main.py link gat citeseer 64 0.001 0.3 1e-4 200 1
python main.py link gat citeseer 64 0.001 0.3 5e-4 200 1
python main.py link gat citeseer 64 0.005 0.3 1e-4 200 1
python main.py link gat citeseer 64 0.005 0.3 5e-4 200 1
python main.py link gat citeseer 64 0.01 0.3 1e-4 200 1
python main.py link gat citeseer 64 0.01 0.3 5e-4 200 1
python main.py link gat citeseer 128 0.001 0.5 1e-4 200 1
python main.py link gat citeseer 128 0.001 0.5 5e-4 200 1
python main.py link gat citeseer 128 0.005 0.5 1e-4 200 1
python main.py link gat citeseer 128 0.005 0.5 5e-4 200 1
python main.py link gat citeseer 128 0.01 0.5 1e-4 200 1
python main.py link gat citeseer 128 0.01 0.5 5e-4 200 1

echo --- GRAPHSAGE ---
python main.py link graphsage citeseer 32 0.001 0.3 1e-4 200 1
python main.py link graphsage citeseer 32 0.001 0.3 5e-4 200 1
python main.py link graphsage citeseer 32 0.005 0.3 1e-4 200 1
python main.py link graphsage citeseer 32 0.005 0.3 5e-4 200 1
python main.py link graphsage citeseer 32 0.01 0.3 1e-4 200 1
python main.py link graphsage citeseer 32 0.01 0.3 5e-4 200 1
python main.py link graphsage citeseer 64 0.001 0.3 1e-4 200 1
python main.py link graphsage citeseer 64 0.001 0.3 5e-4 200 1
python main.py link graphsage citeseer 64 0.005 0.3 1e-4 200 1
python main.py link graphsage citeseer 64 0.005 0.3 5e-4 200 1
python main.py link graphsage citeseer 64 0.01 0.3 1e-4 200 1
python main.py link graphsage citeseer 64 0.01 0.3 5e-4 200 1
python main.py link graphsage citeseer 128 0.001 0.5 1e-4 200 1
python main.py link graphsage citeseer 128 0.001 0.5 5e-4 200 1
python main.py link graphsage citeseer 128 0.005 0.5 1e-4 200 1
python main.py link graphsage citeseer 128 0.005 0.5 5e-4 200 1
python main.py link graphsage citeseer 128 0.01 0.5 1e-4 200 1
python main.py link graphsage citeseer 128 0.01 0.5 5e-4 200 1

echo --- GIN ---
python main.py link gin citeseer 32 0.001 0.3 1e-4 200 1
python main.py link gin citeseer 32 0.001 0.3 5e-4 200 1
python main.py link gin citeseer 32 0.005 0.3 1e-4 200 1
python main.py link gin citeseer 32 0.005 0.3 5e-4 200 1
python main.py link gin citeseer 32 0.01 0.3 1e-4 200 1
python main.py link gin citeseer 32 0.01 0.3 5e-4 200 1
python main.py link gin citeseer 64 0.001 0.3 1e-4 200 1
python main.py link gin citeseer 64 0.001 0.3 5e-4 200 1
python main.py link gin citeseer 64 0.005 0.3 1e-4 200 1
python main.py link gin citeseer 64 0.005 0.3 5e-4 200 1
python main.py link gin citeseer 64 0.01 0.3 1e-4 200 1
python main.py link gin citeseer 64 0.01 0.3 5e-4 200 1
python main.py link gin citeseer 128 0.001 0.5 1e-4 200 1
python main.py link gin citeseer 128 0.001 0.5 5e-4 200 1
python main.py link gin citeseer 128 0.005 0.5 1e-4 200 1
python main.py link gin citeseer 128 0.005 0.5 5e-4 200 1
python main.py link gin citeseer 128 0.01 0.5 1e-4 200 1
python main.py link gin citeseer 128 0.01 0.5 5e-4 200 1

echo =================== PUBMED ===================
echo --- GCN ---
python main.py link gcn pubmed 32 0.001 0.3 1e-4 200 1
python main.py link gcn pubmed 32 0.001 0.3 5e-4 200 1
python main.py link gcn pubmed 32 0.005 0.3 1e-4 200 1
python main.py link gcn pubmed 32 0.005 0.3 5e-4 200 1
python main.py link gcn pubmed 32 0.01 0.3 1e-4 200 1
python main.py link gcn pubmed 32 0.01 0.3 5e-4 200 1
python main.py link gcn pubmed 64 0.001 0.3 1e-4 200 1
python main.py link gcn pubmed 64 0.001 0.3 5e-4 200 1
python main.py link gcn pubmed 64 0.005 0.3 1e-4 200 1
python main.py link gcn pubmed 64 0.005 0.3 5e-4 200 1
python main.py link gcn pubmed 64 0.01 0.3 1e-4 200 1
python main.py link gcn pubmed 64 0.01 0.3 5e-4 200 1
python main.py link gcn pubmed 128 0.001 0.5 1e-4 200 1
python main.py link gcn pubmed 128 0.001 0.5 5e-4 200 1
python main.py link gcn pubmed 128 0.005 0.5 1e-4 200 1
python main.py link gcn pubmed 128 0.005 0.5 5e-4 200 1
python main.py link gcn pubmed 128 0.01 0.5 1e-4 200 1
python main.py link gcn pubmed 128 0.01 0.5 5e-4 200 1

echo --- GAT ---
python main.py link gat pubmed 32 0.001 0.3 1e-4 200 1
python main.py link gat pubmed 32 0.001 0.3 5e-4 200 1
python main.py link gat pubmed 32 0.005 0.3 1e-4 200 1
python main.py link gat pubmed 32 0.005 0.3 5e-4 200 1
python main.py link gat pubmed 32 0.01 0.3 1e-4 200 1
python main.py link gat pubmed 32 0.01 0.3 5e-4 200 1
python main.py link gat pubmed 64 0.001 0.3 1e-4 200 1
python main.py link gat pubmed 64 0.001 0.3 5e-4 200 1
python main.py link gat pubmed 64 0.005 0.3 1e-4 200 1
python main.py link gat pubmed 64 0.005 0.3 5e-4 200 1
python main.py link gat pubmed 64 0.01 0.3 1e-4 200 1
python main.py link gat pubmed 64 0.01 0.3 5e-4 200 1
python main.py link gat pubmed 128 0.001 0.5 1e-4 200 1
python main.py link gat pubmed 128 0.001 0.5 5e-4 200 1
python main.py link gat pubmed 128 0.005 0.5 1e-4 200 1
python main.py link gat pubmed 128 0.005 0.5 5e-4 200 1
python main.py link gat pubmed 128 0.01 0.5 1e-4 200 1
python main.py link gat pubmed 128 0.01 0.5 5e-4 200 1

echo --- GRAPHSAGE ---
python main.py link graphsage pubmed 32 0.001 0.3 1e-4 200 1
python main.py link graphsage pubmed 32 0.001 0.3 5e-4 200 1
python main.py link graphsage pubmed 32 0.005 0.3 1e-4 200 1
python main.py link graphsage pubmed 32 0.005 0.3 5e-4 200 1
python main.py link graphsage pubmed 32 0.01 0.3 1e-4 200 1
python main.py link graphsage pubmed 32 0.01 0.3 5e-4 200 1
python main.py link graphsage pubmed 64 0.001 0.3 1e-4 200 1
python main.py link graphsage pubmed 64 0.001 0.3 5e-4 200 1
python main.py link graphsage pubmed 64 0.005 0.3 1e-4 200 1
python main.py link graphsage pubmed 64 0.005 0.3 5e-4 200 1
python main.py link graphsage pubmed 64 0.01 0.3 1e-4 200 1
python main.py link graphsage pubmed 64 0.01 0.3 5e-4 200 1
python main.py link graphsage pubmed 128 0.001 0.5 1e-4 200 1
python main.py link graphsage pubmed 128 0.001 0.5 5e-4 200 1
python main.py link graphsage pubmed 128 0.005 0.5 1e-4 200 1
python main.py link graphsage pubmed 128 0.005 0.5 5e-4 200 1
python main.py link graphsage pubmed 128 0.01 0.5 1e-4 200 1
python main.py link graphsage pubmed 128 0.01 0.5 5e-4 200 1

echo --- GIN ---
python main.py link gin pubmed 32 0.001 0.3 1e-4 200 1
python main.py link gin pubmed 32 0.001 0.3 5e-4 200 1
python main.py link gin pubmed 32 0.005 0.3 1e-4 200 1
python main.py link gin pubmed 32 0.005 0.3 5e-4 200 1
python main.py link gin pubmed 32 0.01 0.3 1e-4 200 1
python main.py link gin pubmed 32 0.01 0.3 5e-4 200 1
python main.py link gin pubmed 64 0.001 0.3 1e-4 200 1
python main.py link gin pubmed 64 0.001 0.3 5e-4 200 1
python main.py link gin pubmed 64 0.005 0.3 1e-4 200 1
python main.py link gin pubmed 64 0.005 0.3 5e-4 200 1
python main.py link gin pubmed 64 0.01 0.3 1e-4 200 1
python main.py link gin pubmed 64 0.01 0.3 5e-4 200 1
python main.py link gin pubmed 128 0.001 0.5 1e-4 200 1
python main.py link gin pubmed 128 0.001 0.5 5e-4 200 1
python main.py link gin pubmed 128 0.005 0.5 1e-4 200 1
python main.py link gin pubmed 128 0.005 0.5 5e-4 200 1
python main.py link gin pubmed 128 0.01 0.5 1e-4 200 1
python main.py link gin pubmed 128 0.01 0.5 5e-4 200 1

echo ===================
echo GRAPH CLASSIFICATION
echo ===================

echo =================== MUTAG ===================
echo --- GCN ---
python main.py graph gcn mutag 32 0.001 0.3 1e-4 100
python main.py graph gcn mutag 32 0.001 0.3 5e-4 100
python main.py graph gcn mutag 32 0.005 0.3 1e-4 100
python main.py graph gcn mutag 32 0.005 0.3 5e-4 100
python main.py graph gcn mutag 32 0.01 0.3 1e-4 100
python main.py graph gcn mutag 32 0.01 0.3 5e-4 100
python main.py graph gcn mutag 64 0.001 0.3 1e-4 100
python main.py graph gcn mutag 64 0.001 0.3 5e-4 100
python main.py graph gcn mutag 64 0.005 0.3 1e-4 100
python main.py graph gcn mutag 64 0.005 0.3 5e-4 100
python main.py graph gcn mutag 64 0.01 0.3 1e-4 100
python main.py graph gcn mutag 64 0.01 0.3 5e-4 100
python main.py graph gcn mutag 128 0.001 0.5 1e-4 100
python main.py graph gcn mutag 128 0.001 0.5 5e-4 100
python main.py graph gcn mutag 128 0.005 0.5 1e-4 100
python main.py graph gcn mutag 128 0.005 0.5 5e-4 100
python main.py graph gcn mutag 128 0.01 0.5 1e-4 100
python main.py graph gcn mutag 128 0.01 0.5 5e-4 100

echo --- GAT ---
python main.py graph gat mutag 32 0.001 0.3 1e-4 100
python main.py graph gat mutag 32 0.001 0.3 5e-4 100
python main.py graph gat mutag 32 0.005 0.3 1e-4 100
python main.py graph gat mutag 32 0.005 0.3 5e-4 100
python main.py graph gat mutag 32 0.01 0.3 1e-4 100
python main.py graph gat mutag 32 0.01 0.3 5e-4 100
python main.py graph gat mutag 64 0.001 0.3 1e-4 100
python main.py graph gat mutag 64 0.001 0.3 5e-4 100
python main.py graph gat mutag 64 0.005 0.3 1e-4 100
python main.py graph gat mutag 64 0.005 0.3 5e-4 100
python main.py graph gat mutag 64 0.01 0.3 1e-4 100
python main.py graph gat mutag 64 0.01 0.3 5e-4 100
python main.py graph gat mutag 128 0.001 0.5 1e-4 100
python main.py graph gat mutag 128 0.001 0.5 5e-4 100
python main.py graph gat mutag 128 0.005 0.5 1e-4 100
python main.py graph gat mutag 128 0.005 0.5 5e-4 100
python main.py graph gat mutag 128 0.01 0.5 1e-4 100
python main.py graph gat mutag 128 0.01 0.5 5e-4 100

echo --- GRAPHSAGE ---
python main.py graph graphsage mutag 32 0.001 0.3 1e-4 100
python main.py graph graphsage mutag 32 0.001 0.3 5e-4 100
python main.py graph graphsage mutag 32 0.005 0.3 1e-4 100
python main.py graph graphsage mutag 32 0.005 0.3 5e-4 100
python main.py graph graphsage mutag 32 0.01 0.3 1e-4 100
python main.py graph graphsage mutag 32 0.01 0.3 5e-4 100
python main.py graph graphsage mutag 64 0.001 0.3 1e-4 100
python main.py graph graphsage mutag 64 0.001 0.3 5e-4 100
python main.py graph graphsage mutag 64 0.005 0.3 1e-4 100
python main.py graph graphsage mutag 64 0.005 0.3 5e-4 100
python main.py graph graphsage mutag 64 0.01 0.3 1e-4 100
python main.py graph graphsage mutag 64 0.01 0.3 5e-4 100
python main.py graph graphsage mutag 128 0.001 0.5 1e-4 100
python main.py graph graphsage mutag 128 0.001 0.5 5e-4 100
python main.py graph graphsage mutag 128 0.005 0.5 1e-4 100
python main.py graph graphsage mutag 128 0.005 0.5 5e-4 100
python main.py graph graphsage mutag 128 0.01 0.5 1e-4 100
python main.py graph graphsage mutag 128 0.01 0.5 5e-4 100

echo --- GIN ---
python main.py graph gin mutag 32 0.001 0.3 1e-4 100
python main.py graph gin mutag 32 0.001 0.3 5e-4 100
python main.py graph gin mutag 32 0.005 0.3 1e-4 100
python main.py graph gin mutag 32 0.005 0.3 5e-4 100
python main.py graph gin mutag 32 0.01 0.3 1e-4 100
python main.py graph gin mutag 32 0.01 0.3 5e-4 100
python main.py graph gin mutag 64 0.001 0.3 1e-4 100
python main.py graph gin mutag 64 0.001 0.3 5e-4 100
python main.py graph gin mutag 64 0.005 0.3 1e-4 100
python main.py graph gin mutag 64 0.005 0.3 5e-4 100
python main.py graph gin mutag 64 0.01 0.3 1e-4 100
python main.py graph gin mutag 64 0.01 0.3 5e-4 100
python main.py graph gin mutag 128 0.001 0.5 1e-4 100
python main.py graph gin mutag 128 0.001 0.5 5e-4 100
python main.py graph gin mutag 128 0.005 0.5 1e-4 100
python main.py graph gin mutag 128 0.005 0.5 5e-4 100
python main.py graph gin mutag 128 0.01 0.5 1e-4 100
python main.py graph gin mutag 128 0.01 0.5 5e-4 100

echo =================== PROTEINS ===================
echo --- GCN ---
python main.py graph gcn proteins 32 0.001 0.3 1e-4 100
python main.py graph gcn proteins 32 0.001 0.3 5e-4 100
python main.py graph gcn proteins 32 0.005 0.3 1e-4 100
python main.py graph gcn proteins 32 0.005 0.3 5e-4 100
python main.py graph gcn proteins 32 0.01 0.3 1e-4 100
python main.py graph gcn proteins 32 0.01 0.3 5e-4 100
python main.py graph gcn proteins 64 0.001 0.3 1e-4 100
python main.py graph gcn proteins 64 0.001 0.3 5e-4 100
python main.py graph gcn proteins 64 0.005 0.3 1e-4 100
python main.py graph gcn proteins 64 0.005 0.3 5e-4 100
python main.py graph gcn proteins 64 0.01 0.3 1e-4 100
python main.py graph gcn proteins 64 0.01 0.3 5e-4 100
python main.py graph gcn proteins 128 0.001 0.5 1e-4 100
python main.py graph gcn proteins 128 0.001 0.5 5e-4 100
python main.py graph gcn proteins 128 0.005 0.5 1e-4 100
python main.py graph gcn proteins 128 0.005 0.5 5e-4 100
python main.py graph gcn proteins 128 0.01 0.5 1e-4 100
python main.py graph gcn proteins 128 0.01 0.5 5e-4 100

echo --- GAT ---
python main.py graph gat proteins 32 0.001 0.3 1e-4 100
python main.py graph gat proteins 32 0.001 0.3 5e-4 100
python main.py graph gat proteins 32 0.005 0.3 1e-4 100
python main.py graph gat proteins 32 0.005 0.3 5e-4 100
python main.py graph gat proteins 32 0.01 0.3 1e-4 100
python main.py graph gat proteins 32 0.01 0.3 5e-4 100
python main.py graph gat proteins 64 0.001 0.3 1e-4 100
python main.py graph gat proteins 64 0.001 0.3 5e-4 100
python main.py graph gat proteins 64 0.005 0.3 1e-4 100
python main.py graph gat proteins 64 0.005 0.3 5e-4 100
python main.py graph gat proteins 64 0.01 0.3 1e-4 100
python main.py graph gat proteins 64 0.01 0.3 5e-4 100
python main.py graph gat proteins 128 0.001 0.5 1e-4 100
python main.py graph gat proteins 128 0.001 0.5 5e-4 100
python main.py graph gat proteins 128 0.005 0.5 1e-4 100
python main.py graph gat proteins 128 0.005 0.5 5e-4 100
python main.py graph gat proteins 128 0.01 0.5 1e-4 100
python main.py graph gat proteins 128 0.01 0.5 5e-4 100

echo --- GRAPHSAGE ---
python main.py graph graphsage proteins 32 0.001 0.3 1e-4 100
python main.py graph graphsage proteins 32 0.001 0.3 5e-4 100
python main.py graph graphsage proteins 32 0.005 0.3 1e-4 100
python main.py graph graphsage proteins 32 0.005 0.3 5e-4 100
python main.py graph graphsage proteins 32 0.01 0.3 1e-4 100
python main.py graph graphsage proteins 32 0.01 0.3 5e-4 100
python main.py graph graphsage proteins 64 0.001 0.3 1e-4 100
python main.py graph graphsage proteins 64 0.001 0.3 5e-4 100
python main.py graph graphsage proteins 64 0.005 0.3 1e-4 100
python main.py graph graphsage proteins 64 0.005 0.3 5e-4 100
python main.py graph graphsage proteins 64 0.01 0.3 1e-4 100
python main.py graph graphsage proteins 64 0.01 0.3 5e-4 100
python main.py graph graphsage proteins 128 0.001 0.5 1e-4 100
python main.py graph graphsage proteins 128 0.001 0.5 5e-4 100
python main.py graph graphsage proteins 128 0.005 0.5 1e-4 100
python main.py graph graphsage proteins 128 0.005 0.5 5e-4 100
python main.py graph graphsage proteins 128 0.01 0.5 1e-4 100
python main.py graph graphsage proteins 128 0.01 0.5 5e-4 100

echo --- GIN ---
python main.py graph gin proteins 32 0.001 0.3 1e-4 100
python main.py graph gin proteins 32 0.001 0.3 5e-4 100
python main.py graph gin proteins 32 0.005 0.3 1e-4 100
python main.py graph gin proteins 32 0.005 0.3 5e-4 100
python main.py graph gin proteins 32 0.01 0.3 1e-4 100
python main.py graph gin proteins 32 0.01 0.3 5e-4 100
python main.py graph gin proteins 64 0.001 0.3 1e-4 100
python main.py graph gin proteins 64 0.001 0.3 5e-4 100
python main.py graph gin proteins 64 0.005 0.3 1e-4 100
python main.py graph gin proteins 64 0.005 0.3 5e-4 100
python main.py graph gin proteins 64 0.01 0.3 1e-4 100
python main.py graph gin proteins 64 0.01 0.3 5e-4 100
python main.py graph gin proteins 128 0.001 0.5 1e-4 100
python main.py graph gin proteins 128 0.001 0.5 5e-4 100
python main.py graph gin proteins 128 0.005 0.5 1e-4 100
python main.py graph gin proteins 128 0.005 0.5 5e-4 100
python main.py graph gin proteins 128 0.01 0.5 1e-4 100
python main.py graph gin proteins 128 0.01 0.5 5e-4 100

echo =================== ENZYMES ===================
echo --- GCN ---
python main.py graph gcn enzymes 32 0.001 0.3 1e-4 100
python main.py graph gcn enzymes 32 0.001 0.3 5e-4 100
python main.py graph gcn enzymes 32 0.005 0.3 1e-4 100
python main.py graph gcn enzymes 32 0.005 0.3 5e-4 100
python main.py graph gcn enzymes 32 0.01 0.3 1e-4 100
python main.py graph gcn enzymes 32 0.01 0.3 5e-4 100
python main.py graph gcn enzymes 64 0.001 0.3 1e-4 100
python main.py graph gcn enzymes 64 0.001 0.3 5e-4 100
python main.py graph gcn enzymes 64 0.005 0.3 1e-4 100
python main.py graph gcn enzymes 64 0.005 0.3 5e-4 100
python main.py graph gcn enzymes 64 0.01 0.3 1e-4 100
python main.py graph gcn enzymes 64 0.01 0.3 5e-4 100
python main.py graph gcn enzymes 128 0.001 0.5 1e-4 100
python main.py graph gcn enzymes 128 0.001 0.5 5e-4 100
python main.py graph gcn enzymes 128 0.005 0.5 1e-4 100
python main.py graph gcn enzymes 128 0.005 0.5 5e-4 100
python main.py graph gcn enzymes 128 0.01 0.5 1e-4 100
python main.py graph gcn enzymes 128 0.01 0.5 5e-4 100

echo --- GAT ---
python main.py graph gat enzymes 32 0.001 0.3 1e-4 100
python main.py graph gat enzymes 32 0.001 0.3 5e-4 100
python main.py graph gat enzymes 32 0.005 0.3 1e-4 100
python main.py graph gat enzymes 32 0.005 0.3 5e-4 100
python main.py graph gat enzymes 32 0.01 0.3 1e-4 100
python main.py graph gat enzymes 32 0.01 0.3 5e-4 100
python main.py graph gat enzymes 64 0.001 0.3 1e-4 100
python main.py graph gat enzymes 64 0.001 0.3 5e-4 100
python main.py graph gat enzymes 64 0.005 0.3 1e-4 100
python main.py graph gat enzymes 64 0.005 0.3 5e-4 100
python main.py graph gat enzymes 64 0.01 0.3 1e-4 100
python main.py graph gat enzymes 64 0.01 0.3 5e-4 100
python main.py graph gat enzymes 128 0.001 0.5 1e-4 100
python main.py graph gat enzymes 128 0.001 0.5 5e-4 100
python main.py graph gat enzymes 128 0.005 0.5 1e-4 100
python main.py graph gat enzymes 128 0.005 0.5 5e-4 100
python main.py graph gat enzymes 128 0.01 0.5 1e-4 100
python main.py graph gat enzymes 128 0.01 0.5 5e-4 100

echo --- GRAPHSAGE ---
python main.py graph graphsage enzymes 32 0.001 0.3 1e-4 100
python main.py graph graphsage enzymes 32 0.001 0.3 5e-4 100
python main.py graph graphsage enzymes 32 0.005 0.3 1e-4 100
python main.py graph graphsage enzymes 32 0.005 0.3 5e-4 100
python main.py graph graphsage enzymes 32 0.01 0.3 1e-4 100
python main.py graph graphsage enzymes 32 0.01 0.3 5e-4 100
python main.py graph graphsage enzymes 64 0.001 0.3 1e-4 100
python main.py graph graphsage enzymes 64 0.001 0.3 5e-4 100
python main.py graph graphsage enzymes 64 0.005 0.3 1e-4 100
python main.py graph graphsage enzymes 64 0.005 0.3 5e-4 100
python main.py graph graphsage enzymes 64 0.01 0.3 1e-4 100
python main.py graph graphsage enzymes 64 0.01 0.3 5e-4 100
python main.py graph graphsage enzymes 128 0.001 0.5 1e-4 100
python main.py graph graphsage enzymes 128 0.001 0.5 5e-4 100
python main.py graph graphsage enzymes 128 0.005 0.5 1e-4 100
python main.py graph graphsage enzymes 128 0.005 0.5 5e-4 100
python main.py graph graphsage enzymes 128 0.01 0.5 1e-4 100
python main.py graph graphsage enzymes 128 0.01 0.5 5e-4 100

echo --- GIN ---
python main.py graph gin enzymes 32 0.001 0.3 1e-4 100
python main.py graph gin enzymes 32 0.001 0.3 5e-4 100
python main.py graph gin enzymes 32 0.005 0.3 1e-4 100
python main.py graph gin enzymes 32 0.005 0.3 5e-4 100
python main.py graph gin enzymes 32 0.01 0.3 1e-4 100
python main.py graph gin enzymes 32 0.01 0.3 5e-4 100
python main.py graph gin enzymes 64 0.001 0.3 1e-4 100
python main.py graph gin enzymes 64 0.001 0.3 5e-4 100
python main.py graph gin enzymes 64 0.005 0.3 1e-4 100
python main.py graph gin enzymes 64 0.005 0.3 5e-4 100
python main.py graph gin enzymes 64 0.01 0.3 1e-4 100
python main.py graph gin enzymes 64 0.01 0.3 5e-4 100
python main.py graph gin enzymes 128 0.001 0.5 1e-4 100
python main.py graph gin enzymes 128 0.001 0.5 5e-4 100
python main.py graph gin enzymes 128 0.005 0.5 1e-4 100
python main.py graph gin enzymes 128 0.005 0.5 5e-4 100
python main.py graph gin enzymes 128 0.01 0.5 1e-4 100
python main.py graph gin enzymes 128 0.01 0.5 5e-4 100

echo =================== NCI1 ===================
echo --- GCN ---
python main.py graph gcn nci1 32 0.001 0.3 1e-4 100
python main.py graph gcn nci1 32 0.001 0.3 5e-4 100
python main.py graph gcn nci1 32 0.005 0.3 1e-4 100
python main.py graph gcn nci1 32 0.005 0.3 5e-4 100
python main.py graph gcn nci1 32 0.01 0.3 1e-4 100
python main.py graph gcn nci1 32 0.01 0.3 5e-4 100
python main.py graph gcn nci1 64 0.001 0.3 1e-4 100
python main.py graph gcn nci1 64 0.001 0.3 5e-4 100
python main.py graph gcn nci1 64 0.005 0.3 1e-4 100
python main.py graph gcn nci1 64 0.005 0.3 5e-4 100
python main.py graph gcn nci1 64 0.01 0.3 1e-4 100
python main.py graph gcn nci1 64 0.01 0.3 5e-4 100
python main.py graph gcn nci1 128 0.001 0.5 1e-4 100
python main.py graph gcn nci1 128 0.001 0.5 5e-4 100
python main.py graph gcn nci1 128 0.005 0.5 1e-4 100
python main.py graph gcn nci1 128 0.005 0.5 5e-4 100
python main.py graph gcn nci1 128 0.01 0.5 1e-4 100
python main.py graph gcn nci1 128 0.01 0.5 5e-4 100

echo --- GAT ---
python main.py graph gat nci1 32 0.001 0.3 1e-4 100
python main.py graph gat nci1 32 0.001 0.3 5e-4 100
python main.py graph gat nci1 32 0.005 0.3 1e-4 100
python main.py graph gat nci1 32 0.005 0.3 5e-4 100
python main.py graph gat nci1 32 0.01 0.3 1e-4 100
python main.py graph gat nci1 32 0.01 0.3 5e-4 100
python main.py graph gat nci1 64 0.001 0.3 1e-4 100
python main.py graph gat nci1 64 0.001 0.3 5e-4 100
python main.py graph gat nci1 64 0.005 0.3 1e-4 100
python main.py graph gat nci1 64 0.005 0.3 5e-4 100
python main.py graph gat nci1 64 0.01 0.3 1e-4 100
python main.py graph gat nci1 64 0.01 0.3 5e-4 100
python main.py graph gat nci1 128 0.001 0.5 1e-4 100
python main.py graph gat nci1 128 0.001 0.5 5e-4 100
python main.py graph gat nci1 128 0.005 0.5 1e-4 100
python main.py graph gat nci1 128 0.005 0.5 5e-4 100
python main.py graph gat nci1 128 0.01 0.5 1e-4 100
python main.py graph gat nci1 128 0.01 0.5 5e-4 100

echo --- GRAPHSAGE ---
python main.py graph graphsage nci1 32 0.001 0.3 1e-4 100
python main.py graph graphsage nci1 32 0.001 0.3 5e-4 100
python main.py graph graphsage nci1 32 0.005 0.3 1e-4 100
python main.py graph graphsage nci1 32 0.005 0.3 5e-4 100
python main.py graph graphsage nci1 32 0.01 0.3 1e-4 100
python main.py graph graphsage nci1 32 0.01 0.3 5e-4 100
python main.py graph graphsage nci1 64 0.001 0.3 1e-4 100
python main.py graph graphsage nci1 64 0.001 0.3 5e-4 100
python main.py graph graphsage nci1 64 0.005 0.3 1e-4 100
python main.py graph graphsage nci1 64 0.005 0.3 5e-4 100
python main.py graph graphsage nci1 64 0.01 0.3 1e-4 100
python main.py graph graphsage nci1 64 0.01 0.3 5e-4 100
python main.py graph graphsage nci1 128 0.001 0.5 1e-4 100
python main.py graph graphsage nci1 128 0.001 0.5 5e-4 100
python main.py graph graphsage nci1 128 0.005 0.5 1e-4 100
python main.py graph graphsage nci1 128 0.005 0.5 5e-4 100
python main.py graph graphsage nci1 128 0.01 0.5 1e-4 100
python main.py graph graphsage nci1 128 0.01 0.5 5e-4 100

echo --- GIN ---
python main.py graph gin nci1 32 0.001 0.3 1e-4 100
python main.py graph gin nci1 32 0.001 0.3 5e-4 100
python main.py graph gin nci1 32 0.005 0.3 1e-4 100
python main.py graph gin nci1 32 0.005 0.3 5e-4 100
python main.py graph gin nci1 32 0.01 0.3 1e-4 100
python main.py graph gin nci1 32 0.01 0.3 5e-4 100
python main.py graph gin nci1 64 0.001 0.3 1e-4 100
python main.py graph gin nci1 64 0.001 0.3 5e-4 100
python main.py graph gin nci1 64 0.005 0.3 1e-4 100
python main.py graph gin nci1 64 0.005 0.3 5e-4 100
python main.py graph gin nci1 64 0.01 0.3 1e-4 100
python main.py graph gin nci1 64 0.01 0.3 5e-4 100
python main.py graph gin nci1 128 0.001 0.5 1e-4 100
python main.py graph gin nci1 128 0.001 0.5 5e-4 100
python main.py graph gin nci1 128 0.005 0.5 1e-4 100
python main.py graph gin nci1 128 0.005 0.5 5e-4 100
python main.py graph gin nci1 128 0.01 0.5 1e-4 100
python main.py graph gin nci1 128 0.01 0.5 5e-4 100

echo COMPLETE

set HYPER=
pause