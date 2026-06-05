import os


def save_result(

    task,

    model,

    dataset,

    accuracy

):

    os.makedirs(

        "results",

        exist_ok=True

    )


    path = (

        "results/auto_results.txt"

    )


    with open(

        path,

        "a",

        encoding="utf-8"

    ) as file:

        file.write(

            f"\n"

            f"Task: {task}\n"

            f"Model: {model}\n"

            f"Dataset: {dataset}\n"

            f"Accuracy: {accuracy:.4f}\n"

        )


    print()

    print(

        "Result Saved"

    )