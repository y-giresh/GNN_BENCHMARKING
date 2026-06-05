from torch_geometric.datasets import Planetoid


def get_dataset(
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

    return dataset
from tasks.link_prediction import (
    load_link_dataset
)