import torch
import numpy as np

from sklearn.metrics import (

    f1_score,

    roc_auc_score,

    average_precision_score,

    confusion_matrix,

    accuracy_score,

    precision_score,

    recall_score

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


    y_true = []

    y_pred = []

    y_prob = []


    with torch.no_grad():

        for batch in loader:

            out = model(

                batch.x,

                batch.edge_index,

                batch.batch

            )


            prob = (

                torch.softmax(

                    out,

                    dim=1

                )

            )


            pred = (

                out.argmax(

                    dim=1

                )

            )


            y_true.extend(

                batch.y

                .cpu()

                .numpy()

            )


            y_pred.extend(

                pred

                .cpu()

                .numpy()

            )


            y_prob.extend(

                prob

                .cpu()

                .numpy()

            )


    y_true = np.array(

        y_true

    )


    y_pred = np.array(

        y_pred

    )


    y_prob = np.array(

        y_prob

    )


    cm = confusion_matrix(

        y_true,

        y_pred

    )


    print()

    print(

        "Confusion Matrix"

    )

    print(

        cm

    )


    try:

        roc = round(

            roc_auc_score(

                y_true,

                y_prob,

                multi_class="ovr"

            ),

            4

        )

    except:

        roc = 0


    return {

        "Accuracy":

        round(

            accuracy_score(

                y_true,

                y_pred

            ),

            4

        ),


        "Precision":

        round(

            precision_score(

                y_true,

                y_pred,

                average="macro",

                zero_division=0

            ),

            4

        ),


        "Recall":

        round(

            recall_score(

                y_true,

                y_pred,

                average="macro",

                zero_division=0

            ),

            4

        ),


        "F1":

        round(

            f1_score(

                y_true,

                y_pred,

                average="macro",

                zero_division=0

            ),

            4

        ),


        "ROC_AUC":

        roc

    }