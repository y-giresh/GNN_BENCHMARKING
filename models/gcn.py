import torch
import torch.nn.functional as F

from torch_geometric.nn import GCNConv


class GCN(
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
            output_dim
        )


    def forward(
        self,
        x,
        edge_index,
        batch=None
    ):

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


        if batch is not None:

            from torch_geometric.nn import (
                global_mean_pool
            )

            x = global_mean_pool(
                x,
                batch
            )

        return x