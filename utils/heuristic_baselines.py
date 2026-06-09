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

            out_u = set(

                graph.successors(

                    u

                )

            )


            in_v = set(

                graph.predecessors(

                    v

                )

            )


            score = len(

                out_u

                &

                in_v

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

            out_u = set(

                graph.successors(

                    u

                )

            )


            in_v = set(

                graph.predecessors(

                    v

                )

            )


            common = (

                out_u

                &

                in_v

            )


            score = sum(

                1

                /

                np.log(

                    graph.in_degree(

                        n

                    )

                    +

                    2

                )

                for n in common

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




def preferential_attachment_score(

    graph,

    edge_pairs,

    labels

):

    scores = []


    for u, v in edge_pairs:

        try:

            score = (

                graph.out_degree(

                    u

                )

                *

                graph.in_degree(

                    v

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