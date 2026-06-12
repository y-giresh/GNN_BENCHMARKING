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

            "Hits@10pct": 0

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


    k = max(1, int(0.1 * len(scores)))

    top_k_indices = np.argsort(scores)[::-1][:k]

    hits_at_k = round(

        float(labels[top_k_indices].mean()),

        4

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

        "Hits@10pct":

        hits_at_k

    }




def common_neighbors_score(

    graph,

    edge_pairs,

    labels

):

    scores = []


    for u, v in edge_pairs:

        try:

            neighbors_u = set(

                graph.neighbors(

                    u

                )

            )


            neighbors_v = set(

                graph.neighbors(

                    v

                )

            )


            score = len(

                neighbors_u

                &

                neighbors_v

            )


        except Exception:

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

            neighbors_u = set(

                graph.neighbors(

                    u

                )

            )


            neighbors_v = set(

                graph.neighbors(

                    v

                )

            )


            common = (

                neighbors_u

                &

                neighbors_v

            )


            score = sum(

                1

                /

                np.log(

                    graph.degree(

                        n

                    )

                    +

                    2

                )

                for n in common

            )


        except Exception:

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

         
            score = (

                graph.degree(

                    u

                )

                *

                graph.degree(

                    v

                )

            )

        except Exception:

            score = 0


        scores.append(

            score

        )


    return evaluate_scores(

        scores,

        labels

    )
