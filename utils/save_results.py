import os
import pandas as pd


def save_result(

    task,

    model,

    dataset,

    metrics,

    hidden=None,

    lr=None,

    dropout=None,

    weight_decay=None,

    epochs=None

):

    os.makedirs(

        "results",

        exist_ok=True

    )


    hyper = (

        os.environ.get(

            "HYPER"

        )

        ==

        "1"

    )


    if hyper:

        file_name = (

            "results/hyperparameter_results.xlsx"

        )

    else:

        if task == "node":

            file_name = (

                "results/node_results.xlsx"

            )

        elif task == "link":

            file_name = (

                "results/link_results.xlsx"

            )

        elif task == "graph":

            file_name = (

                "results/graph_results.xlsx"

            )

        else:

            file_name = (

                "results/results.xlsx"

            )


    row = {

        "Task": task,

        "Model": model,

        "Dataset": dataset,

        "Hidden": hidden,

        "LR": lr,

        "Dropout": dropout,

        "Weight_Decay": weight_decay,

        "Epochs": epochs

    }


    row.update(

        metrics

    )


    if os.path.exists(

        file_name

    ):

        df = pd.read_excel(

            file_name,

            dtype=object

        )

    else:

        df = pd.DataFrame()


    for col in row:

        if col not in df.columns:

            df[col] = None


    duplicate = (

        (df["Task"] == task)

        &

        (df["Model"] == model)

        &

        (df["Dataset"] == dataset)

        &

        (df["Hidden"].astype(str) == str(hidden))

        &

        (df["LR"].astype(str) == str(lr))

        &

        (df["Dropout"].astype(str) == str(dropout))

        &

        (df["Weight_Decay"].astype(str) == str(weight_decay))

        &

        (df["Epochs"].astype(str) == str(epochs))

    )


    if len(df) > 0 and duplicate.any():

        idx = (

            df[

                duplicate

            ]

            .index[0]

        )


        for col in row:

            df[col] = (

                df[col]

                .astype(

                    object

                )

            )

            df.loc[

                idx,

                col

            ] = row[col]

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


    df = df.astype(

        object

    )


    df.to_excel(

        file_name,

        index=False

    )


    print()

    print(

        f"Saved -> {file_name}"

    )