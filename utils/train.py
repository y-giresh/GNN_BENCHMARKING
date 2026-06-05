import torch
import torch.nn.functional as F


def train(
    model,
    data,
    optimizer,
    epochs=200
):

    model.train()

    for epoch in range(
        epochs
    ):

        optimizer.zero_grad()

        out = model(
            data
        )

        loss = F.cross_entropy(

            out[
                data.train_mask
            ],

            data.y[
                data.train_mask
            ]

        )

        loss.backward()

        optimizer.step()

        model.eval()

        with torch.no_grad():

            pred = out.argmax(
                dim=1
            )

            train_acc = (

                pred[
                    data.train_mask
                ]

                ==

                data.y[
                    data.train_mask
                ]

            ).float().mean()

        model.train()

        if epoch % 20 == 0:

            print(

                f"Epoch {epoch}"

                f" | Loss {loss:.4f}"

                f" | Train {train_acc:.4f}"

            )


def train_link(
    model,
    train_data,
    optimizer
):

    print(
        "Link training later"
    )