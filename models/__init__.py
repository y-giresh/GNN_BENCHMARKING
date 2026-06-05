from models.gcn import GCN
from models.gat import GAT
from models.graphsage import GraphSAGE
from models.gin import GIN
from models.graph_gcn import GraphGCN


def get_model(
    name,
    input_dim,
    hidden_dim,
    output_dim
):

    models = {

        "gcn": GCN,

        "gat": GAT,

        "graphsage": GraphSAGE,

        "gin": GIN,
        
        "graph_gcn": GraphGCN,

    }

    return models[
        name
    ](

        input_dim,

        hidden_dim,

        output_dim

    )