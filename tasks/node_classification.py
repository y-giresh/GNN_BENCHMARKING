from torch_geometric.datasets import Planetoid


def load_dataset(

    dataset_name="pubmed"

):

    # FIX #9: dataset_name is now a parameter instead of being hardcoded to
    # PubMed.  This aligns node_classification.py with the rest of the
    # pipeline (main.py uses tasks/__init__.py → get_dataset() for the actual
    # training flow; this module is used for quick standalone inspection only).
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
