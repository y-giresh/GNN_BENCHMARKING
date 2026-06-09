import torch
import torch.nn.functional as F

from sklearn.metrics import (

    roc_auc_score

)



def train(

    model,

    data,

    optimizer,

    epochs=200,

    patience=40

):

    best_val = float(

        "inf"

    )

    wait = 0
    
    
    best_state = None


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

            try:

                val_out = model(

                    data.x,

                    data.edge_index

                )

            except TypeError:

                val_out = model(

                    data

                )


            if hasattr(

                data,

                "val_mask"

            ):

                val_loss = (

                    F.cross_entropy(

                        val_out[
                            data.val_mask
                        ],

                        data.y[
                            data.val_mask
                        ]

                    )

                )

            else:

                val_loss = loss


        model.train()


        if val_loss < best_val:

         best_val = val_loss

         wait = 0

         best_state = {

         k:

         v.cpu()

         for k, v

         in model.state_dict()

         .items()

        }

        else:

            wait += 1


        if wait >= patience:

            print()

            print(

                f"Early stopping at epoch {epoch}"

            )

            break


        if epoch % 20 == 0:

            print(

                f"Epoch {epoch}"

                f" | Loss {loss:.4f}"

                f" | Val {val_loss:.4f}"

            )
        
    if best_state is not None:

     model.load_state_dict(

         best_state

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

    val_data,

    optimizer,

    epochs=200,

    patience=20

):

    best_auc = 0

    wait = 0

    best_state = None


    for epoch in range(

        epochs

    ):

        model.train()

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


        model.eval()


        with torch.no_grad():

            try:

                z_val = model(

                    val_data.x,

                    val_data.edge_index

                )

            except TypeError:

                z_val = model(

                    val_data

                )


            val_pred = decode(

                z_val,

                val_data.edge_label_index

            )


            val_prob = (

                torch.sigmoid(

                    val_pred

                )

                .cpu()

            )


            val_true = (

                val_data.edge_label

                .cpu()

            )


            val_auc = (

                roc_auc_score(

                    val_true,

                    val_prob

                )

            )


        if val_auc > best_auc:

            best_auc = val_auc

            wait = 0


            best_state = (

                {

                    k:

                    v.cpu()

                    for k, v

                    in model.state_dict()

                    .items()

                }

            )

        else:

            wait += 1


        if wait >= patience:

            print()

            print(

                f"Link Early stopping at epoch {epoch}"

            )

            break


        if epoch % 20 == 0:

            print(

                f"Epoch {epoch}"

                f" | Loss {loss:.4f}"

                f" | Val_AUC {val_auc:.4f}"

            )


    if best_state is not None:

        model.load_state_dict(

            best_state

        )




def train_graph(

    model,

    train_loader,

    val_loader,

    optimizer,

    epochs=50,
    
    patience=20

):

    model.train()

    best_val = float(

        "inf"

    )

    wait = 0

    best_state = None
    for epoch in range(

        epochs

    ):

        total_loss = 0


        for batch in train_loader:

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

            model.eval()


        val_loss = 0


        with torch.no_grad():

            for batch in val_loader:

                out = model(

                    batch.x,

                    batch.edge_index,

                    batch.batch

                )


                val_loss += (

                    F.cross_entropy(

                        out,

                        batch.y

                    )

                    .item()

                )


        model.train()


        if val_loss < best_val:

            best_val = val_loss

            wait = 0


            best_state = {

                k:

                v.cpu()

                for k, v

                in model.state_dict()

                .items()

            }


        else:

            wait += 1


        if wait >= patience:

            print(

                f"Graph Early stopping at epoch {epoch}"

            )

            break
        if epoch % 10 == 0:

            print(

                f"Epoch {epoch}"

                f" | Loss {total_loss:.4f}"

            )

    if best_state is not None:

        model.load_state_dict(

            best_state

        )
