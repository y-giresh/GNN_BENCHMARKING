import torch


def evaluate(
    model,
    data
):

    model.eval()

    with torch.no_grad():

        pred = model(
            data
        ).argmax(
            dim=1
        )

        acc = (

            pred[
                data.test_mask
            ]

            ==

            data.y[
                data.test_mask
            ]

        ).float().mean()

    return acc.item()


def decode(
    z,
    edge_index
):

    return (

        z[
            edge_index[0]
        ]

        *

        z[
            edge_index[1]
        ]

    ).sum(
        dim=1
    )


def evaluate_link(
    model,
    test_data
):

    model.eval()

    with torch.no_grad():

        z = model(
            test_data
        )

        out = decode(

            z,

            test_data.edge_label_index

        )

        pred = (

            torch.sigmoid(
                out
            )

            >

            0.5

        )

        acc = (

            pred

            ==

            test_data.edge_label

        ).float().mean()

    return acc.item()