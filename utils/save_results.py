def save_result(
    task,
    model,
    dataset,
    accuracy
):

    with open(

        "results/auto_results.txt",

        "a"

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