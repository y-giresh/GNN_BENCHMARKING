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

            file_name

        )

    else:

        df = pd.DataFrame()


    duplicate = (

        (df.get("Task", pd.Series(dtype=str)) == task)

        &

        (df.get("Model", pd.Series(dtype=str)) == model)

        &

        (df.get("Dataset", pd.Series(dtype=str)) == dataset)

        &

        (df.get("Hidden", pd.Series(dtype=float)) == hidden)

        &

        (df.get("LR", pd.Series(dtype=float)) == lr)

        &

        (df.get("Dropout", pd.Series(dtype=float)) == dropout)

        &

        (df.get("Weight_Decay", pd.Series(dtype=float)) == weight_decay)

        &

        (df.get("Epochs", pd.Series(dtype=float)) == epochs)

    )


    if len(df) > 0 and duplicate.any():

        idx = (

            df[

                duplicate

            ]

            .index[0]

        )

        for col in row:

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


    df.to_excel(

        file_name,

        index=False

    )


    print()

    print(

        f"Saved -> {file_name}"

    )