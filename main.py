import sys
import torch

from tasks import get_dataset

from models import get_model

from utils.train import train

from utils.evaluate import evaluate

from utils.save_results import save_result

from utils.metrics import compare_results


if len(sys.argv) != 4:

    print(
        "Usage:"
    )

    print(
        "python main.py [task] [model] [dataset]"
    )

    sys.exit()


task = sys.argv[1]

model_name = sys.argv[2]

dataset_name = sys.argv[3]


dataset = get_dataset(
    dataset_name
)

data = dataset[0]


model = get_model(

    model_name,

    dataset.num_features,

    32,

    dataset.num_classes

)


optimizer = torch.optim.Adam(

    model.parameters(),

    lr=0.01,

    weight_decay=5e-4

)


print()

print(
    "Running Experiment"
)

print()

print(
    task,
    model_name,
    dataset_name
)

print()


if task == "node":

    train(

        model,

        data,

        optimizer

    )

    acc = evaluate(

        model,

        data

    )


elif task == "link":

    from tasks import (
        load_link_dataset
    )

    from utils.train import (
        train_link
    )

    from utils.evaluate import (
        evaluate_link
    )

    dataset, train_data, val_data, test_data = (

        load_link_dataset(
            dataset_name
        )

    )

    model = get_model(

        model_name,

        dataset.num_features,

        32,

        32

    )

    optimizer = torch.optim.Adam(

        model.parameters(),

        lr=0.01,

        weight_decay=5e-4

    )

    train_link(

        model,

        train_data,

        optimizer

    )

    acc = evaluate_link(

        model,

        test_data

    )


else:

    print(
        "Invalid Task"
    )

    sys.exit()


print()

print(
    "Final Accuracy:",
    acc
)

save_result(

    task,

    model_name,

    dataset_name,

    acc

)

compare_results()