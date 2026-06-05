import torch
import torch.nn.functional as F

from torch.nn import Sequential
from torch.nn import Linear
from torch.nn import ReLU

from torch_geometric.nn import GINConv


torch.manual_seed(42)


class GIN(torch.nn.Module):

    def __init__(
        self,
        input_dim,
        hidden_dim,
        output_dim
    ):

        super().__init__()

        nn1 = Sequential(

            Linear(
                input_dim,
                hidden_dim
            ),

            ReLU(),

            Linear(
                hidden_dim,
                hidden_dim
            )

        )

        nn2 = Sequential(

            Linear(
                hidden_dim,
                hidden_dim
            ),

            ReLU(),

            Linear(
                hidden_dim,
                output_dim
            )

        )

        self.conv1 = GINConv(
            nn1
        )

        self.conv2 = GINConv(
            nn2
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