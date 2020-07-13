
### 机器学习二分类模型性能评价指标 AUC
### ROC曲线下的面积，随机抽取一个阳性样本和阴性样本，正确判断阳性样本的值高于
### 阴性样本的机率

preds = [0.5,0.1,0.4,0.5,0.7,0.8,0.3]
labels = [1,1,1,-1,-1,-1,1]

preds_labels = [(pred, label) for pred, label in zip(preds, labels)]
preds_labels.sort()

N = (len(labels) - sum(labels)) / 2
M = len(labels) - N

negetive = 0
cont = 0
for i in range(len(preds_labels)):
    if(preds_labels[i][1] == 1):
        pair += negative
    else:
        negative += 1

print(pair / (M*N))
