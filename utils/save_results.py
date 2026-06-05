def save_result(
    task,
    model,
    dataset,
    accuracy
):

    file = open(

        "results/auto_results.txt",

        "a"

    )

    file.write(

        f"{task}, "

        f"{model}, "

        f"{dataset}, "

        f"{accuracy:.4f}\n"

    )

    file.close()

    print()

    print(
        "Result Saved"
    )