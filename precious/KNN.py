

### KNN pytorch实现 Demo

class KNN(object):
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels

    def knn(self, sample):
        distance = torch.sum(torch.mul(sample-self.data,sample-self.data), dim=1)
        closest_idx = torch.argmin(distance).item()
        return labels[closest_idx]
