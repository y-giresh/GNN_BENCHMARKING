import torch
from torch_geometric.datasets import TUDataset


torch.manual_seed(42)


def load_graph_dataset():

    dataset = TUDataset(

        root="data",

        name="MUTAG"

    )

    return dataset