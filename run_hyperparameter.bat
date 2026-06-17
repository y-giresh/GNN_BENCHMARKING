@echo off
set HYPER=1

echo =================== 
echo NODE CLASSIFICATION
echo ===================

python main.py node gcn cora 32 0.01 0.5 0.0005 200
python main.py node gat cora 64 0.01 0.5 0.0005 200
python main.py node graphsage cora 32 0.005 0.5 0.0005 200
python main.py node gin cora 128 0.01 0.3 0.0005 200


echo ===================
echo LINK PREDICTION
echo ===================

python main.py link gcn cora 32 0.01 0.5 0.0005 200
python main.py link gin cora 64 0.01 0.5 0.0005 200
python main.py link gat cora 128 0.005 0.5 0.0005 200
python main.py link graphsage cora 32 0.01 0.3 0.0005 200


echo ===================
echo GRAPH CLASSIFICATION
echo ===================

python main.py graph gcn mutag 128 0.01 0.5 0.0005 200
python main.py graph gat mutag 64 0.01 0.5 0.0005 200
python main.py graph gin mutag 32 0.005 0.5 0.0005 200
python main.py graph graphsage mutag 32 0.01 0.3 0.0005 200


echo ===================
echo EXTRA CHECKS
echo ===================

python main.py node gcn cora 32 0.01 0.5 0.0001 200
python main.py link graphsage cora 32 0.01 0.5 0.0001 200
python main.py graph gin mutag 32 0.01 0.5 0.0001 200


echo COMPLETE

set HYPER=
pause