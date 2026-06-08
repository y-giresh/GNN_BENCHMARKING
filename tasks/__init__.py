import torch

from torch_geometric.datasets import (

    Planetoid,

    TUDataset

)



def create_split(

    dataset

):

    data = dataset[0]

    num_nodes = (

        data.num_nodes

    )


    torch.manual_seed(

        42

    )


    indices = (

        torch.randperm(

            num_nodes

        )

    )


    train_end = int(

        0.70

        *

        num_nodes

    )


    val_end = int(

        0.85

        *

        num_nodes

    )


    train_mask = torch.zeros(

        num_nodes,

        dtype=torch.bool

    )


    val_mask = torch.zeros(

        num_nodes,

        dtype=torch.bool

    )


    test_mask = torch.zeros(

        num_nodes,

        dtype=torch.bool

    )


    train_mask[

        indices[

            :train_end

        ]

    ] = True


    val_mask[

        indices[

            train_end:val_end

        ]

    ] = True


    test_mask[

        indices[

            val_end:

        ]

    ] = True


    data.train_mask = (

        train_mask

    )


    data.val_mask = (

        val_mask

    )


    data.test_mask = (

        test_mask

    )


    return dataset




def get_dataset(

    dataset_name

):

    dataset_name = (

        dataset_name.lower()

    )


    if dataset_name == "cora":

        return create_split(

            Planetoid(

                root="data",

                name="Cora"

            )

        )


    elif dataset_name == "citeseer":

        return create_split(

            Planetoid(

                root="data",

                name="CiteSeer"

            )

        )


    elif dataset_name == "pubmed":

        return create_split(

            Planetoid(

                root="data",

                name="PubMed"

            )

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