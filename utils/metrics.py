def compare_results():

    file = open(
        "results/auto_results.txt",
        "r"
    )

    lines = file.readlines()

    file.close()

    out = open(
        "results/comparison.txt",
        "w"
    )

    out.write(
        "BENCHMARK COMPARISON\n\n"
    )

    for line in lines:

        if line.strip():

            out.write(
                line
            )

    out.close()

    print()

    print(
        "Comparison File Generated"
    )