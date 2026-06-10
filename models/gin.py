import torch
import torch.nn.functional as F

from torch.nn import Sequential
from torch.nn import Linear
from torch.nn import ReLU

from torch_geometric.nn import (

    GINConv,

    BatchNorm,

    global_mean_pool

)


class GIN(

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


        mlp1 = Sequential(

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


        self.conv1 = GINConv(

            mlp1

        )


        self.bn1 = BatchNorm(

            hidden_dim

        )

       
        mlp2 = Sequential(

            Linear(

                hidden_dim,

                hidden_dim

            )

        )


        self.conv2 = GINConv(

            mlp2

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
