import os
import pandas as pd


def compare_results():

    result_files = {

        "node": "results/node_results.xlsx",

        "link": "results/link_results.xlsx",

        "graph": "results/graph_results.xlsx",

    }

    target = (

        "results/comparison.txt"

    )

    found_any = False

    lines = [

        "BENCHMARK SUMMARY\n\n"

    ]

    for task, file_name in result_files.items():

        if not os.path.exists(

            file_name

        ):

            continue

        found_any = True

        df = pd.read_excel(

            file_name,

            dtype=object

        )

        lines.append(

            f"=== {task.upper()} CLASSIFICATION ===\n\n"

        )

        lines.append(

            df.to_string(

                index=False

            )

        )

        lines.append(

            "\n\n"

        )

    if not found_any:

        print()

        print(

            "No result files found yet. "

            "Run at least one experiment before calling compare_results()."

        )

        return

    os.makedirs(

        "results",

        exist_ok=True

    )

    with open(

        target,

        "w",

        encoding="utf-8"

    ) as f:

        f.writelines(

            lines

        )

    print()

    print(

        "Comparison File Generated"

    )
