def compare_results():

    input_file = open(
        "results/auto_results.txt",
        "r"
    )

    lines = input_file.readlines()

    input_file.close()

    output = open(
        "results/comparison.txt",
        "w"
    )

    output.write(
        "BENCHMARK SUMMARY\n\n"
    )

    for i in range(
        len(lines)
    ):

        line = lines[i].strip()

        if (
            line.startswith(
                "Task:"
            )

            or

            line.startswith(
                "Model:"
            )

            or

            line.startswith(
                "Dataset:"
            )

            or

            line.startswith(
                "Accuracy:"
            )

        ):

            output.write(
                line
            )

            output.write(
                "\n"
            )

        if line.startswith(
            "Accuracy:"
        ):

            output.write(
                "\n"
            )

    output.close()

    print()

    print(
        "Comparison File Generated"
    )