import torch
from torch_geometric.datasets import Planetoid
from torch_geometric.transforms import RandomLinkSplit


torch.manual_seed(42)


def load_link_dataset(
    name,
    directed=False
):
    """
    NOTE on `directed`: this only controls RandomLinkSplit's negative
    edge sampling strategy (is_undirected=not directed). It does NOT
    make the GNN encoders themselves direction-aware -- GCNConv, GATConv,
    SAGEConv, and GINConv as used in this project all perform standard
    undirected message passing over edge_index regardless of this flag.
    So this is not true directed link prediction; treat `directed` as a
    negative-sampling option only, not a modeling capability.
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