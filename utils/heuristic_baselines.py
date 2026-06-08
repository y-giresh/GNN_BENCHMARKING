import networkx as nx
import numpy as np


def common_neighbors_score(

    graph,

    edge_pairs

):

    scores = []


    for u, v in edge_pairs:

        try:

            if (

                u not in graph

                or

                v not in graph

            ):

                continue


            score = len(

                list(

                    nx.common_neighbors(

                        graph,

                        u,

                        v

                    )

                )

            )


            scores.append(

                score

            )

        except:

            continue


    if len(

        scores

    ) == 0:

        return 0


    return round(

        float(

            np.mean(

                scores

            )

        ),

        4

    )




def adamic_adar_score(

    graph,

    edge_pairs

):

    scores = []


    for u, v in edge_pairs:

        try:

            if (

                u not in graph

                or

                v not in graph

            ):

                continue


            score = list(

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

                score

            ) > 0:

                scores.append(

                    score[0][2]

                )

        except:

            continue


    if len(

        scores

    ) == 0:

        return 0


    return round(

        float(

            np.mean(

                scores

            )

        ),

        4

    )




def preferential_attachment_score(

    graph,

    edge_pairs

):

    scores = []


    for u, v in edge_pairs:

        try:

            if (

                u not in graph

                or

                v not in graph

            ):

                continue


            score = list(

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

                score

            ) > 0:

                scores.append(

                    score[0][2]

                )

        except:

            continue


    if len(

        scores

    ) == 0:

        return 0


    return round(

        float(

            np.mean(

                scores

            )

        ),

        4

    )