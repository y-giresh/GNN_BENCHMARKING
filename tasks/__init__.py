from torch_geometric.datasets import (
    Planetoid,
    TUDataset
)


def get_dataset(

    dataset_name

):

    dataset_name = (

        dataset_name.lower()

    )


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


    elif dataset_name == "proteins":

        return TUDataset(

            root="data",

            name="PROTEINS"

        )


    elif dataset_name == "enzymes":

        return TUDataset(

            root="data",

            name="ENZYMES"

        )


    elif dataset_name == "nci1":

        return TUDataset(

            root="data",

            name="NCI1"

        )


    else:

        raise ValueError(

            f"Dataset not supported: {dataset_name}"

        )



from .link_prediction import (

    load_link_dataset

)