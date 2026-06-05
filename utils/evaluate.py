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