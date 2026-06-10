import torch
import torch.nn.functional as F

from torch_geometric.nn import (

    GATConv,

    BatchNorm,

    global_mean_pool

)


class GAT(

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

        assert hidden_dim % 8 == 0, (
            f"GAT requires hidden_dim divisible by 8 (got {hidden_dim})"
        )

        self.dropout = dropout

     
        self.conv1 = GATConv(

            input_dim,

            hidden_dim // 8,

            heads=8,

            dropout=0.0

        )


        self.bn1 = BatchNorm(

            hidden_dim

        )

      
        self.conv2 = GATConv(

            hidden_dim,

            hidden_dim,

            heads=1,

            concat=False,

            dropout=0.0

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
