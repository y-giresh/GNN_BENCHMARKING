from torch_geometric.datasets import Planetoid


def load_dataset(

    dataset_name="pubmed"

):

   
    name_map = {

        "cora": "Cora",

        "citeseer": "CiteSeer",

        "pubmed": "PubMed"

    }

    canonical = name_map.get(

        dataset_name.lower(),

        dataset_name

    )

    dataset = Planetoid(

        root="data",

        name=canonical

    )

    return dataset


if __name__ == "__main__":

    import sys

    name = sys.argv[1] if len(sys.argv) > 1 else "pubmed"

    dataset = load_dataset(name)

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
