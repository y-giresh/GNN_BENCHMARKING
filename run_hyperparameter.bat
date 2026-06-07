@echo off

echo ===================
echo HIDDEN DIMENSION
echo ===================

python main.py node gcn cora 32 0.01 0.5 0.0005 200
python main.py node gcn cora 64 0.01 0.5 0.0005 200
python main.py node gcn cora 128 0.01 0.5 0.0005 200


echo ===================
echo LEARNING RATE
echo ===================

python main.py node gcn cora 32 0.001 0.5 0.0005 200
python main.py node gcn cora 32 0.005 0.5 0.0005 200
python main.py node gcn cora 32 0.01 0.5 0.0005 200


echo ===================
echo DROPOUT
echo ===================

python main.py node gcn cora 32 0.01 0.3 0.0005 200
python main.py node gcn cora 32 0.01 0.5 0.0005 200


echo ===================
echo WEIGHT DECAY
echo ===================

python main.py node gcn cora 32 0.01 0.5 0.0001 200
python main.py node gcn cora 32 0.01 0.5 0.0005 200


echo ===================
echo EPOCHS
echo ===================

python main.py node gcn cora 32 0.01 0.5 0.0005 100
python main.py node gcn cora 32 0.01 0.5 0.0005 200
python main.py node gcn cora 32 0.01 0.5 0.0005 300


echo COMPLETE

pause