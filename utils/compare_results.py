import os


def compare_results():

    source = (

        "results/auto_results.txt"

    )

    target = (

        "results/comparison.txt"

    )


    if not os.path.exists(

        source

    ):

        return


    with open(

        source,

        "r",

        encoding="utf-8"

    ) as f:

        content = f.read()


    with open(

        target,

        "w",

        encoding="utf-8"

    ) as f:

        f.write(

            "BENCHMARK SUMMARY\n\n"

        )

        f.write(

            content

        )


    print()

    print(

        "Comparison File Generated"

    )