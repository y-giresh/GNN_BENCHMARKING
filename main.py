import sys
import torch
import time
import psutil
import os
import random
import numpy as np
import networkx as nx

from tasks import get_dataset, create_split
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


# FIX #11: validate GAT hidden_dim constraint BEFORE data loading so the
# user gets a clear error message immediately, not after waiting for the
# dataset to download and preprocess.
if model_name == "gat" and hidden_dim % 8 != 0:

    print()

    print(

        f"Error: GAT requires hidden_dim divisible by 8, got {hidden_dim}."

    )

    print(

        "Please choose a value such as 32, 64, 128, 256."

    )

    sys.exit(1)


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

    dataset = create_split(
        dataset
    )

    data = dataset[0]

    # FIX #13: start timer AFTER data loading so Training_Time reflects only
    # actual training + evaluation time, not dataset download/preprocessing.
    start = time.time()

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

    # FIX #13: start timer AFTER data loading.
    start = time.time()

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

        val_data,

        optimizer,

        epochs

    )


    acc = evaluate_link(

        model,

        test_data

    )


    graph = nx.Graph()

    graph.add_nodes_from(

        range(

            dataset[0].num_nodes

        )

    )

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


    edge_pairs = []


    test_edges = (

        test_data.edge_label_index

        .cpu()

        .numpy()

    )


    for i in range(

        test_edges.shape[1]

    ):

        edge_pairs.append(

            (

                int(

                    test_edges[0][i]

                ),

                int(

                    test_edges[1][i]

                )

            )

        )


    labels = (

        test_data.edge_label

        .cpu()

        .numpy()

    )


    cn = (

        common_neighbors_score(

            graph,

            edge_pairs,

            labels

        )

    )


    aa = (

        adamic_adar_score(

            graph,

            edge_pairs,

            labels

        )

    )


    pa = (

        preferential_attachment_score(

            graph,

            edge_pairs,

            labels

        )

    )


    for k, v in cn.items():

        acc[

            f"CN_{k}"

        ] = v


    for k, v in aa.items():

        acc[

            f"AA_{k}"

        ] = v


    for k, v in pa.items():

        acc[

            f"PA_{k}"

        ] = v

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

    # FIX #3: guard against empty fold_loaders (dataset too small for the
    # requested number of folds) which would leave `model` undefined and crash
    # when computing acc["Parameters"] below.
    if len(fold_loaders) == 0:

        print()

        print(

            "Error: no folds were created. "

            "The dataset may be too small for the requested number of folds."

        )

        sys.exit(1)

    # FIX #13: start timer AFTER data loading and fold preparation.
    start = time.time()

    fold_acc = []

    fold_precision = []

    fold_recall = []

    fold_f1 = []

    fold_roc = []


    for fold_num, (

        train_loader,
        val_loader,
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
            val_loader,

            optimizer,

            epochs

        )


        result = evaluate_graph(

            model,

            test_loader

        )


        fold_acc.append(

            result["Accuracy"]

        )


        fold_precision.append(

            result["Precision"]

        )


        fold_recall.append(

            result["Recall"]

        )


        fold_f1.append(

            result["F1"]

        )

        if result["ROC_AUC"] is not None:

            fold_roc.append(

                result["ROC_AUC"]

            )


        print(

            f"Fold Accuracy: {result['Accuracy']:.4f}"

        )


    acc = {

        "Accuracy_Mean":

        round(

            float(

                np.mean(

                    fold_acc

                )

            ),

            4

        ),


        "Accuracy_Std":

        round(

            float(

                np.std(

                    fold_acc

                )

            ),

            4

        ),


        "Precision":

        round(

            float(

                np.mean(

                    fold_precision

                )

            ),

            4

        ),


        "Recall":

        round(

            float(

                np.mean(

                    fold_recall

                )

            ),

            4

        ),


        "F1":

        round(

            float(

                np.mean(

                    fold_f1

                )

            ),

            4

        ),


        "ROC_AUC":

        round(

            float(

                np.mean(

                    fold_roc

                )

            ),

            4

        )

        if fold_roc

        else "NA",

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
