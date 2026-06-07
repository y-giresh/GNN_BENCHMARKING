@echo off

echo NODE

python main.py node gcn cora
python main.py node gat cora
python main.py node graphsage cora
python main.py node gin cora

python main.py node gcn citeseer
python main.py node gat citeseer
python main.py node graphsage citeseer
python main.py node gin citeseer

python main.py node gcn pubmed
python main.py node gat pubmed
python main.py node graphsage pubmed
python main.py node gin pubmed


echo LINK

python main.py link gcn cora
python main.py link gat cora
python main.py link graphsage cora
python main.py link gin cora

python main.py link gcn citeseer
python main.py link gat citeseer
python main.py link graphsage citeseer
python main.py link gin citeseer

python main.py link gcn pubmed
python main.py link gat pubmed
python main.py link graphsage pubmed
python main.py link gin pubmed


echo GRAPH

python main.py graph gcn mutag
python main.py graph gat mutag
python main.py graph graphsage mutag
python main.py graph gin mutag

python main.py graph gcn proteins
python main.py graph gat proteins
python main.py graph graphsage proteins
python main.py graph gin proteins

python main.py graph gcn enzymes
python main.py graph gat enzymes
python main.py graph graphsage enzymes
python main.py graph gin enzymes

python main.py graph gcn nci1
python main.py graph gat nci1
python main.py graph graphsage nci1
python main.py graph gin nci1


echo COMPLETE

pause