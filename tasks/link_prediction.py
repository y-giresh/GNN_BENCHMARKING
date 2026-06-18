import torch
from torch_geometric.datasets import Planetoid
from torch_geometric.transforms import RandomLinkSplit


torch.manual_seed(42)


def load_link_dataset(
    name,
    directed=False
):
    """
    `directed` controls two things together:
      1. RandomLinkSplit's negative edge sampling strategy here
         (is_undirected=not directed).
      2. In main.py's link branch, directed=True switches the model to
         models.directed_link.DirectedLinkEncoder, which learns separate
         source/destination embeddings and scores edges asymmetrically
         (see utils/train.py:decode_directed and
         utils/evaluate.py:decode_directed). directed=False keeps using
         the original single-embedding encoder with the symmetric
         decode(), which cannot distinguish u->v from v->u.
    The base GNN layers (GCNConv/GATConv/SAGEConv/GINConv) still perform
    standard message passing over edge_index either way -- direction
    awareness comes from the two-head wrapper and asymmetric decoder on
    top, not from the conv layers themselves.
    """

    datasets = {

        "cora": "Cora",

        "citeseer": "CiteSeer",

        "pubmed": "PubMed"

    }

    dataset = Planetoid(

        root="data",

        name=datasets[
            name.lower()
        ]

    )

    data = dataset[0]

    transform = RandomLinkSplit(

        num_val=0.1,

        num_test=0.2,

        is_undirected=not directed,

        add_negative_train_samples=True

    )

    train_data, val_data, test_data = transform(
        data
    )

    return (

        dataset,

        train_data,

        val_data,

        test_data

    )