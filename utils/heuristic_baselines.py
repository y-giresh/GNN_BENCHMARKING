import networkx as nx


def common_neighbors_score(

    graph,

    u,

    v

):

    try:

        if (

            u not in graph

            or

            v not in graph

        ):

            return 0


        return len(

            list(

                nx.common_neighbors(

                    graph,

                    u,

                    v

                )

            )

        )

    except:

        return 0




def adamic_adar_score(

    graph,

    u,

    v

):

    try:

        if (

            u not in graph

            or

            v not in graph

        ):

            return 0


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


        if len(score) == 0:

            return 0


        return round(

            score[0][2],

            4

        )

    except:

        return 0




def preferential_attachment_score(

    graph,

    u,

    v

):

    try:

        if (

            u not in graph

            or

            v not in graph

        ):

            return 0


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


        if len(score) == 0:

            return 0


        return round(

            score[0][2],

            4

        )

    except:

        return 0