import torch
import numpy as np

from sklearn.metrics import (

    f1_score,

    roc_auc_score,

    average_precision_score

)



def evaluate(

    model,

    data

):

    model.eval()

    with torch.no_grad():

        try:

            out = model(

                data.x,

                data.edge_index

            )

        except TypeError:

            out = model(

                data

            )


        pred = out.argmax(

            dim=1

        )


        y_true = (

            data.y[
                data.test_mask
            ]

            .cpu()

        )


        y_pred = (

            pred[
                data.test_mask
            ]

            .cpu()

        )


        acc = (

            (

                y_pred

                ==

                y_true

            )

            .float()

            .mean()

            .item()

        )


        macro_f1 = (

            f1_score(

                y_true,

                y_pred,

                average="macro"

            )

        )


        weighted_f1 = (

            f1_score(

                y_true,

                y_pred,

                average="weighted"

            )

        )


    return {

        "Accuracy":

        round(

            acc,

            4

        ),

        "Macro_F1":

        round(

            macro_f1,

            4

        ),

        "Weighted_F1":

        round(

            weighted_f1,

            4

        )

    }




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

        try:

            z = model(

                test_data.x,

                test_data.edge_index

            )

        except TypeError:

            z = model(

                test_data

            )


        out = decode(

            z,

            test_data.edge_label_index

        )


        prob = (

            torch.sigmoid(

                out

            )

            .cpu()

        )


        pred = (

            prob

            >

            0.5

        )


        y_true = (

            test_data.edge_label

            .cpu()

        )


        auc = (

            roc_auc_score(

                y_true,

                prob

            )

        )


        ap = (

            average_precision_score(

                y_true,

                prob

            )

        )


        f1 = (

            f1_score(

                y_true,

                pred

            )

        )


        hits = (

            pred

            .float()

            .mean()

            .item()

        )


    return {

        "AUC":

        round(

            auc,

            4

        ),

        "Average_Precision":

        round(

            ap,

            4

        ),

        "F1":

        round(

            f1,

            4

        ),

        "Hits@K":

        round(

            hits,

            4

        )

    }




def evaluate_graph(

    model,

    loader

):

    model.eval()

    fold_scores = []


    with torch.no_grad():

        for batch in loader:

            out = model(

                batch.x,

                batch.edge_index,

                batch.batch

            )


            pred = (

                out.argmax(

                    dim=1

                )

            )


            acc = (

                (

                    pred

                    ==

                    batch.y

                )

                .float()

                .mean()

                .item()

            )


            fold_scores.append(

                acc

            )


    mean_acc = (

        np.mean(

            fold_scores

        )

    )


    std_acc = (

        np.std(

            fold_scores

        )

    )


    return {

        "Accuracy":

        f"{mean_acc:.5f} ± {std_acc:.5f}",


        "Accuracy_Mean":

        round(

            mean_acc,

            5

        ),


        "Accuracy_STD":

        round(

            std_acc,

            5

        ),


        "Folds":

        len(

            fold_scores

        )

    }