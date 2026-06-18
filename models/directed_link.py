import torch

from models import get_model


class DirectedLinkEncoder(torch.nn.Module):
    """
    Wraps one of the existing node encoders (GCN/GAT/GraphSAGE/GIN) to
    produce two *different* embeddings per node -- one used when the
    node acts as the source of an edge (u -> v) and one used when it
    acts as the destination -- instead of a single shared embedding.

    This is what actually makes link prediction directed:
      - the base encoder is unchanged (models/gcn.py etc. are not
        touched, and node/graph classification keep using the base
        encoder directly, with no wrapper involved)
      - two small linear heads (src_head, dst_head) sit on top of the
        base encoder's output and learn separate source/destination
        representations
      - scoring u -> v as dot(src_head(z[u]), dst_head(z[v])) is
        asymmetric: scoring v -> u uses dot(src_head(z[v]), dst_head(z[u])),
        which is generally a different value. The previous symmetric
        decode() (z[u] * z[v]).sum() could never tell u->v from v->u.

    Only used for task == "link" with directed=True. Undirected link
    prediction keeps using the base encoder's output directly with the
    original symmetric decode(), unchanged.
    """

    def __init__(
        self,
        model_name,
        input_dim,
        hidden_dim,
        dropout=0.5
    ):
        super().__init__()

        # base encoder's output_dim is set to hidden_dim, same trick
        # already used for undirected link prediction in main.py: the
        # "classifier" layer of the base model just produces a
        # hidden_dim-sized node representation here, not class logits.
        self.encoder = get_model(
            model_name,
            input_dim,
            hidden_dim,
            hidden_dim,
            dropout
        )

        self.src_head = torch.nn.Linear(hidden_dim, hidden_dim)
        self.dst_head = torch.nn.Linear(hidden_dim, hidden_dim)

    def forward(self, x, edge_index, batch=None):
        z = self.encoder(x, edge_index, batch)

        z_src = self.src_head(z)
        z_dst = self.dst_head(z)

        return z_src, z_dst
