import os
import pandas as pd


def compare_results():

    result_files = {

        "node": "results/node_results.xlsx",

        "link": "results/link_results.xlsx",

        "graph": "results/graph_results.xlsx",

    }

    rank_metric = {

        "node": "Accuracy",

        "link": "AUC",

        "graph": "Accuracy_Mean",

    }

    target = (

        "results/comparison.txt"

    )

    found_any = False

    lines = [

        "BENCHMARK SUMMARY\n\n"

    ]

    # --- Overall "best model per task/dataset" table, shown first so it's
    # not buried under the raw per-row dumps further down. Built from the
    # same ranking logic used below, just collected across all tasks first.
    overall_best = []

    for task, file_name in result_files.items():

        if not os.path.exists(file_name):

            continue

        metric = rank_metric.get(task)

        df_peek = pd.read_excel(file_name, dtype=object)

        if not (metric and metric in df_peek.columns and "Dataset" in df_peek.columns):

            continue

        ranked_peek = df_peek.copy()

        ranked_peek[metric] = pd.to_numeric(ranked_peek[metric], errors="coerce")

        ranked_peek = ranked_peek.dropna(subset=[metric])

        for dataset_name, group in ranked_peek.groupby("Dataset"):

            best_row = group.sort_values(metric, ascending=False).iloc[0]

            overall_best.append(

                f"{task.upper():<6} {dataset_name:<10} "
                f"best={best_row['Model']:<10} {metric}={best_row[metric]}"

            )

    if overall_best:

        lines.append("=== BEST MODEL PER TASK/DATASET (OVERALL) ===\n\n")

        lines.extend(line + "\n" for line in overall_best)

        lines.append("\n\n")

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

        metric = rank_metric.get(

            task

        )

        if metric and metric in df.columns and "Dataset" in df.columns:

            lines.append(

                f"--- Best {task.upper()} model per dataset (ranked by {metric}) ---\n\n"

            )

            ranked = df.copy()

            ranked[metric] = pd.to_numeric(

                ranked[metric],

                errors="coerce"

            )

            ranked = ranked.dropna(

                subset=[metric]

            )

            for dataset_name, group in ranked.groupby("Dataset"):

                group_sorted = group.sort_values(

                    metric,

                    ascending=False

                )

                best_row = group_sorted.iloc[0]

                lines.append(

                    f"{dataset_name}: {best_row['Model']} "

                    f"({metric}={best_row[metric]})\n"

                )

                lines.append(

                    group_sorted[["Model", metric]]

                    .to_string(

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
