import torch
from torch_geometric.datasets import Planetoid
from torch_geometric.transforms import RandomLinkSplit


torch.manual_seed(42)


def load_link_dataset(
    name
):

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

        is_undirected=True,

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