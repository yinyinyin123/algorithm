
### 卷积神经网络相关

conv = nn.Conv2d(chanel_num, filter_num, (size, d_model))
x = torch.randn(batch_size, squence_length, d_model)

fiter_sizes = [3,4,5]
convs = nn.ModuleList([conv = nn.Conv2d(chanel_num, filter_num, (size, d_model)) for size in filter_size])
x = x.unsqueeze(1)
x = [nn.functional.relu(conv(x)).squeeze(3) for conv in convs]
x = [nn.functional.max_pool1d(item, item.size(2)).suqeeze(2) for item in x]
x = torch.cat(x, dim=1)
