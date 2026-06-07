import os
import pandas as pd


def save_result(

    task,

    model,

    dataset,

    metrics

):

    os.makedirs(

        "results",

        exist_ok=True

    )


    if (

        "Accuracy"

        in

        metrics

        and

        (

            "Macro_F1"

            in metrics

            or

            "Weighted_F1"

            in metrics

        )

    ):

        file_name = (

            "results/node_results.xlsx"

        )


    elif (

        "AUC"

        in metrics

    ):

        file_name = (

            "results/link_results.xlsx"

        )


    else:

        file_name = (

            "results/graph_results.xlsx"

        )


    row = {

        "Task": task,

        "Model": model,

        "Dataset": dataset

    }


    row.update(

        metrics

    )


    if os.path.exists(

        file_name

    ):

        df = pd.read_excel(

            file_name

        )

    else:

        df = pd.DataFrame()


    duplicate = (

        (df.get(

            "Task",

            pd.Series()

        )

        ==

        task)

        &

        (df.get(

            "Model",

            pd.Series()

        )

        ==

        model)

        &

        (df.get(

            "Dataset",

            pd.Series()

        )

        ==

        dataset)

    )


    if len(df) > 0 and duplicate.any():

        index = (

            df[

                duplicate

            ]

            .index[0]

        )

        for k, v in row.items():

            df.loc[

                index,

                k

            ] = v

    else:

        df = pd.concat(

            [

                df,

                pd.DataFrame(

                    [

                        row

                    ]

                )

            ],

            ignore_index=True

        )


    df.to_excel(

        file_name,

        index=False

    )


    print()

    print(

        f"Saved → {file_name}"

    )