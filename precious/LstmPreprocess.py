

### 在使用rnn之前 对序列进行从长到短 重排

def sort_by_lentgh(batch, batch_lengths):
    sorted_lengths, sorted_index = batch.sort(0, descending=True)
    sorted_batch = batch.index_select(0, sorted_index)
    _, reverse_index = sorted_index.sort(0, decending=False)
    return sorted_batch, sorted_lengths, reverse_index

def rnn(batch, batch_lengths):
    sorted_batch, sorted_lengths, reverse_index = sort_by_lentgh(batch, batch_lengths)
    packed_batch = nn.utils.rnn.pack_padded_sequence(sorted_batch, sorted_lengths, batch_first=True)
    outputs, _ = Rnn(packed_batch, None)
    outputs, _ = nn.utils.rnn.pad_packed_sequence(outputs, batch_first=True)
    outputs = outputs.index_selct(0, reverse_index)
    return outputs

### rnn参数
rnn(input_size, hidden_size, num_layers, bidirectional, bias, dropout, batch_first)
