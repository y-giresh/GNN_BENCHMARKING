from torch_geometric.datasets import TUDataset
from torch_geometric.loader import DataLoader


def load_graph_dataset(

    dataset_name

):

    dataset = TUDataset(

        root="data",

        name=dataset_name.upper()

    )


    loader = DataLoader(

        dataset,

        batch_size=32,

        shuffle=True

    )


    return (

        dataset,

        loader

    )