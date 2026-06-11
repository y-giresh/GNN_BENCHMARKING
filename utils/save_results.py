import os
import pandas as pd


def _norm(

    value

):


    try:

        return f"{float(value):.10g}"

    except (

        TypeError,

        ValueError

    ):

        return str(value)


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

        (df["Hidden"].apply(_norm) == _norm(hidden))

        &

        (df["LR"].apply(_norm) == _norm(lr))

        &

        (df["Dropout"].apply(_norm) == _norm(dropout))

        &

        (df["Weight_Decay"].apply(_norm) == _norm(weight_decay))

        &

        (df["Epochs"].apply(_norm) == _norm(epochs))

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
