import sys
import torch
import time
import psutil
import os

from tasks import get_dataset
from models import get_model

from utils.train import train
from utils.evaluate import evaluate

from utils.save_results import save_result
from utils.metrics import compare_results


if len(sys.argv) < 4:

    print()

    print(
        "Usage:"
    )

    print()

    print(
        "python main.py [task] [model] [dataset] [hidden] [lr] [dropout] [weight_decay] [epochs]"
    )

    sys.exit()


task = sys.argv[1]

model_name = sys.argv[2]

dataset_name = sys.argv[3]


hidden_dim = (

    int(sys.argv[4])

    if len(sys.argv) > 4

    else 32

)

learning_rate = (

    float(sys.argv[5])

    if len(sys.argv) > 5

    else 0.01

)

dropout = (

    float(sys.argv[6])

    if len(sys.argv) > 6

    else 0.5

)

weight_decay = (

    float(sys.argv[7])

    if len(sys.argv) > 7

    else 5e-4

)

epochs = (

    int(sys.argv[8])

    if len(sys.argv) > 8

    else 200

)


start = time.time()

process = (

    psutil.Process(

        os.getpid()

    )

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

print(
    f"Hidden={hidden_dim}"
)

print(
    f"LR={learning_rate}"
)

print(
    f"Dropout={dropout}"
)

print(
    f"Weight Decay={weight_decay}"
)

print(
    f"Epochs={epochs}"
)

print()


if task == "node":

    dataset = get_dataset(
        dataset_name
    )

    data = dataset[0]

    model = get_model(

        model_name,

        dataset.num_features,

        hidden_dim,

        dataset.num_classes

    )

    optimizer = torch.optim.Adam(

        model.parameters(),

        lr=learning_rate,

        weight_decay=weight_decay

    )

    train(

        model,

        data,

        optimizer,

        epochs

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

        hidden_dim,

        hidden_dim

    )

    optimizer = torch.optim.Adam(

        model.parameters(),

        lr=learning_rate,

        weight_decay=weight_decay

    )

    train_link(

        model,

        train_data,

        optimizer,

        epochs

    )

    acc = evaluate_link(

        model,

        test_data

    )


elif task == "graph":

    from tasks.graph_classification import (
        load_graph_dataset
    )

    from utils.train import (
        train_graph
    )

    from utils.evaluate import (
        evaluate_graph
    )

    dataset, loader = (

        load_graph_dataset(
            dataset_name
        )

    )

    print()

    print(
        "Graph Classification Mode"
    )

    print()

    print(
        "Graphs:",
        len(dataset)
    )

    print(
        "Classes:",
        dataset.num_classes
    )

    model = get_model(

        model_name,

        dataset.num_features,

        hidden_dim,

        dataset.num_classes

    )

    optimizer = torch.optim.Adam(

        model.parameters(),

        lr=learning_rate,

        weight_decay=weight_decay

    )

    train_graph(

        model,

        loader,

        optimizer,

        epochs

    )

    acc = evaluate_graph(

        model,

        loader

    )

else:

    print(
        "Invalid Task"
    )

    sys.exit()



end = time.time()


train_time = round(

    end - start,

    2

)


params = (

    sum(

        p.numel()

        for p in model.parameters()

    )

)


memory = round(

    process.memory_info().rss

    /

    1024

    /

    1024,

    2

)


acc[

    "Training_Time"

] = train_time


acc[

    "Parameters"

] = params


acc[

    "Memory_MB"

] = memory


print()

print(
    "Final Metrics:"
)

print()

print(
    acc
)


save_result(

    task,

    model_name,

    dataset_name,

    acc

)


compare_results()