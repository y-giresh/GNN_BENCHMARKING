from torch_geometric.datasets import TUDataset
from torch_geometric.loader import DataLoader


def load_graph_dataset():

    dataset = TUDataset(

        root="data",

        name="MUTAG"

    )

    train_loader = DataLoader(

        dataset,

        batch_size=32,

        shuffle=True

    )

    return dataset, train_loader