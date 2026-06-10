import torch
import torch.nn.functional as F

from torch_geometric.nn import (

    SAGEConv,

    BatchNorm,

    global_mean_pool

)


class GraphSAGE(

    torch.nn.Module

):

    def __init__(

        self,

        input_dim,

        hidden_dim,

        output_dim,

        dropout=0.5

    ):

        super().__init__()


        self.dropout = dropout


        self.conv1 = SAGEConv(

            input_dim,

            hidden_dim

        )


        self.bn1 = BatchNorm(

            hidden_dim

        )

        # FIX #1: conv2 now outputs hidden_dim (was output_dim).
        # That made classifier a pointless output_dim->output_dim identity layer.
        # Now classifier does the real hidden_dim->output_dim projection, same as GCN.
        self.conv2 = SAGEConv(

            hidden_dim,

            hidden_dim

        )
        
        self.bn2 = BatchNorm(

          hidden_dim

         )
        
        self.classifier = torch.nn.Linear(

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


        x = self.bn1(

            x

        )


        x = F.relu(

            x

        )


        x = F.dropout(

            x,

            p=self.dropout,

            training=self.training

        )


        x = self.conv2(

            x,

            edge_index

        )
        
        x = self.bn2(

          x

          )


        x = F.relu(

          x

         )


        x = F.dropout(

         x,

         p=self.dropout,

         training=self.training

        )


        if batch is not None:

          x = global_mean_pool(

          x,

          batch

         )


        x = self.classifier(

         x

        )


        return x
