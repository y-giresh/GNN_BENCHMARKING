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

        try:

            out = model(

                data.x,

                data.edge_index

            )

        except TypeError:

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



def train_link(
    model,
    train_data,
    optimizer,
    epochs=200
):

    model.train()

    for epoch in range(
        epochs
    ):

        optimizer.zero_grad()

        try:

            z = model(

                train_data.x,

                train_data.edge_index

            )

        except TypeError:

            z = model(
                train_data
            )

        pos = decode(

            z,

            train_data.edge_label_index[
                :,
                train_data.edge_label == 1
            ]

        )

        neg = decode(

            z,

            train_data.edge_label_index[
                :,
                train_data.edge_label == 0
            ]

        )

        loss = (

            F.binary_cross_entropy_with_logits(

                pos,

                torch.ones_like(
                    pos
                )

            )

            +

            F.binary_cross_entropy_with_logits(

                neg,

                torch.zeros_like(
                    neg
                )

            )

        )

        loss.backward()

        optimizer.step()

        if epoch % 20 == 0:

            print(

                f"Epoch {epoch}"

                f" | Loss {loss:.4f}"

            )



def train_graph(

    model,

    loader,

    optimizer,

    epochs=50

):

    model.train()

    for epoch in range(

        epochs

    ):

        total_loss = 0

        for batch in loader:

            optimizer.zero_grad()

            out = model(

                batch.x,

                batch.edge_index,

                batch.batch

            )

            loss = F.cross_entropy(

                out,

                batch.y

            )

            loss.backward()

            optimizer.step()

            total_loss += (

                loss.item()

            )

        if epoch % 10 == 0:

            print(

                f"Epoch {epoch}"

                f" | Loss "

                f"{total_loss:.4f}"

            )