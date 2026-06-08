import networkx as nx
import numpy as np

from sklearn.metrics import (

    roc_auc_score,

    average_precision_score,

    f1_score

)




def evaluate_scores(

    scores,

    labels

):

    scores = np.array(

        scores

    )


    labels = np.array(

        labels

    )


    if len(

        scores

    ) == 0:

        return {

            "AUC": 0,

            "Average_Precision": 0,

            "F1": 0,

            "Hits@K": 0

        }


    threshold = np.median(

        scores

    )


    pred = (

        scores

        >=

        threshold

    ).astype(

        int

    )


    return {

        "AUC":

        round(

            roc_auc_score(

                labels,

                scores

            ),

            4

        ),

        "Average_Precision":

        round(

            average_precision_score(

                labels,

                scores

            ),

            4

        ),

        "F1":

        round(

            f1_score(

                labels,

                pred

            ),

            4

        ),

        "Hits@K":

        round(

            pred.mean(),

            4

        )

    }




def common_neighbors_score(

    graph,

    edge_pairs,

    labels

):

    scores = []


    for u, v in edge_pairs:

        try:

            score = len(

                list(

                    nx.common_neighbors(

                        graph,

                        u,

                        v

                    )

                )

            )

        except:

            score = 0


        scores.append(

            score

        )


    return evaluate_scores(

        scores,

        labels

    )




def adamic_adar_score(

    graph,

    edge_pairs,

    labels

):

    scores = []


    for u, v in edge_pairs:

        try:

            value = list(

                nx.adamic_adar_index(

                    graph,

                    [

                        (

                            u,

                            v

                        )

                    ]

                )

            )


            if len(

                value

            ) > 0:

                score = value[0][2]

            else:

                score = 0


        except:

            score = 0


        scores.append(

            score

        )


    return evaluate_scores(

        scores,

        labels

    )




def preferential_attachment_score(

    graph,

    edge_pairs,

    labels

):

    scores = []


    for u, v in edge_pairs:

        try:

            value = list(

                nx.preferential_attachment(

                    graph,

                    [

                        (

                            u,

                            v

                        )

                    ]

                )

            )


            if len(

                value

            ) > 0:

                score = value[0][2]

            else:

                score = 0


        except:

            score = 0


        scores.append(

            score

        )


    return evaluate_scores(

        scores,

        labels

    )