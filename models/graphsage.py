import torch
import torch.nn.functional as F

from torch_geometric.nn import (
    SAGEConv,
    global_mean_pool
)


torch.manual_seed(42)


class GraphSAGE(
    torch.nn.Module
):

    def __init__(
        self,
        input_dim,
        hidden_dim,
        output_dim
    ):

        super().__init__()

        self.conv1 = SAGEConv(

            input_dim,

            hidden_dim

        )

        self.conv2 = SAGEConv(

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

            x = global_mean_pool(

                x,

                batch

            )


        return x