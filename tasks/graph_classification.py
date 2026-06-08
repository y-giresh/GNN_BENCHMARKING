from torch_geometric.datasets import TUDataset

from torch_geometric.loader import DataLoader

from sklearn.model_selection import KFold



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


    for train_idx, test_idx in kf.split(

        range(

            len(dataset)

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


        train_loader = DataLoader(

            train_dataset,

            batch_size=batch_size,

            shuffle=True

        )


        test_loader = DataLoader(

            test_dataset,

            batch_size=batch_size,

            shuffle=False

        )


        fold_loaders.append(

            (

                train_loader,

                test_loader

            )

        )


    return (

        dataset,

        fold_loaders

    )