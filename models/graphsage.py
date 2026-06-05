import torch
import torch.nn.functional as F
from torch_geometric.nn import SAGEConv


torch.manual_seed(42)


class GraphSAGE(torch.nn.Module):

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
        data
    ):

        x = data.x
        edge_index = data.edge_index

        x = self.conv1(
            x,
            edge_index
        )

        x = F.relu(
            x
        )

        x = F.dropout(
            x,
            p=0.5,
            training=self.training
        )

        x = self.conv2(
            x,
            edge_index
        )

        return x