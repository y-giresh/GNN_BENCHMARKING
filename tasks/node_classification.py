from torch_geometric.datasets import Planetoid


def load_dataset():

    dataset = Planetoid(
        root='data',
        name='PubMed'
    )

    return dataset


dataset = load_dataset()

data = dataset[0]

print(dataset)

print("Number of classes:", dataset.num_classes)

print("Number of features:", dataset.num_features)

print()

print(data)

print("Nodes:", data.num_nodes)

print("Edges:", data.num_edges)

print("Training nodes:", data.train_mask.sum().item())

print("Validation nodes:", data.val_mask.sum().item())

print("Testing nodes:", data.test_mask.sum().item())