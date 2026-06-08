import sys
import torch
import time
import psutil
import os
import random
import numpy as np
import networkx as nx

from tasks import get_dataset
from models import get_model

from utils.train import train
from utils.evaluate import evaluate

from utils.save_results import save_result
from utils.compare_results import compare_results

from utils.heuristic_baselines import (

    common_neighbors_score,

    adamic_adar_score,

    preferential_attachment_score

)


SEED = 42

random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)

if torch.cuda.is_available():

    torch.cuda.manual_seed_all(SEED)

torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False


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


hidden_dim = int(sys.argv[4]) if len(sys.argv) > 4 else 32

learning_rate = float(sys.argv[5]) if len(sys.argv) > 5 else 0.01

dropout = float(sys.argv[6]) if len(sys.argv) > 6 else 0.5

weight_decay = float(sys.argv[7]) if len(sys.argv) > 7 else 5e-4

epochs = int(sys.argv[8]) if len(sys.argv) > 8 else 200


start = time.time()

process = psutil.Process(
    os.getpid()
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


if task == "node":

    dataset = get_dataset(
        dataset_name
    )

    data = dataset[0]

    model = get_model(

        model_name,

        dataset.num_features,

        hidden_dim,

        dataset.num_classes,

        dropout

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

    from tasks import load_link_dataset

    from utils.train import train_link

    from utils.evaluate import evaluate_link


    dataset, train_data, val_data, test_data = (

        load_link_dataset(
            dataset_name
        )

    )


    model = get_model(

        model_name,

        dataset.num_features,

        hidden_dim,

        hidden_dim,

        dropout

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


    graph = nx.Graph()

    edges = (

        train_data.edge_index

        .cpu()

        .numpy()

    )


    for i in range(

        edges.shape[1]

    ):

        graph.add_edge(

            int(

                edges[0][i]

            ),

            int(

                edges[1][i]

            )

        )


    u = 0

    v = 1


    acc["Common_Neighbors"] = (

        common_neighbors_score(

            graph,

            u,

            v

        )

    )


    acc["Adamic_Adar"] = round(

        adamic_adar_score(

            graph,

            u,

            v

        ),

        4

    )


    acc["Preferential_Attachment"] = (

        preferential_attachment_score(

            graph,

            u,

            v

        )

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


    dataset, fold_loaders = (

        load_graph_dataset(
            dataset_name
        )

    )


    fold_scores = []


    for fold_num, (

        train_loader,

        test_loader

    ) in enumerate(

        fold_loaders,

        1

    ):


        print()

        print(

            f"Fold {fold_num}"

        )


        model = get_model(

            model_name,

            dataset.num_features,

            hidden_dim,

            dataset.num_classes,

            dropout

        )


        optimizer = torch.optim.Adam(

            model.parameters(),

            lr=learning_rate,

            weight_decay=weight_decay

        )


        train_graph(

            model,

            train_loader,

            optimizer,

            epochs

        )


        result = evaluate_graph(

            model,

            test_loader

        )


        score = result["Accuracy"]


        fold_scores.append(

            score

        )


        print(

            f"Fold Accuracy: {score:.4f}"

        )


    acc = {

        "Accuracy":

        f"{round(np.mean(fold_scores),4)} ± {round(np.std(fold_scores),4)}"

    }


else:

    print(
        "Invalid Task"
    )

    sys.exit()


end = time.time()


acc["Training_Time"] = round(

    end - start,

    2

)


acc["Parameters"] = (

    sum(

        p.numel()

        for p in model.parameters()

    )

)


acc["Memory_MB"] = round(

    process.memory_info().rss

    /

    1024

    /

    1024,

    2

)


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

    acc,
    
    hidden_dim,
    
    learning_rate,
    
    dropout,
    
    weight_decay,
    
    epochs

)


compare_results()