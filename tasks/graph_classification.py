from torch_geometric.datasets import TUDataset

from torch_geometric.loader import DataLoader

from torch_geometric.utils import degree

from sklearn.model_selection import StratifiedKFold

import torch
import numpy as np


def _add_degree_features(dataset):
    """
    For TU datasets with no node features (data.x is None), compute
    one-hot degree features so all models receive a valid input tensor.
    The degree is capped at max_degree to keep the feature dimension
    manageable, and every node gets a float32 feature vector of that size.
    """
    max_degree = 0
    for data in dataset:
        if data.edge_index.numel() > 0:
            d = degree(
                data.edge_index[0],
                num_nodes=data.num_nodes,
                dtype=torch.long
            )
            max_degree = max(max_degree, int(d.max()))

    for data in dataset:
        d = degree(
            data.edge_index[0],
            num_nodes=data.num_nodes,
            dtype=torch.long
        )
        # clamp so isolated nodes or very high-degree nodes stay in range
        d = d.clamp(max=max_degree)
        one_hot = torch.zeros(data.num_nodes, max_degree + 1)
        one_hot[torch.arange(data.num_nodes), d] = 1.0
        data.x = one_hot

    return dataset, max_degree + 1


def load_graph_dataset(

    dataset_name,

    folds=10,

    batch_size=32

):

    dataset = TUDataset(

        root="data",

        name=dataset_name.upper()

    )

    # --- Handle missing node features ---
    # Check the first graph; if x is None the whole dataset lacks features.
    if dataset[0].x is None:
        print(
            f"\n[Warning] '{dataset_name.upper()}' has no node features. "
            "Using one-hot degree features as input."
        )
        dataset, num_features = _add_degree_features(dataset)
    else:
        num_features = dataset.num_features

    # Collect graph-level labels for stratified splitting
    graph_labels = np.array([int(data.y.item()) for data in dataset])

    kf = StratifiedKFold(

        n_splits=folds,

        shuffle=True,

        random_state=42

    )


    fold_loaders = []


    for fold_idx, (train_idx, test_idx) in enumerate(

        # Pass graph_labels so folds are class-balanced
        kf.split(

            range(

                len(dataset)

            ),

            graph_labels

        )

    ):

        train_dataset = (

            dataset[

                train_idx.tolist()

            ]

        )


        test_dataset = (

            dataset[

                test_idx.tolist()

            ]

        )


        train_size = int(

            0.8

            *

            len(

                train_dataset

            )

        )


        val_size = (

            len(

                train_dataset

            )

            -

            train_size

        )

        torch.manual_seed(42 + fold_idx)

        indices = torch.randperm(

            len(

                train_dataset

            )

        )


        original_train = train_dataset


        train_indices = indices[

            :train_size

        ]


        val_indices = indices[

            train_size:

        ]


        train_dataset = [

            original_train[i]

            for i in train_indices

        ]


        val_dataset = [

            original_train[i]

            for i in val_indices

        ]

        train_loader = DataLoader(

            train_dataset,

            batch_size=batch_size,

            shuffle=True

        )

        val_loader = DataLoader(

            val_dataset,

            batch_size=batch_size,

            shuffle=False

        )


        test_loader = DataLoader(

            test_dataset,

            batch_size=batch_size,

            shuffle=False

        )


        fold_loaders.append(

            (

                train_loader,

                val_loader,

                test_loader

            )

        )


    dataset._num_features = num_features

    return (

        dataset,

        fold_loaders

    )
