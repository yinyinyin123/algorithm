

def attention(query, key, value, mask=None, dropout=None):
    d_k = query.size(-1)
    scores = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(d_k)
    if(mask is not None):
        scores = scores.masked_fill(mask==0, 1e-9)
    scores = F.softmax(scores, dim=-1)
    if(dropout is not None):
        scores = dropout(scores)
    return torch.matmul(scores, value), scores


class MultiHeadAttention(nn.Module):
    def __init__(self, head, d_model, dropout=0.1):
        super().__init__()
        self.head = head
        self.d_k = d_model // head
        self.linears = nn.ModuleList([nn.Linear(d_model, d_model) for _ in range(4)])
        self.dropout = nn.Dropout(p=dropout)

    def forward(query, key, value, mask=None):
        if mask is not None:
            mask = mask.unsqueeze(1)
        batch_size = query.size(0)
        query, key, value = [l(x).view(batch_size, -1, self.head, self.d_k) for l, x in zip(self.linears, (query, key, value))]
        x, atten = attention(query, key, value, mask, self.dropout)
        x =  x.transpose(1,2).contiguous().view(batch_size, -1 , self.head * self.d_k)
        return self.linears[-1](x)
