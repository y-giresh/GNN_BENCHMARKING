import torch
import torch.nn.functional as F

from torch_geometric.nn import (
    GATConv,
    global_mean_pool
)


torch.manual_seed(42)


class GAT(
    torch.nn.Module
):

    def __init__(
        self,
        input_dim,
        hidden_dim,
        output_dim
    ):

        super().__init__()

        self.conv1 = GATConv(

            input_dim,

            hidden_dim,

            heads=8,

            dropout=0.6

        )

        self.conv2 = GATConv(

            hidden_dim * 8,

            output_dim,

            heads=1,

            concat=False,

            dropout=0.6

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

        x = F.elu(
            x
        )

        x = F.dropout(

            x,

            p=0.6,

            training=self.training

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