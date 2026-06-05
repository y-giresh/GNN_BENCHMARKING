from torch_geometric.datasets import Planetoid
from torch_geometric.datasets import TUDataset


def get_dataset(dataset_name):

    dataset_name = dataset_name.lower()

    if dataset_name == "cora":

        return Planetoid(
            root="data",
            name="Cora"
        )


    elif dataset_name == "citeseer":

        return Planetoid(
            root="data",
            name="CiteSeer"
        )


    elif dataset_name == "pubmed":

        return Planetoid(
            root="data",
            name="PubMed"
        )


    elif dataset_name == "mutag":

        return TUDataset(
            root="data",
            name="MUTAG"
        )


    else:

        raise ValueError(
            f"Dataset '{dataset_name}' not supported"
        )