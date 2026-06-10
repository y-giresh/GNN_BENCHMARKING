from torch_geometric.datasets import TUDataset

from torch_geometric.loader import DataLoader

from sklearn.model_selection import KFold

import torch


def load_graph_dataset(

    dataset_name,

    folds=10,

    batch_size=32

):

    dataset = TUDataset(

        root="data",

        name=dataset_name.upper()

    )


    kf = KFold(

        n_splits=folds,

        shuffle=True,

        random_state=42

    )


    fold_loaders = []


    for fold_idx, (train_idx, test_idx) in enumerate(

        kf.split(

            range(

                len(dataset)

            )

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

        # FIX #2: Seed torch.randperm per fold using 42 + fold_idx.
        # Without this the split is non-deterministic across separate runs
        # even when a global seed is set, because the global RNG state is
        # consumed differently each time. Now each fold always gets the
        # same train/val assignment regardless of when you run it.
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


    return (

        dataset,

        fold_loaders

    )
