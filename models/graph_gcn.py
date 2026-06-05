import torch
import torch.nn.functional as F

from torch_geometric.nn import (
    GCNConv,
    global_mean_pool
)


class GraphGCN(
    torch.nn.Module
):

    def __init__(

        self,

        input_dim,

        hidden_dim,

        output_dim

    ):

        super().__init__()

        self.conv1 = GCNConv(

            input_dim,

            hidden_dim

        )

        self.conv2 = GCNConv(

            hidden_dim,

            hidden_dim

        )

        self.linear = torch.nn.Linear(

            hidden_dim,

            output_dim

        )


    def forward(

        self,

        data

    ):

        x = data.x

        edge_index = data.edge_index

        batch = data.batch


        x = self.conv1(

            x,

            edge_index

        )

        x = F.relu(
            x
        )


        x = self.conv2(

            x,

            edge_index

        )

        x = F.relu(
            x
        )


        x = global_mean_pool(

            x,

            batch

        )


        x = self.linear(
            x
        )

        return x