from models.gcn import GCN
from models.gat import GAT
from models.graphsage import GraphSAGE
from models.gin import GIN


def get_model(

    name,

    input_dim,

    hidden_dim,

    output_dim,

    dropout=0.5

):

    models = {

        "gcn": GCN,

        "gat": GAT,

        "graphsage": GraphSAGE,

        "gin": GIN,

    }


    return models[

        name

    ](

        input_dim,

        hidden_dim,

        output_dim,

        dropout

    )